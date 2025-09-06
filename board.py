from ship import Ship
#0 = EMPTY
#1 = MISS
#2 = HIT
#3 = SHIP
class Board:
    def __init__(self,size,ships):
        self.size = size
        self.ships = ships #LIST OF SHIPS , a ship itself is a list of cells
        self.shots = set()
        grid = []

        for i in range(size):
            row = []
            for j in range(size):
                row.append(0)
            grid.append(row)
        self.grid = grid
        #adding ship cells to grid
        for ship in self.ships:
            for cell in ship.cells:
                x,y = cell
                self.grid[x][y] = 3

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.grid)
    
    def can_place_ship(self,ship):
        for cell in ship.cells:
            if not self.valid_move(cell):
                return False
        return True
    
    def fire(self,move):
        x, y = move
        if self.valid_move(move):
            self.shots.add(move)
            result = ""          # Will store "Hit" or "Miss"
            sunk_message = ""    # Used only if a ship sinks
            # if ship -> hit
            if self.grid[x][y] == 3:
                result = 'Hit'
                self.grid[x][y] = 2
                for s in self.ships:
                    if move in s.cells:
                        s.cells.remove(move)
                        s.check_float()
                        if not s.floating:
                            sunk_message = f"\nShip from {s.c1} to {s.c2} has sunk..."
                            self.ships.remove(s)  # Optional: Remove sunk ship
                        break  # Stop once correct ship is found
            # else -> miss
            else:
                result = "Miss"
                self.grid[x][y] = 1
            # Single safe print statement
            if result:
                print(f"FIRED AT {move}: {result}{sunk_message}")
        else:
            raise Exception('Not possible move')
        

    def valid_move(self,move):
        if move[0] >= 0 and move[0] <self.size and move[1] >= 0 and move[1] <self.size and (move not in self.shots) :
            return True
        else: 
            print(f'Not Valid Move, {move}')
            return False
        
        
newShip = Ship((0,4), (0,0))
newShip1 = Ship((9,9),(7,9))
shipz = [newShip,newShip1]
tester = Board(10,shipz)
# print(tester.ships[1].cells)
print(shipz[1].cells)
tester.fire((9,9))
tester.fire((3,9))
tester.fire((8,9))
tester.fire((7,9))
# print(tester.valid_move((3,1)))     
print(tester)
