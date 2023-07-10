import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QWidget, QTableWidgetItem
from PySide6.QtCore import QThread, Signal, QTimer
from ui import numain, nuaction, nuselect, nuresult, nutt, nucv, nupd

from model import Model
from dataset import Dataset, DatasetSelection

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

class CrossValidationThread(QThread):
    finished = Signal(tuple)

    def __init__(self, model:Model, dataset:Dataset, batch_size:int, epochs:int):
        super(CrossValidationThread, self).__init__()
        self.model = model
        self.dataset = dataset
        self.batch_size = batch_size
        self.epochs = epochs

    def run(self):
        metrics = None
        try:
            metrics = self.model.kfold(self.dataset, self.batch_size, self.epochs)
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

class DatasetSelectionWindow(QWidget):
    select = Signal(Dataset)

    def __init__(self, caller, slot):
        super(DatasetSelectionWindow, self).__init__()
        self.ui = nuselect.Ui_Form()
        self.ui.setupUi(self)

        self.caller = caller

        columnHeader = ["Name", "Count"]
        self.ui.tableWidget.setColumnCount(len(columnHeader))
        self.ui.tableWidget.setHorizontalHeaderLabels(columnHeader)

        self.ui.loadDatasetButton.clicked.connect(self.add_dataset)
        self.ui.selectDatasetButton.clicked.connect(self.select_dataset)
        self.ui.saveDatasetButton.clicked.connect(self.save_dataset)
        self.ui.splitButton.clicked.connect(self.split_dataset)
        self.select.connect(slot)

        if len(dataset_selections.datasets) > 0:
            self.refresh_table()
    
    @classmethod
    def get_dataset(cls, caller, slot):
        caller.dataset_selection_window = cls(caller, slot)
        caller.dataset_selection_window.show()
    
    def select_dataset(self):
        dataset = dataset_selections.get(self.ui.tableWidget.currentRow())
        self.caller.dataset_selection_window.close()
        del self.caller.dataset_selection_window
        self.select.emit(dataset)
    
    def save_dataset(self):
        dataset = dataset_selections.get(self.ui.tableWidget.currentRow())
        path, _ = QFileDialog.getSaveFileName(self, "Save Dataset As", dataset.name, "JSON files (*.json *.jsonl)")
        
        if path:
            name = path.split('/')[-1]
            dataset.save(path)
            dataset.name = name
            self.refresh_table()

    def add_dataset(self):
        dataset_path, _ = QFileDialog.getOpenFileName(self, "Select Dataset File", "", "JSON files (*.json *.jsonl)")
        dataset_selections.add(dataset_path)
        self.refresh_table()
    
    def split_dataset(self):
        index = self.ui.tableWidget.currentRow()
        ratio = self.ui.ratioSpinBox.value()
        dataset_selections.split(index, ratio)
        self.refresh_table()
    
    def refresh_table(self):
        self.ui.tableWidget.setRowCount(len(dataset_selections.datasets))
        for i, dataset in enumerate(dataset_selections.datasets):
            dataset_name = QTableWidgetItem(dataset.name)
            dataset_count = QTableWidgetItem(str(dataset.total()))
            self.ui.tableWidget.setItem(i, 0, dataset_name)
            self.ui.tableWidget.setItem(i, 1, dataset_count)
        
        self.ui.selectDatasetButton.setEnabled(True)
        self.ui.saveDatasetButton.setEnabled(True)
        self.ui.ratioSpinBox.setEnabled(True)
        self.ui.splitButton.setEnabled(True)

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

        self.ui.trainSelectButton.clicked.connect(lambda: DatasetSelectionWindow.get_dataset(self, self.load_train_data))
        self.ui.testSelectButton.clicked.connect(lambda: DatasetSelectionWindow.get_dataset(self, self.load_test_data))
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
    
    def load_train_data(self, dataset:Dataset):
        self.train_data = dataset
        self.ui.trainDatasetView.setText(f'{self.train_data.name} - {self.train_data.total()}')
        self.ui.trainDatasetView.setEnabled(True)

        self.train_loaded = True
        if self.train_loaded and self.test_loaded:
            self.ui.pushButton.setEnabled(True)
    
    def load_test_data(self, dataset:Dataset):
        self.test_data = dataset
        self.ui.testDatasetView.setText(f'{self.test_data.name} - {self.test_data.total()}')
        self.ui.testDatasetView.setEnabled(True)

        self.test_loaded = True
        if self.train_loaded and self.test_loaded:
            self.ui.pushButton.setEnabled(True)
    
    def show_model_summary(self):
        self.summary_window = ModelSummaryWindow(self.model)
        self.summary_window.show()
        self.close()

