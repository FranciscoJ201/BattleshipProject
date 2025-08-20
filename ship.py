class Ship:
    def __init__(self,c1,c2):
        self.c1 = c1
        self.c2 = c2
        self.cells = []
        if c1[0] == c2[0]:
            for i in range(c2[1]+1):
                self.cells.append((c1[0],c2[1]-i))
        elif c1[1] == c2[1]:
            for i in range(c2[0]+1):
                self.cells.append((c1[0]+i,c2[1]))
            
newShip = Ship((0,4),(0,0))
print(newShip.c1,newShip.c2)
print(newShip.cells)

#if c2 isnt greater it bugs out fix it