#########################################################################

class cell(object):

    def __init__(self, x, y, c=None, a=None):
        self.x = x * w
        self.y = y * w
        if c == None:
            self.c = color(50, 50, 50)
        if a == None:
            self.a = 255

    def changeColor(self, c=None, a=None):
        if c == None:
            self.c = color(50, 50, 50)
        else:
            self.c = c
        if a == None:
            self.a = 255
        else:
            self.a = a

    def display(self):
        # stroke(150)
        noStroke()
        fill(self.c, self.a)
        rect(self.x, self.y, w, w)

##########################################################################

class ant(object):

    def __init__(self, path=None, c=None):
        self.x = floor(col / 2)
        self.y = row - 1
        if c == None:
            self.c = color(random(55, 255), random(55, 255), random(55, 255))
        else:
            self.c = c
        self.a = 255
        if path == None:
            self.path = []
            for i in range(pathLength):
                self.path.append(int(random(4)))
        else:
            self.path = path
        self.score = 0

    def display(self, a=None):
        if a != None:
            self.a = a
        grid[self.x + self.y * col].changeColor(self.c, self.a)

    def move(self):
        if counter < pathLength - 1:
            if self.x == target()[0] and self.y == target()[1]:
                self.score *= 3 * (pathLength - counter)
                self.c = color(255, 255, 255)
            else:
                if self.path[counter] == 0 and 0 < self.y:
                    self.y += -1
                if self.path[counter] == 2 and self.y < row - 1:
                    self.y += 1
                if self.path[counter] == 1 and self.x < col - 1:
                    self.x += 1
                if self.path[counter] == 3 and self.x > 0:
                    self.x += -1

    def fitness(self):
        self.score = (1 / (sqrt((self.x - target()[0]) ** 2 + 2 * (self.y - target()[1]) ** 2) + 1))
        return self.score

##########################################################################

class population(object):

    def __init__(self):
        self.group = []

    def addAnt(self, path=None):
        if path == None:
            self.group.append(ant())
        else:
            self.group.append(ant(path))

    def update(self):
        for ant in self.group:
            ant.display(a=100)
            ant.move()
            ant.display(a=255)

    def crossfeed(self, A, B):
        self.newc = (A.c + B.c) / 2
        self.i = floor(random(pathLength))
        self.newpath = A.path[:self.i]
        self.newpath.extend(B.path[self.i:])
        if random(1) < mutationChance:
            for n in range(pathLength / 10):
                self.i = floor(random(pathLength))
                self.newpath[self.i] = floor(random(4))

        return [self.newpath, self.newc]

    def evaluate(self):
        self.maxscore = 0
        self.genepool = []
        self.newgroup = []
        for a in self.group:
            if a.fitness() > self.maxscore:
                self.maxscore = a.fitness()
        for a in self.group:
            a.score = a.score / self.maxscore * 100
        for a in self.group:
            for i in range(floor(a.score)):
                self.genepool.append(a)
        for i in range(popNumber):
            self.newparams = self.crossfeed(self.genepool[floor(
                random(len(self.genepool)))], self.genepool[floor(random(len(self.genepool)))])
            self.newgroup.append(
                ant(path=self.newparams[0], c=self.newparams[1]))
        self.group = self.newgroup

##########################################################################

def target():
    x = floor(col / 2)
    y = floor(row / 10)
    h = 3 * w
    '''
    grid[ x + y * col].changeColor(c=color(255, 0, 0))
    grid[ (x+1) + y * col].changeColor(c=color(255, 255, 255))
    grid[ (x-1) + y * col].changeColor(c=color(255, 255, 255))
    grid[ x + (y+1) * col].changeColor(c=color(255, 255, 255))
    grid[ x + (y-1) * col].changeColor(c=color(255, 255, 255))
    grid[ (x+1) + (y-1) * col].changeColor(c=color(255, 255, 255))
    grid[ (x-1) + (y-1) * col].changeColor(c=color(255, 255, 255))
    grid[ (x+1) + (y+1) * col].changeColor(c=color(255, 255, 255))
    grid[ (x-1) + (y+1) * col].changeColor(c=color(255, 255, 255))
    '''
    noStroke()
    fill(255)
    rect((x - 1) * w, (y - 1) * w, h, h)
    fill(color(255, 0, 0))
    rect(x * w, y * w, 1 * w, 1 * w)
    return [x, y]

def obstacle():
    x = floor(col * 0.25)
    y = floor(row * 0.5)
    wid = floor(col * 0.5)
    hei = floor(row * 0.1)
    noStroke()
    fill(225, 100)
    rect(x * w, y * w, wid * w, hei * w)
    return [x, y, wid, hei]

##########################################################################

w = 5
width = 400 + w
height = 400
col = floor(width / w)
row = floor(height / w)
generation = 0
pathLength = 300
popNumber = 30
mutationChance = 0.1
counter = 0

grid = []
p = population()

def setup():
    size(width + 1, height + 1)
    # frameRate(25)
    for i in range(row):
        for j in range(col):
            grid.append(cell(j, i))
    for i in range(popNumber - 1):
        p.addAnt()

def draw():
    global counter
    global generation
    background(0)
    p.update()
    for cell in grid:
        cell.display()
    target()
    #obstacle()
    fill(255)
    text(generation, 15, 20)
    counter += 1
    if counter == pathLength:
        p.evaluate()
        counter = 0
        generation += 1
        for cell in grid:
            cell.changeColor()
        print 'GENERATION:', generation