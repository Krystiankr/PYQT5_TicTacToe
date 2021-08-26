from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore, QtWidgets
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_move = "X"

        # connect button
        self.ui.r1_c1.clicked.connect(lambda: self.clicked_button(self.ui.r1_c1, "r1_c1"))
        self.ui.r1_c2.clicked.connect(lambda: self.clicked_button(self.ui.r1_c2, "r1_c2"))
        self.ui.r1_c3.clicked.connect(lambda: self.clicked_button(self.ui.r1_c3, "r1_c3"))

        self.ui.r2_c1.clicked.connect(lambda: self.clicked_button(self.ui.r2_c1, "r2_c1"))
        self.ui.r2_c2.clicked.connect(lambda: self.clicked_button(self.ui.r2_c2, "r2_c2"))
        self.ui.r2_c3.clicked.connect(lambda: self.clicked_button(self.ui.r2_c3, "r2_c3"))

        self.ui.r3_c1.clicked.connect(lambda: self.clicked_button(self.ui.r3_c1, "r3_c1"))
        self.ui.r3_c2.clicked.connect(lambda: self.clicked_button(self.ui.r3_c2, "r3_c2"))
        self.ui.r3_c3.clicked.connect(lambda: self.clicked_button(self.ui.r3_c3, "r3_c3"))

    def clicked_button(self, btn, text):
        btn.setText(self.current_move)
        btn.setEnabled(False)
        self.switch()

    def change_current(self):
        self.ui.current_move.setText(self.current_move)

    def switch(self):
        self.current_move = "O" if self.current_move == "X" else "X"
        self.change_current()
        return self.current_move

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
