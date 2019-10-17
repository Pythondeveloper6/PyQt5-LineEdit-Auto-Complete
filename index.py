from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import sqlite3


FORM_CLASS,_ = loadUiType("main.ui")

names_list = []

class MainWindow(QMainWindow , FORM_CLASS):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.DB()
        self.LineEdit()

    def DB(self):
        self.connection = sqlite3.connect("names.db")
        names  = self.connection.execute("SELECT name FROM names")
        for name in names :
            names_list.append(name[0])


    def Auto_Complete(self , model):
        model.setStringList(names_list)

    def LineEdit(self):
        names_line_edit = self.lineEdit
        completer= QCompleter()
        names_line_edit.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.Auto_Complete(model)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_() ## main loop


if __name__ == '__main__':
    main()