# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(911, 716)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setWindowOpacity(0.990000000000000)
        self.action_Instructions = QAction(MainWindow)
        self.action_Instructions.setObjectName(u"action_Instructions")
        self.action_Authors = QAction(MainWindow)
        self.action_Authors.setObjectName(u"action_Authors")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(60, 50, 781, 541))
        self.mainLayout = QGridLayout(self.gridLayoutWidget)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.graphWidget = PlotWidget(self.gridLayoutWidget)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setMinimumSize(QSize(500, 500))
        self.graphWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.graphWidget, 0, 0, 1, 1)


        self.mainLayout.addLayout(self.gridLayout_4, 0, 2, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.line_function = QLineEdit(self.gridLayoutWidget)
        self.line_function.setObjectName(u"line_function")

        self.horizontalLayout.addWidget(self.line_function)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.but_Graph = QPushButton(self.gridLayoutWidget)
        self.but_Graph.setObjectName(u"but_Graph")
        self.but_Graph.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.but_Graph)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)

        self.lab_type_func = QLabel(self.gridLayoutWidget)
        self.lab_type_func.setObjectName(u"lab_type_func")
        self.lab_type_func.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lab_type_func, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.line_intervalA = QLineEdit(self.gridLayoutWidget)
        self.line_intervalA.setObjectName(u"line_intervalA")
        self.line_intervalA.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.line_intervalA)

        self.line_intervalB = QLineEdit(self.gridLayoutWidget)
        self.line_intervalB.setObjectName(u"line_intervalB")
        self.line_intervalB.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.line_intervalB)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.line_step = QLineEdit(self.gridLayoutWidget)
        self.line_step.setObjectName(u"line_step")
        self.line_step.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.line_step)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout_3.addLayout(self.verticalLayout, 4, 0, 1, 1)

        self.function_photo = QLabel(self.gridLayoutWidget)
        self.function_photo.setObjectName(u"function_photo")
        self.function_photo.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.function_photo, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.mainLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 911, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_Instructions)
        self.menu.addAction(self.action_Authors)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Builder Math Functions", None))
        self.action_Instructions.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.action_Authors.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u044b", None))
        self.but_Graph.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.lab_type_func.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0444\u0443\u043d\u043a\u0446\u0438\u0438: ...", None))
        self.function_photo.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
    # retranslateUi

