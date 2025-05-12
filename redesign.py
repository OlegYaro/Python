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
        #####################################################   Инициализация главного окна   #######################################################
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
        top_widget.setStyleSheet("background-color: #111;  border-radius: 15px;")
        
        # Balance Section
        balance_widget = QWidget()
        balance_layout = QVBoxLayout()
        balance_widget.setFixedSize(402, 176) 
        balance_widget.setStyleSheet("background-color: #7F5FFF;  border-radius: 15px;")
        balance_layout.setContentsMargins(15, 10, 0, 0)
        balance_layout.setSpacing(0)
        
        # Button Section
        button_widget = QWidget()
        button_layout = QVBoxLayout()
        button_widget.setFixedSize(163, 200) 
        button_widget.setStyleSheet("background-color: #7F5FFF;  border-radius: 15px;")

        # Current Balance section
        Current_balance_widget = QWidget()
        Current_balance_layout = QVBoxLayout()
        Current_balance_widget.setFixedSize(363, 74) 
        Current_balance_widget.setStyleSheet("background-color: #7F5FFF;  border-radius: 15px;")
        
        #Additional Info section
        additional_info_widget = QWidget()
        additional_info_layout = QHBoxLayout()
        additional_info_widget.setFixedSize(363, 84) 
        additional_info_widget.setStyleSheet("background-color: #7F5FFF; border-radius: 0px; ")
        additional_info_layout.setContentsMargins(0, 0, 0, 0)
        
        #Additional Info text section
        additional_info_text_widget = QWidget()
        additional_info_text_layout = QVBoxLayout()
        additional_info_text_widget.setFixedSize(190, 80) 
        additional_info_text_widget.setStyleSheet("background-color: #7F5FFF;  border-radius: 0px; padding-left: 0px;margin: 0px;")
        additional_info_text_layout.setContentsMargins(15, 0, 0, 0)
        additional_info_text_layout.setSpacing(0)

        #Additional Info vari section
        additional_info_value_widget = QWidget()
        additional_info_value_layout = QVBoxLayout()
        additional_info_value_widget.setFixedSize(180, 80) 
        additional_info_value_widget.setStyleSheet("background-color: #7F5FFF;  ")
        additional_info_value_layout.setContentsMargins(0, 0, 0, 0)

        # Table Section
        table_widget = QWidget()
        table_layout = QVBoxLayout()
        table_widget.setFixedSize(644, 500)
        table_widget.setStyleSheet("background-color: #a020f0;  border-radius: 15px;")


    ###################################################### секция с балансом ###########################################################
        Current_balance_label = QLabel(f"Current balance: ") 
        Current_balance_label.setStyleSheet("""
            QLabel {
                color: white;
                border-radius: 10px;
                font-size: 15px;   
                font-weight: bold;
                padding-left: 5px;
                }
        """)
            
        test_number = 23453 # Здесь будет баланс
        Current_balance_value = QLabel(f"{test_number}$")  # Здесь будет баланс
        Current_balance_value.setStyleSheet("""
            QLabel {    
                color: white;
                border-radius: 10px;
                font-size: 25px;   
                font-weight: bold;
                padding-left: 2px;
                
            }
        """)

        additional_info_text_label = QLabel("""<div style="line-height: 170%;">Total invested: <br>
                                                Total Profit: <br>
                                                Realised Profit: </div>""")
        additional_info_text_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 12px;   
                font-weight: medium;
                padding-left: 0px;
                }
                
            }
        """)
        


        additional_info_value_label = QLabel(f"""<div style="line-height: 170%;">{test_number}$ <br>
                                                {test_number}$ <br>
                                                {test_number}$ </div>""")  
        additional_info_value_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 12px;   
                font-weight: bold;
                padding-left: 0px;
                }
        """)


        additional_info_text_layout.addWidget(additional_info_text_label)
        additional_info_text_widget.setLayout(additional_info_text_layout)
        additional_info_value_layout.addWidget(additional_info_value_label, alignment=Qt.AlignRight)
        additional_info_value_widget.setLayout(additional_info_value_layout)
        
        Current_balance_layout.addWidget(Current_balance_label)
        Current_balance_layout.addWidget(Current_balance_value)
        Current_balance_widget.setLayout(Current_balance_layout)

    ################################################   Формирование виджетов   #######################################################
        # добавление виджетов с доп инфой в виджет доп инфы             
        additional_info_layout.addWidget(additional_info_text_widget)
        additional_info_layout.addLayout(additional_info_text_layout)
        additional_info_widget.setLayout(additional_info_layout)

        additional_info_layout.addWidget(additional_info_value_widget)
        additional_info_layout.addLayout(additional_info_value_layout)
        additional_info_widget.setLayout(additional_info_layout)


        # добавляем виждет с текужим балансом и виджет с доп инфой в виджет аланса
        balance_layout.addWidget(Current_balance_widget)
        balance_layout.addLayout(Current_balance_layout)
        balance_widget.setLayout(balance_layout)
        
        balance_layout.addWidget(additional_info_widget)
        balance_layout.addLayout(additional_info_layout)
        balance_widget.setLayout(balance_layout) 

        # добавляем виджет с балансом и виджет с кнопками в верхний виджет
        top_layout.addWidget(balance_widget)
        top_layout.addLayout(balance_layout)
        top_widget.setLayout(top_layout )

        # добавляем виджет с кнопками в верхний виджет
        top_layout.addWidget(button_widget)
        top_layout.addLayout(button_layout)
        top_widget.setLayout(top_layout)

        # добавляем верхний виджет в основной лейаут
        main_layout.addWidget(top_widget)
        main_layout.addLayout(top_layout)
        main_widget.setLayout(main_layout)

        main_layout.addWidget(table_widget)
        main_layout.addLayout(table_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)               


app = QApplication(sys.argv)
window = PortfolioApp()
window.show()
sys.exit(app.exec_())