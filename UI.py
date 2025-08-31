# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ModBusSim.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1070, 607)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1070, 607))
        MainWindow.setMaximumSize(QSize(1070, 607))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Seperator01 = QFrame(self.centralwidget)
        self.Seperator01.setObjectName(u"Seperator01")
        self.Seperator01.setGeometry(QRect(10, 30, 1211, 16))
        self.Seperator01.setFrameShape(QFrame.HLine)
        self.Seperator01.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 241, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblProject = QLabel(self.layoutWidget)
        self.lblProject.setObjectName(u"lblProject")
        self.lblProject.setMaximumSize(QSize(42, 20))

        self.horizontalLayout.addWidget(self.lblProject)

        self.lblProjectName = QLabel(self.layoutWidget)
        self.lblProjectName.setObjectName(u"lblProjectName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblProjectName.sizePolicy().hasHeightForWidth())
        self.lblProjectName.setSizePolicy(sizePolicy1)
        self.lblProjectName.setMaximumSize(QSize(16777215, 16777215))
        self.lblProjectName.setStyleSheet(u"")
        self.lblProjectName.setFrameShape(QFrame.WinPanel)
        self.lblProjectName.setFrameShadow(QFrame.Sunken)
        self.lblProjectName.setLineWidth(1)

        self.horizontalLayout.addWidget(self.lblProjectName)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(270, 10, 111, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lblServinfo01 = QLabel(self.horizontalLayoutWidget)
        self.lblServinfo01.setObjectName(u"lblServinfo01")
        self.lblServinfo01.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lblServinfo01.sizePolicy().hasHeightForWidth())
        self.lblServinfo01.setSizePolicy(sizePolicy2)
        self.lblServinfo01.setMaximumSize(QSize(38, 20))

        self.horizontalLayout_2.addWidget(self.lblServinfo01)

        self.lblServStatus = QLabel(self.horizontalLayoutWidget)
        self.lblServStatus.setObjectName(u"lblServStatus")
        self.lblServStatus.setBaseSize(QSize(0, 0))
        self.lblServStatus.setFrameShape(QFrame.WinPanel)
        self.lblServStatus.setFrameShadow(QFrame.Sunken)
        self.lblServStatus.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lblServStatus)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(400, 10, 151, 22))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lblSevInfo02 = QLabel(self.horizontalLayoutWidget_2)
        self.lblSevInfo02.setObjectName(u"lblSevInfo02")
        self.lblSevInfo02.setMinimumSize(QSize(0, 0))
        self.lblSevInfo02.setMaximumSize(QSize(58, 20))

        self.horizontalLayout_3.addWidget(self.lblSevInfo02)

        self.lblServIP = QLabel(self.horizontalLayoutWidget_2)
        self.lblServIP.setObjectName(u"lblServIP")
        self.lblServIP.setFrameShape(QFrame.WinPanel)
        self.lblServIP.setFrameShadow(QFrame.Sunken)
        self.lblServIP.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lblServIP)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(570, 10, 61, 22))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lblSevInfo03 = QLabel(self.horizontalLayoutWidget_3)
        self.lblSevInfo03.setObjectName(u"lblSevInfo03")
        self.lblSevInfo03.setMinimumSize(QSize(0, 0))
        self.lblSevInfo03.setMaximumSize(QSize(25, 20))

        self.horizontalLayout_4.addWidget(self.lblSevInfo03)

        self.lblServPort = QLabel(self.horizontalLayoutWidget_3)
        self.lblServPort.setObjectName(u"lblServPort")
        self.lblServPort.setFrameShape(QFrame.WinPanel)
        self.lblServPort.setFrameShadow(QFrame.Sunken)
        self.lblServPort.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lblServPort)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 50, 243, 131))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblDevDesc01 = QLabel(self.formLayoutWidget)
        self.lblDevDesc01.setObjectName(u"lblDevDesc01")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblDevDesc01)

        self.cmbPlace = QComboBox(self.formLayoutWidget)
        self.cmbPlace.setObjectName(u"cmbPlace")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cmbPlace)

        self.lblDevDesc02 = QLabel(self.formLayoutWidget)
        self.lblDevDesc02.setObjectName(u"lblDevDesc02")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblDevDesc02)

        self.lblDeviceType = QLabel(self.formLayoutWidget)
        self.lblDeviceType.setObjectName(u"lblDeviceType")
        self.lblDeviceType.setFrameShape(QFrame.Box)
        self.lblDeviceType.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lblDeviceType)

        self.lblDevDesc04 = QLabel(self.formLayoutWidget)
        self.lblDevDesc04.setObjectName(u"lblDevDesc04")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lblDevDesc04)

        self.spnSimScale = QSpinBox(self.formLayoutWidget)
        self.spnSimScale.setObjectName(u"spnSimScale")
        self.spnSimScale.setMaximumSize(QSize(50, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spnSimScale)

        self.lblDevDesc05 = QLabel(self.formLayoutWidget)
        self.lblDevDesc05.setObjectName(u"lblDevDesc05")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lblDevDesc05)

        self.chkSimulate = QCheckBox(self.formLayoutWidget)
        self.chkSimulate.setObjectName(u"chkSimulate")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.chkSimulate)

        self.lblPreloadDesc = QLabel(self.formLayoutWidget)
        self.lblPreloadDesc.setObjectName(u"lblPreloadDesc")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lblPreloadDesc)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.chkPreloadSettings = QCheckBox(self.formLayoutWidget)
        self.chkPreloadSettings.setObjectName(u"chkPreloadSettings")

        self.horizontalLayout_13.addWidget(self.chkPreloadSettings)

        self.chkPreloadAnalog = QCheckBox(self.formLayoutWidget)
        self.chkPreloadAnalog.setObjectName(u"chkPreloadAnalog")

        self.horizontalLayout_13.addWidget(self.chkPreloadAnalog)

        self.chkPreloadStatus = QCheckBox(self.formLayoutWidget)
        self.chkPreloadStatus.setObjectName(u"chkPreloadStatus")

        self.horizontalLayout_13.addWidget(self.chkPreloadStatus)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_13)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 190, 241, 411))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblDeviceInfo01 = QLabel(self.verticalLayoutWidget)
        self.lblDeviceInfo01.setObjectName(u"lblDeviceInfo01")

        self.verticalLayout.addWidget(self.lblDeviceInfo01)

        self.treeDevices = QTreeWidget(self.verticalLayoutWidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeDevices.setHeaderItem(__qtreewidgetitem)
        self.treeDevices.setObjectName(u"treeDevices")
        self.treeDevices.setIndentation(20)
        self.treeDevices.setItemsExpandable(True)
        self.treeDevices.setHeaderHidden(True)

        self.verticalLayout.addWidget(self.treeDevices)

        self.grpStatus01 = QGroupBox(self.centralwidget)
        self.grpStatus01.setObjectName(u"grpStatus01")
        self.grpStatus01.setGeometry(QRect(270, 50, 251, 271))
        self.grpStatus01.setAutoFillBackground(False)
        self.grpStatus01.setStyleSheet(u"QGroupBox {\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"	margin-top:0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	top:-9;\n"
"	left:10px;\n"
"}")
        self.grpStatus01.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.grpStatus01.setFlat(False)
        self.grpStatus01.setCheckable(False)
        self.gridLayoutWidget = QWidget(self.grpStatus01)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 239, 241))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.chkStatus01_05 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_05.setObjectName(u"chkStatus01_05")

        self.gridLayout.addWidget(self.chkStatus01_05, 5, 0, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 8, 0, 1, 1)

        self.chkStatus01_12 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_12.setObjectName(u"chkStatus01_12")
        self.chkStatus01_12.setMinimumSize(QSize(110, 0))
        self.chkStatus01_12.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.chkStatus01_12, 4, 1, 1, 1)

        self.chkStatus01_14 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_14.setObjectName(u"chkStatus01_14")
        self.chkStatus01_14.setMinimumSize(QSize(110, 0))
        self.chkStatus01_14.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.chkStatus01_14, 6, 1, 1, 1)

        self.chkStatus01_09 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_09.setObjectName(u"chkStatus01_09")
        self.chkStatus01_09.setMinimumSize(QSize(110, 0))
        self.chkStatus01_09.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.chkStatus01_09, 1, 1, 1, 1)

        self.chkStatus01_00 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_00.setObjectName(u"chkStatus01_00")
        self.chkStatus01_00.setMinimumSize(QSize(110, 0))
        self.chkStatus01_00.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.chkStatus01_00, 0, 0, 1, 1)

        self.chkStatus01_04 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_04.setObjectName(u"chkStatus01_04")

        self.gridLayout.addWidget(self.chkStatus01_04, 4, 0, 1, 1)

        self.chkStatus01_13 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_13.setObjectName(u"chkStatus01_13")
        self.chkStatus01_13.setMinimumSize(QSize(110, 0))
        self.chkStatus01_13.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.chkStatus01_13, 5, 1, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 8, 1, 1, 1)

        self.chkStatus01_03 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_03.setObjectName(u"chkStatus01_03")

        self.gridLayout.addWidget(self.chkStatus01_03, 3, 0, 1, 1)

        self.chkStatus01_10 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_10.setObjectName(u"chkStatus01_10")
        self.chkStatus01_10.setMinimumSize(QSize(110, 0))
        self.chkStatus01_10.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.chkStatus01_10, 2, 1, 1, 1)

        self.chkStatus01_06 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_06.setObjectName(u"chkStatus01_06")

        self.gridLayout.addWidget(self.chkStatus01_06, 6, 0, 1, 1)

        self.chkStatus01_15 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_15.setObjectName(u"chkStatus01_15")
        self.chkStatus01_15.setMinimumSize(QSize(110, 0))
        self.chkStatus01_15.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.chkStatus01_15, 7, 1, 1, 1)

        self.chkStatus01_08 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_08.setObjectName(u"chkStatus01_08")
        self.chkStatus01_08.setMinimumSize(QSize(110, 0))
        self.chkStatus01_08.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.chkStatus01_08, 0, 1, 1, 1)

        self.chkStatus01_01 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_01.setObjectName(u"chkStatus01_01")

        self.gridLayout.addWidget(self.chkStatus01_01, 1, 0, 1, 1)

        self.chkStatus01_02 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_02.setObjectName(u"chkStatus01_02")

        self.gridLayout.addWidget(self.chkStatus01_02, 2, 0, 1, 1)

        self.chkStatus01_07 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_07.setObjectName(u"chkStatus01_07")

        self.gridLayout.addWidget(self.chkStatus01_07, 7, 0, 1, 1)

        self.chkStatus01_11 = QCheckBox(self.gridLayoutWidget)
        self.chkStatus01_11.setObjectName(u"chkStatus01_11")
        self.chkStatus01_11.setMinimumSize(QSize(110, 0))
        self.chkStatus01_11.setMaximumSize(QSize(110, 16777215))

        self.gridLayout.addWidget(self.chkStatus01_11, 3, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblStatDesc = QLabel(self.gridLayoutWidget)
        self.lblStatDesc.setObjectName(u"lblStatDesc")
        self.lblStatDesc.setMinimumSize(QSize(50, 0))
        self.lblStatDesc.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.lblStatDesc)

        self.lblStatus01Address = QLabel(self.gridLayoutWidget)
        self.lblStatus01Address.setObjectName(u"lblStatus01Address")
        self.lblStatus01Address.setMinimumSize(QSize(50, 0))
        self.lblStatus01Address.setMaximumSize(QSize(50, 16777215))
        self.lblStatus01Address.setFrameShape(QFrame.WinPanel)
        self.lblStatus01Address.setFrameShadow(QFrame.Sunken)
        self.lblStatus01Address.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lblStatus01Address)


        self.gridLayout.addLayout(self.horizontalLayout_5, 9, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblStatusDesc02 = QLabel(self.gridLayoutWidget)
        self.lblStatusDesc02.setObjectName(u"lblStatusDesc02")
        self.lblStatusDesc02.setMinimumSize(QSize(55, 0))
        self.lblStatusDesc02.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_6.addWidget(self.lblStatusDesc02)

        self.lblStatus01Value = QLabel(self.gridLayoutWidget)
        self.lblStatus01Value.setObjectName(u"lblStatus01Value")
        self.lblStatus01Value.setMinimumSize(QSize(40, 0))
        self.lblStatus01Value.setMaximumSize(QSize(40, 16777215))
        self.lblStatus01Value.setFrameShape(QFrame.WinPanel)
        self.lblStatus01Value.setFrameShadow(QFrame.Sunken)
        self.lblStatus01Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lblStatus01Value)


        self.gridLayout.addLayout(self.horizontalLayout_6, 9, 1, 1, 1)

        self.grpStatus02 = QGroupBox(self.centralwidget)
        self.grpStatus02.setObjectName(u"grpStatus02")
        self.grpStatus02.setGeometry(QRect(270, 330, 251, 271))
        self.grpStatus02.setStyleSheet(u"QGroupBox {\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"	margin-top:0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	top:-9;\n"
"	left:10px;\n"
"}")
        self.grpStatus02.setFlat(False)
        self.gridLayoutWidget_2 = QWidget(self.grpStatus02)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 20, 239, 241))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.chkStatus02_05 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_05.setObjectName(u"chkStatus02_05")

        self.gridLayout_2.addWidget(self.chkStatus02_05, 5, 0, 1, 1)

        self.line_3 = QFrame(self.gridLayoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 8, 0, 1, 1)

        self.chkStatus02_12 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_12.setObjectName(u"chkStatus02_12")
        self.chkStatus02_12.setMinimumSize(QSize(110, 0))
        self.chkStatus02_12.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_2.addWidget(self.chkStatus02_12, 4, 1, 1, 1)

        self.chkStatus02_14 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_14.setObjectName(u"chkStatus02_14")
        self.chkStatus02_14.setMinimumSize(QSize(110, 0))
        self.chkStatus02_14.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_2.addWidget(self.chkStatus02_14, 6, 1, 1, 1)

        self.chkStatus02_09 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_09.setObjectName(u"chkStatus02_09")
        self.chkStatus02_09.setMinimumSize(QSize(110, 0))
        self.chkStatus02_09.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_2.addWidget(self.chkStatus02_09, 1, 1, 1, 1)

        self.chkStatus02_00 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_00.setObjectName(u"chkStatus02_00")
        self.chkStatus02_00.setMinimumSize(QSize(110, 0))
        self.chkStatus02_00.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_2.addWidget(self.chkStatus02_00, 0, 0, 1, 1)

        self.chkStatus02_04 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_04.setObjectName(u"chkStatus02_04")

        self.gridLayout_2.addWidget(self.chkStatus02_04, 4, 0, 1, 1)

        self.chkStatus02_13 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_13.setObjectName(u"chkStatus02_13")
        self.chkStatus02_13.setMinimumSize(QSize(110, 0))
        self.chkStatus02_13.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_2.addWidget(self.chkStatus02_13, 5, 1, 1, 1)

        self.line_4 = QFrame(self.gridLayoutWidget_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 8, 1, 1, 1)

        self.chkStatus02_03 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_03.setObjectName(u"chkStatus02_03")

        self.gridLayout_2.addWidget(self.chkStatus02_03, 3, 0, 1, 1)

        self.chkStatus02_10 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_10.setObjectName(u"chkStatus02_10")
        self.chkStatus02_10.setMinimumSize(QSize(110, 0))
        self.chkStatus02_10.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_2.addWidget(self.chkStatus02_10, 2, 1, 1, 1)

        self.chkStatus02_06 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_06.setObjectName(u"chkStatus02_06")

        self.gridLayout_2.addWidget(self.chkStatus02_06, 6, 0, 1, 1)

        self.chkStatus02_15 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_15.setObjectName(u"chkStatus02_15")
        self.chkStatus02_15.setMinimumSize(QSize(110, 0))
        self.chkStatus02_15.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_2.addWidget(self.chkStatus02_15, 7, 1, 1, 1)

        self.chkStatus02_08 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_08.setObjectName(u"chkStatus02_08")
        self.chkStatus02_08.setMinimumSize(QSize(110, 0))
        self.chkStatus02_08.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_2.addWidget(self.chkStatus02_08, 0, 1, 1, 1)

        self.chkStatus02_01 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_01.setObjectName(u"chkStatus02_01")

        self.gridLayout_2.addWidget(self.chkStatus02_01, 1, 0, 1, 1)

        self.chkStatus02_02 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_02.setObjectName(u"chkStatus02_02")

        self.gridLayout_2.addWidget(self.chkStatus02_02, 2, 0, 1, 1)

        self.chkStatus02_07 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_07.setObjectName(u"chkStatus02_07")

        self.gridLayout_2.addWidget(self.chkStatus02_07, 7, 0, 1, 1)

        self.chkStatus02_11 = QCheckBox(self.gridLayoutWidget_2)
        self.chkStatus02_11.setObjectName(u"chkStatus02_11")
        self.chkStatus02_11.setMinimumSize(QSize(110, 0))
        self.chkStatus02_11.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_2.addWidget(self.chkStatus02_11, 3, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblStatDesc_2 = QLabel(self.gridLayoutWidget_2)
        self.lblStatDesc_2.setObjectName(u"lblStatDesc_2")
        self.lblStatDesc_2.setMinimumSize(QSize(50, 0))
        self.lblStatDesc_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_7.addWidget(self.lblStatDesc_2)

        self.lblStatus02Address = QLabel(self.gridLayoutWidget_2)
        self.lblStatus02Address.setObjectName(u"lblStatus02Address")
        self.lblStatus02Address.setMinimumSize(QSize(50, 0))
        self.lblStatus02Address.setMaximumSize(QSize(50, 16777215))
        self.lblStatus02Address.setFrameShape(QFrame.WinPanel)
        self.lblStatus02Address.setFrameShadow(QFrame.Sunken)
        self.lblStatus02Address.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lblStatus02Address)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 9, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblStatusDesc02_2 = QLabel(self.gridLayoutWidget_2)
        self.lblStatusDesc02_2.setObjectName(u"lblStatusDesc02_2")
        self.lblStatusDesc02_2.setMinimumSize(QSize(55, 0))
        self.lblStatusDesc02_2.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_8.addWidget(self.lblStatusDesc02_2)

        self.lblStatus02Value = QLabel(self.gridLayoutWidget_2)
        self.lblStatus02Value.setObjectName(u"lblStatus02Value")
        self.lblStatus02Value.setMinimumSize(QSize(40, 0))
        self.lblStatus02Value.setMaximumSize(QSize(40, 16777215))
        self.lblStatus02Value.setFrameShape(QFrame.WinPanel)
        self.lblStatus02Value.setFrameShadow(QFrame.Sunken)
        self.lblStatus02Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lblStatus02Value)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 9, 1, 1, 1)

        self.grpControl01 = QGroupBox(self.centralwidget)
        self.grpControl01.setObjectName(u"grpControl01")
        self.grpControl01.setGeometry(QRect(540, 50, 251, 271))
        self.grpControl01.setAutoFillBackground(False)
        self.grpControl01.setStyleSheet(u"QGroupBox {\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"	margin-top:0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	top:-9;\n"
"	left:10px;\n"
"}")
        self.grpControl01.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.grpControl01.setFlat(False)
        self.grpControl01.setCheckable(False)
        self.gridLayoutWidget_3 = QWidget(self.grpControl01)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 20, 239, 241))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.chkControl01_05 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_05.setObjectName(u"chkControl01_05")

        self.gridLayout_3.addWidget(self.chkControl01_05, 5, 0, 1, 1)

        self.line_5 = QFrame(self.gridLayoutWidget_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 8, 0, 1, 1)

        self.chkControl01_12 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_12.setObjectName(u"chkControl01_12")
        self.chkControl01_12.setMinimumSize(QSize(110, 0))
        self.chkControl01_12.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_3.addWidget(self.chkControl01_12, 4, 1, 1, 1)

        self.chkControl01_14 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_14.setObjectName(u"chkControl01_14")
        self.chkControl01_14.setMinimumSize(QSize(110, 0))
        self.chkControl01_14.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_3.addWidget(self.chkControl01_14, 6, 1, 1, 1)

        self.chkControl01_09 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_09.setObjectName(u"chkControl01_09")
        self.chkControl01_09.setMinimumSize(QSize(110, 0))
        self.chkControl01_09.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_3.addWidget(self.chkControl01_09, 1, 1, 1, 1)

        self.chkControl01_00 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_00.setObjectName(u"chkControl01_00")
        self.chkControl01_00.setMinimumSize(QSize(110, 0))
        self.chkControl01_00.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_3.addWidget(self.chkControl01_00, 0, 0, 1, 1)

        self.chkControl01_04 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_04.setObjectName(u"chkControl01_04")

        self.gridLayout_3.addWidget(self.chkControl01_04, 4, 0, 1, 1)

        self.chkControl01_13 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_13.setObjectName(u"chkControl01_13")
        self.chkControl01_13.setMinimumSize(QSize(110, 0))
        self.chkControl01_13.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_3.addWidget(self.chkControl01_13, 5, 1, 1, 1)

        self.line_6 = QFrame(self.gridLayoutWidget_3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_6, 8, 1, 1, 1)

        self.chkControl01_03 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_03.setObjectName(u"chkControl01_03")

        self.gridLayout_3.addWidget(self.chkControl01_03, 3, 0, 1, 1)

        self.chkControl01_10 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_10.setObjectName(u"chkControl01_10")
        self.chkControl01_10.setMinimumSize(QSize(110, 0))
        self.chkControl01_10.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_3.addWidget(self.chkControl01_10, 2, 1, 1, 1)

        self.chkControl01_06 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_06.setObjectName(u"chkControl01_06")

        self.gridLayout_3.addWidget(self.chkControl01_06, 6, 0, 1, 1)

        self.chkControl01_15 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_15.setObjectName(u"chkControl01_15")
        self.chkControl01_15.setMinimumSize(QSize(110, 0))
        self.chkControl01_15.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_3.addWidget(self.chkControl01_15, 7, 1, 1, 1)

        self.chkControl01_08 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_08.setObjectName(u"chkControl01_08")
        self.chkControl01_08.setMinimumSize(QSize(110, 0))
        self.chkControl01_08.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_3.addWidget(self.chkControl01_08, 0, 1, 1, 1)

        self.chkControl01_01 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_01.setObjectName(u"chkControl01_01")

        self.gridLayout_3.addWidget(self.chkControl01_01, 1, 0, 1, 1)

        self.chkControl01_02 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_02.setObjectName(u"chkControl01_02")

        self.gridLayout_3.addWidget(self.chkControl01_02, 2, 0, 1, 1)

        self.chkControl01_07 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_07.setObjectName(u"chkControl01_07")

        self.gridLayout_3.addWidget(self.chkControl01_07, 7, 0, 1, 1)

        self.chkControl01_11 = QCheckBox(self.gridLayoutWidget_3)
        self.chkControl01_11.setObjectName(u"chkControl01_11")
        self.chkControl01_11.setMinimumSize(QSize(110, 0))
        self.chkControl01_11.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_3.addWidget(self.chkControl01_11, 3, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lblCtrl01Desc_3 = QLabel(self.gridLayoutWidget_3)
        self.lblCtrl01Desc_3.setObjectName(u"lblCtrl01Desc_3")
        self.lblCtrl01Desc_3.setMinimumSize(QSize(50, 0))
        self.lblCtrl01Desc_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_9.addWidget(self.lblCtrl01Desc_3)

        self.lblControl01Address = QLabel(self.gridLayoutWidget_3)
        self.lblControl01Address.setObjectName(u"lblControl01Address")
        self.lblControl01Address.setMinimumSize(QSize(50, 0))
        self.lblControl01Address.setMaximumSize(QSize(50, 16777215))
        self.lblControl01Address.setFrameShape(QFrame.WinPanel)
        self.lblControl01Address.setFrameShadow(QFrame.Sunken)
        self.lblControl01Address.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lblControl01Address)


        self.gridLayout_3.addLayout(self.horizontalLayout_9, 9, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lblCtrl01Desc02_3 = QLabel(self.gridLayoutWidget_3)
        self.lblCtrl01Desc02_3.setObjectName(u"lblCtrl01Desc02_3")
        self.lblCtrl01Desc02_3.setMinimumSize(QSize(55, 0))
        self.lblCtrl01Desc02_3.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_10.addWidget(self.lblCtrl01Desc02_3)

        self.lblControl01Value = QLabel(self.gridLayoutWidget_3)
        self.lblControl01Value.setObjectName(u"lblControl01Value")
        self.lblControl01Value.setMinimumSize(QSize(40, 0))
        self.lblControl01Value.setMaximumSize(QSize(40, 16777215))
        self.lblControl01Value.setFrameShape(QFrame.WinPanel)
        self.lblControl01Value.setFrameShadow(QFrame.Sunken)
        self.lblControl01Value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lblControl01Value)


        self.gridLayout_3.addLayout(self.horizontalLayout_10, 9, 1, 1, 1)

        self.grpSettings = QGroupBox(self.centralwidget)
        self.grpSettings.setObjectName(u"grpSettings")
        self.grpSettings.setGeometry(QRect(540, 330, 251, 271))
        self.grpSettings.setStyleSheet(u"QGroupBox {\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"	margin-top:0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	top:-9;\n"
"	left:10px;\n"
"}")
        self.tblSettings = QTableWidget(self.grpSettings)
        if (self.tblSettings.columnCount() < 2):
            self.tblSettings.setColumnCount(2)
        self.tblSettings.setObjectName(u"tblSettings")
        self.tblSettings.setGeometry(QRect(10, 21, 231, 241))
        self.tblSettings.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tblSettings.setRowCount(0)
        self.tblSettings.setColumnCount(2)
        self.tblSettings.horizontalHeader().setVisible(True)
        self.tblSettings.verticalHeader().setVisible(False)
        self.grpTags = QGroupBox(self.centralwidget)
        self.grpTags.setObjectName(u"grpTags")
        self.grpTags.setGeometry(QRect(810, 50, 251, 551))
        self.grpTags.setStyleSheet(u"QGroupBox {\n"
"	border: 1px solid gray;\n"
"	border-radius: 2px;\n"
"	margin-top:0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	top:-9;\n"
"	left:10px;\n"
"}")
        self.tblAnalog = QTableWidget(self.grpTags)
        if (self.tblAnalog.columnCount() < 2):
            self.tblAnalog.setColumnCount(2)
        self.tblAnalog.setObjectName(u"tblAnalog")
        self.tblAnalog.setGeometry(QRect(10, 21, 231, 521))
        self.tblAnalog.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tblAnalog.setColumnCount(2)
        self.tblAnalog.verticalHeader().setVisible(False)
        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(650, 10, 111, 22))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lblSevInfo03_2 = QLabel(self.horizontalLayoutWidget_4)
        self.lblSevInfo03_2.setObjectName(u"lblSevInfo03_2")
        self.lblSevInfo03_2.setMinimumSize(QSize(0, 0))
        self.lblSevInfo03_2.setMaximumSize(QSize(70, 20))

        self.horizontalLayout_11.addWidget(self.lblSevInfo03_2)

        self.lblTotDev = QLabel(self.horizontalLayoutWidget_4)
        self.lblTotDev.setObjectName(u"lblTotDev")
        self.lblTotDev.setFrameShape(QFrame.WinPanel)
        self.lblTotDev.setFrameShadow(QFrame.Sunken)
        self.lblTotDev.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.lblTotDev)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(780, 10, 111, 22))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lblSevInfo03_3 = QLabel(self.horizontalLayoutWidget_5)
        self.lblSevInfo03_3.setObjectName(u"lblSevInfo03_3")
        self.lblSevInfo03_3.setMinimumSize(QSize(0, 0))
        self.lblSevInfo03_3.setMaximumSize(QSize(70, 20))

        self.horizontalLayout_12.addWidget(self.lblSevInfo03_3)

        self.lblSimDev = QLabel(self.horizontalLayoutWidget_5)
        self.lblSimDev.setObjectName(u"lblSimDev")
        self.lblSimDev.setFrameShape(QFrame.WinPanel)
        self.lblSimDev.setFrameShadow(QFrame.Sunken)
        self.lblSimDev.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.lblSimDev)

        self.btnConfigure = QPushButton(self.centralwidget)
        self.btnConfigure.setObjectName(u"btnConfigure")
        self.btnConfigure.setGeometry(QRect(910, 10, 71, 24))
        self.btnReload = QPushButton(self.centralwidget)
        self.btnReload.setObjectName(u"btnReload")
        self.btnReload.setGeometry(QRect(990, 10, 71, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Nuwans ModBusSimulator V2.0", None))
        self.lblProject.setText(QCoreApplication.translate("MainWindow", u"Project :", None))
        self.lblProjectName.setText(QCoreApplication.translate("MainWindow", u"Project Name", None))
        self.lblServinfo01.setText(QCoreApplication.translate("MainWindow", u"Server :", None))
        self.lblServStatus.setText(QCoreApplication.translate("MainWindow", u"STOPPED", None))
        self.lblSevInfo02.setText(QCoreApplication.translate("MainWindow", u"IP Address:", None))
        self.lblServIP.setText(QCoreApplication.translate("MainWindow", u"255.255.255.255", None))
        self.lblSevInfo03.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.lblServPort.setText(QCoreApplication.translate("MainWindow", u"502", None))
        self.lblDevDesc01.setText(QCoreApplication.translate("MainWindow", u"Place :", None))
        self.lblDevDesc02.setText(QCoreApplication.translate("MainWindow", u"Dev Type :", None))
        self.lblDeviceType.setText("")
        self.lblDevDesc04.setText(QCoreApplication.translate("MainWindow", u"Sim Scale :", None))
        self.lblDevDesc05.setText(QCoreApplication.translate("MainWindow", u"Simulate :", None))
        self.chkSimulate.setText("")
        self.lblPreloadDesc.setText(QCoreApplication.translate("MainWindow", u"Preload :", None))
        self.chkPreloadSettings.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.chkPreloadAnalog.setText(QCoreApplication.translate("MainWindow", u"Tag", None))
        self.chkPreloadStatus.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.lblDeviceInfo01.setText(QCoreApplication.translate("MainWindow", u"Device :", None))
        self.grpStatus01.setTitle(QCoreApplication.translate("MainWindow", u"Status 01", None))
        self.chkStatus01_05.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 05", None))
        self.chkStatus01_12.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 12", None))
        self.chkStatus01_14.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 14", None))
        self.chkStatus01_09.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 09", None))
        self.chkStatus01_00.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 00", None))
        self.chkStatus01_04.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 04", None))
        self.chkStatus01_13.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 13", None))
        self.chkStatus01_03.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 03", None))
        self.chkStatus01_10.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 10", None))
        self.chkStatus01_06.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 06", None))
        self.chkStatus01_15.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 15", None))
        self.chkStatus01_08.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 08", None))
        self.chkStatus01_01.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 01", None))
        self.chkStatus01_02.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 02", None))
        self.chkStatus01_07.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 07", None))
        self.chkStatus01_11.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 11", None))
        self.lblStatDesc.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.lblStatus01Address.setText(QCoreApplication.translate("MainWindow", u"400000", None))
        self.lblStatusDesc02.setText(QCoreApplication.translate("MainWindow", u"Tag Value:", None))
        self.lblStatus01Value.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.grpStatus02.setTitle(QCoreApplication.translate("MainWindow", u"Status 02", None))
        self.chkStatus02_05.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 05", None))
        self.chkStatus02_12.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 12", None))
        self.chkStatus02_14.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 14", None))
        self.chkStatus02_09.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 09", None))
        self.chkStatus02_00.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 00", None))
        self.chkStatus02_04.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 04", None))
        self.chkStatus02_13.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 13", None))
        self.chkStatus02_03.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 03", None))
        self.chkStatus02_10.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 10", None))
        self.chkStatus02_06.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 06", None))
        self.chkStatus02_15.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 15", None))
        self.chkStatus02_08.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 08", None))
        self.chkStatus02_01.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 01", None))
        self.chkStatus02_02.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 02", None))
        self.chkStatus02_07.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 07", None))
        self.chkStatus02_11.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 11", None))
        self.lblStatDesc_2.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.lblStatus02Address.setText(QCoreApplication.translate("MainWindow", u"400000", None))
        self.lblStatusDesc02_2.setText(QCoreApplication.translate("MainWindow", u"Tag Value:", None))
        self.lblStatus02Value.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.grpControl01.setTitle(QCoreApplication.translate("MainWindow", u"Control 01", None))
        self.chkControl01_05.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 05", None))
        self.chkControl01_12.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 12", None))
        self.chkControl01_14.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 14", None))
        self.chkControl01_09.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 09", None))
        self.chkControl01_00.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 00", None))
        self.chkControl01_04.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 04", None))
        self.chkControl01_13.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 13", None))
        self.chkControl01_03.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 03", None))
        self.chkControl01_10.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 10", None))
        self.chkControl01_06.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 06", None))
        self.chkControl01_15.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 15", None))
        self.chkControl01_08.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 08", None))
        self.chkControl01_01.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 01", None))
        self.chkControl01_02.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 02", None))
        self.chkControl01_07.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 07", None))
        self.chkControl01_11.setText(QCoreApplication.translate("MainWindow", u"Tag Bit Value 11", None))
        self.lblCtrl01Desc_3.setText(QCoreApplication.translate("MainWindow", u"Address :", None))
        self.lblControl01Address.setText(QCoreApplication.translate("MainWindow", u"400000", None))
        self.lblCtrl01Desc02_3.setText(QCoreApplication.translate("MainWindow", u"Tag Value:", None))
        self.lblControl01Value.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.grpSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.grpTags.setTitle(QCoreApplication.translate("MainWindow", u"Tags", None))
        self.lblSevInfo03_2.setText(QCoreApplication.translate("MainWindow", u"Total Devices", None))
        self.lblTotDev.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.lblSevInfo03_3.setText(QCoreApplication.translate("MainWindow", u"Sim. Devices", None))
        self.lblSimDev.setText(QCoreApplication.translate("MainWindow", u"000", None))
        self.btnConfigure.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.btnReload.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
    # retranslateUi

