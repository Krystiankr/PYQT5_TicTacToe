import sys
from random import choice

from Interface_code.AnimatedToggle import AnimatedToggle
from Interface_code.MainWindow import Ui_MainWindow

from control_files.TicTacToe import TicTacToe
from control_files.FileIO import File_Json

from PyQt5.QtWidgets import QLabel
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QVBoxLayout

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_move = "X"

        # Tic Tac Toe logic class
        self.tc = TicTacToe()

        # We have to create a class every time.
        self.load_scores()

        # Redirection of the button signal to its own function
        self.buttons = [self.ui.r1_c1, self.ui.r1_c2, self.ui.r1_c3,
                        self.ui.r2_c1, self.ui.r2_c2, self.ui.r2_c3,
                        self.ui.r3_c1, self.ui.r3_c2, self.ui.r3_c3]

        self.ui.r1_c1.clicked.connect(lambda: self.clicked_button(self.ui.r1_c1, 0))
        self.ui.r1_c2.clicked.connect(lambda: self.clicked_button(self.ui.r1_c2, 1))
        self.ui.r1_c3.clicked.connect(lambda: self.clicked_button(self.ui.r1_c3, 2))
        self.ui.r2_c1.clicked.connect(lambda: self.clicked_button(self.ui.r2_c1, 3))
        self.ui.r2_c2.clicked.connect(lambda: self.clicked_button(self.ui.r2_c2, 4))
        self.ui.r2_c3.clicked.connect(lambda: self.clicked_button(self.ui.r2_c3, 5))
        self.ui.r3_c1.clicked.connect(lambda: self.clicked_button(self.ui.r3_c1, 6))
        self.ui.r3_c2.clicked.connect(lambda: self.clicked_button(self.ui.r3_c2, 7))
        self.ui.r3_c3.clicked.connect(lambda: self.clicked_button(self.ui.r3_c3, 8))
        self.ui.reset_button.clicked.connect(self.reset_button)

        self.ui.reset_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.reset_button.customContextMenuRequested.connect(self.test)

        # Status bar, it informs you about current changes
        self.bar_label = QLabel("Welcome")
        self.statusBar().setStyleSheet("QLabel{font-weight:bold;color:grey}QStatusBar{border :1px solid gray;padding-left:8px;background:rgba(0,0,0,0);color:black;font-weight:bold;}")
        self.statusBar().addPermanentWidget(self.bar_label)

        mainToggle = AnimatedToggle()
        secondaryToggle = AnimatedToggle(
            checked_color="#FFB000",
            pulse_checked_color="#44FFB000"
        )

        self.mainToggle = AnimatedToggle()
        self.mainToggle.setFixedSize(mainToggle.sizeHint())
        self.ui.horizontalLayout_7.addWidget(self.mainToggle, alignment=QtCore.Qt.AlignLeft)
        self.mainToggle.stateChanged.connect(self.Toggle)
        self.ui.horizontalLayout_7.setContentsMargins(0, 0, 20, 0)

        self.clicked_button(self.buttons[0], 0)
        self.clicked_button(self.buttons[3], 3)
        self.clicked_button(self.buttons[4], 4)
        self.clicked_button(self.buttons[4], 4)

        self.ui.test_button.clicked.connect(self.edited)

    def edited(self):
        move = int(self.ui.edit_space.text())
        if move >= 0 and move <= 8:
            self.clean_move(move)
            self.ui.edit_space.setText("")
        else:
            print("number out of range")


    def test(self):
        print(self.tc.available_moves())

    def Toggle(self):
        if self.mainToggle.isChecked() == True:
            self.ui.o_label.setText("[PC]")
        else:
            self.ui.o_label.setText("[P]")
        #print("efect")

    def load_scores(self):
        file = File_Json()
        data = file.return_data() #output dict
        scores = [self.ui.points_x, self.ui.points_o]
        for label, text in zip(scores, data.values()):
            print(label.setText(str(text)))

    def update_scores(self, what_x_o):
        file = File_Json()
        file.increase_1(what_x_o)
        self.load_scores()

    def reset_button(self):
        for button in self.buttons:
            button.setEnabled(True)
            button.setText("")
        self.ui.current_move.setText(self.current_move)
        for btn in self.buttons:
            btn.setStyleSheet("")
        self.tc.reset_moves()
        self.switch_current_move()
        self.bar("Switch & Reset")

    def bar(self, text):
        self.bar_label.setText(text)

    def clicked_button(self, btn, position):
        if self.tc.is_move_possible(position):
            btn.setText(self.current_move)
            self.tc.set_move(position, self.current_move)
            btn.setEnabled(False)
            win_state = self.tc.check_if_winning_position(self.current_move)
            if win_state[0]:
                self.bar(f"Win {self.current_move}")
                self.end_of_game(win_state[1], self.current_move)
                return
            self.switch_current_move()
        else:
            self.bar("an impossible move")

    def end_of_game(self, winning_position, who):
        for position in winning_position:
            self.buttons[position].setStyleSheet("QPushButton{border: 4px solid lightgreen;}")
            self.statusBar().setStyleSheet(
                "QLabel{font-weight:bold;color:grey}QStatusBar{border :1px solid gray;padding-left:8px;background:rgba(0,0,0,0);color:black;font-weight:bold;}")
        self.turn_off_buttons()
        self.update_scores(who)

    def turn_off_buttons(self):
        for btn in self.buttons:
            btn.setEnabled(False)

    def change_display_current_move(self):
        self.ui.current_move.setText(self.current_move)

    def switch_current_move(self):

        self.current_move = ("O" if self.current_move == "X" else "X")
        self.change_display_current_move()
        if self.current_move == "O" and self.ui.o_label.text() == "[PC]":
            print("TT")
            print()
            rand_pos = self.tc.available_moves()
            choice_pos = choice(rand_pos)
            print()
            #self.tc.set_move(choice_pos, self.current_move)
            self.clicked_button(self.buttons[choice_pos], choice_pos)

    def winning_moves(self):
        pass

    def clean_move(self, pos):
        if self.buttons[pos].text() != "":
            self.buttons[pos].setText("")
            self.tc.clean_move(pos)
            self.buttons[pos].setEnabled(True)
            self.switch_current_move()
        else:
            print("pass")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
