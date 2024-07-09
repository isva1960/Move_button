import random
import sys
from Move_button import Ui_MainWindow
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushB_yes.enterEvent = self.on_button_hover
        self.pushB_yes.clicked.connect(self.on_button_yes)
        self.x_pushB_yes = self.pushB_yes.geometry().x()
        self.y_pushB_yes = self.pushB_yes.geometry().y()
        self.number_of_movements = 0

    def on_button_hover(self, event):
        # Измените положение кнопки случайным образом
        self.number_of_movements += 1
        if self.number_of_movements <= 9:
            x = random.randint(0, self.width() - self.pushB_yes.width())
            y = random.randint(self.y_pushB_yes + self.pushB_yes.height(), self.height() - self.pushB_yes.height())
            self.pushB_yes.move(x, y)
        else:
            self.pushB_yes.move(self.x_pushB_yes, self.y_pushB_yes)

    def on_button_yes(self):
        self.pushB_yes.setEnabled(False)
        self.label.setText("УРА!!! Пенсию повысят!!!")
        self.pushB_no.setText("Выход")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
