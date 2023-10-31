# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Nayeshi_frontend.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QProgressBar, QPushButton,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 250)
        Widget.setStyleSheet(u"QWidget {\n"
"color: white;\n"
"background-color: rgb(60, 60, 60);\n"
"border: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 12px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100); \n"
"    color: #FFFFFF; \n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  \n"
"    color: #aaaaaa; \n"
"    border-color: #aaaaaa;\n"
"}\n"
"\n"
"QPushButton {\n"
"        background-color: #5a2a82;\n"
"        color: #ffffff; \n"
"        border: none;\n"
"        border-radius: 10px;\n"
"        padding: 5px 20px; \n"
"        font-size: 12px;\n"
"        outline: none;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: #7b3ca3; \n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        background-color: #481f61; \n"
"    }\n"
"\n"
"    QPushButton:disabled {\n"
"        background-color: #3f1d4d; \n"
"        color"
                        ": #8a7b9a; \n"
"    }\n"
"\n"
"\n"
"QProgressBar {\n"
"	color: rgb(255, 153, 0);\n"
"    border: 2px solid #5a2a82;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: rgb(74, 74, 74);\n"
"    color: #ffffff;  /* Adding text color for better visibility */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(0, 255, 224);\n"
"    width: 10px; /* Adjust this to change the width of the 'chunk' */\n"
"}\n"
"\n"
"QRadioButton {\n"
"	color: rgb(255,255,255)}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border : 4px solid;\n"
"	border-color: black;\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0, 255, 183);\n"
"\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #5a2a82;\n"
"    height: 8px;\n"
"    background: #e0e0e0;\n"
"    margin: 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #5"
                        "a2a82;\n"
"    border: 1px solid #5a2a82;\n"
"    width: 18px;\n"
"    margin: -6px 0;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #e0e0e0;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #5a2a82;\n"
"}\n"
"\n"
"QTreeWidget {\n"
"    background-color: rgb(94, 94, 94);\n"
"    color: white;\n"
"}\n"
"\n"
"QTreeWidget QHeaderView::section {\n"
"    background-color: rgb(94, 94, 94);\n"
"    color: black; \n"
"    border: 1px solid #5a2a82;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QGroupBox {\n"
"        border: 0px;\n"
"        margin-top: 1ex; /* Adjust as needed */\n"
"    }\n"
"    QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        subcontrol-position: top center;\n"
"        padding: 0 3px;\n"
"    }")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(Widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">		Information:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'JetBrains Mono','monospace'; color:#ffffff;\">The Aimbot will now start generating / updating the pointers for<br />Fortnite, CS:GO, Rainbow Six Siege, Valorant and possibly other FPS game"
                        "s.<br />This only needs to be done once, and can then be re-used. How long it takes depends<br />on your system resources. Generating the pointers takes a lot of CPU and DISK usage.<br /><br /><br />DO NOT RUN IT ON SPLITGATE! Splitgate can detect the Aimbot. All other games didn't.</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Start", None))
    # retranslateUi

