import random


class Cell:
    def __init__(self, around_mines=0, mine=0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = 0


class GamePole():
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.init()

    def init(self):
        self.pole = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        return self.pole

    def add_mines(self, field):
        total_cells = [(i, j) for i in range(self.N) for j in range(self.N)]
        random.shuffle(total_cells)

        for i in range(self.M):
            x, y = total_cells[i]
            field[x][y].mine = 1
        return field


    def find_around_mines(self, field):
        rows = len(field)
        cols = len(field[0]) if rows > 0 else 0

        for ind in range(rows):
            for ind1 in range(cols):
                for i in range(max(0, ind - 1), min(rows, ind + 2)):
                    for j in range(max(0, ind1 - 1), min(cols, ind1 + 2)):
                        if (i, j) != (ind, ind1) and field[i][j].mine == 1:
                            field[ind][ind1].around_mines += 1
        self.pole = field
        return self.pole

    def show(self, field):
        for i in field:
            for j in i:
                if j.mine == 1:
                    print('*', end=' ')
                else:
                    print(f"{j.around_mines}", end=' ')
            print()


pole_game = GamePole(10, 12)
mine_field = pole_game.add_mines(pole_game.init())
mine_field1 = pole_game.find_around_mines(mine_field)
pole_game.show(mine_field1)



