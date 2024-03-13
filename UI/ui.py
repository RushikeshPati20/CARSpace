from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import sys
from subprocess import call

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.p = None
        self.setWindowTitle("CheckParkingSpace") #title name
        self.setWindowIcon(QIcon("dependencies/icon1.png"))
        self.setFixedSize(1280, 720)  # Set window size to 1280x720
        self.setStyleSheet("background-color : #E0F4FF;  ")   #bg color
        self.UiComponents()
        self.center()
        self.show()

    def UiComponents(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        label = QLabel(self)
        pixmap = QPixmap("dependencies/logoo.png")
        label.setPixmap(pixmap)
        label.setGeometry(253, 10, 200, 200)
        main_layout.addWidget(label)

        # Horizontal layout for "Select Image" label and "Browse File" button
        hbox_layout = QHBoxLayout()
        hbox_layout.setAlignment(Qt.AlignCenter)

        self.label_1 = QLabel("Select Image:")
        font = self.label_1.font()
        font.setPointSize(14)
        self.label_1.setFont(font)
        hbox_layout.addWidget(self.label_1)

        button = QPushButton("Browse File")
        button.setStyleSheet("background-color:#87C4FF ;border-width: 2px;border-radius: 15px; font-size: 15px;")
        button.clicked.connect(self.pushbutton_handler)
        button.setFixedSize(QSize(130, 60))
        hbox_layout.addWidget(button)

        main_layout.addLayout(hbox_layout)

        self.label_2 = QLabel("")
        #main_layout.addWidget(self.label_2) path for the image

        start_button = QPushButton("Start App")
        start_button.setStyleSheet("background-color:#87C4FF ;border-width: 2px;border-radius: 20px; font-size: 16px;")
        start_button.clicked.connect(self.start_App)
        start_button.setFixedSize(QSize(280, 60))
        main_layout.addWidget(start_button)

        self.setLayout(main_layout)

    def pushbutton_handler(self):
        self.open_dialogbox()

    def open_dialogbox(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Image Files(*.png)")
        if filename:
            self.label_2.setText(filename)
            self.p = QProcess()
            self.p.start("python", ['src/ParkingSpacePicker.py'])

    def start_App(self):
        self.p = QProcess()
        self.p.start("python", ['src/main.py'])

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())