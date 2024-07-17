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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

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
        self.btn_deleteRow = QPushButton(self.centralwidget)
        self.btn_deleteRow.setObjectName(u"btn_deleteRow")
        self.btn_deleteRow.setGeometry(QRect(690, 350, 81, 24))
        self.btn_insertRow = QPushButton(self.centralwidget)
        self.btn_insertRow.setObjectName(u"btn_insertRow")
        self.btn_insertRow.setGeometry(QRect(610, 350, 75, 24))
        self.grd_list = QListWidget(self.centralwidget)
        self.grd_list.setObjectName(u"grd_list")
        self.grd_list.setGeometry(QRect(30, 380, 741, 171))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 350, 491, 21))
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
        self.btn_deleteRow.setText(QCoreApplication.translate("MainWindow", u"- \ud589 \uc0ad\uc81c", None))
        self.btn_insertRow.setText(QCoreApplication.translate("MainWindow", u"+ \ud589 \ucd94\uac00", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uadf8\ub9ac\ub4dc \ud589 \ud074\ub9ad\uc2dc \ubcf5\uc0ac. \ub354\ube14\ud074\ub9ad\uc2dc \ud3b8\uc9d1 \uac00\ub2a5", None))
    # retranslateUi

