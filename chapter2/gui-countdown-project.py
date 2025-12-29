import sys
from PySide6.QtCore import QSize,QTimer,Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import(
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton)


class CountDownApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.base_time = 60
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.setWindowTitle("test")
        self.setFixedSize(QSize(300, 200))
        self.create_widgets()    
        self.setup_layout()  
        self.setup_connections()
                    
    def create_widgets(self):
        # labels
        font = QFont("Arial", 24)
        font.setBold(True)
        
        self.welcome_label = QLabel("Welcome to my app")
        self.timer_label = QLabel("01:00")
        self.timer_label.setFont(font)
        # Buttons
        self.start_btn = QPushButton(text="Start")
        self.stop_btn = QPushButton(text="Stop")
        self.start_btn.setFixedSize(150, 50)
        self.stop_btn.setFixedSize(150, 50)
        
    def setup_layout(self):    
        layout = QVBoxLayout()
        layout.addWidget(self.welcome_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.timer_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.start_btn, alignment=Qt.AlignCenter)
        layout.addWidget(self.stop_btn, alignment=Qt.AlignCenter)
        
        main_widget = QWidget()
        main_widget.setLayout(layout)
        
        main_layout = QHBoxLayout()
        main_layout.addWidget(main_widget)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
    def setup_connections(self):
        self.start_btn.clicked.connect(self.start_timer)
        self.stop_btn.clicked.connect(self.stop_timer)
    
    def start_timer(self):
        if not self.timer.isActive():
            self.timer.start(1000)
            
    def update_timer(self):
        if self.base_time <= 0:
            self.timer.stop()
            return

        mins, secs = divmod(self.base_time, 60)
        timer_text = '{:02d}:{:02d}'.format(mins, secs)
        self.timer_label.setText(timer_text)

        self.base_time -= 1        
            
    def stop_timer(self):
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CountDownApp()
    window.show()
    sys.exit(app.exec())