import os
import subprocess
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                             QLabel, QTextEdit)


class Tab1(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)

        self.btn_unlock = QPushButton("解锁 Bootloader")
        self.btn_unlock.clicked.connect(self.run_unlock_bl)
        self.btn_unlock.setFixedSize(200, 40)
        self.btn_unlock.setStyleSheet("""
            QPushButton {
                background-color: #0078d4;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #006cbd;
            }
        """)

        self.output = QTextEdit()
        self.output.setReadOnly(True)

        layout.addWidget(self.btn_unlock)
        layout.addWidget(QLabel("执行输出："))
        layout.addWidget(self.output)
        self.setLayout(layout)

    def run_unlock_bl(self):
        bat_path = os.path.join(
            os.path.dirname(__file__),
            "..", "..", "Functions", "UnlockBL", "unlock_bl.bat"
        )
        try:
            result = subprocess.run(
                [bat_path],
                capture_output=True,
                text=True,
                check=True,
                shell=True
            )
            self.output.append(result.stdout)
        except subprocess.CalledProcessError as e:
            self.output.append(f"错误：\n{e.stderr}")