width = 400
height = 400

particleRate = 3
deathRate = 1
gravity = -0.05
velocityOffset = 1

class particleSystem(object):
    position=None
    def __init__(self, position=None):
        self.system = []
        self.position = position
    
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
        self.acceleration = PVector(0, gravity)
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
        
systems = []
particles = []
                
def setup():
    size(height, width)

    
def draw():
    background(255)
    translate(0,height)
    scale(1, -1)
    #ellipse(width/2, height/2, 3, 3)
    for s in systems:
        s.update()
        s.display()
    for p in particles:
        p.update()
        p.display()
        
    if mousePressed == True:
        #systems.append(particleSystem(PVector(mouseX, -mouseY+height)))
        for i in range(particleRate):
            particles.append(particle(PVector(mouseX, -mouseY+height)))
    particles[:] = [p for p in particles if p.dead == False]
        
    