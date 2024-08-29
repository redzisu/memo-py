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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QLayout,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_View(object):
    def setupUi(self, View):
        if not View.objectName():
            View.setObjectName(u"View")
        View.resize(451, 696)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(View.sizePolicy().hasHeightForWidth())
        View.setSizePolicy(sizePolicy)
        View.setMinimumSize(QSize(0, 0))
        View.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.centralwidget = QWidget(View)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.btn_insertList = QPushButton(self.centralwidget)
        self.btn_insertList.setObjectName(u"btn_insertList")

        self.horizontalLayout.addWidget(self.btn_insertList)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_topWindow = QPushButton(self.centralwidget)
        self.btn_topWindow.setObjectName(u"btn_topWindow")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_topWindow.sizePolicy().hasHeightForWidth())
        self.btn_topWindow.setSizePolicy(sizePolicy1)
        self.btn_topWindow.setMinimumSize(QSize(30, 0))
        self.btn_topWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.btn_topWindow)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.grd_list = QListWidget(self.centralwidget)
        self.grd_list.setObjectName(u"grd_list")
        self.grd_list.setEnabled(True)
        sizePolicy.setHeightForWidth(self.grd_list.sizePolicy().hasHeightForWidth())
        self.grd_list.setSizePolicy(sizePolicy)
        self.grd_list.setMinimumSize(QSize(100, 100))
        self.grd_list.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.grd_list.setStyleSheet(u"")
        self.grd_list.setLineWidth(1)
        self.grd_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.grd_list.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.grd_list.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.grd_list.setResizeMode(QListView.ResizeMode.Adjust)
        self.grd_list.setWordWrap(True)
        self.grd_list.setItemAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.grd_list)

        View.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(View)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 451, 22))
        View.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(View)
        self.statusbar.setObjectName(u"statusbar")
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        View.setStatusBar(self.statusbar)

        self.retranslateUi(View)

        QMetaObject.connectSlotsByName(View)
    # setupUi

    def retranslateUi(self, View):
        View.setWindowTitle(QCoreApplication.translate("View", u"View", None))
        self.btn_insertList.setText(QCoreApplication.translate("View", u"New", None))
        self.btn_topWindow.setText("")
    # retranslateUi

