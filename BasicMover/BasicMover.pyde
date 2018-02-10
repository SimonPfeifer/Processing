class mover(object):
    def __init__(self, x, y):
        self.pos = PVector(x,y)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        
    def applyForce(self, force):
        self.acc += force
        
    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0
        
        stroke(200)
        fill(50, 50)
        self.angle = atan(self.vel.y/(self.vel.x + 0.01))
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(self.angle)
        triangle(0, 0, 0, 10, 15, 5)
        popMatrix()

                
        
height = 400
width = 400

group = []
gravity = PVector(0,0.05)

def setup():
    size(height, width)
    

def draw():
    background(255)
    #frameRate(20)
    if mousePressed:
        group.append(mover(mouseX, mouseY))
    for m in group:
        m.applyForce(gravity)        
        m.update()
        
        
        
        

    