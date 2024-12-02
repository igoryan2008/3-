import sys
import random
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Случайный цвет
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for (x, y, diameter, color) in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("MainWindow")
        self.setGeometry(0, 0, 800, 600)

        self.circle_widget = CircleWidget()
        self.setCentralWidget(self.circle_widget)

        self.pushButton = QPushButton("Кнопка", self)
        self.pushButton.setGeometry(320, 290, 75, 23)
        self.pushButton.clicked.connect(self.circle_widget.add_circle)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
