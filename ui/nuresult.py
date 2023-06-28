# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuresult.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(342, 292)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.resultGroup = QGroupBox(Form)
        self.resultGroup.setObjectName(u"resultGroup")
        self.verticalLayout = QVBoxLayout(self.resultGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.confusionTable = QTableWidget(self.resultGroup)
        if (self.confusionTable.columnCount() < 2):
            self.confusionTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.confusionTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.confusionTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.confusionTable.rowCount() < 2):
            self.confusionTable.setRowCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.confusionTable.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.confusionTable.setVerticalHeaderItem(1, __qtablewidgetitem3)
        self.confusionTable.setObjectName(u"confusionTable")
        self.confusionTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.confusionTable.setShowGrid(True)
        self.confusionTable.setWordWrap(True)
        self.confusionTable.horizontalHeader().setStretchLastSection(True)
        self.confusionTable.verticalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.confusionTable)

        self.line = QFrame(self.resultGroup)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.resultGroup)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.resultGroup)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.resultGroup)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_4 = QLabel(self.resultGroup)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.accuracyText = QTextEdit(self.resultGroup)
        self.accuracyText.setObjectName(u"accuracyText")
        self.accuracyText.setMaximumSize(QSize(16777215, 80))
        self.accuracyText.setReadOnly(True)

        self.gridLayout.addWidget(self.accuracyText, 1, 0, 1, 1)

        self.precisionText = QTextEdit(self.resultGroup)
        self.precisionText.setObjectName(u"precisionText")
        self.precisionText.setMaximumSize(QSize(16777215, 80))
        self.precisionText.setReadOnly(True)

        self.gridLayout.addWidget(self.precisionText, 1, 1, 1, 1)

        self.recallText = QTextEdit(self.resultGroup)
        self.recallText.setObjectName(u"recallText")
        self.recallText.setMaximumSize(QSize(16777215, 80))
        self.recallText.setReadOnly(True)

        self.gridLayout.addWidget(self.recallText, 1, 2, 1, 1)

        self.fscoreText = QTextEdit(self.resultGroup)
        self.fscoreText.setObjectName(u"fscoreText")
        self.fscoreText.setMaximumSize(QSize(16777215, 80))
        self.fscoreText.setReadOnly(True)

        self.gridLayout.addWidget(self.fscoreText, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.resultGroup)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.backButton = QPushButton(Form)
        self.backButton.setObjectName(u"backButton")

        self.verticalLayout_2.addWidget(self.backButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Result", None))
        self.resultGroup.setTitle(QCoreApplication.translate("Form", u"Result", None))
        ___qtablewidgetitem = self.confusionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Predicted Human", None));
        ___qtablewidgetitem1 = self.confusionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Predicted ChatGPT", None));
        ___qtablewidgetitem2 = self.confusionTable.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Actual Human", None));
        ___qtablewidgetitem3 = self.confusionTable.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Actual ChatGPT", None));
        self.label.setText(QCoreApplication.translate("Form", u"Accuracy", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Precision", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Recall", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"F1-score", None))
        self.backButton.setText(QCoreApplication.translate("Form", u"Back to Model Summary", None))
    # retranslateUi

