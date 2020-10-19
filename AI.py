import numpy as np


class RandomAI:
    def __init__(self):
        pass

    def take_action(self, board: np.ndarray):
        board = board.reshape((2, 15 * 15))
        board = np.sum(board, axis=0)
        board = np.nonzero(board)[0]
        resume_position = [ind for ind in range(15 * 15)]
        for ind in board:
            resume_position.remove(ind)
        step = np.random.choice(resume_position, 1)
        x = chr(step % 15 + 65)
        y = int(step) // 15
        return x, y + 1


class MCTS:
    class __TreeNode:
        def __init__(self):
            pass

        def myprint(self):
            print("成员类的init函数")

    def __init__(self, playout: int = 400):
        self.node = MCTS.__TreeNode()


if __name__ == '__main__':
    mcts = MCTS()
    print()
