from vpython import *
L1 = 1
L2 = 1
g = 9.81
t = 0
dt = 0.0001
theta1 = 90*pi/180
theta2 = 0*pi/180
dtheta1 = 0
dtheta2 = 0
ddtheta1 = 0
ddtheta2 = 0

top = sphere(pos = vector(0,L1/2,0), radius = 0.01)
ball = sphere(pos = top.pos + vector(L1*sin(theta1),-L1*cos(theta1),0), radius = 0.05, make_trail=True, trail_color = color.white)
ball2 = sphere(pos = ball.pos + vector(L2*sin(theta2),-L2*cos(theta2),0), radius = 0.05, make_trail = True, trail_color = color.cyan)
string = cylinder(pos = top.pos, axis = ball.pos - top.pos, radius = 0.01)
string2 = cylinder(pos = ball.pos, axis = ball2.pos - ball.pos, radius = 0.01)

while True:
    rate(10000)
    ddtheta1 = -(9*g*sin(theta1)+3*L1*sin(theta1-theta2)*dtheta2**2+3*L1*cos(theta1-theta2)*ddtheta2)/(8*L1)
    dtheta1 = dtheta1 + ddtheta1*dt
    theta1 = theta1 + dtheta1*dt
    ddtheta2 = (-3*g*sin(theta2)+3*L2*sin(theta1-theta2)*dtheta1**2-3*L2*cos(theta1-theta2)*ddtheta1)/(2*L2)
    dtheta2 = dtheta2 + ddtheta2*dt
    theta2 = theta2 + dtheta2*dt
    t = t + dt
    ball.pos = top.pos + vector(L1*sin(theta1),-L1*cos(theta1),0)
    ball2.pos = ball.pos + vector(L2*sin(theta2),-L2*cos(theta2),0)
    string.axis = ball.pos - top.pos
    string2.pos = ball.pos
    string2.axis = ball2.pos - ball.pos

