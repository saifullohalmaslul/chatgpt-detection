import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QTableWidgetItem
from PySide6.QtCore import QThread, Signal, QTimer
from ui import numain, nuaction, nuresult, nutt, nupd

from model import Model
from dataset import Dataset

class CompilingThread(QThread):
    finished = Signal(Model)

    def __init__(self, corpus:Dataset, embeddings_path:str, filters:int, kernel_sizes:list, dropout:float):
        super(CompilingThread, self).__init__()
        self.corpus = corpus
        self.embeddings_path = embeddings_path
        self.filters = filters
        self.kernel_sizes = kernel_sizes
        self.dropout = dropout

    def run(self):
        model = None
        try:
            model = Model.create_from_params(
                self.corpus,
                self.embeddings_path,
                self.filters,
                self.kernel_sizes,
                self.dropout,
            )
        finally:
            self.finished.emit(model)

class LoadingModelThread(QThread):
    finished = Signal(Model)

    def __init__(self, model_path:str):
        super(LoadingModelThread, self).__init__()
        self.model_path = model_path

    def run(self):
        model = None
        try:
            model = Model.load(self.model_path)
        finally:
            self.finished.emit(model)

class TrainTestThread(QThread):
    finished = Signal(tuple)

    def __init__(self, model:Model, train_data:Dataset, test_data:Dataset, train_batch:int, epochs:int):
        super(TrainTestThread, self).__init__()
        self.model = model
        self.train_data = train_data
        self.test_data = test_data
        self.train_batch = train_batch
        self.epochs = epochs

    def run(self):
        metrics = None
        try:
            self.model.train(self.train_data, self.train_batch, self.epochs)
            metrics = self.model.test(self.test_data)
        finally:
            self.finished.emit(metrics)

class SaveModelThread(QThread):
    def __init__(self, path:str, model:Model):
        super(SaveModelThread, self).__init__()
        self.model = model
        self.path = path

    def run(self):
        self.model.save(self.path)
        self.model.name = self.path.split('/')[-1]

class ResultWindow(QDialog):
    def __init__(self, model:Model, result:tuple):
        super(ResultWindow, self).__init__()
        self.ui = nuresult.Ui_Form()
        self.ui.setupUi(self)

        self.model = model
        self.ui.backButton.clicked.connect(self.show_model_summary)

        cm = result[0]
        self.ui.confusionTable.setItem(0, 0, QTableWidgetItem(str(cm[0][0])))
        self.ui.confusionTable.setItem(0, 1, QTableWidgetItem(str(cm[0][1])))
        self.ui.confusionTable.setItem(1, 0, QTableWidgetItem(str(cm[1][0])))
        self.ui.confusionTable.setItem(1, 1, QTableWidgetItem(str(cm[1][1])))

        accuracy = f'{result[1] * 100:.2f}%'
        precision = f'{result[2] * 100:.2f}%'
        recall = f'{result[3] * 100:.2f}%'
        fscore = f'{result[4] * 100:.2f}%'

        self.ui.accuracyText.setText(accuracy)
        self.ui.precisionText.setText(precision)
        self.ui.recallText.setText(recall)
        self.ui.fscoreText.setText(fscore)
    
    def show_model_summary(self):
        self.summary_window = ModelSummaryWindow(self.model)
        self.summary_window.show()
        self.close()

