from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class Tab4(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("功能4 界面待开发"))
        self.setLayout(layout)