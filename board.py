from ship import Ship

class Board:
    def __init__(self,size,ships):
        self.size = size
        self.ships = []
        self.shots = set()
        grid = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(0)
            grid.append(row)
        self.grid = grid
        


    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.grid)


tester = Board(10)
tester.grid[0][1]=2
tester.grid[0][0]=1
print(tester)
