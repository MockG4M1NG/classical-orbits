import math as m
import numpy as np
import numpy.linalg as npl

# Defines test parameters
PERIOD = 20 * m.pi
TIME_STEP = 0.0005
SIN_T, COS_T = m.sin(TIME_STEP), m.cos(TIME_STEP)

def starPos(r, t):
    d1 = r + [0.5 * m.cos(t), 0.5 * m.sin(t)]
    d2 = r + [-0.5 * m.cos(t), -0.5 * m.sin(t)]
    return d1, d2

def accel(r, t):
    d1, d2 = starPos(r, t)
    return -0.5 * (d1 / npl.norm(d1) ** 3 + d2 / npl.norm(d2) ** 3)

def Jacobai(r, v, t):
    d1, d2 = starPos(r, t)
    return npl.norm(v) ** 2 - 1 / (npl.norm(d1)) - 1 / (npl.norm(d2)) - 2 * np.cross(r, v)

def updatePos(r, v, tStep, t):
    return r + np.multiply(tStep, v), t + tStep

def updateVel(r, v, tStep, t):
    return v + np.multiply(tStep, accel(r, t))

def rotate(r, t):
    x = r[0] * COS_T + r[1] * SIN_T
    y = r[0] * -SIN_T + r[1] * COS_T
    return [x, y]

# Position-Verlet Algorithm
def PV(r0, v0, tStep, t):
    r1, t = updatePos(r0, v0, 0.5 * tStep, t)
    v1 = updateVel(r1, v0, tStep, t)
    r2, t = updatePos(r1, v1, 0.5 * tStep, t)
    return r2, v1, t

# Forest-Ruth Algorithm
def FR(r0, v0, tStep, t):
    s = 2 ** (1/3.0)
    tStep /= (2 - s)
    r1, v1, t = PV(r0, v0, tStep, t)
    r2, v2, t = PV(r1, v1, - s * tStep, t)
    return PV(r2, v2, tStep, t)

INITIAL_POSITION = [0.05, -0.05]
INITIAL_VELOCITY = [0.2, -0.2]
INITIAL_JACOBAI = Jacobai(INITIAL_POSITION, INITIAL_VELOCITY, 0)
RS = open("Rotating Stars Rotating Funky.txt", "w")

r, v = INITIAL_POSITION, INITIAL_VELOCITY
RS.write(f'{r[0]} {r[1]}\n')
t = 0

while t < PERIOD:
    r, v, t = FR(r, v, TIME_STEP, t)
    r = rotate(r, t)
    RS.write(f'{r[0]} {r[1]}\n')