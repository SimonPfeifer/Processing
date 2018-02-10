height = 500
width = 500


n = 2    # set to '1' for single pendulum and '2' for double pendulum


G = 100
h = 0.01   # time-step 
r1 = 100
r2 = 100
m1 = 1.5
m2 = 1
theta_start1 = 45    # starting angle of pendulum 1 in degrees
theta_start2 = 180   # starting angle of pendulum 2 in degrees



trail_segments = 50
trail_resolution = 20
X1_old = []
X2_old = []
counter = 0

def setup():
    global X1
    global X2
    size(height, width)
    X1=[theta_start1 * PI/180, 0.0]
    X2=[theta_start1 * PI/180, 0.0, theta_start2 * PI/180, 0.0]
    for i in range(trail_segments):
        X1_old.append(X1)
        X2_old.append(X2)


def draw():
    global X1
    global X2
    global n
    global counter
    frameRate(2/h)
    translate(width/2, height/2 - height/10)
    background(40)
    stroke(255,255,255)
    ellipse(0,0,2,2)
    
    if n == 1:
        X1 = RK(X1, h)
        display(X1)
        
    else:
        X2 = RK(X2, h)
        for i in range(trail_segments-1):
            drawLine(X2_old[i], X2_old[i+1])
        drawLine(X2, X2_old[-1])
        display(X2)
        
        if counter == ceil(1000.0/trail_resolution * (0.001/h)):
            X2_old[:-1] = X2_old[1:]
            X2_old[-1] = X2
            counter = 0
        counter += 1
        
                
        
########################### Functions ####################################
    
    
def f(X):
    if len(X) == 2:
        a = X[1]
        b = -(G/r1) * sin(X[0])
        
        return [a, b]
    
    else:
        a1 = X[0]
        b1 = X[1]
        a2 = X[2]
        b2 = X[3]
        
        A1 = -G*(2*m1+m2)*sin(a1) - m2*G*sin(a1-2*a2) - 2*sin(a1-a2)*m2*((b2**2)*r2 + (b1**2)*r1*cos(a1-a2))
        B1 = r1*(2*m1 + m2 - m2*cos(2*a1-2*a2))        
        C1 = A1/B1
        
        A2 = 2*sin(a1-a2)*((b1**2)*r1*(m1+m2) + G*(m1+m2)*cos(a1) + (b2**2)*r2*m2*cos(a1-a2))
        B2 = r2*(2*m1 + m2 - m2*cos(2*a1-2*a2))
        C2 = A2/B2
        
        return [b1, C1, b2, C2]


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
    x1 = r1 * sin(X[0])
    y1 = r1 * cos(X[0])
    stroke(255,255,255, 100)
    ellipse(x1, y1, 10*m1, 10*m1)
    line(0,0, x1, y1)
    
    if len(X) == 4:
        x2 = r2 * sin(X[2]) + x1
        y2 = r2 * cos(X[2]) + y1
        stroke(255,255,255, 100)
        ellipse(x2, y2, 10*m2, 10*m2)
        line(x1,y1, x2, y2)
  
              
def drawLine(X, Y):
    x0 = r1 * sin(X[0])
    y0 = r1 * cos(X[0])
    x1 = r1 * sin(Y[0])
    y1 = r1 * cos(Y[0])
    stroke(200,50,50)
    #line(x0, y0, x1, y1)
    
    if len(X) == 4:
        stroke(100,200,100)
        line(r2 * sin(X[2]) + x0, r2 * cos(X[2]) + y0, r2 * sin(Y[2]) + x1, r2 * cos(Y[2]) + y1)
        