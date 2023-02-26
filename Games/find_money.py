from random import choice


class GameFindMoney:
    def __init__(self, deposit=10):
        self.deposit = deposit
        self.map = None
        self.show_map = None

    def active_map(self, cols, rows):
        show_map = ["" for y in range(rows) for x in range(cols)]
        for y in range(rows):
            for x in range(cols):
                show_map[x + y * rows] = "❓"

        self.show_map = show_map

    def get_map(self, cols, rows):
        class Cell:
            def __init__(selfcell, x, y, type):
                selfcell.x = x
                selfcell.y = y
                selfcell.type = type

        obj = [Cell(x, y, None) for y in range(rows) for x in range(cols)]

        for y in range(rows):
            types = [self.deposit * 2, self.deposit * 5, self.deposit * 10]

            for x in range(cols):
                elem = choice(types)
                obj[x + y * cols].type = elem

        self.map = obj