class TrainTestWindow(QDialog):
    def __init__(self, model:Model):
        super(TrainTestWindow, self).__init__()
        self.ui = nutt.Ui_Form()
        self.ui.setupUi(self)

        self.model = model
        self.train_loaded = False
        self.test_loaded = False

        self.ui.trainSelectButton.clicked.connect(self.load_train_data)
        self.ui.testSelectButton.clicked.connect(self.load_test_data)
        self.ui.pushButton.clicked.connect(self.start_train_test)
        self.ui.backButton.clicked.connect(self.show_model_summary)

    def start_train_test(self):
        self.train_test_thread = TrainTestThread(
            self.model,
            self.train_data,
            self.test_data,
            self.ui.batchSpinBox.value(),
            self.ui.epochsSpinBox.value()
        )

        self.train_test_thread.finished.connect(self.show_result)
        self.train_test_thread.start()
        self.disable_inputs()
    
    def show_result(self, result:tuple):
        if result is None:
            self.enable_inputs()
        else:
            self.result_window = ResultWindow(self.model, result)
            self.result_window.show()
            self.close()
    
    def disable_inputs(self):
        self.ui.trainDatasetView.setDisabled(True)
        self.ui.trainSelectButton.setDisabled(True)
        self.ui.testDatasetView.setDisabled(True)
        self.ui.testSelectButton.setDisabled(True)
        self.ui.batchSpinBox.setDisabled(True)
        self.ui.epochsSpinBox.setDisabled(True)
        self.ui.pushButton.setDisabled(True)
        self.ui.backButton.setDisabled(True)
    
    def enable_inputs(self):
        self.ui.trainDatasetView.setEnabled(True)
        self.ui.trainSelectButton.setEnabled(True)
        self.ui.testDatasetView.setEnabled(True)
        self.ui.testSelectButton.setEnabled(True)
        self.ui.batchSpinBox.setEnabled(True)
        self.ui.epochsSpinBox.setEnabled(True)
        self.ui.pushButton.setEnabled(True)
        self.ui.backButton.setEnabled(True)
    
    def load_train_data(self):
        dataset_path, _ = QFileDialog.getOpenFileName(self, "Select Dataset File", "", "JSON files (*.json *.jsonl)")
        self.train_data = Dataset.from_json(dataset_path)
        self.ui.trainDatasetView.setText(f'{self.train_data.name} - {self.train_data.total()}')
        self.ui.trainDatasetView.setEnabled(True)

        self.train_loaded = True
        if self.train_loaded and self.test_loaded:
            self.ui.pushButton.setEnabled(True)
    
    def load_test_data(self):
        dataset_path, _ = QFileDialog.getOpenFileName(self, "Select Dataset File", "", "JSON files (*.json *.jsonl)")
        self.test_data = Dataset.from_json(dataset_path)
        self.ui.testDatasetView.setText(f'{self.test_data.name} - {self.test_data.total()}')
        self.ui.testDatasetView.setEnabled(True)

        self.test_loaded = True
        if self.train_loaded and self.test_loaded:
            self.ui.pushButton.setEnabled(True)
    
    def show_model_summary(self):
        self.summary_window = ModelSummaryWindow(self.model)
        self.summary_window.show()
        self.close()

class PredictWindow(QDialog):
    def __init__(self, model:Model):
        super(PredictWindow, self).__init__()
        self.model = model

        self.ui = nupd.Ui_Form()
        self.ui.setupUi(self)

        self.ui.predictButton.clicked.connect(self.predict)
        self.ui.backButton.clicked.connect(self.show_model_summary)
    
    def predict(self):
        text = self.ui.textEdit.toPlainText()
        probabilities = self.model.predict(text)
        prediction = str(np.where(probabilities < 0.5, 'Human Answer','ChatGPT Answer').flat[0])
        self.ui.predictionView.setStyleSheet("background-color: rgb(47, 255, 10)")
        QTimer.singleShot(50, lambda :self.ui.predictionView.setStyleSheet("background-color: rgb(255, 255, 255)") )
        self.ui.predictionView.setText(prediction)
    
    def show_model_summary(self):
        self.summary_window = ModelSummaryWindow(self.model)
        self.summary_window.show()
        self.close()

class ModelSummaryWindow(QDialog):
    def __init__(self, model:Model):
        super(ModelSummaryWindow, self).__init__()
        self.model = model

        self.ui = nuaction.Ui_Form()
        self.ui.setupUi(self)

        self.summary_text = ""
        self.model.summary(self.print_summary)

        self.ui.nameView.setText(self.model.name)
        self.ui.saveButton.clicked.connect(self.save_model)
        self.ui.summaryView.setText(self.summary_text)
        self.ui.trainTestButton.clicked.connect(self.show_train_test)
        self.ui.predictButton.clicked.connect(self.show_predict)
        self.ui.backButton.clicked.connect(self.show_model_config)
    
    def print_summary(self, line):
        self.summary_text += line + '\n'
    
    def save_model(self):
        name = self.ui.nameView.text()
        path, _ = QFileDialog.getSaveFileName(self, "Save Model As", name)
        
        if path:
            self.disable_inputs()
            self.save_model_thread = SaveModelThread(path, self.model)
            self.save_model_thread.finished.connect(self.enable_inputs)
            self.save_model_thread.start()
    
    def show_train_test(self):
        self.train_test_window = TrainTestWindow(self.model)
        self.train_test_window.show()
        self.close()
    
    def show_predict(self):
        self.predict_window = PredictWindow(self.model)
        self.predict_window.show()
        self.close()
    
    def show_model_config(self):
        self.config_window = ModelConfigWindow()
        self.config_window.show()
        self.close()
    
    def disable_inputs(self):
        self.ui.nameView.setDisabled(True)
        self.ui.saveButton.setDisabled(True)
        self.ui.summaryView.setDisabled(True)
        self.ui.trainTestButton.setDisabled(True)
        self.ui.predictButton.setDisabled(True)
        self.ui.backButton.setDisabled(True)
    
    def enable_inputs(self):
        self.ui.nameView.setText(self.model.name)
        self.ui.nameView.setEnabled(True)
        self.ui.saveButton.setEnabled(True)
        self.ui.summaryView.setEnabled(True)
        self.ui.trainTestButton.setEnabled(True)
        self.ui.predictButton.setEnabled(True)
        self.ui.backButton.setEnabled(True)

