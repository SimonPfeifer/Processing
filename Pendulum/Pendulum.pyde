height = 300
width = 300

r = 100
g = 100
h = 0.001
theta_start = 45 
X=[theta_start * PI/180, 0.0]  

def setup():
    size(height, width)

def draw():
    global X
    frameRate(2/h)
    translate(width/2, height/2)
    background(50)
    ellipse(0,0,5,5)
    
    X_new = RK(X, h)
    X = X_new
    display(X)
    
########################### Functions ####################################
    
    
def f(X):
    theta = X[1]
    theta_dot = -g/(r) * sin(X[0])

    return [theta, theta_dot]


def RK(X, h):
    k1 = [h*a for a in f(X)]
    k1 = [a/2 for a in k1]
    k2 = [h*a for a in f([b + c for b,c in zip(X, k1)])]
    k2 = [a/2 for a in k2]
    k3 = [h*a for a in f([b + c for b,c in zip(X, k2)])]
    k4 = [h*a for a in f([b + c for b,c in zip(X, k3)])]
    
    k1 = [a/3 for a in k1]
    k2 = [a * 2/3 for a in k2]
    k3 = [a * 2/3 for a in k3]
    k4 = [a/3 for a in k4]
    
    return [sum(i) for i in zip(X,k1,k2,k3,k4)]


def display(X):
    x = r * sin(X[0])
    y = r * cos(X[0])
    ellipse(x, y, 10, 10)
    line(0,0, x, y)