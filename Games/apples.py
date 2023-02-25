from random import choice


class GameApple:
    def __init__(self, deposit=0):
        self.deposit = deposit
        self.level = 0
        self.map = None
        self.show_map = None

    def active_map(self, str_map):
        show_map = ["" for y in range(10) for x in range(3)]
        for y in range(10):
            for x in range(3):
                if self.level < y:
                    show_map[x + y * 3] = "⬛"
                if self.level == y:
                    show_map[x + y * 3] = "❓"
                if self.level > y:
                    show_map[x + y * 3] = str_map[x + y * 3].type

        self.show_map = show_map

    def get_map(self, cols, rows):
        class Cell:
            def __init__(selfcell, x, y, type):
                selfcell.x = x
                selfcell.y = y
                selfcell.type = type

        obj = [Cell(x, y, None) for y in range(rows) for x in range(cols)]

        for y in range(rows):
            if y < 4:
                types = ["🍏", "🍏", "💣"]
            else:
                types = ["🍏", "💣", "💣"]

            types_copy = types
            for x in range(cols):
                elem = choice(types_copy)
                types_copy.remove(elem)
                obj[x + y * cols].type = elem

        self.map = obj
