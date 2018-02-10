width = 400
height = 400
vOffset = 1
deathRate = 2

class particleSystem(object):
    def __init__(self):
        self.system = []
    
    def update(self):
        self.system.append(particle())
        self.system[:] = [p for p in self.system if p.dead == False]
        
    def display(self):
        for p in self.system:
            p.update()
            p.display()
            

class particle(object):
    def __init__(self):
        self.position = PVector(width/2,height/1.5)
        self.velocity = PVector(random(-vOffset,vOffset), random(0,2*vOffset))
        self.acceleration = PVector(0, -0.05)
        self.life = 255
        self.dead = False
    
    
    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.life -= deathRate
        if self.life <= 0:
            self.dead = True            
        
    def display(self):
        stroke(0, self.life)
        fill(125, self.life)
        ellipse(self.position.x, self.position.y, 10, 10)        
        

b = particleSystem()
        
def setup():
    size(height, width)

    
def draw():
    background(255)
    translate(0,height)
    scale(1, -1)
    #ellipse(width/2, height/2, 3, 3)
    b.update()
    b.display()
    