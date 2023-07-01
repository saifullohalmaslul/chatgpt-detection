# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuaction.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(827, 392)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.nameView = QLineEdit(Form)
        self.nameView.setObjectName(u"nameView")
        self.nameView.setMinimumSize(QSize(200, 0))
        self.nameView.setMaximumSize(QSize(200, 16777215))
        self.nameView.setReadOnly(False)

        self.horizontalLayout.addWidget(self.nameView)

        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.saveButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.backButton = QPushButton(Form)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout.addWidget(self.backButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.summaryView = QTextEdit(Form)
        self.summaryView.setObjectName(u"summaryView")
        self.summaryView.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Cascadia Code"])
        self.summaryView.setFont(font)
        self.summaryView.setReadOnly(True)
        self.summaryView.setAcceptRichText(False)

        self.verticalLayout_3.addWidget(self.summaryView)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.trainTestButton = QPushButton(Form)
        self.trainTestButton.setObjectName(u"trainTestButton")

        self.verticalLayout.addWidget(self.trainTestButton)

        self.crossValButton = QPushButton(Form)
        self.crossValButton.setObjectName(u"crossValButton")

        self.verticalLayout.addWidget(self.crossValButton)

        self.predictButton = QPushButton(Form)
        self.predictButton.setObjectName(u"predictButton")

        self.verticalLayout.addWidget(self.predictButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Model Summary - Select Action", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save Model..", None))
        self.backButton.setText(QCoreApplication.translate("Form", u"Back to Model Config", None))
        self.trainTestButton.setText(QCoreApplication.translate("Form", u"Train-Test", None))
        self.crossValButton.setText(QCoreApplication.translate("Form", u"Cross Validation", None))
        self.predictButton.setText(QCoreApplication.translate("Form", u"Predict", None))
    # retranslateUi

