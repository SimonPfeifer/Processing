width = 400
height = 400

class particle(object):
    def __init__(self):
        self.position = PVector(width/2, height)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, -0.05)
    
    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        if self.position.y <= 0:
            self.position.y = height
        
    def display(self):
        stroke(0, 100)
        fill(125)
        ellipse(self.position.x, self.position.y, 20, 20)        
        
p = particle()    
        
def setup():
    size(height, width)
    
def draw():
    background(255)
    translate(0,height)
    scale(1, -1)
    #ellipse(width/2, height/2, 3, 3)
    p.update()
    p.display()