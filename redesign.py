import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt

class PortfolioApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crypto Portfolio")
        self.setGeometry(100, 100, 702, 782)
        self.setStyleSheet("background-color: #111; color: white;")
        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(28, 28, 28, 28)

        # все вцелом находиться в вертикальгом лейауте
        # короче сначала будет секция с балансом и кнопками которая будет горизонтально 
        # секция с кнопками должна быть в вертекальном лейауте
        # секция с балансом труднее всего, снизу то что 3 это горизонтальный лейаут, при этом все остальное в вертикальном чтоб она хорошо встала на место 
        # как идея можно таблицу оформить через QGridLayout

        # Верхняя секция (баланс и кнопки)
        top_widget = QWidget()
        top_layout = QHBoxLayout()
        top_widget.setFixedSize(644, 206) 
        top_widget.setStyleSheet("background-color: #a020f0;  border-radius: 15px;")
        
        # Balance Section
        balance_widget = QWidget()
        balance_layout = QVBoxLayout()
        balance_widget.setFixedSize(402, 186) 
        balance_widget.setStyleSheet("background-color: #a02000;  border-radius: 15px;")

        # Button Section
        button_widget = QWidget()
        button_layout = QVBoxLayout()
        button_widget.setFixedSize(163, 200) 
        button_widget.setStyleSheet("background-color: #a02220;  border-radius: 15px;")

        # Crurrent Balance section
        Crurrent_balance_wiget = QWidget()
        Crurrent_balance_layout = QHBoxLayout()
        Crurrent_balance_wiget.setFixedSize(363, 63) 
        Crurrent_balance_wiget.setStyleSheet("background-color: #a020c0;  border-radius: 15px;")

        #Additional Info section
        additional_info_widget = QWidget()
        additional_info_layout = QHBoxLayout()
        additional_info_widget.setFixedSize(363, 84) 
        additional_info_widget.setStyleSheet("background-color: #a020a0;  border-radius: 15px;")


        #Additional Info text section
        additional_info_widget = QWidget()
        additional_info_layout = QVBoxLayout()
        additional_info_widget.setFixedSize(363, 84) 
        additional_info_widget.setStyleSheet("background-color: #a020b0;  border-radius: 15px;")

        #Additional Info vari section
        additional_info_widget = QWidget()
        additional_info_layout = QVBoxLayout()
        additional_info_widget.setFixedSize(363, 84) 
        additional_info_widget.setStyleSheet("background-color: #a020d0;  border-radius: 15px;")

        # Table Section
        table_widget = QWidget()
        table_layout = QVBoxLayout()
        table_widget.setFixedSize(702, 552) 
        table_widget.setStyleSheet("background-color: #a020e0;  border-radius: 15px;")

        main_layout.addWidget(table_widget)
        main_layout.addLayout(table_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)               


app = QApplication(sys.argv)
window = PortfolioApp()
window.show()
sys.exit(app.exec_())