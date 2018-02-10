
class pxl(object):

    def __init__(self, i, j, c=None):
        self.x = i * scl + scl / 2
        self.y = j * scl + scl / 2
        self.i = i
        self.j = j
        if c == None:
            self.c = 50
        else:
            self.c = c

    def show(self):
        strokeWeight(1)
        stroke(200)
        fill(self.c)
        rect(self.x - scl / 2, self.y - scl / 2, scl - 1, scl - 1)
        ellipse(self.x, self.y, scl / 30, scl / 30)

    def colorchange(self, c=None):
        self.c = c

def populate(order=None):
    if order == 1:
        hset = []
        for i in range(1, col, 2):
            for j in range(0, row, 2):
                hset.append(pxls[j + i * row])
                hset.append(pxls[j + (i - 1) * row])
                hset.append(pxls[j + 1 + (i - 1) * row])
                hset.append(pxls[j + 1 + i * row])
                curveset.extend(hset)
                hset = []
    if order > 1:
        template = curveset
        for i in [0, 0.5*2**order]:
            for j in [0, 0.5*2**order]:
                
                
                


def drawline(points=None):
    strokeWeight(5)
    for i in range(len(points[:-1])):
        line(points[i].x, points[i].y,
             points[i + 1].x, points[i + 1].y)

'''
def drawline(order=1):
    strokeWeight(5)
    for i in range(0, len(curveset), 4 ** order):
        segment = curveset[i:i + 4 ** order]
        for j in range(1, 4 ** order, 1):
            line(segment[j].x, segment[j].y,
                 segment[j - 1].x, segment[j - 1].y)
'''

def rotateClock(points):
    pushMatrix()
    translate(scl * 2, 0)
    rotate(PI / 2)
    drawline(points=points)
    popMatrix()

def rotateAnticlock():
    pushMatrix()
    translate(0, scl * 2)
    rotate(-PI / 2)
    drawline(points=points)
    popMatrix()


def keyTyped():
    print("pressed %s " % (key))


width = 500
height = 500
scl = 250
col = width / scl
row = height / scl
curveset = []
pxls = []
order = 1
def setup():
    size(width, height)
    for i in range(floor(width / scl)):
        for j in range(floor(height / scl)):
            pxls.append(pxl(j, i))


def draw():
    global curveset
    global order
    frameRate(1)
    background(0)
    for p in pxls:
        p.show()
    populate(order=order)

    '''
    if mousePressed:
        rotateAnticlock(curveset)
        for c in curveset:
            print c.i, c.j
            print len(curveset)
    else:
        #rotateClock(curveset)
        drawline(points=curveset)
    '''
    curveset = []