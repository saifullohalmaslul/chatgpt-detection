from datetime import datetime
import statistics
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers, metrics
from keras.layers import TextVectorization, Embedding
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import preprocessing
from dataset import Dataset

class Model:
    def __init__(self, model:keras.Model, name:str):
        self.model = model
        self.name = name
    
    @classmethod
    def create_from_params(cls, input_size:int, vocab_size:int, corpus:Dataset, embeddings_path:str, filters:int, kernel_sizes:list, dropout:float, name:str=""):
        vectorizer = cls._create_vectorizer(input_size, vocab_size, corpus)
        embedding = cls._create_embedding(embeddings_path, vectorizer.get_vocabulary())
        
        string_sequences_input = keras.Input(shape=(1,), dtype=tf.string)
        vectorize_layer = vectorizer(string_sequences_input)
        embedded_sequences = embedding(vectorize_layer)
        convs = []
        for kernel_size in kernel_sizes:
            x = layers.Conv1D(filters, kernel_size, padding="same", activation="relu")(embedded_sequences)
            x = layers.GlobalMaxPooling1D()(x)
            convs.append(x)
        if len(convs) > 1:
            x = tf.keras.layers.Concatenate(axis=-1)(convs)
        x = layers.Dropout(dropout)(x)
        preds = layers.Dense(1, activation="sigmoid")(x)
        model = keras.Model(string_sequences_input, preds)

        model.compile(
            loss="binary_crossentropy", optimizer="adam", metrics=["acc",metrics.Precision(),metrics.Recall()]
        )

        if not name:
            name = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

        return cls(model, name)
    
    @classmethod
    def load(cls, path:str):
        name = path.split('/')[-1]
        return cls(tf.keras.models.load_model(path), name)
    
    def save(self, path:str):
        self.model.save(path, save_format="tf")
    
    def summary(self, print_fn):
        self.model.summary(print_fn=print_fn)

    def kfold(self, dataset:Dataset, batch_size:int, epochs:int, callbacks=None):
        n_folds = 10
        cm = [[0, 0], [0, 0]]
        accuracies = []
        precisions = []
        recalls = []
        fscores = []
        for i, (test_data, train_data) in enumerate(dataset.kfold(n_folds)):
            self.train(dataset=train_data, batch_size=batch_size, epochs=epochs, callbacks=callbacks)
            metrics = self.test(test_data)
            cm[0][0] += metrics[0][0][0]
            cm[0][1] += metrics[0][0][1]
            cm[1][0] += metrics[0][1][0]
            cm[1][1] += metrics[0][1][1]
            accuracies.append(metrics[1])
            precisions.append(metrics[2])
            recalls.append(metrics[3])
            fscores.append(metrics[4])
            self._reinitialize_model()

        mean_accuracy = statistics.fmean(accuracies)
        mean_precision = statistics.fmean(precisions)
        mean_recall = statistics.fmean(recalls)
        mean_fscore = statistics.fmean(fscores)
        return cm, mean_accuracy, mean_precision, mean_recall, mean_fscore

    def train(self, dataset:Dataset, batch_size:int, epochs:int, callbacks=None):
        dataset.filter(preprocessing.contains_chatgpt_error)
        dataset.apply(preprocessing.clean_chatgpt_output)
        dataset.apply(preprocessing.clean)
        dataset.apply(preprocessing.lowercase)
        dataset = dataset.make_xy(batch_size)
        self.model.fit(dataset, batch_size=batch_size, epochs=epochs, callbacks=callbacks)

    def test(self, dataset:Dataset):
        dataset.apply(preprocessing.clean)
        dataset.apply(preprocessing.lowercase)

        predictions = self.model.predict(dataset.make_xy())
        predictions = np.where(predictions < 0.5, 0 , 1)
        labels = dataset.get_labels()
        cm = confusion_matrix(labels, predictions)
        print('Confusion matrix:\n', cm)
        accuracy = accuracy_score(labels, predictions)
        precision = precision_score(labels, predictions, average='weighted', zero_division=0)
        recall = recall_score(labels, predictions, average='weighted', zero_division=0)
        fscore = f1_score(labels, predictions, average='weighted', zero_division=0)

        return cm, accuracy, precision, recall, fscore

    def predict(self, text:str):
        text = preprocessing.clean(text)
        text = preprocessing.lowercase(text)
        probabilities = self.model.predict(
            [text]
        )

        return probabilities

    @classmethod
    def _create_vectorizer(cls, input_size:int, vocab_size:int, corpus:Dataset) -> TextVectorization:
        corpus.filter(preprocessing.contains_chatgpt_error)
        corpus.apply(preprocessing.clean_chatgpt_output)
        corpus.apply(preprocessing.clean)
        corpus.apply(preprocessing.lowercase)
        vectorizer = TextVectorization(max_tokens=vocab_size, output_mode="int", output_sequence_length=input_size, standardize=None)
        corpus_texts = tf.data.Dataset.from_tensor_slices(corpus.get_texts()).batch(128)
        vectorizer.adapt(corpus_texts)

        return vectorizer
    
    @classmethod
    def _create_embedding(cls, filepath:str, vocab:list) -> Embedding:
        embeddings_index = {}
        coefs = np.ndarray((0))
        with open(filepath, encoding="utf8") as f:
            for line in f:
                word, coefs = line.split(maxsplit=1)
                coefs = np.fromstring(coefs, "f", sep=" ")
                embeddings_index[word] = coefs

        word_index = dict(zip(vocab, range(len(vocab))))
        num_tokens = len(vocab) + 2
        embedding_dim = coefs.size

        embedding_matrix = np.zeros((num_tokens, embedding_dim))
        for word, i in word_index.items():
            embedding_vector = embeddings_index.get(word)
            if embedding_vector is not None:
                embedding_matrix[i] = embedding_vector
        
        embedding = Embedding(
            num_tokens,
            embedding_dim,
            embeddings_initializer=keras.initializers.Constant(embedding_matrix),
            trainable=False,
        )

        return embedding

    def _reinitialize_model(self):
        for l in self.model.layers:
            if hasattr(l,"kernel_initializer"):
                l.kernel.assign(l.kernel_initializer(tf.shape(l.kernel)))
            if hasattr(l,"bias_initializer"):
                l.bias.assign(l.bias_initializer(tf.shape(l.bias)))
            if hasattr(l,"recurrent_initializer"):
                l.recurrent_kernel.assign(l.recurrent_initializer(tf.shape(l.recurrent_kernel)))