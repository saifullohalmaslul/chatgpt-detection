# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nutt.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(359, 218)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.epochsSpinBox = QSpinBox(Form)
        self.epochsSpinBox.setObjectName(u"epochsSpinBox")
        self.epochsSpinBox.setMinimum(1)
        self.epochsSpinBox.setMaximum(999)

        self.horizontalLayout.addWidget(self.epochsSpinBox)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.batchSpinBox = QSpinBox(Form)
        self.batchSpinBox.setObjectName(u"batchSpinBox")
        self.batchSpinBox.setMinimum(1)
        self.batchSpinBox.setMaximum(99999)

        self.horizontalLayout_2.addWidget(self.batchSpinBox)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.trainDatasetView = QTextEdit(Form)
        self.trainDatasetView.setObjectName(u"trainDatasetView")
        self.trainDatasetView.setEnabled(False)
        self.trainDatasetView.setMinimumSize(QSize(0, 30))
        self.trainDatasetView.setMaximumSize(QSize(16777215, 16777215))
        self.trainDatasetView.setReadOnly(True)

        self.verticalLayout.addWidget(self.trainDatasetView)

        self.trainSelectButton = QPushButton(Form)
        self.trainSelectButton.setObjectName(u"trainSelectButton")

        self.verticalLayout.addWidget(self.trainSelectButton)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.testDatasetView = QTextEdit(Form)
        self.testDatasetView.setObjectName(u"testDatasetView")
        self.testDatasetView.setEnabled(False)
        self.testDatasetView.setMinimumSize(QSize(0, 30))
        self.testDatasetView.setMaximumSize(QSize(16777215, 16777215))
        self.testDatasetView.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.testDatasetView)

        self.testSelectButton = QPushButton(Form)
        self.testSelectButton.setObjectName(u"testSelectButton")

        self.verticalLayout_2.addWidget(self.testSelectButton)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)

        self.gridLayout.addWidget(self.pushButton, 5, 2, 1, 1)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 6, 1)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Train/Test", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"epochs", None))
        self.label.setText(QCoreApplication.translate("Form", u"batch_size", None))
        self.trainSelectButton.setText(QCoreApplication.translate("Form", u"Select Train Dataset", None))
        self.testSelectButton.setText(QCoreApplication.translate("Form", u"Select Test Dataset", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Train-Test", None))
    # retranslateUi

