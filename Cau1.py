import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import QTimer, Qt

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Đồng hồ đếm thời gian")
        self.setGeometry(100, 100, 600, 300)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.elapsed_time = 0  # Tổng thời gian tính bằng giây

    def initUI(self):
        # Nhãn tiêu đề
        self.title_label = QLabel("Đồng hồ đếm thời gian", self)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignCenter)

        # Nhãn hiển thị thời gian
        self.time_label = QLabel("Thời gian: 00:00:00", self)
        self.time_label.setStyleSheet("font-size: 18px;")
        self.time_label.setAlignment(Qt.AlignCenter)

        # Nhập FPS
        self.fps_label = QLabel("FPS:", self)
        self.fps_input = QLineEdit(self)

        # Nhãn trạng thái
        self.status_label = QLabel("Trạng thái: Dừng", self)

        # Nút
        self.start_button = QPushButton("Bắt đầu", self)
        self.pause_button = QPushButton("Tạm dừng", self)
        self.continue_button = QPushButton("Tiếp tục", self)
        self.stop_button = QPushButton("Kết thúc", self)

        self.start_button.clicked.connect(self.start_timer)
        self.pause_button.clicked.connect(self.pause_timer)
        self.continue_button.clicked.connect(self.continue_timer)
        self.stop_button.clicked.connect(self.stop_timer)

        # Bố cục
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.pause_button)
        hbox.addWidget(self.continue_button)
        hbox.addWidget(self.stop_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title_label)
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.fps_label)
        vbox.addWidget(self.fps_input)
        vbox.addLayout(hbox)
        vbox.addWidget(self.status_label)

        self.setLayout(vbox)

    def start_timer(self):
        self.elapsed_time = 0
        self.timer.start(1000)  # Cập nhật mỗi giây
        self.status_label.setText("Trạng thái: Đang chạy")

    def pause_timer(self):
        self.timer.stop()
        self.status_label.setText("Trạng thái: Tạm dừng")

    def continue_timer(self):
        self.timer.start(1000)  # Tiếp tục cập nhật mỗi giây
        self.status_label.setText("Trạng thái: Đang chạy")

    def stop_timer(self):
        reply = QMessageBox.question(self, 'Kết thúc', 'Bạn có chắc muốn thoát?', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            self.status_label.setText("Trạng thái: Dừng")

    def update_timer(self):
        self.elapsed_time += 1
        hours = self.elapsed_time // 3600
        minutes = (self.elapsed_time % 3600) // 60
        seconds = self.elapsed_time % 60
        self.time_label.setText(f"Thời gian: {hours:02}:{minutes:02}:{seconds:02}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec_())
