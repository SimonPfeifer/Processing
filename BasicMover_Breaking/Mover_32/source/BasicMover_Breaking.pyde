class mover(object):

    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector(random(2, 5), random(2,5))
        self.acc = PVector(0, 0)
        self.steering = PVector(0, 0)
        self.nimble = random(1)
        self.angle = 0

        self.maxspeed = map(self.nimble, 0, 1, 2, 4)
        self.maxforce = map(self.nimble, 0, 1, 0.01, 0.2)
        self.target = self.pos

    def applyForce(self, force):
        self.acc += force

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

        stroke(200)
        fill(50, 50)
        if abs(self.vel.x) > self.maxforce or abs(self.vel.y) > self.maxforce:
            self.angle = self.vel.heading()
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        rotate(self.angle)
        triangle(-15, -5, -15, 5, 0, 0)
        #strokeWeight(2)
        #line(0, 0, 10*abs(self.vel.mag()), 0)
        popMatrix()

    def seek(self, target=PVector(0, 0)):
        if target == PVector(0, 0):
            self.target = self.pos
        else:
            self.target = target
        self.breakDistance = 0.5 * (self.vel.mag() + stopRadius * self.maxforce) ** 2 / self.maxforce
        self.desire = PVector.sub(self.target, self.pos)
        if self.breakDistance > self.desire.mag():
            self.temp = PVector(self.vel.x, self.vel.y)
            self.breaking = self.temp.setMag(-self.maxforce)
            self.applyForce(self.breaking)
        else:
            self.desire.setMag(self.maxspeed)
            self.steering = PVector.sub(self.desire, self.vel)
            self.steering.limit(self.maxforce)
            self.applyForce(self.steering)


height = 400
width = 400

n = 20
group = []
gravity = PVector(0, 0.05)
target = PVector(height / 2, width / 2)
stopRadius = 5


def setup():
    size(height, width)
    for i in range(n):
        group.append(mover(0, 0))

def draw():
    global mouse
    background(255)
    #frameRate(10)
    mouse = PVector(mouseX, mouseY)
    ellipse(target.x, target.y, 5, 5)
    # if mousePressed:
    #    group.append(mover(mouseX, mouseY))
    for m in group:
        #m.seek(target)
        m.seek(mouse)
        m.update()