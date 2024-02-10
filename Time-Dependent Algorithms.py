import math as m
import numpy as np
import numpy.linalg as npl
from typing import TypeAlias

# Defines test parameters
PERIOD = 20 * m.pi
TIME_STEP = 0.0005
Vector: TypeAlias = list[float]

def c_orbit(r: Vector, t: float = 0) -> tuple[Vector, Vector]:
    d1 = np.add(r, [0.5 * m.cos(t), 0.5 * m.sin(t)])
    d2 = np.subtract(r, [0.5 * m.cos(t), 0.5 * m.sin(t)])
    return d1, d2


def c_acc(r: Vector, t: float = 0) -> Vector:
    d1, d2 = c_orbit(r, t)
    return np.add(np.divide(d1, -2 * np.norm(d1) ** 3), np.divide(d2, -2 * np.norm(d2) ** 3))


def c_jacobi(r: Vector, v: Vector, t: float = 0):
    d1, d2 = c_orbit(r, t)
    return npl.norm(v) ** 2 - 1 / (npl.norm(d1)) - 1 / (npl.norm(d2)) - 2 * np.cross(r, v)


def u_pos(r: Vector, v: Vector, t: float, t_step: float) -> tuple[Vector, float]:
    return r + t_step * v, t + t_step


def u_vel(r: Vector, v: Vector, t: float, t_step: float):
    return v + t_step * c_acc(r, t)


def r_pos(time: float, pos: [float, float]):
    x = pos[0] * m.cos(time) + pos[1] * m.sin(time)
    y = pos[0] * -m.sin(time) + pos[1] * m.cos(time)
    return [x, y]


# Position-Verlet Algorithm
def pos_verlet(time: float, , v0, tStep, t):
    r1, t = updatePos(r0, v0, 0.5 * tStep, t)
    v1 = updateVel(r1, v0, tStep, t)
    r2, t = updatePos(r1, v1, 0.5 * tStep, t)
    return r2, v1, t


# Forest-Ruth Algorithm
def FR(r0, v0, tStep, t):
    s = 2 ** (1 / 3.0)
    tStep /= (2 - s)
    r1, v1, t = PV(r0, v0, tStep, t)
    r2, v2, t = PV(r1, v1, - s * tStep, t)
    return PV(r2, v2, tStep, t)


# INITIAL_POSITION = [0.05, -0.05]
# INITIAL_VELOCITY = [0.2, -0.2]
# INITIAL_JACOBAI = Jacobai(INITIAL_POSITION, INITIAL_VELOCITY, 0)
# RS = open("Rotating Stars Rotating Funky.txt", "w")
#
# r, v = INITIAL_POSITION, INITIAL_VELOCITY
# RS.write(f'{r[0]} {r[1]}\n')
# t = 0
#
# while t < PERIOD:
#     r, v, t = FR(r, v, TIME_STEP, t)
#     r = rotate(r, t)
#     RS.write(f'{r[0]} {r[1]}\n')
