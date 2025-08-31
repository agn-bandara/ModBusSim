# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfigDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTableWidget, QTableWidgetItem, QToolButton, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        if not ConfigDialog.objectName():
            ConfigDialog.setObjectName(u"ConfigDialog")
        ConfigDialog.setWindowModality(Qt.NonModal)
        ConfigDialog.resize(1170, 375)
        ConfigDialog.setMinimumSize(QSize(1170, 375))
        ConfigDialog.setMaximumSize(QSize(1170, 375))
        self.verticalLayoutWidget = QWidget(ConfigDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 251, 361))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lstPlaces = QListWidget(self.verticalLayoutWidget)
        self.lstPlaces.setObjectName(u"lstPlaces")

        self.verticalLayout.addWidget(self.lstPlaces)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.txtNewPlace = QLineEdit(self.verticalLayoutWidget)
        self.txtNewPlace.setObjectName(u"txtNewPlace")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.txtNewPlace)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.txtPlaceAlias = QLineEdit(self.verticalLayoutWidget)
        self.txtPlaceAlias.setObjectName(u"txtPlaceAlias")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.txtPlaceAlias)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAddPlace = QPushButton(self.verticalLayoutWidget)
        self.btnAddPlace.setObjectName(u"btnAddPlace")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAddPlace.sizePolicy().hasHeightForWidth())
        self.btnAddPlace.setSizePolicy(sizePolicy)
        self.btnAddPlace.setMaximumSize(QSize(59, 16777215))

        self.horizontalLayout.addWidget(self.btnAddPlace)

        self.btnRemovePlace = QPushButton(self.verticalLayoutWidget)
        self.btnRemovePlace.setObjectName(u"btnRemovePlace")
        sizePolicy.setHeightForWidth(self.btnRemovePlace.sizePolicy().hasHeightForWidth())
        self.btnRemovePlace.setSizePolicy(sizePolicy)
        self.btnRemovePlace.setMaximumSize(QSize(59, 16777215))

        self.horizontalLayout.addWidget(self.btnRemovePlace)

        self.btnRenamePlace = QPushButton(self.verticalLayoutWidget)
        self.btnRenamePlace.setObjectName(u"btnRenamePlace")
        self.btnRenamePlace.setMaximumSize(QSize(59, 16777215))

        self.horizontalLayout.addWidget(self.btnRenamePlace)

        self.btnPlaceUp = QToolButton(self.verticalLayoutWidget)
        self.btnPlaceUp.setObjectName(u"btnPlaceUp")
        self.btnPlaceUp.setArrowType(Qt.UpArrow)

        self.horizontalLayout.addWidget(self.btnPlaceUp)

        self.btnPlaceDn = QToolButton(self.verticalLayoutWidget)
        self.btnPlaceDn.setObjectName(u"btnPlaceDn")
        self.btnPlaceDn.setArrowType(Qt.DownArrow)

        self.horizontalLayout.addWidget(self.btnPlaceDn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayoutWidget_2 = QWidget(ConfigDialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(280, 10, 242, 361))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.treeDevices = QTreeWidget(self.verticalLayoutWidget_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeDevices.setHeaderItem(__qtreewidgetitem)
        self.treeDevices.setObjectName(u"treeDevices")
        self.treeDevices.setHeaderHidden(True)
        self.treeDevices.setColumnCount(1)

        self.verticalLayout_2.addWidget(self.treeDevices)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblDevAddConfig = QLabel(self.verticalLayoutWidget_2)
        self.lblDevAddConfig.setObjectName(u"lblDevAddConfig")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblDevAddConfig)

        self.txtNewDevice = QLineEdit(self.verticalLayoutWidget_2)
        self.txtNewDevice.setObjectName(u"txtNewDevice")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txtNewDevice)

        self.lblDevDesc02 = QLabel(self.verticalLayoutWidget_2)
        self.lblDevDesc02.setObjectName(u"lblDevDesc02")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblDevDesc02)

        self.cmbDevTypeConfig = QComboBox(self.verticalLayoutWidget_2)
        self.cmbDevTypeConfig.setObjectName(u"cmbDevTypeConfig")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cmbDevTypeConfig)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.cmbParent = QComboBox(self.verticalLayoutWidget_2)
        self.cmbParent.setObjectName(u"cmbParent")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cmbParent)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAddDevice = QPushButton(self.verticalLayoutWidget_2)
        self.btnAddDevice.setObjectName(u"btnAddDevice")
        self.btnAddDevice.setMaximumSize(QSize(56, 16777215))

        self.horizontalLayout_2.addWidget(self.btnAddDevice)

        self.btnRemoveDevice = QPushButton(self.verticalLayoutWidget_2)
        self.btnRemoveDevice.setObjectName(u"btnRemoveDevice")
        self.btnRemoveDevice.setMaximumSize(QSize(56, 16777215))

        self.horizontalLayout_2.addWidget(self.btnRemoveDevice)

        self.btnRenameDevice = QPushButton(self.verticalLayoutWidget_2)
        self.btnRenameDevice.setObjectName(u"btnRenameDevice")
        self.btnRenameDevice.setMaximumSize(QSize(55, 16777215))

        self.horizontalLayout_2.addWidget(self.btnRenameDevice)

        self.btnDeviceUp = QToolButton(self.verticalLayoutWidget_2)
        self.btnDeviceUp.setObjectName(u"btnDeviceUp")
        self.btnDeviceUp.setArrowType(Qt.UpArrow)

        self.horizontalLayout_2.addWidget(self.btnDeviceUp)

        self.btnDeviceDn = QToolButton(self.verticalLayoutWidget_2)
        self.btnDeviceDn.setObjectName(u"btnDeviceDn")
        self.btnDeviceDn.setArrowType(Qt.DownArrow)

        self.horizontalLayout_2.addWidget(self.btnDeviceDn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayoutWidget_3 = QWidget(ConfigDialog)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(540, 10, 231, 361))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.tblAnalogPreload = QTableWidget(self.verticalLayoutWidget_3)
        if (self.tblAnalogPreload.columnCount() < 2):
            self.tblAnalogPreload.setColumnCount(2)
        self.tblAnalogPreload.setObjectName(u"tblAnalogPreload")
        self.tblAnalogPreload.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tblAnalogPreload.setColumnCount(2)

        self.verticalLayout_3.addWidget(self.tblAnalogPreload)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnUpdateAnalog = QPushButton(self.verticalLayoutWidget_3)
        self.btnUpdateAnalog.setObjectName(u"btnUpdateAnalog")

        self.horizontalLayout_3.addWidget(self.btnUpdateAnalog)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayoutWidget_4 = QWidget(ConfigDialog)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(790, 10, 231, 361))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.tblSettingsPreload = QTableWidget(self.verticalLayoutWidget_4)
        if (self.tblSettingsPreload.columnCount() < 2):
            self.tblSettingsPreload.setColumnCount(2)
        self.tblSettingsPreload.setObjectName(u"tblSettingsPreload")
        self.tblSettingsPreload.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tblSettingsPreload.setColumnCount(2)

        self.verticalLayout_4.addWidget(self.tblSettingsPreload)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnUpdateSettings = QPushButton(self.verticalLayoutWidget_4)
        self.btnUpdateSettings.setObjectName(u"btnUpdateSettings")

        self.horizontalLayout_4.addWidget(self.btnUpdateSettings)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.line = QFrame(self.verticalLayoutWidget_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_9 = QLabel(self.verticalLayoutWidget_4)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.spnStatus01 = QSpinBox(self.verticalLayoutWidget_4)
        self.spnStatus01.setObjectName(u"spnStatus01")
        self.spnStatus01.setMinimumSize(QSize(0, 0))
        self.spnStatus01.setMaximumSize(QSize(70, 16777215))
        self.spnStatus01.setMaximum(65535)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.spnStatus01)

        self.label_10 = QLabel(self.verticalLayoutWidget_4)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.spnStatus02 = QSpinBox(self.verticalLayoutWidget_4)
        self.spnStatus02.setObjectName(u"spnStatus02")
        self.spnStatus02.setMaximumSize(QSize(70, 16777215))
        self.spnStatus02.setMaximum(65535)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.spnStatus02)

        self.label_11 = QLabel(self.verticalLayoutWidget_4)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.spnSimScale = QSpinBox(self.verticalLayoutWidget_4)
        self.spnSimScale.setObjectName(u"spnSimScale")
        self.spnSimScale.setMaximumSize(QSize(70, 16777215))

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.spnSimScale)

        self.label_8 = QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.cmbLink = QComboBox(self.verticalLayoutWidget_4)
        self.cmbLink.setObjectName(u"cmbLink")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.cmbLink)


        self.verticalLayout_4.addLayout(self.formLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnUpdateOthers = QPushButton(self.verticalLayoutWidget_4)
        self.btnUpdateOthers.setObjectName(u"btnUpdateOthers")

        self.horizontalLayout_5.addWidget(self.btnUpdateOthers)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalLayoutWidget_5 = QWidget(ConfigDialog)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(1040, 30, 121, 86))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btnOpen = QPushButton(self.verticalLayoutWidget_5)
        self.btnOpen.setObjectName(u"btnOpen")

        self.verticalLayout_5.addWidget(self.btnOpen)

        self.btnSave = QPushButton(self.verticalLayoutWidget_5)
        self.btnSave.setObjectName(u"btnSave")

        self.verticalLayout_5.addWidget(self.btnSave)

        self.btnClose = QPushButton(self.verticalLayoutWidget_5)
        self.btnClose.setObjectName(u"btnClose")

        self.verticalLayout_5.addWidget(self.btnClose)

        self.verticalLayoutWidget_6 = QWidget(ConfigDialog)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(1040, 140, 121, 111))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.verticalLayoutWidget_6)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_2)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_13 = QLabel(self.verticalLayoutWidget_6)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.lblCurrentAddress = QLabel(self.verticalLayoutWidget_6)
        self.lblCurrentAddress.setObjectName(u"lblCurrentAddress")
        self.lblCurrentAddress.setFrameShape(QFrame.Panel)
        self.lblCurrentAddress.setFrameShadow(QFrame.Sunken)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lblCurrentAddress)

        self.label_14 = QLabel(self.verticalLayoutWidget_6)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.lblAvilableAddress = QLabel(self.verticalLayoutWidget_6)
        self.lblAvilableAddress.setObjectName(u"lblAvilableAddress")
        self.lblAvilableAddress.setFrameShape(QFrame.Panel)
        self.lblAvilableAddress.setFrameShadow(QFrame.Sunken)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lblAvilableAddress)

        self.label_12 = QLabel(self.verticalLayoutWidget_6)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.lblAddrLength = QLabel(self.verticalLayoutWidget_6)
        self.lblAddrLength.setObjectName(u"lblAddrLength")
        self.lblAddrLength.setFrameShape(QFrame.Panel)
        self.lblAddrLength.setFrameShadow(QFrame.Sunken)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lblAddrLength)


        self.verticalLayout_6.addLayout(self.formLayout_4)

        self.btnReSeqAddress = QPushButton(self.verticalLayoutWidget_6)
        self.btnReSeqAddress.setObjectName(u"btnReSeqAddress")

        self.verticalLayout_6.addWidget(self.btnReSeqAddress)


        self.retranslateUi(ConfigDialog)

        QMetaObject.connectSlotsByName(ConfigDialog)
    # setupUi

    def retranslateUi(self, ConfigDialog):
        ConfigDialog.setWindowTitle(QCoreApplication.translate("ConfigDialog", u"Plant Configuration", None))
        self.label.setText(QCoreApplication.translate("ConfigDialog", u"Places :", None))
        self.label_2.setText(QCoreApplication.translate("ConfigDialog", u"Place :", None))
        self.label_5.setText(QCoreApplication.translate("ConfigDialog", u"Alias :", None))
        self.btnAddPlace.setText(QCoreApplication.translate("ConfigDialog", u"Add", None))
        self.btnRemovePlace.setText(QCoreApplication.translate("ConfigDialog", u"Remove", None))
        self.btnRenamePlace.setText(QCoreApplication.translate("ConfigDialog", u"Change", None))
        self.btnPlaceUp.setText(QCoreApplication.translate("ConfigDialog", u"...", None))
        self.btnPlaceDn.setText(QCoreApplication.translate("ConfigDialog", u"...", None))
        self.label_3.setText(QCoreApplication.translate("ConfigDialog", u"Devices:", None))
        self.lblDevAddConfig.setText(QCoreApplication.translate("ConfigDialog", u"Device :", None))
        self.lblDevDesc02.setText(QCoreApplication.translate("ConfigDialog", u"Dev Type :", None))
        self.label_4.setText(QCoreApplication.translate("ConfigDialog", u"Parent :", None))
        self.btnAddDevice.setText(QCoreApplication.translate("ConfigDialog", u"Add", None))
        self.btnRemoveDevice.setText(QCoreApplication.translate("ConfigDialog", u"Remove", None))
        self.btnRenameDevice.setText(QCoreApplication.translate("ConfigDialog", u"Change", None))
        self.btnDeviceUp.setText(QCoreApplication.translate("ConfigDialog", u"...", None))
        self.btnDeviceDn.setText(QCoreApplication.translate("ConfigDialog", u"...", None))
        self.label_6.setText(QCoreApplication.translate("ConfigDialog", u"Preload Tags :", None))
        self.btnUpdateAnalog.setText(QCoreApplication.translate("ConfigDialog", u"Update", None))
        self.label_7.setText(QCoreApplication.translate("ConfigDialog", u"Preload Settings :", None))
        self.btnUpdateSettings.setText(QCoreApplication.translate("ConfigDialog", u"Update", None))
        self.label_9.setText(QCoreApplication.translate("ConfigDialog", u"Status 01:", None))
        self.label_10.setText(QCoreApplication.translate("ConfigDialog", u"Status 02:", None))
        self.label_11.setText(QCoreApplication.translate("ConfigDialog", u"SimScale :", None))
        self.label_8.setText(QCoreApplication.translate("ConfigDialog", u"Link :", None))
        self.btnUpdateOthers.setText(QCoreApplication.translate("ConfigDialog", u"Update", None))
        self.btnOpen.setText(QCoreApplication.translate("ConfigDialog", u"Open", None))
        self.btnSave.setText(QCoreApplication.translate("ConfigDialog", u"Save", None))
        self.btnClose.setText(QCoreApplication.translate("ConfigDialog", u"Close", None))
        self.label_13.setText(QCoreApplication.translate("ConfigDialog", u"Address: :", None))
        self.lblCurrentAddress.setText(QCoreApplication.translate("ConfigDialog", u"000", None))
        self.label_14.setText(QCoreApplication.translate("ConfigDialog", u"Avail:", None))
        self.lblAvilableAddress.setText(QCoreApplication.translate("ConfigDialog", u"000", None))
        self.label_12.setText(QCoreApplication.translate("ConfigDialog", u"Length:", None))
        self.lblAddrLength.setText(QCoreApplication.translate("ConfigDialog", u"0", None))
        self.btnReSeqAddress.setText(QCoreApplication.translate("ConfigDialog", u"Resequence", None))
    # retranslateUi

