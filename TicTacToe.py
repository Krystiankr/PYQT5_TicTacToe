class TicTacToe:
    def __init__(self):
        self.moves = ["", "", "",
                      "", "", "",
                      "", "", ""]


    def check_if_winning_position(self) -> bool:
        winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for X_O in ["X", "O"]:
            tmp = True
            for position in winning_positions:
                for pos in position:
                    if self.moves[pos] != X_O:
                        tmp = False
                if tmp:
                    return True
        return False

    def set_move(self, position, who):
        self.moves[position] = who

    def print_board(self):
        for row in self.moves:
            print(row+str(1))
tc = TicTacToe()
tc.print_board()

print(tc.check_if_winning_position())