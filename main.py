from board import Board
from ship import Ship

        
newShip = Ship((0,4), (0,0))
newShip1 = Ship((9,9),(7,9))
shipz = [newShip,newShip1]
tester = Board(10,shipz)

# print(tester.ships[1].cells)
# print(shipz[1].cells)
# tester.fire((9,9))
# tester.fire((3,9))
# tester.fire((8,9))
# tester.fire((7,9))
# print(tester.valid_move((3,1)))   
#   
# while tester.ships_left():
r = 0
c = 0
i = 1 
for j in range(30):
    if (r == 10) or (c==10):
        r = 0 + 2*i
        c = 0
        i+=1
    tester.fire((r,c))
    r+=1
    c+=1
    
    
print(tester)