#!/usr/bin/python3

# -*- coding: UTF-8 -*-

import sys
from PyQt4.QtCore import QObject, pyqtSlot, QUrl
from PyQt4.QtGui import QApplication
from PyQt4.QtWebKit import QWebView
from PyQt4 import QtNetwork

# import initapp

# initapp.main()

html = """
<html>
<body>
    <h1>Hello!</h1><br>
    <h2><a href="#" onclick="printer.text('Message from QWebView')">QObject Test</a></h2>
<h2><a href="#" onclick="alert('Javascript works!')">JS test</a></h2>
</body>
</html>
"""

class RecoveryPlan(QObject):
    def __init__(self, parent=None):
        super(RecoveryPlan, self).__init__(parent)

    @pyqtSlot(str)
    def text(self, message):
        print(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QWebView()
    frame = view.page().mainFrame()
    printer = RecoveryPlan()
    
    view.setWindowTitle("RecoveryPlan")
    view.resize(600, 600)

    # view.setHtml(html)
    # view.load(QUrl("http://jquerymobile.com/test/"));
    view.load(QUrl("login.html"));
    frame.addToJavaScriptWindowObject('printer', printer)
    # frame.evaluateJavaScript("alert('Hello');")
    frame.evaluateJavaScript("printer.text('Goooooooooo!');")
    view.show()
    app.exec_()
