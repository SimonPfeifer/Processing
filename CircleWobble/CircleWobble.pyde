height = 600
width = 600
n = 500
r = 200
i = 0
j = 0
amplitude = 20
frequency = 0.08
rate = 0.05

nodes = []

def circle(r, theta):
    r = r
    theta = theta
    x = r * sin(theta)
    y = r * cos(theta)
    return [x, y]


def setup():
    size(height,width)
    #frameRate(20)
    for i in range(n):
        theta = i * TWO_PI / (n)
        nodes.append([r, theta])
    
def draw():
    global i
    global j
    i = 0
    translate(height/2, width/2)
    background(0)
    fill(255, 255, 255)
    beginShape()
    for node in nodes:
        roff = noise(i, j)
        roff = map(roff, 0, 1, -amplitude, amplitude)
        newr = node[0] + roff
        x = circle(newr, node[1])[0]
        y = circle(newr + roff, node[1])[1]
        vertex(x, y)
        #ellipse(x, y, 5, 5)
        i += frequency
    j += rate
    endShape()
