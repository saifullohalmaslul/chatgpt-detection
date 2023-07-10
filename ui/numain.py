# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'numain.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(301, 390)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.loadModelButton = QPushButton(Form)
        self.loadModelButton.setObjectName(u"loadModelButton")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadModelButton.sizePolicy().hasHeightForWidth())
        self.loadModelButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.loadModelButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.corpusTextView = QTextEdit(self.groupBox)
        self.corpusTextView.setObjectName(u"corpusTextView")
        self.corpusTextView.setEnabled(False)
        self.corpusTextView.setMaximumSize(QSize(16777215, 30))
        self.corpusTextView.setReadOnly(True)

        self.verticalLayout.addWidget(self.corpusTextView)

        self.corpusSelectButton = QPushButton(self.groupBox)
        self.corpusSelectButton.setObjectName(u"corpusSelectButton")

        self.verticalLayout.addWidget(self.corpusSelectButton)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.filtersSpinBox = QSpinBox(self.groupBox)
        self.filtersSpinBox.setObjectName(u"filtersSpinBox")
        self.filtersSpinBox.setMinimum(1)
        self.filtersSpinBox.setMaximum(999)

        self.gridLayout.addWidget(self.filtersSpinBox, 4, 1, 1, 1)

        self.kernelSizeTextInput = QTextEdit(self.groupBox)
        self.kernelSizeTextInput.setObjectName(u"kernelSizeTextInput")

        self.gridLayout.addWidget(self.kernelSizeTextInput, 5, 1, 1, 1)

        self.dropoutSpinBox = QDoubleSpinBox(self.groupBox)
        self.dropoutSpinBox.setObjectName(u"dropoutSpinBox")
        self.dropoutSpinBox.setMaximum(1.000000000000000)
        self.dropoutSpinBox.setSingleStep(0.100000000000000)

        self.gridLayout.addWidget(self.dropoutSpinBox, 6, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.embeddingsTextView = QTextEdit(self.groupBox)
        self.embeddingsTextView.setObjectName(u"embeddingsTextView")
        self.embeddingsTextView.setEnabled(False)
        self.embeddingsTextView.setMaximumSize(QSize(16777215, 30))
        self.embeddingsTextView.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.embeddingsTextView)

        self.embeddingsSelectButton = QPushButton(self.groupBox)
        self.embeddingsSelectButton.setObjectName(u"embeddingsSelectButton")

        self.verticalLayout_3.addWidget(self.embeddingsSelectButton)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 1, 1, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 2)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 3, 0, 1, 2)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.compileButton = QPushButton(Form)
        self.compileButton.setObjectName(u"compileButton")

        self.horizontalLayout_9.addWidget(self.compileButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        QWidget.setTabOrder(self.loadModelButton, self.corpusTextView)
        QWidget.setTabOrder(self.corpusTextView, self.corpusSelectButton)
        QWidget.setTabOrder(self.corpusSelectButton, self.embeddingsTextView)
        QWidget.setTabOrder(self.embeddingsTextView, self.embeddingsSelectButton)
        QWidget.setTabOrder(self.embeddingsSelectButton, self.filtersSpinBox)
        QWidget.setTabOrder(self.filtersSpinBox, self.kernelSizeTextInput)
        QWidget.setTabOrder(self.kernelSizeTextInput, self.dropoutSpinBox)
        QWidget.setTabOrder(self.dropoutSpinBox, self.compileButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Model Config", None))
        self.loadModelButton.setText(QCoreApplication.translate("Form", u"Load Model..", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Hyperparameters", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"embeddings", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"corpus", None))
        self.corpusSelectButton.setText(QCoreApplication.translate("Form", u"Select Dataset..", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"filters", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"dropout", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"kernel_sizes", None))
        self.kernelSizeTextInput.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.kernelSizeTextInput.setPlaceholderText(QCoreApplication.translate("Form", u"1,2,...", None))
        self.embeddingsSelectButton.setText(QCoreApplication.translate("Form", u"Select File..", None))
        self.compileButton.setText(QCoreApplication.translate("Form", u"Compile", None))
    # retranslateUi

