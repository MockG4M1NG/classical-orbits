import math as m
import numpy as np
import numpy.linalg as npl
from typing import TypeAlias
from Trajectory_Algorithms import c_orbit

Vector: TypeAlias = list[float]


def c_jacobi(r: Vector, v: Vector, t: float):
    d1, d2 = c_orbit(r, t)
    return npl.norm(v) ** 2 - 1 / (npl.norm(d1)) - 1 / (npl.norm(d2)) - 2 * np.cross(r, v)
