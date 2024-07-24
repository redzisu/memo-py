# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
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

class Ui_View(object):
    def setupUi(self, View):
        if not View.objectName():
            View.setObjectName(u"View")
        View.resize(791, 637)
        self.centralwidget = QWidget(View)
        self.centralwidget.setObjectName(u"centralwidget")
        self.grd_list = QListWidget(self.centralwidget)
        self.grd_list.setObjectName(u"grd_list")
        self.grd_list.setGeometry(QRect(20, 60, 751, 521))
        self.grd_list.setStyleSheet(u"")
        self.grd_list.setLineWidth(1)
        self.grd_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.grd_list.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.grd_list.setWordWrap(True)
        self.grd_list.setItemAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(510, 10, 261, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_editList = QPushButton(self.horizontalLayoutWidget)
        self.btn_editList.setObjectName(u"btn_editList")

        self.horizontalLayout.addWidget(self.btn_editList)

        self.btn_insertList = QPushButton(self.horizontalLayoutWidget)
        self.btn_insertList.setObjectName(u"btn_insertList")

        self.horizontalLayout.addWidget(self.btn_insertList)

        self.btn_deleteList = QPushButton(self.horizontalLayoutWidget)
        self.btn_deleteList.setObjectName(u"btn_deleteList")

        self.horizontalLayout.addWidget(self.btn_deleteList)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 301, 41))
        View.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(View)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 791, 22))
        View.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(View)
        self.statusbar.setObjectName(u"statusbar")
        View.setStatusBar(self.statusbar)

        self.retranslateUi(View)

        QMetaObject.connectSlotsByName(View)
    # setupUi

    def retranslateUi(self, View):
        View.setWindowTitle(QCoreApplication.translate("View", u"View", None))
        self.btn_editList.setText(QCoreApplication.translate("View", u"\ud3b8\uc9d1", None))
        self.btn_insertList.setText(QCoreApplication.translate("View", u"\ucd94\uac00", None))
        self.btn_deleteList.setText(QCoreApplication.translate("View", u"\uc0ad\uc81c", None))
        self.label.setText(QCoreApplication.translate("View", u"- \ud589 \ub354\ube14\ud074\ub9ad : \ud074\ub9bd\ubcf4\ub4dc \ubcf5\uc0ac\n"
"- Ctrl+Enter : \ud3b8\uc9d1 \uc885\ub8cc \ubc0f \uc800\uc7a5", None))
    # retranslateUi

