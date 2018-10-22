from gtVector import *
class gtVertex:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vec = gtVector((x,y,z))
        
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
   
class cornerTable:
    def __init__(self, gTable, vTable):
        self.gTable = gTable
        self.vTable = vTable
        self.oTable = []
        
        for i in range(0, len(vTable)):
            self.oTable.append(0)
        
        for x in range(0,len(vTable)):
            for y in range(0, len(self.vTable)):
                if self.vTable[self.getN(x)] == self.vTable[self.getP(y)] and self.vTable[self.getP(x)] ==  self.vTable[self.getN(y)]:
                    self.oTable[x] = y
                    self.oTable[y] = x

    def getN(self, i):
        triangleNum = i//3
        return 3 * triangleNum + (i + 1) % 3
    
    def getP(self, i):
        return self.getN(self.getN(i))
    
    def getO(self, i):
        return self.oTable[i]
    
    def getR(self, i):
        return self.getO(self.getN(i))
    
    def getL(self, i):
        return self.getO(self.getP(i))     