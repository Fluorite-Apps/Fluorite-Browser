# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsqrFAKl.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(689, 592)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(20, 30, 611, 531))
        self.main_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.main_frame.setStyleSheet(u"QPushButton{\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(46, 49, 63);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 64, 82);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.main_frame.setLineWidth(0)
        self.button_frame_1 = QFrame(self.main_frame)
        self.button_frame_1.setObjectName(u"button_frame_1")
        self.button_frame_1.setGeometry(QRect(230, 410, 281, 71))
        self.button_frame_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_frame_1.setStyleSheet(u"QPushButton{\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(46, 49, 63);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 64, 82);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}")
        self.button_frame_1.setFrameShape(QFrame.NoFrame)
        self.button_frame_1.setFrameShadow(QFrame.Raised)
        self.button_frame_1.setLineWidth(0)
        self.apply_button_layout = QHBoxLayout(self.button_frame_1)
        self.apply_button_layout.setSpacing(0)
        self.apply_button_layout.setObjectName(u"apply_button_layout")
        self.apply_button_layout.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.main_frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(20, 0, 561, 521))
        self.label_28.setStyleSheet(u"QLabel {\n"
"			background-color: #3C4052;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_29 = QLabel(self.main_frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(50, 110, 501, 391))
        self.label_29.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(70, 74, 95);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_40 = QLabel(self.main_frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(360, 140, 151, 71))
        self.label_40.setStyleSheet(u"QLabel {\n"
"			background-color: rgb(60, 64, 82);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_8 = QLabel(self.main_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 19, 501, 71))
        font = QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: gray")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_41 = QLabel(self.main_frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(360, 230, 151, 71))
        self.label_41.setStyleSheet(u"QLabel {\n"
"			background-color: rgb(60, 64, 82);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.toggle_frame_3 = QFrame(self.main_frame)
        self.toggle_frame_3.setObjectName(u"toggle_frame_3")
        self.toggle_frame_3.setGeometry(QRect(360, 320, 151, 71))
        self.toggle_frame_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggle_frame_3.setStyleSheet(u"QPushButton{\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(46, 49, 63);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 64, 82);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}")
        self.toggle_frame_3.setFrameShape(QFrame.NoFrame)
        self.toggle_frame_3.setFrameShadow(QFrame.Raised)
        self.toggle_frame_3.setLineWidth(0)
        self.placeholder_toggle_layout_2 = QHBoxLayout(self.toggle_frame_3)
        self.placeholder_toggle_layout_2.setSpacing(0)
        self.placeholder_toggle_layout_2.setObjectName(u"placeholder_toggle_layout_2")
        self.placeholder_toggle_layout_2.setContentsMargins(0, 0, 0, 0)
        self.toggle_frame_1 = QFrame(self.main_frame)
        self.toggle_frame_1.setObjectName(u"toggle_frame_1")
        self.toggle_frame_1.setGeometry(QRect(360, 140, 151, 71))
        self.toggle_frame_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggle_frame_1.setStyleSheet(u"QPushButton{\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(46, 49, 63);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 64, 82);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}")
        self.toggle_frame_1.setFrameShape(QFrame.NoFrame)
        self.toggle_frame_1.setFrameShadow(QFrame.Raised)
        self.toggle_frame_1.setLineWidth(0)
        self.cookies_toggle_layout = QHBoxLayout(self.toggle_frame_1)
        self.cookies_toggle_layout.setSpacing(0)
        self.cookies_toggle_layout.setObjectName(u"cookies_toggle_layout")
        self.cookies_toggle_layout.setContentsMargins(0, 0, 0, 0)
        self.toggle_frame_2 = QFrame(self.main_frame)
        self.toggle_frame_2.setObjectName(u"toggle_frame_2")
        self.toggle_frame_2.setGeometry(QRect(360, 230, 151, 71))
        self.toggle_frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggle_frame_2.setStyleSheet(u"QPushButton{\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(46, 49, 63);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 64, 82);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}")
        self.toggle_frame_2.setFrameShape(QFrame.NoFrame)
        self.toggle_frame_2.setFrameShadow(QFrame.Raised)
        self.toggle_frame_2.setLineWidth(0)
        self.placeholder_toggle_layout_1 = QHBoxLayout(self.toggle_frame_2)
        self.placeholder_toggle_layout_1.setSpacing(0)
        self.placeholder_toggle_layout_1.setObjectName(u"placeholder_toggle_layout_1")
        self.placeholder_toggle_layout_1.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.main_frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(80, 320, 251, 71))
        self.label_37.setStyleSheet(u"QLabel {\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"			color: gray;\n"
"        }")
        self.label_36 = QLabel(self.main_frame)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(80, 230, 251, 71))
        self.label_36.setStyleSheet(u"QLabel {\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"			color: gray;\n"
"        }")
        self.label_35 = QLabel(self.main_frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(80, 140, 251, 71))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_35.setFont(font1)
        self.label_35.setStyleSheet(u"QLabel {\n"
"			background-color: #595D75;\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"			color: gray;\n"
"        }")
        self.label_35.setAlignment(Qt.AlignCenter)
        self.label_42 = QLabel(self.main_frame)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(360, 320, 151, 71))
        self.label_42.setStyleSheet(u"QLabel {\n"
"			background-color: rgb(60, 64, 82);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_30 = QLabel(self.main_frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(50, 20, 501, 71))
        self.label_30.setStyleSheet(u"QLabel {\n"
"        	\n"
"	background-color: rgb(70, 74, 95);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border-bottom: 30px shadow;\n"
"        }")
        self.label_43 = QLabel(self.main_frame)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(230, 410, 281, 71))
        self.label_43.setStyleSheet(u"QLabel {\n"
"			background-color: rgb(45, 48, 61);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border: 2px solid rgb(73, 88, 97);\n"
"        }")
        self.label_44 = QLabel(self.main_frame)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(80, 410, 131, 71))
        self.label_44.setStyleSheet(u"QLabel {\n"
"			background-color: rgb(45, 48, 61);\n"
"			padding: 12px;\n"
"			border-radius: 25px;\n"
"			border: 2px solid rgb(73, 88, 97);\n"
"        }")
        self.button_frame_2 = QFrame(self.main_frame)
        self.button_frame_2.setObjectName(u"button_frame_2")
        self.button_frame_2.setGeometry(QRect(80, 410, 131, 71))
        self.button_frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_frame_2.setStyleSheet(u"QPushButton{\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"QPushButton:pressed:hover{\n"
"	background-color: rgb(46, 49, 63);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 64, 82);\n"
"	padding: 12px;\n"
"	border-radius: 25px;\n"
"	border-bottom: 30px shadow;\n"
"}")
        self.button_frame_2.setFrameShape(QFrame.NoFrame)
        self.button_frame_2.setFrameShadow(QFrame.Raised)
        self.button_frame_2.setLineWidth(0)
        self.settings_back_button_layout = QHBoxLayout(self.button_frame_2)
        self.settings_back_button_layout.setSpacing(0)
        self.settings_back_button_layout.setObjectName(u"settings_back_button_layout")
        self.settings_back_button_layout.setContentsMargins(0, 0, 0, 0)
        self.label_28.raise_()
        self.label_29.raise_()
        self.label_43.raise_()
        self.label_30.raise_()
        self.button_frame_1.raise_()
        self.label_40.raise_()
        self.label_8.raise_()
        self.label_41.raise_()
        self.toggle_frame_3.raise_()
        self.toggle_frame_1.raise_()
        self.toggle_frame_2.raise_()
        self.label_37.raise_()
        self.label_36.raise_()
        self.label_35.raise_()
        self.label_42.raise_()
        self.label_44.raise_()
        self.button_frame_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_28.setText("")
        self.label_29.setText("")
        self.label_40.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_41.setText("")
        self.label_37.setText("")
        self.label_36.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Enable cookies", None))
        self.label_42.setText("")
        self.label_30.setText("")
        self.label_43.setText("")
        self.label_44.setText("")
    # retranslateUi

