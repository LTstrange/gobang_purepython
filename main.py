import pickle

import AI
from chestboard import Board

if __name__ == '__main__':
    board = Board()
    ai = AI.RandomAI()
    player = True
    i = 0

    while not board.check_win():
        print(board)
        print(f"{['白棋', '黑棋'][player]}回合:{[chr(9678), chr(9679)][player]}")
        if player:
            step = ai.take_action(board.get_board())
            # step = input("enter you step, like H-8:")
            # step = step.split('-')
            board.put_stone(step[0].upper(), int(step[1]), int(player))
        else:
            step = ai.take_action(board.get_board())
            # step = input("enter you step, like H-8:")
            # step = step.split('-')
            board.put_stone(step[0].upper(), int(step[1]), int(player))

        player = not player
    print(board)
    board.check_win()
    print(board.get_pre_step())
    with open('chess_book_temp.pkl', 'wb') as file:
        pickle.dump(board.get_chess_book(), file)