class ModelConfigWindow(QDialog):
    def __init__(self):
        super(ModelConfigWindow, self).__init__()
        self.ui = numain.Ui_Form()
        self.ui.setupUi(self)
        self.ui.loadModelButton.clicked.connect(self.load_model)
        self.ui.corpusSelectButton.clicked.connect(self.load_corpus)
        self.ui.embeddingsSelectButton.clicked.connect(self.get_embeddings_path)
        self.ui.compileButton.clicked.connect(self.start_compile)

    def load_model(self):
        model_path = QFileDialog.getExistingDirectory(self, "Select Model Directory", "")
        if model_path:
            self.loading_thread = LoadingModelThread(model_path)
            self.loading_thread.finished.connect(self.show_model_summary)
            self.loading_thread.start()
            self.disable_inputs()

    def load_corpus(self):
        dataset_path, _ = QFileDialog.getOpenFileName(self, "Select Dataset File", "", "JSON files (*.json *.jsonl)")
        self.corpus = Dataset.from_json(dataset_path)
        self.ui.corpusTextView.setText(f'{self.corpus.name} - {self.corpus.total()}')
        self.ui.corpusTextView.setEnabled(True)

    def get_embeddings_path(self):
        embeddings_path, _ = QFileDialog.getOpenFileName(self, "Select Embeddings File", "", "Text files (*.txt)")
        if embeddings_path:
            self.embeddings_path = embeddings_path
            embeddings_name = self.embeddings_path.split('/')[-1]
            self.ui.embeddingsTextView.setText(embeddings_name)
            self.ui.embeddingsTextView.setEnabled(True)
    
    def get_kernel_sizes(self):
        kernel_sizes_text = self.ui.kernelSizeTextInput.toPlainText()
        kernel_sizes = [int(size.strip()) for size in kernel_sizes_text.split(",") if size]
        return kernel_sizes

    def start_compile(self):
        self.loading_thread = CompilingThread(
            corpus = self.corpus,
            embeddings_path = self.embeddings_path,
            filters = self.ui.filtersSpinBox.value(),
            kernel_sizes = self.get_kernel_sizes(),
            dropout = self.ui.dropoutSpinBox.value(),
        )

        self.loading_thread.finished.connect(self.show_model_summary)
        self.loading_thread.start()
        self.disable_inputs()
    
    def disable_inputs(self):
        self.ui.loadModelButton.setDisabled(True)
        self.ui.corpusTextView.setDisabled(True)
        self.ui.corpusSelectButton.setDisabled(True)
        self.ui.embeddingsTextView.setDisabled(True)
        self.ui.embeddingsSelectButton.setDisabled(True)
        self.ui.filtersSpinBox.setDisabled(True)
        self.ui.kernelSizeTextInput.setDisabled(True)
        self.ui.dropoutSpinBox.setDisabled(True)
        self.ui.compileButton.setDisabled(True)
    
    def enable_inputs(self):
        self.ui.loadModelButton.setEnabled(True)
        self.ui.corpusTextView.setEnabled(True)
        self.ui.corpusSelectButton.setEnabled(True)
        self.ui.embeddingsTextView.setEnabled(True)
        self.ui.embeddingsSelectButton.setEnabled(True)
        self.ui.filtersSpinBox.setEnabled(True)
        self.ui.kernelSizeTextInput.setEnabled(True)
        self.ui.dropoutSpinBox.setEnabled(True)
        self.ui.compileButton.setEnabled(True)
    
    def show_model_summary(self, model:Model):
        if model is None:
            print("Error when loading/compiling model")
            self.enable_inputs()
        else:
            self.summary_window = ModelSummaryWindow(model)
            self.summary_window.show()
            self.close()

def main():
    app = QApplication(sys.argv)
    form = ModelConfigWindow()
    form.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()