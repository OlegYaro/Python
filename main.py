import sys
import sqlite3 as sq
from appUI import App
import PyQt5.QtWidgets as QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
