class Ship:
    def __init__(self, c1, c2):
        x1, y1 = c1
        x2, y2 = c2
        self.cells = []
        self.floating = True
        if x1 == x2:  # vertical
            y1, y2 = sorted((y1, y2))
            self.c1, self.c2 = (x1, y1), (x2, y2)
            for y in range(y1, y2 + 1):
                self.cells.append((x1, y))
        elif y1 == y2:  # horizontal
            x1, x2 = sorted((x1, x2))
            self.c1, self.c2 = (x1, y1), (x2, y2)
            for x in range(x1, x2 + 1):
                self.cells.append((x, y1))
        else:
            raise ValueError("Ships must be horizontal or vertical (same x or same y).")
    def check_float(self):
        if len(self.cells) < 1:
            self.floating = False
    def __len__(self):
        return len(self.cells)
    def __str__(self):
        return f"Ship (c1={self.c1}, c2={self.c2}, cells={self.cells})"


# demo
# newShip = Ship((0,4), (0,0))
# # print(newShip.c1, newShip.c2)  # -> (0, 0) (0, 4)
# print(newShip.cells)           # -> [(0,0),(0,1),(0,2),(0,3),(0,4)]
# print(len(newShip))
# print(newShip)