import os
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QListWidget,
                             QTabWidget, QFrame)
from .tab1 import Tab1
from .tab2 import Tab2
from .tab3 import Tab3
from .tab4 import Tab4


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EEBBK S3刷机工具箱")
        self.setGeometry(100, 100, 1000, 600)
        self.setup_ui()

    def setup_ui(self):
        # 主布局
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # 侧边导航栏
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(200)
        self.sidebar.addItems(["解锁BL", "功能2", "功能3", "功能4"])
        self.sidebar.currentRowChanged.connect(self.switch_tab)

        # 标签页
        self.tabs = QTabWidget()
        self.tabs.tabBar().hide()  # 隐藏标签头
        self.tabs.addTab(Tab1(), "")
        self.tabs.addTab(Tab2(), "")
        self.tabs.addTab(Tab3(), "")
        self.tabs.addTab(Tab4(), "")

        # 添加分割线
        separator = QFrame()
        separator.setFrameShape(QFrame.VLine)
        separator.setLineWidth(1)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(separator)
        main_layout.addWidget(self.tabs)

        self.setCentralWidget(main_widget)
        self.apply_styles()

    def switch_tab(self, index):
        self.tabs.setCurrentIndex(index)

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f3f3f3;
            }
            QListWidget {
                background-color: #ffffff;
                border: none;
                font-size: 14px;
                padding: 10px 0;
            }
            QListWidget::item {
                height: 40px;
                padding-left: 20px;
            }
            QListWidget::item:selected {
                background-color: #e5f1fb;
                color: #0078d4;
            }
        """)