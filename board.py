from ship import Ship

class Board:
    def __init__(self,size):
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
    def can_place(self,ship):
        pass
    def valid_move(self,move):
        if move[0] >= 0 and move[0] <self.size and move[1] >= 0 and move[1] <self.size and (move not in self.shots) :
            return True
        else: 
            return False
        
        

tester = Board(10)
tester.grid[0][1]=2
tester.grid[0][0]=1
tester.shots.add((3,1))
print(tester.valid_move((3,1)))     
# print(tester)
