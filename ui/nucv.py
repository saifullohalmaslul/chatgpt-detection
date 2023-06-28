# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nucv.ui'
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
        Form.resize(357, 151)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.datasetView = QTextEdit(Form)
        self.datasetView.setObjectName(u"datasetView")
        self.datasetView.setEnabled(False)
        self.datasetView.setMinimumSize(QSize(0, 30))
        self.datasetView.setMaximumSize(QSize(16777215, 16777215))
        self.datasetView.setReadOnly(True)

        self.verticalLayout.addWidget(self.datasetView)

        self.datasetSelectButton = QPushButton(Form)
        self.datasetSelectButton.setObjectName(u"datasetSelectButton")

        self.verticalLayout.addWidget(self.datasetSelectButton)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 2, 0, 1, 1)

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


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

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


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)

        self.gridLayout.addWidget(self.pushButton, 4, 2, 1, 1)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 5, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Cross Validation", None))
        self.datasetSelectButton.setText(QCoreApplication.translate("Form", u"Select Dataset", None))
        self.label.setText(QCoreApplication.translate("Form", u"batch_size", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"epochs", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Cross validate", None))
    # retranslateUi

