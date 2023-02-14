from backend import Chatbot
from PyQt6.QtWidgets import  QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
import threading

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)
        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10,10,680,400)
        self.chat_area.setReadOnly(True)

        # Add input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10,420,560,40)
        self.input_field.returnPressed.connect(self.send_message)

        # Add button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(580,420,100,40)
        self.button.clicked.connect(self.send_message)

        self.show()
    
    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))  # Here args is a tuple with 1 item.
        thread.start()  # In order to not wait the response before updateing chat_area with already the user question. 

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input).replace("\n","<br>")
        self.chat_area.append(f"<p style='color:blue'>Bot: {response}</p>")

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())