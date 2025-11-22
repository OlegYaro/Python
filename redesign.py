import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView,
    QApplication,QLineEdit , QLineEdit, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class HistoryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("History" )
        self.setStyleSheet("background-color: #222;")
        self.setGeometry(100, 100, 648, 425)
        self.init_ui()

    def init_ui(self):
        main_history_layoty = QVBoxLayout()
        self.search_field = QLineEdit()
        text_label = QLabel(f"<b style='font-size: 20px;'>History</b>")
        text_label.setFont(QFont("Arial", 16))
        text_label.setStyleSheet("""
            QLabel {
                padding-left: 15px;
            }
        """)
        main_history_layoty.addWidget(text_label)
        self.search_field.setPlaceholderText("Search for token history...")
        main_history_layoty.addWidget(self.search_field)
        self.search_field.setStyleSheet("""
            QLineEdit {
                background-color: #595959;
                color: white;
                border: 1px solid #7F5FFF;
                border-radius: 10px;
                padding: 10px;
                font-family: Arial;
                
            }
        """)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Name", "Invested", "Buy/Sell", "Price", "Amount", "Date"])
        self.table.setShowGrid(False)
        main_history_layoty.addWidget(self.table)

        self.setLayout(main_history_layoty)

        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #222;
                color: white;
                gridline-color: rgba(255, 255, 255, 50);  /* Не нужен если setShowGrid(False) */
                font-family: Arial;
                
            }

            QTableWidget::item {
                border-bottom: 1px solid rgba(255, 255, 255, 50);  /* Только горизонтальные */
                padding: 0px;
            }
        """)
        self.table.verticalHeader().setVisible(False)

        
        self.table.setColumnWidth(5, 113)
        
        header = self.table.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #111;
                color: white;
                padding: 8px;
                font-weight: bold;
                font-size: 14px;
                border: none;
                border-bottom: 1px solid rgba(255, 255, 255, 0.2);
                font-family: Arial;

            }
        """)
        self.search_field.textChanged.connect(self.filter_table)

        
        self.all_data = [
            ("BTC", "$500", "Buy", "$20000", "0.025", "2024-04-01"),
            ("ETH", "$200", "Sell", "$3000", "0.0667", "2024-04-02"),
            ("LTC", "$150", "Buy", "$150", "1.0", "2024-04-03"),
            ("USDT", "$300", "Deposit", "$1", "300.0", "2024-04-04"),
            ("XRP", "$100", "Buy", "$0.5", "200.0", "2024-04-05"),
            ("ADA", "$250", "Sell", "$1.5", "166.67", "2024-04-06"),
            ("DOT", "$350", "Buy", "$20", "17.5", "2024-04-07"),
            ("LINK", "$400", "Sell", "$25", "16.0", "2024-04-08"),
            ("SOL", "$450", "Buy", "$50", "9.0", "2024-04-09"),
            ("MATIC", "$500", "Sell", "$2", "250.0", "2024-04-10"),
            ("DOGE", "$600", "Buy", "$0.1", "6000.0", "2024-04-11"),
            ("SHIB", "$700", "Sell", "$0.00001", "70000000.0", "2024-04-12"),
            ("TRX", "$800", "Buy", "$0.05", "16000.0", "2024-04-13"),
            ("BNB", "$900", "Sell", "$300", "3.0", "2024-04-14"),
            ("XLM", "$1000", "Buy", "$0.1", "10000.0", "2024-04-15"),
            ("AVAX", "$1100", "Sell", "$50", "22.0", "2024-04-16"),
            ("MATIC", "$500", "Sell", "$2", "250.0", "2024-04-10"),
            ("DOGE", "$600", "Buy", "$0.1", "6000.0", "2024-04-11"),
            ("SHIB", "$700", "Sell", "$0.00001", "70000000.0", "2024-04-12"),
            ("TRX", "$800", "Buy", "$0.05", "16000.0", "2024-04-13"),
            ("BNB", "$900", "Sell", "$300", "3.0", "2024-04-14"),
            ("XLM", "$1000", "Buy", "$0.1", "10000.0", "2024-04-15"),
            ("AVAX", "$1100", "Sell", "$50", "22.0", "2024-04-16"), 
            ("MATIC", "$500", "Sell", "$2", "250.0", "2024-04-10"),
            ("DOGE", "$600", "Buy", "$0.1", "6000.0", "2024-04-11"),
            ("SHIB", "$700", "Sell", "$0.00001", "70000000.0", "2024-04-12"),
            ("TRX", "$800", "Buy", "$0.05", "16000.0", "2024-04-13"),
            ("BNB", "$900", "Sell", "$300", "3.0", "2024-04-14"),
            ("XLM", "$1000", "Buy", "$0.1", "10000.0", "2024-04-15"),
            ("AVAX", "$1100", "Sell", "$50", "22.0", "2024-04-16"),

            
        ]
        self.populate_table(self.all_data)

        


        for row in range(self.table.rowCount()):
            self.table.setRowHeight(row, 50)

    def row_clicked(self, row, column):
        selected_token = self.table.item(row, 1).text()  # тикет (например, ETH)
        self.open_add_token_window(selected_token)
    
    def open_add_token_window(self, token_ticker):
        self.token_window = AddTokenWindow()
        self.token_window.setWindowTitle(f"Add Token: {token_ticker}")
        self.token_window.show()


    def populate_table(self, data):
        self.table.setRowCount(0)
        for row_data in data:
            row = self.table.rowCount()
            self.table.insertRow(row)
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(value)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  
                self.table.setItem(row, col, item)

    def filter_table(self, text):
        filtered = []
        text = text.lower()
        for row in self.all_data:
            if any(text in str(cell).lower() for cell in row):
                filtered.append(row)
        self.populate_table(filtered)

