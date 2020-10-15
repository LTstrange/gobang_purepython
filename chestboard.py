import time
import numpy as np
import os


class Board:
    def __init__(self):
        self.__board = np.zeros((2, 15, 15))
        self.__chess_book = []
        self.__previews_step = None

    def put_stone(self, x, y, blackOrWhite):
        if type(x) == str and x in [chr(i) for i in range(65, 80)] \
                and type(y) == int and 1 <= y <= 15 \
                and type(blackOrWhite) == int and blackOrWhite in [0, 1]:
            if 1 not in self.__board[:, y - 1, ord(x) - 65]:
                self.__board[blackOrWhite, y - 1, ord(x) - 65] = 1
                self.__previews_step = x + '-' + str(y) + '-' + str(blackOrWhite)
                self.__chess_book.append(self.__previews_step)
            else:
                print("重复落子")
                raise
        else:
            raise TypeError(
                f"落子输入格式错误, x:{x}:{type(x)}, y:{y}:{type(y)}, blackOrWhite:{blackOrWhite}:{type(blackOrWhite)}")

    @property
    def board(self):
        return self.__board

    @property
    def previews_step(self):
        return self.__previews_step

    @property
    def chess_book(self):
        return self.__chess_book

    def check_win(self):
        if self.__previews_step is None:
            return False
        coor = int(self.__previews_step[2:-2]) - 1, ord(self.__previews_step[0]) - 64 - 1  # 算出上一步在棋盘的坐标：【0-14】
        blackOrWhite = int(self.__previews_step[-1:])
        counter = [0, 0, 0, 0]  # 分别是水平，垂直，左上至右下，右上至左下
        for i in range(-4, 5):
            if 0 <= coor[0] + i <= 14 and \
                    self.__board[blackOrWhite, coor[0] + i, coor[1]]:
                counter[0] += 1
            else:
                counter[0] = 0
            if 0 <= coor[1] + i <= 14 and \
                    self.__board[blackOrWhite, coor[0], coor[1] + i]:
                counter[1] += 1
            else:
                counter[1] = 0
            if 0 <= coor[0] + i <= 14 and 0 <= coor[1] + i <= 14 and \
                    self.__board[blackOrWhite, coor[0] + i, coor[1] + i]:
                counter[2] += 1
            else:
                counter[2] = 0
            if 0 <= coor[0] - i <= 14 and 0 <= coor[1] + i <= 14 and \
                    self.__board[blackOrWhite, coor[0] - i, coor[1] + i]:
                counter[3] += 1
            else:
                counter[3] = 0
            if 5 in counter:
                print(f"{['白棋', '黑棋'][blackOrWhite]}获胜：{[chr(9678), chr(9679)][blackOrWhite]}")
                return True
        return False

    def __str__(self):
        os.system('cls')
        output = "   A B C D E F G H I J K L M N O\n"
        for row in range(15):
            output += f"{row + 1:2d}"
            for column in range(15):
                if self.__board[:, row, column][0]:
                    output += chr(9678)
                elif self.__board[:, row, column][1]:
                    output += chr(9679)
                else:
                    if row == 0 and column == 0:
                        output += '┏'
                    elif row == 14 and column == 0:
                        output += '┗'
                    elif row == 0 and column == 14:
                        output += '┓'
                    elif row == 14 and column == 14:
                        output += '┛'
                    elif row == 0:
                        output += '┯'
                    elif column == 0:
                        output += '┠'
                    elif row == 14:
                        output += '┷'
                    elif column == 14:
                        output += '┨'
                    else:
                        output += '┼'
            output += '\n'
        return output


if __name__ == '__main__':
    board = Board()
    for i in range(0, 6):
        board.put_stone(chr(ord('J') + i), 1, 0)
        print(board)
        board.check_win()
        time.sleep(1)
