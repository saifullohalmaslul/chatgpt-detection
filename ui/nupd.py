# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nupd.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(363, 136)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.predictionView = QLineEdit(Form)
        self.predictionView.setObjectName(u"predictionView")
        self.predictionView.setReadOnly(True)

        self.gridLayout.addWidget(self.predictionView, 0, 0, 1, 1)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 2, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.predictButton = QPushButton(Form)
        self.predictButton.setObjectName(u"predictButton")

        self.verticalLayout_3.addWidget(self.predictButton)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 2, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setMinimumSize(QSize(0, 30))
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit.setReadOnly(False)
        self.textEdit.setAcceptRichText(False)

        self.verticalLayout.addWidget(self.textEdit)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.backButton = QPushButton(Form)
        self.backButton.setObjectName(u"backButton")

        self.gridLayout.addWidget(self.backButton, 3, 0, 1, 3)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Predict", None))
        self.predictionView.setPlaceholderText("")
        self.predictButton.setText(QCoreApplication.translate("Form", u"Predict", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter text here...", None))
        self.backButton.setText(QCoreApplication.translate("Form", u"Back to Model Summary", None))
    # retranslateUi

