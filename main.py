from chestboard import Board

if __name__ == '__main__':
    board = Board()
    player = True

    while not board.check_win():
        print(board)
        print(f"{['白棋', '黑棋'][player]}回合:{[chr(9678), chr(9679)][player]}")
        if player:
            step = input("enter you step, like H-8:")
            step = step.split('-')
            print(step)
            board.put_stone(step[0].upper(), int(step[1]), int(player))
        else:
            step = input("enter you step, like H-8:")
            step = step.split('-')
            board.put_stone(step[0].upper(), int(step[1]), int(player))

        player = not player

