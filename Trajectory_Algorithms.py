import math as m
import numpy as np
import numpy.linalg as npl
from typing import TypeAlias

Vector: TypeAlias = list[float]


def c_orbit(r: Vector, t: float, fixed: bool = False) -> tuple[Vector, Vector]:
    if fixed:
        return np.subtract(r, [0.5, 0.0]), np.subtract(r, [0.5, 0.0])
    return np.subtract(r, [0.5 * m.cos(t), 0.5 * m.sin(t)]), np.add(r, [0.5 * m.cos(t), 0.5 * m.sin(t)])


def c_accel(r: Vector, t: float, fixed: bool = False) -> Vector:
    d1, d2 = c_orbit(r, t, fixed)
    return np.add(np.divide(d1, -2 * npl.norm(d1) ** 3), np.divide(d2, -2 * npl.norm(d2) ** 3))


def u_pos(r: Vector, v: Vector, t: float, t_step: float) -> tuple[Vector, float]:
    return np.add(r, np.multiply(v, t_step)), t + t_step


def u_vel(r: Vector, v: Vector, t: float, t_step: float, fixed: bool = False) -> tuple[Vector, float]:
    return np.add(v, np.multiply(c_accel(r, t, fixed), t_step)), t + t_step


def r_pos(r: Vector, t: float) -> Vector:
    x = r[0] * m.cos(t) + r[1] * m.sin(t)
    y = r[0] * -m.sin(t) + r[1] * m.cos(t)
    return [x, y]


def position_verlet(r0: Vector, v0: Vector, t: float, t_step: float, fixed: bool = False) -> tuple[
  Vector, Vector, float]:
    r1, t = u_pos(r0, v0, t, t_step / 2)
    v1, t = u_vel(r1, v0, t, t_step, fixed)
    r2, t = u_pos(r1, v1, t, t_step / 2)
    return r2, v1, t


def forest_ruth(r0: Vector, v0: Vector, t: float, t_step: float, fixed: bool = False) -> tuple[
  Vector, Vector, float]:
    s = 2**(1/3)
    t_step /= (2 - s)
    r1, v1, t = position_verlet(r0, v0, t, t_step, fixed)
    r2, v2, t = position_verlet(r1, v1, t, - s * t_step, fixed)
    r3, v3, t = position_verlet(r2, v2, t, t_step, fixed)
    return r3, v3, t
