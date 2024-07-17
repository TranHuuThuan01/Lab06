import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QFrame
)
from PyQt5.QtCore import Qt

class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ứng dụng Quét và Bảo vệ")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.initUI()

    def initUI(self):
        # Bố cục chính
        main_layout = QHBoxLayout()

        # Thanh bên
        sidebar = QFrame(self)
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("background-color: #4a90e2; color: white;")
        
        sidebar_layout = QVBoxLayout()
        self.status_label = QLabel("Trạng thái: Sẵn sàng", self)
        self.status_label.setStyleSheet("font-weight: bold; color: #f0f0f0;")
        sidebar_layout.addWidget(QLabel("Trạng thái:", self))
        sidebar_layout.addWidget(self.status_label)
        sidebar_layout.addWidget(QLabel("Cập nhật:", self))
        
        scan_button = QPushButton("Quét ngay", self)
        scan_button.setStyleSheet("background-color: #50e3c2; color: white; font-weight: bold;")
        sidebar_layout.addWidget(scan_button)
        
        sidebar.setLayout(sidebar_layout)
        main_layout.addWidget(sidebar)

        # Khu vực chính
        main_content = QFrame(self)
        main_content_layout = QVBoxLayout()

        title_label = QLabel("Tiêu đề Ứng dụng", self)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #4a90e2;")
        subtitle_label = QLabel("Phụ đề mô tả chức năng", self)
        subtitle_label.setStyleSheet("font-size: 18px; color: #7f8c8d;")

        main_content_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        main_content_layout.addWidget(subtitle_label, alignment=Qt.AlignCenter)

        # Nút trong khu vực chính
        button_layout = QGridLayout()
        quick_scan_button = QPushButton("Quét nhanh", self)
        quick_scan_button.setStyleSheet("background-color: #e67e22; color: white;")
        web_protect_button = QPushButton("Bảo vệ web", self)
        web_protect_button.setStyleSheet("background-color: #e74c3c; color: white;")
        settings_button = QPushButton("Cài đặt", self)
        settings_button.setStyleSheet("background-color: #3498db; color: white;")

        button_layout.addWidget(quick_scan_button, 0, 0)
        button_layout.addWidget(web_protect_button, 0, 1)
        button_layout.addWidget(settings_button, 1, 0, 1, 2)  # Nút lớn hơn

        main_content_layout.addLayout(button_layout)
        main_content.setLayout(main_content_layout)

        # Thêm khu vực chính vào bố cục
        main_layout.addWidget(main_content)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
