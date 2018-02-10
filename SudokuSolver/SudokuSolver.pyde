
inputMatrix = [2, 0, 0,  8, 0, 4,  0, 0, 6,
             0, 0, 6,  0, 0, 0,  5, 0, 0,
             0, 7, 4,  0, 0, 0,  9, 2, 0,
             
             3, 0, 0,  0, 4, 0,  0, 0, 7,
             0, 0, 0,  3, 0, 5,  0, 0, 0,
             4, 0, 0,  0, 6, 0,  0, 0, 9,
             
             0, 1, 9,  0, 0, 0,  7, 4, 0,
             0, 0, 8,  0, 0, 0,  2, 0, 0,
             5, 0, 0,  6, 0, 8,  0, 0, 1,]


emptyMatrix = [0, 0, 0,  0, 0, 0,  0, 0, 0,
             0, 0, 0,  0, 0, 0,  0, 0, 0,
             0, 0, 0,  0, 0, 0,  0, 0, 0,
             
             0, 0, 0,  0, 0, 0,  0, 0, 0,
             0, 0, 0,  0, 0, 0,  0, 0, 0,
             0, 0, 0,  0, 0, 0,  0, 0, 0,
             
             0, 0, 0,  0, 0, 0,  0, 0, 0,
             0, 0, 0,  0, 0, 0,  0, 0, 0,
             0, 0, 0,  0, 0, 0,  0, 0, 0,]


cells = []
finished = False

def setup():
    for i in range(9**2):
        n = inputMatrix[i]
        cells.append(cell(i, n))
    dispMatrix(cells)
    print ''
    print ''


def draw():
    global finished

    if finished == False:
        checkAll = [x in [m.n for m in cells] for x in emptyMatrix]
        if any(checkAll):
            for c in cells:
                c.checkRow()
                c.checkCol()
                c.checkBox()
        else:
            dispMatrix(cells)
            finished = True
            print 'DONE'
        
    
################################### Classes ############################################

class cell():
    def __init__(self, pos=0, n=0):
        self.pos = pos
        self.i = floor((pos/9.0 - floor(pos/9)) * 9)
        self.j = floor(pos/9)
        self.n = n
        if self.n == 0: self.posNum = [1,2,3,4,5,6,7,8,9]
        
        
    def checkRow(self):
        if self.n == 0:
            row = [m.n for m in cells[self.j*9:self.j*9 + 9]]
            check = [x in row for x in self.posNum]
            self.posNum = [x for (x, v) in zip(self.posNum, check) if not v]
            #print self.posNum
            if len(self.posNum) == 1: self.n = self.posNum[0]
            
    def checkCol(self):
        if self.n == 0:
            col = [m.n for m in cells[self.i::9]]
            check = [x in col for x in self.posNum]
            self.posNum = [x for (x, v) in zip(self.posNum, check) if not v]
            #print self.posNum
            if len(self.posNum) == 1: self.n = self.posNum[0]
            
    def checkBox(self):
        if self.n == 0:
            iBox = floor(self.i/3)
            jBox = floor(self.j/3)
            Box = []
            for i in range(3):
                Box.extend(cells[(jBox*3 + i)*9 + iBox*3:(jBox*3 + i)*9 + iBox*3 + 3])
            Box = [m.n for m in Box]
            check = [x in Box for x in self.posNum]
            self.posNum = [x for (x, v) in zip(self.posNum, check) if not v]
            #print self.posNum
            if len(self.posNum) == 1: self.n = self.posNum[0]
            
        
############################### Functions #################################

def dispMatrix(M):
    if type(M[0]) == type(0):
        for i in range(9):
            row = []
            for j in range(3):
                row.append(M[i*9 + 3*j])
                row.append(M[i*9 + 3*j + 1])
                row.append(M[i*9 + 3*j + 2])
                row.append('|')
            row = row[:-1]
            print row
            if i == 2 or i == 5:
                print ['---------|-------------|---------']
                
    if type(M[0]) == type(cell()):
        for i in range(9):
            row = []
            for j in range(3):
                row.append(M[i*9 + 3*j].n)
                row.append(M[i*9 + 3*j + 1].n)
                row.append(M[i*9 + 3*j + 2].n)
                row.append('|')
            row = row[:-1]
            print row
            if i == 2 or i == 5:
                print ['---------|-------------|---------']
                