class CrossValidationWindow(QDialog):
    def __init__(self, model:Model):
        super(CrossValidationWindow, self).__init__()
        self.ui = nucv.Ui_Form()
        self.ui.setupUi(self)
        self.ui.datasetSelectButton.clicked.connect(lambda: DatasetSelectionWindow.get_dataset(self, self.load_dataset))
        self.ui.pushButton.clicked.connect(self.start_cross_validation)
        self.ui.backButton.clicked.connect(self.show_model_summary)

        self.model = model
    
    def load_dataset(self, dataset:Dataset):
        self.dataset = dataset
        self.ui.datasetView.setText(f'{self.dataset.name} - {self.dataset.total()}')
        self.ui.datasetView.setEnabled(True)

        self.ui.pushButton.setEnabled(True)
    
    def show_model_summary(self):
        self.summary_window = ModelSummaryWindow(self.model)
        self.summary_window.show()
        self.close()
    
    def start_cross_validation(self):
        self.cross_validation_thread = CrossValidationThread(
            self.model,
            self.dataset,
            self.ui.batchSpinBox.value(),
            self.ui.epochsSpinBox.value()
        )

        self.cross_validation_thread.finished.connect(self.show_result)
        self.cross_validation_thread.start()
        self.disable_inputs()
    
    def show_result(self, result:tuple):
        if result is None:
            self.enable_inputs()
        else:
            self.result_window = ResultWindow(self.model, result)
            self.result_window.show()
            self.close()
    
    def disable_inputs(self):
        self.ui.datasetView.setDisabled(True)
        self.ui.datasetSelectButton.setDisabled(True)
        self.ui.batchSpinBox.setDisabled(True)
        self.ui.epochsSpinBox.setDisabled(True)
        self.ui.pushButton.setDisabled(True)
        self.ui.backButton.setDisabled(True)
    
    def enable_inputs(self):
        self.ui.datasetView.setEnabled(True)
        self.ui.datasetSelectButton.setEnabled(True)
        self.ui.batchSpinBox.setEnabled(True)
        self.ui.epochsSpinBox.setEnabled(True)
        self.ui.pushButton.setEnabled(True)
        self.ui.backButton.setEnabled(True)

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
        self.ui.crossValButton.clicked.connect(self.show_cross_validation)
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
    
    def show_cross_validation(self):
        self.cross_validation_window = CrossValidationWindow(self.model)
        self.cross_validation_window.show()
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
        self.ui.crossValButton.setDisabled(True)
        self.ui.predictButton.setDisabled(True)
        self.ui.backButton.setDisabled(True)
    
    def enable_inputs(self):
        self.ui.nameView.setText(self.model.name)
        self.ui.nameView.setEnabled(True)
        self.ui.saveButton.setEnabled(True)
        self.ui.summaryView.setEnabled(True)
        self.ui.trainTestButton.setEnabled(True)
        self.ui.crossValButton.setEnabled(True)
        self.ui.predictButton.setEnabled(True)
        self.ui.backButton.setEnabled(True)

class ModelConfigWindow(QDialog):
    def __init__(self):
        super(ModelConfigWindow, self).__init__()
        self.ui = numain.Ui_Form()
        self.ui.setupUi(self)
        self.ui.loadModelButton.clicked.connect(self.load_model)
        self.ui.corpusSelectButton.clicked.connect(lambda: DatasetSelectionWindow.get_dataset(self, self.load_corpus))
        self.ui.embeddingsSelectButton.clicked.connect(self.get_embeddings_path)
        self.ui.compileButton.clicked.connect(self.start_compile)

    def load_model(self):
        model_path = QFileDialog.getExistingDirectory(self, "Select Model Directory", "")
        if model_path:
            self.loading_thread = LoadingModelThread(model_path)
            self.loading_thread.finished.connect(self.show_model_summary)
            self.loading_thread.start()
            self.disable_inputs()

    def load_corpus(self, corpus:Dataset):
        self.corpus = corpus
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
    dataset_selections = DatasetSelection()
    main()