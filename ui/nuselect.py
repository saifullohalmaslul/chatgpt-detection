# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuselect.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDoubleSpinBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLayout,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 303)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loadDatasetButton = QPushButton(Form)
        self.loadDatasetButton.setObjectName(u"loadDatasetButton")

        self.verticalLayout.addWidget(self.loadDatasetButton)

        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMinimumSize(QSize(380, 0))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setVisible(True)

        self.verticalLayout.addWidget(self.tableWidget)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.selectDatasetButton = QPushButton(Form)
        self.selectDatasetButton.setObjectName(u"selectDatasetButton")
        self.selectDatasetButton.setEnabled(False)
        self.selectDatasetButton.setAutoDefault(False)
        self.selectDatasetButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.selectDatasetButton)

        self.saveDatasetButton = QPushButton(Form)
        self.saveDatasetButton.setObjectName(u"saveDatasetButton")
        self.saveDatasetButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.saveDatasetButton)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ratioSpinBox = QDoubleSpinBox(self.groupBox)
        self.ratioSpinBox.setObjectName(u"ratioSpinBox")
        self.ratioSpinBox.setEnabled(False)
        self.ratioSpinBox.setMinimum(0.050000000000000)
        self.ratioSpinBox.setMaximum(0.950000000000000)
        self.ratioSpinBox.setSingleStep(0.050000000000000)

        self.horizontalLayout.addWidget(self.ratioSpinBox)

        self.splitButton = QPushButton(self.groupBox)
        self.splitButton.setObjectName(u"splitButton")
        self.splitButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.splitButton)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        self.selectDatasetButton.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Dataset Selection", None))
        self.loadDatasetButton.setText(QCoreApplication.translate("Form", u"Load Dataset", None))
        self.selectDatasetButton.setText(QCoreApplication.translate("Form", u"Select", None))
        self.saveDatasetButton.setText(QCoreApplication.translate("Form", u"Save to File", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Split dataset", None))
        self.splitButton.setText(QCoreApplication.translate("Form", u"Split", None))
    # retranslateUi

