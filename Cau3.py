import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout,
    QLineEdit, QCheckBox, QSpinBox, QPushButton, QLabel
)

class UserRegistrationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Đăng Ký Thông Tin Người Dùng')
        self.setFixedSize(500, 400)

        layout = QVBoxLayout()
        formLayout = QFormLayout()

        # Thông tin người dùng
        self.firstNameInput = QLineEdit()
        self.lastNameInput = QLineEdit()
        self.titleInput = QLineEdit()
        self.ageInput = QSpinBox()
        self.nationalityInput = QLineEdit()

        formLayout.addRow("Tên:", self.firstNameInput)
        formLayout.addRow("Họ:", self.lastNameInput)
        formLayout.addRow("Chức danh:", self.titleInput)
        formLayout.addRow("Tuổi:", self.ageInput)
        formLayout.addRow("Quốc tịch:", self.nationalityInput)

        layout.addLayout(formLayout)

        # Khung đăng ký
        self.registeredCheckbox = QCheckBox("Trạng thái đăng ký")
        self.completedCoursesInput = QSpinBox()
        self.completedCoursesInput.setMinimum(0)
        self.semesterInput = QSpinBox()
        self.semesterInput.setMinimum(1)

        layout.addWidget(self.registeredCheckbox)
        layout.addWidget(QLabel("Số khóa học đã hoàn thành:"))
        layout.addWidget(self.completedCoursesInput)
        layout.addWidget(QLabel("Học kỳ:"))
        layout.addWidget(self.semesterInput)

        # Khung Điều khoản và Điều kiện
        self.termsCheckbox = QCheckBox("Tôi đồng ý với các điều khoản và điều kiện")
        layout.addWidget(self.termsCheckbox)

        # Nút Gửi
        self.submitButton = QPushButton("Gửi")
        self.submitButton.clicked.connect(self.submit_data)
        layout.addWidget(self.submitButton)

        self.setLayout(layout)

    def submit_data(self):
        firstName = self.firstNameInput.text()
        lastName = self.lastNameInput.text()
        title = self.titleInput.text()
        age = self.ageInput.value()
        nationality = self.nationalityInput.text()
        registered = self.registeredCheckbox.isChecked()
        completedCourses = self.completedCoursesInput.value()
        semester = self.semesterInput.value()
        termsAccepted = self.termsCheckbox.isChecked()

        print('Thông tin người dùng:', {
            'Tên': firstName,
            'Họ': lastName,
            'Chức danh': title,
            'Tuổi': age,
            'Quốc tịch': nationality,
            'Trạng thái đăng ký': registered,
            'Số khóa học đã hoàn thành': completedCourses,
            'Học kỳ': semester,
            'Chấp nhận điều khoản': termsAccepted
        })

        print("Dữ liệu đã được gửi thành công!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserRegistrationApp()
    window.show()
    sys.exit(app.exec_())
