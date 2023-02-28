import sqlite3
import sys

from PyQt6 import uic, QtWidgets


class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.base = sqlite3.connect("coffee.db")
        self.crsr = self.base.cursor()

        self.search()

    def search(self):
        res = self.crsr.execute(f"SELECT * FROM coffee").fetchall()
        if len(res) > 0:
            self.table.setColumnCount(len(res[0]))
            self.table.setRowCount(len(res))

            for _ in range(len(res)):
                for _2 in range(len(res[0])):
                    self.table.setItem(_, _2, QtWidgets.QTableWidgetItem(str(res[_][_2])))

    def update(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
