class TicTacToe:
    def __init__(self):
        self.reset_moves()

    def check_if_winning_position(self, x_o) -> (bool, []):
        winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for position in winning_positions:
            tmp = True
            for pos in position:
                if self.moves[pos] != x_o:
                    tmp = False
            if tmp:
                return True, position
        return False, []

    def set_move(self, position, who):
        self.moves[position] = who

    def print_board(self): # interesting to list an array, but not useful at the moment
        for i, row in enumerate(self.moves):
            move = 0 if row == "" else row
            print(move, end=' ') if ((i+1) % 3 != 0) else print(move)
        print("-----")

    def is_move_possible(self, position):
        return True if self.moves[position] == "" else False

    def reset_moves(self):
        self.moves = ["", "", "",
                      "", "", "",
                      "", "", ""]

    def available_moves(self):
        return [i for i, el in enumerate(self.moves) if el == ""]

    def clean_move(self, pos):
        self.moves[pos] = ""
    # winning moves
    # blocked moves
    # random
