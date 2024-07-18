# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_pathFolder = QPushButton(self.centralwidget)
        self.btn_pathFolder.setObjectName(u"btn_pathFolder")
        self.btn_pathFolder.setGeometry(QRect(710, 10, 75, 24))
        self.grd_list = QListWidget(self.centralwidget)
        self.grd_list.setObjectName(u"grd_list")
        self.grd_list.setGeometry(QRect(30, 380, 741, 171))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 340, 281, 31))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(610, 340, 161, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_editRow = QPushButton(self.horizontalLayoutWidget)
        self.btn_editRow.setObjectName(u"btn_editRow")

        self.horizontalLayout.addWidget(self.btn_editRow)

        self.btn_insertRow = QPushButton(self.horizontalLayoutWidget)
        self.btn_insertRow.setObjectName(u"btn_insertRow")

        self.horizontalLayout.addWidget(self.btn_insertRow)

        self.btn_deleteRow = QPushButton(self.horizontalLayoutWidget)
        self.btn_deleteRow.setObjectName(u"btn_deleteRow")

        self.horizontalLayout.addWidget(self.btn_deleteRow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_pathFolder.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \ucc3e\uae30", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9ac\ub4dc \ud589 \ud074\ub9ad\uc2dc \ud074\ub9bd\ubcf4\ub4dc\uc5d0 \ubcf5\uc0ac\ub428", None))
        self.btn_editRow.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9d1", None))
        self.btn_insertRow.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00", None))
        self.btn_deleteRow.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
    # retranslateUi