# дата и время должны автоматически подставляться
# добавить метод который будет выбирать иконки

class AddTokenWindow(QWidget):
    def __init__(self, icon_path=None, token_name="Token"):
        super().__init__()
        self.setWindowTitle(f"Add {token_name}")
        self.setGeometry(100, 100, 400, 500)
        self.setStyleSheet("background-color: #2b2a2a; color: white;")
        self.init_ui(icon_path, token_name)

    def init_ui(self, icon_path, token_name):
        main_addtoken_layout = QVBoxLayout()
        main_addtoken_layout.setContentsMargins(20, 20, 20, 20)
        main_addtoken_layout.setSpacing(15)

        header_layout = QHBoxLayout()
        icon_label = QLabel()
        if icon_path:
            pixmap = QPixmap(icon_path).scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon_label.setPixmap(pixmap)
        text_label = QLabel(f"<b style='font-size: 20px;'>Add {token_name.lower()}</b>")
        text_label.setFont(QFont("Arial", 16))
        header_layout.addWidget(icon_label)
        header_layout.addWidget(text_label)
        header_layout.addStretch()
        main_addtoken_layout.addLayout(header_layout)

        action_layout = QHBoxLayout()
        self.buy_button = QPushButton("Buy")
        self.sell_button = QPushButton("Sell")

        for btn in [self.buy_button, self.sell_button]:
            btn.setCheckable(True)
            btn.setFixedHeight(40)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3a3a3a;
                    border-radius: 10px;
                    font-weight: bold;
                    font-size: 14px;
                    color: white;
                    font-family: Arial;
                }
                QPushButton:checked {
                    background-color: #bb6bff;
                }
            """)
            action_layout.addWidget(btn)

        self.buy_button.clicked.connect(lambda: self.set_action("buy"))
        self.sell_button.clicked.connect(lambda: self.set_action("sell"))
        main_addtoken_layout.addLayout(action_layout)

        self.fields = {}
        for label_text in ["Amount", "Price", "Date & Time (auto)", "Total"]:
            main_addtoken_layout.addWidget(QLabel(label_text))
            field = QLineEdit()
            field.setStyleSheet("""
                QLineEdit {
                    background-color: #444;
                    color: white;
                    border: none;
                    border-radius: 10px;
                    padding: 10px;
                    font-size: 14px;
                    font-family: Arial;
                }
            """)
            self.fields[label_text] = field
            main_addtoken_layout.addWidget(field)

        add_button = QPushButton("➕  Add Transaction")
        add_button.setFixedHeight(48)
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #bb6bff;
                color: white;
                border-radius: 12px;
                font-size: 16px;
                font-weight: bold;
                font-family: Arial;
            }
            QPushButton:hover {
                background-color: #a157e8;
            }
        """)
        add_button.clicked.connect(self.close)
        
        main_addtoken_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        main_addtoken_layout.addWidget(add_button)

        self.setLayout(main_addtoken_layout)

    def set_action(self, action):
        if action == "buy":
            self.buy_button.setChecked(True)
            self.sell_button.setChecked(False)
            self.selected_action = "Buy"
        else:
            self.buy_button.setChecked(False)
            self.sell_button.setChecked(True)
            self.selected_action = "Sell"
    

class AddTokenListWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Token")
        self.setGeometry(100, 100, 320, 459)
        self.init_ui()

    def init_ui(self):
        main_listtoken_layout = QVBoxLayout()
        self.search_field = QLineEdit()
        text_label = QLabel(f"<b style='font-size: 20px;padding-left: 10px;'>List of token</b> ")
        text_label.setStyleSheet("""
            QLabel {
                padding-left: 15px;
            }
        """)
        text_label.setFont(QFont("Arial", 16))
        main_listtoken_layout.addWidget(text_label)
        self.search_field.setPlaceholderText("Search for token history...")
        main_listtoken_layout.addWidget(self.search_field)
        self.search_field.setStyleSheet("""
            QLineEdit {
                background-color: #595959;
                color: white;
                border: 1px solid #7F5FFF;
                border-radius: 10px;
                padding: 10px;
                font-family: Arial;
            }
        """)
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Icon", "Tiket", "Full name"])
        self.table.setShowGrid(False)
        main_listtoken_layout.addWidget(self.table)
        self.setLayout(main_listtoken_layout)

        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #222;
                color: white;
                gridline-color: rgba(255, 255, 255, 50);  /* Не нужен если setShowGrid(False) */
                font-family: Arial;
            }
            QTableWidget::item {
                border-bottom: 1px solid rgba(255, 255, 255, 50);  /* Только горизонтальные */
                padding: 0px;
            }
        """)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnWidth(0, 70)
        self.table.setColumnWidth(1, 110)
        self.table.setColumnWidth(2, 110)


        header = self.table.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #111;         
                color: white;
                padding: 8px;
                font-weight: bold;
                font-size: 14px;
                border: none;
                border-bottom: 1px solid rgba(255, 255, 255, 0.2);
                font-family: Arial;
            }
        """)
        self.search_field.textChanged.connect(self.filter_table)

        icon = ("/home/krip/Python/Python/Photo/eth.png")

        # PnL.setAlignment(Qt.AlignCenter) надо добвить вот эту хуйню чтоб было кравиво и исправить то что таблица сбивается 
        self.all_data = [   
            (icon, "BTC", "Bitcoin"),
            (icon, "ETH", "Ethereum"),
            (icon, "LTC", "Litecoin"),
            (icon, "USDT", "Tether"),
            (icon, "XRP", "Ripple"),
            (icon, "ADA", "Cardano"),
            (icon, "DOT", "Polkadot"),
            (icon, "LINK", "Chainlink"),
            (icon, "SOL", "Solana"),
            (icon, "MATIC", "Polygon"),
            (icon, "DOGE", "Dogecoin"),
            (icon, "SHIB", "Shiba Inu"),
            (icon, "TRX", "Tron"),
            (icon, "BNB", "Binance Coin"),            
        ]
        self.populate_table(self.all_data)

        for row in range(self.table.rowCount()):
            self.table.setRowHeight(row, 50)

        self.table.cellClicked.connect(self.row_clicked)

    def row_clicked(self, row, column):
        selected_token = self.table.item(row, 1).text()  # тикет (например, ETH)
        self.open_add_token_window(selected_token)
    
    def open_add_token_window(self, token_ticker):
        self.token_window = AddTokenWindow()
        self.token_window.setWindowTitle(f"Add Token: {token_ticker}")
        parent_geometry = self.geometry()
        new_geometry = self.token_window.frameGeometry()
        
        center_point = parent_geometry.center()
        new_geometry.moveCenter(center_point)
        self.token_window.move(new_geometry.topLeft())

        self.token_window.show() 

    def populate_table(self, data):
        self.table.setRowCount(0)
        for row_data in data:
            row = self.table.rowCount()
            self.table.insertRow(row)
            for col, value in enumerate(row_data):
                if col == 0:
                    icon_label = QLabel()
                    pixmap = QPixmap(value).scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    icon_label.setPixmap(pixmap)
                    icon_label.setAlignment(Qt.AlignCenter)
                    self.table.setCellWidget(row, col, icon_label)
                else:
                    item = QTableWidgetItem(value)
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  
                    self.table.setItem(row, col, item)
    def filter_table(self, text):
        filtered = []
        text = text.lower()
        for row in self.all_data:
            if any(text in str(cell).lower() for cell in row):
                filtered.append(row)
        self.populate_table(filtered)  
    # добавить метод который будет выбирать иконки 
    # добавить метод который будет выбирать иконки  
    # def open_add_token_window(self, token_ticker):
    # # ищем иконку по тикеру
    # token = next((row for row in self.all_data if row[1] == token_ticker), None)
    # if token:
    #     icon_path, ticker, name = token
    #     self.token_window = AddTokenWindow(icon_path, name)
    #     self.token_window.show()


class NotificationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notification")
        self.setGeometry(100, 100, 320, 360)
        self.init_ui()

    def init_ui(self):
        main_notification_layout = QVBoxLayout()
        main_notification_layout.setContentsMargins(20, 20, 20, 20)
        main_notification_layout.setSpacing(15)

        header_layout = QHBoxLayout()
        icon_label = QLabel()
        text_label = QLabel(f"<b style='font-size: 20px;'>Add Notification</b>")
        text_label.setFont(QFont("Arial", 16))
        header_layout.addWidget(icon_label)
        header_layout.addWidget(text_label)
        header_layout.addStretch()
        main_notification_layout.addLayout(header_layout)

     

        self.fields = {}
        for label_text in ["Name of token ", "Price for huj", "Email or phone number"]:
            main_notification_layout.addWidget(QLabel(label_text))
            field = QLineEdit()
            field.setStyleSheet("""
                QLineEdit {
                    background-color: #444;
                    color: white;
                    border: none;
                    border-radius: 10px;
                    padding: 10px;
                    font-size: 14px;
                    font-family: Arial;     
                }
            """)
            self.fields[label_text] = field
            main_notification_layout.addWidget(field)

        add_button = QPushButton("➕  Add Notification")
        add_button.setFixedHeight(48)
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #bb6bff;
                color: white;
                border-radius: 12px;
                font-size: 16px;
                font-weight: bold;
                font-family: Arial;
            }
            QPushButton:hover {
                background-color: #a157e8;
            }
        """)
        add_button.clicked.connect(self.close)
        
        main_notification_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        main_notification_layout.addWidget(add_button)

        self.setLayout(main_notification_layout)
        

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
        button_widget.setStyleSheet("background-color: #111;  border-radius: 15px;")

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
        table_widget.setStyleSheet("background-color: #111;  border-radius: 15px;")


    ###################################################### секция с балансом ###########################################################
        Current_balance_label = QLabel(f"Current balance: ") 
        Current_balance_label.setFont(QFont("Arial"))
        Current_balance_label.setStyleSheet("""
            QLabel {
                color: white;
                border-radius: 10px;
                font-size: 20px;   
                font-weight: bold;
                padding-left: 1px;
                font-family: Arial;                            
                }
        """)
            
        test_number = 23453 # Здесь будет баланс
        Current_balance_value = QLabel(f"{test_number}$")  # Здесь будет баланс
        Current_balance_value.setStyleSheet("""
            QLabel {    
                color: white;
                border-radius: 10px;
                font-size: 30px;   
                font-weight: bold;
                padding-left: 1px;
                font-family: Arial;
            }
        """)

        additional_info_text_label = QLabel("""<div style="line-height: 170%;">Total invested: <br>
                                                Total Profit: <br>
                                                Realised Profit: </div>""")
        additional_info_text_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 14px;   
                font-weight: medium;
                padding-left: 0px;
                font-family: Arial;
                }
                
            }
        """)
        


        additional_info_value_label = QLabel(f"""<div style="line-height: 170%;">{test_number}$ <br>
                                                {test_number}$ <br>
                                                {test_number}$ </div>""")  
        additional_info_value_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 14px;   
                font-weight: bold;
                padding-left: 0px;
                font-family: Arial;
                }
        """)


        additional_info_text_layout.addWidget(additional_info_text_label)
        additional_info_text_widget.setLayout(additional_info_text_layout)
        additional_info_value_layout.addWidget(additional_info_value_label, alignment=Qt.AlignRight)
        additional_info_value_widget.setLayout(additional_info_value_layout)
        
        Current_balance_layout.addWidget(Current_balance_label)
        Current_balance_layout.addWidget(Current_balance_value)
        Current_balance_widget.setLayout(Current_balance_layout)


    ###################################################### секция с кнопками ###########################################################

        history_button = QPushButton()
        history_button.setText("History")
        history_button.setStyleSheet("""
            QPushButton {       
                background-color: #B29EFF;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                font-family: Arial;
            }
            QPushButton:hover {
                background-color: #e0b3ff;
            }
        """)
        history_button.setFixedSize(150, 40)  
        button_layout.addWidget(history_button, alignment=Qt.AlignTop)
        button_widget.setLayout(button_layout)

        add_token_button = QPushButton()
        add_token_button.setText("Add token")
        add_token_button.setStyleSheet("""
            QPushButton {       
                background-color: #B29EFF;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                font-family: Arial;
            }
            QPushButton:hover {
                background-color: #e0b3ff;
            }
        """)
        add_token_button.setFixedSize(150, 40)  
        button_layout.addWidget(add_token_button, alignment=Qt.AlignTop)
        button_widget.setLayout(button_layout)

        notification_button = QPushButton()
        notification_button.setText("Notification")
        notification_button.setStyleSheet("""
            QPushButton {       
                background-color: #B29EFF;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                font-family: Arial;
            }
            QPushButton:hover {
                background-color: #e0b3ff;
            }
        """)
        notification_button.setFixedSize(150, 40)  
        button_layout.addWidget(notification_button, alignment=Qt.AlignTop)
        button_widget.setLayout(button_layout)

        # Подключаем кнопки к функциям
        history_button.clicked.connect(self.open_window_history)
        add_token_button.clicked.connect(self.open_window_add_token)
        notification_button.clicked.connect(self.open_window_notification)


    ################################################   Секция таблицы  #######################################################
        

        # Создаем таблицу
        table = QTableWidget()
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(["","Name", "Invested", "Buy Price", "Price", "Amount", "PnL"])
        table.setShowGrid(False)
        # Invested

        icon = ("/home/krip/Python/Python/Photo/eth.png")


        table.setRowCount(100)
        for row in range(100):
            icon_label = QLabel()
            pixmap = QPixmap(icon).scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon_label.setPixmap(pixmap)
            icon_label.setAlignment(Qt.AlignCenter)

            # тут потом можно сделать цикл котоырй будет принимать например картеж списков и уже добавлять их в значения 
            name = QLabel("ETH")
            invested_value= QLabel("$2003.14")
            Buy_price = QLabel("$464")
            price = QLabel("$3200")
            amount = QLabel("4.56")
            PnL = QLabel("82.34%")
            invested_value.setAlignment(Qt.AlignCenter)
            Buy_price.setAlignment(Qt.AlignCenter)
            price.setAlignment(Qt.AlignCenter)
            amount.setAlignment(Qt.AlignCenter)
            PnL.setAlignment(Qt.AlignCenter)



            table.setCellWidget(row, 0, icon_label)
            table.setCellWidget(row, 1, name)
            table.setCellWidget(row, 2, invested_value)
            table.setCellWidget(row, 3, Buy_price)
            table.setCellWidget(row, 4, price)
            table.setCellWidget(row, 5, amount)
            table.setCellWidget(row, 6, PnL)

        
        table.verticalHeader().setVisible(False)
        #table.setAlternatingRowColors(True)
        #table.setStyleSheet("QTableWidget { background-color: #121212; color: white; }")
        table.setStyleSheet("""
            QTableWidget {
                background-color: #121212;
                color: white;
                gridline-color: rgba(255, 255, 255, 50);  /* Не нужен если setShowGrid(False) */
                font-family: Arial;
            }

            QTableWidget::item {
                border-bottom: 1px solid rgba(255, 255, 255, 50);  /* Только горизонтальные */
                padding: 0px;
            }
        """)
        header = table.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #111;
                color: white;
                padding: 8px;
                font-weight: bold;
                font-size: 14px;
                border: none;
                border-bottom: 1px solid rgba(255, 255, 255, 0.2);
                font-family: Arial;
            }
        """)

        for row in range(table.rowCount()):
            table.setRowHeight(row, 50)

        table.resizeColumnsToContents()
        table.setColumnWidth(0, 32)  
        table.setColumnWidth(1, 120)
        table.setColumnWidth(2, 95)  
        table.setColumnWidth(3, 95)
        table.setColumnWidth(4, 95)  
        table.setColumnWidth(5, 95) 
        table.setColumnWidth(6, 85)   

        table_layout.addWidget(table)
        table_widget.setLayout(table_layout)
        #self.setLayout(layout)

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


    def open_window_history(self):
        self.new_window = HistoryWindow()

        parent_geometry = self.geometry()
        new_geometry = self.new_window.frameGeometry()
        
        center_point = parent_geometry.center()
        new_geometry.moveCenter(center_point)
        self.new_window.move(new_geometry.topLeft())

        self.new_window.show()   


    def open_window_add_token(self):
        self.new_window = AddTokenListWindow()
        parent_geometry = self.geometry()
        new_geometry = self.new_window.frameGeometry()
        
        center_point = parent_geometry.center()
        new_geometry.moveCenter(center_point)
        self.new_window.move(new_geometry.topLeft())

        self.new_window.show()   

    def open_window_notification(self):
        self.new_window = NotificationWindow()
        parent_geometry = self.geometry()
        new_geometry = self.new_window.frameGeometry()
        
        center_point = parent_geometry.center()
        new_geometry.moveCenter(center_point)
        self.new_window.move(new_geometry.topLeft())

        self.new_window.show()         


app = QApplication(sys.argv)
window = PortfolioApp()
window.show()
sys.exit(app.exec_())