from datetime import datetime
import statistics
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers, metrics
from keras.layers import TextVectorization, Embedding

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
        # x = layers.Dense(128, activation="relu")(x)
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

    def kfold(self, dataset:Dataset, batch_size:int, epochs:int):
        n_folds = 10
        dataset.apply(preprocessing.remove_punctuation)
        dataset.apply(preprocessing.lowercase)

        accuracies = []
        precisions = []
        recalls = []
        for test_data, train_data in dataset.kfold(n_folds):
            test_data = test_data.make_xy()
            train_data = train_data.make_xy(batch_size)
            self.model.fit(train_data, epochs=epochs)
            metrics = self.model.evaluate(test_data)
            accuracies.append(metrics[1])
            precisions.append(metrics[2])
            recalls.append(metrics[3])
            self._reinitialize_model()

        f1_scores = [2 * (precisions[i] * recalls[i]) / (precisions[i] + recalls[i]) for i in range(n_folds)]

        mean_accuracy = statistics.fmean(accuracies)
        mean_precisions = statistics.fmean(precisions)
        mean_recalls = statistics.fmean(recalls)
        mean_f1 = statistics.fmean(f1_scores)
        return mean_accuracy, mean_precisions, mean_recalls, mean_f1

    def train(self, dataset:Dataset, batch_size:int, epochs:int):
        dataset.apply(preprocessing.remove_punctuation)
        dataset.apply(preprocessing.lowercase)
        dataset = dataset.make_xy(batch_size)
        self.model.fit(dataset, batch_size=batch_size, epochs=epochs)

    def test(self, dataset:Dataset):
        dataset.apply(preprocessing.remove_punctuation)
        dataset.apply(preprocessing.lowercase)
        dataset = dataset.make_xy()
        metrics = self.model.evaluate(dataset)

        accuracy = metrics[1]
        precision = metrics[2]
        recall = metrics[3]
        f1_score = 2 * (precision * recall) / (precision + recall)

        return accuracy, precision, recall, f1_score

    def predict(self, text:str):
        text = preprocessing.remove_punctuation(text)
        text = preprocessing.lowercase(text)
        probabilities = self.model.predict(
            [text]
        )

        return probabilities

    @classmethod
    def _create_vectorizer(cls, input_size:int, vocab_size:int, corpus:Dataset) -> TextVectorization:
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