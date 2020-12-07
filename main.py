# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM VseCofe""").fetchall()
        for i in range(len(result)):
            self.tableWidget.setRowCount(i + 1)
            for j in range(7):
                # print(str(result[i][j]))
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
