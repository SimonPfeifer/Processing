width = 400
height = 400

particleRate = 2
deathRate = 1
gravity = PVector(0, -0.02)
wind = PVector(0.02, 0)
mouseWind= 5
velocityOffset = 1

class particleSystem(object):
    position=None
    def __init__(self, position=None):
        self.system = []
        self.position = position
    
    def applyForce(self, force):
        for p in self.system:
            p.applyForce(force)
            
    def applyMouseWind(self):
        for p in self.system:
            p.applyMouseWind()
    
    def update(self):
        for i in range(particleRate):
            self.system.append(particle(PVector(self.position.x,self.position.y)))
        self.system[:] = [p for p in self.system if p.dead == False]
        
    def display(self):
        for p in self.system:
            p.update()
            p.display()
            

class particle(object):
    def __init__(self, position=None):
        if position != None:
            self.position = position
        else:
            self.position = PVector(width/2,height/1.5)    
        self.velocity = PVector(random(-velocityOffset,velocityOffset), random(0,2*velocityOffset))
        self.acceleration = PVector(0, 0)
        self.life = 255
        self.dead = False
    
    def applyForce(self, force):        
        self.acceleration += force
        self.velocity += self.acceleration
        
    def applyMouseWind(self):
        self.force = self.position - PVector(mouseX, -mouseY+height)
        self.force = mouseWind*self.force/sq(self.force.mag())
        self.acceleration += self.force
        self.velocity += self.acceleration
        
    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration = PVector(0, 0)
        self.life -= deathRate
        if self.life <= 0:
            self.dead = True            
        
    def display(self):
        stroke(0, self.life)
        fill(125, self.life)
        ellipse(self.position.x, self.position.y, 10, 10)        
        

a = particleSystem(PVector(width/2, height/1.2))
                
def setup():
    size(height, width)

    
def draw():
    background(255)
    translate(0,height)
    scale(1, -1)
    #ellipse(width/2, height/2, 3, 3)
    a.applyForce(gravity)
    if mousePressed:
        a.applyMouseWind()
    a.update()
    a.display()