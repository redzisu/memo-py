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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QLabel,
    QLayout, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_View(object):
    def setupUi(self, View):
        if not View.objectName():
            View.setObjectName(u"View")
        View.resize(915, 696)
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
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 761, 34))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.btn_editList = QPushButton(self.layoutWidget)
        self.btn_editList.setObjectName(u"btn_editList")
        self.btn_editList.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.btn_editList)

        self.btn_insertList = QPushButton(self.layoutWidget)
        self.btn_insertList.setObjectName(u"btn_insertList")

        self.horizontalLayout.addWidget(self.btn_insertList)

        self.btn_deleteList = QPushButton(self.layoutWidget)
        self.btn_deleteList.setObjectName(u"btn_deleteList")

        self.horizontalLayout.addWidget(self.btn_deleteList)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.grd_list = QListWidget(self.centralwidget)
        self.grd_list.setObjectName(u"grd_list")
        self.grd_list.setEnabled(True)
        self.grd_list.setGeometry(QRect(10, 60, 761, 521))
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
        View.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(View)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 915, 22))
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
        self.label.setText(QCoreApplication.translate("View", u"- \ud589 \ub354\ube14\ud074\ub9ad : \ud074\ub9bd\ubcf4\ub4dc \ubcf5\uc0ac\n"
"- Ctrl+Enter : \ud3b8\uc9d1 \uc885\ub8cc \ubc0f \uc800\uc7a5", None))
        self.btn_editList.setText(QCoreApplication.translate("View", u"\ud3b8\uc9d1", None))
        self.btn_insertList.setText(QCoreApplication.translate("View", u"\ucd94\uac00", None))
        self.btn_deleteList.setText(QCoreApplication.translate("View", u"\uc0ad\uc81c", None))
    # retranslateUi

