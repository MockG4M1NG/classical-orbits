import math as m
from typing import TypeAlias
from Trajectory_Algorithms import position_verlet, forest_ruth, r_pos

# Defines test parameters
Vector: TypeAlias = list[float]

runtime: float
res: float
time: float
pos: Vector
vel: Vector
plot: Vector

# SCENARIO 1: Choose binary stars to be stationary for all time
# Algorithm: Position-Verlet
runtime = 9 * m.pi
res = 0.005
time = 0
pos = [0.0, 0.0]
vel = [1 / m.sqrt(2), 1 / m.sqrt(2)]

f = open("Scenario1.txt", "w")
f.write(f'{pos[0]} {pos[1]}\n')
while time < runtime:
    pos, vel, time = position_verlet(pos, vel, time, res, True)
    plot = r_pos(pos, time)
    f.write(f'{plot[0]} {plot[1]}\n')

# SCENARIO 2: Choose binary stars to circle the origin
# Algorithm: (a) Position-Verlet
time = 0
pos = [0.0, 0.0]
vel = [0.0, 0.0]

f = open("Scenario2a.txt", "w")
f.write(f'{pos[0]} {pos[1]}\n')
while time < runtime:
    pos, vel, time = position_verlet(pos, vel, time, res)
    f.write(f'{pos[0]} {pos[1]}\n')

# Algorithm: (b) Forest-Ruth
time = 0
pos = [0.0, 0.0]
vel = [0.0, 0.0]

f = open("Scenario2b.txt", "w")
f.write(f'{pos[0]} {pos[1]}\n')
while time < runtime:
    pos, vel, time = position_verlet(pos, vel, time, res)
    f.write(f'{pos[0]} {pos[1]}\n')

# SCENARIO 3: Choose binary stars to circle the origin and rotate coordinate system with stars
# Algorithm: Forest-Ruth
time = 0
pos = [0.0, 0.0]
vel = [0.0, 0.0]

f = open("Scenario3.txt", "w")
f.write(f'{pos[0]} {pos[1]}\n')
while time < runtime:
    pos, vel, time = forest_ruth(pos, vel, time, res)
    plot = r_pos(pos, time)
    f.write(f'{plot[0]} {plot[1]}\n')
