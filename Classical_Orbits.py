import math as m
from typing import TypeAlias
from Trajectory_Algorithms import position_verlet, forest_ruth, r_pos
from Trajectory_Analyses import c_jacobi

# Defines test parameters
Vector: TypeAlias = list[float]

runtime: float
res: float
time: float
jac0: float
pos: Vector
vel: Vector
plot: Vector

# SCENARIO 1a: Choose binary stars to be stationary for all time (initial velocity 1)
# Algorithm: Position-Verlet
runtime = 20 * m.pi
res = 0.00005
time = 0
pos = [0.0, 0.0]
vel = [m.cos(m.radians(45)), m.sin(m.radians(45))]

f = open("Scenario1.txt", "w")
f.write(f'{pos[0]} {pos[1]}\n')
while time < runtime:
    pos, vel, time = position_verlet(pos, vel, time, res, True)
    f.write(f'{pos[0]} {pos[1]}\n')
f.write(f'\n\n')
print("Scenario 1a Complete")

# SCENARIO 1b: Choose binary stars to be stationary for all time (initial velocity 2)
time = 0
pos = [0.0, 0.0]
vel = [m.cos(m.radians(60))/2, m.sin(m.radians(60))/2]

f.write(f'{pos[0]} {pos[1]}\n')
while time < runtime:
    pos, vel, time = position_verlet(pos, vel, time, res, True)
    f.write(f'{pos[0]} {pos[1]}\n')
f.write(f'\n\n')
print("Scenario 1b Complete")

# SCENARIO 1c: Choose binary stars to be stationary for all time (initial velocity 3)
time = 0
pos = [0.0, 0.0]
vel = [4/3*m.cos(m.radians(75)), 4/3*m.sin(m.radians(75))]

f.write(f'{pos[0]} {pos[1]}\n')
while time < runtime:
    pos, vel, time = position_verlet(pos, vel, time, res, True)
    f.write(f'{pos[0]} {pos[1]}\n')
f.close()

print("Scenario 1c Complete")
# SCENARIO 2a: Choose binary stars to circle the origin (w/ Jacobi constant error comparison)
# Algorithm: Position-Verlet
runtime = 3 * m.pi
res = 0.005
time = 0
pos = [0.0, 0.058]
vel = [0.49, 0]
jac0 = c_jacobi(pos, vel, 0)

f = open("Scenario2.txt", "w")
f1 = open("Scenario2Error.txt", "w")
f.write(f'{pos[0]} {pos[1]}\n')
f1.write(f'{0} {0}')

while time < runtime:
    pos, vel, time = position_verlet(pos, vel, time, res)
    f.write(f'{pos[0]} {pos[1]}\n')
    f1.write(f'{time} {c_jacobi(pos, vel, time) - jac0}\n')
f.write(f'\n\n')
f1.write(f'\n\n')
print("Scenario 2a Complete")

# SCENARIO 2b
# Algorithm: Forest-Ruth
time = 0
pos = [0.0, 0.058]
vel = [0.49, 0]
jac0 = c_jacobi(pos, vel, 0)

f.write(f'{pos[0]} {pos[1]}\n')
f1.write(f'{0} {0}')

while time < runtime:
    pos, vel, time = forest_ruth(pos, vel, time, res)
    f.write(f'{pos[0]} {pos[1]}\n')
    f1.write(f'{time} {c_jacobi(pos, vel, time) - jac0}\n')
f.close()
f1.close()
print("Scenario 2b Complete")

# SCENARIO 3a: Choose binary stars to circle the origin and rotate coordinate system with stars (set one)
# Algorithm: Forest-Ruth
time = 0
pos = [0.0, 0.058]
vel = [0.49, 0]

f = open("Scenario3.txt", "w")
f.write(f'{pos[0]} {pos[1]}\n')
while time < runtime:
    pos, vel, time = forest_ruth(pos, vel, time, res)
    plot = r_pos(pos, time)
    f.write(f'{plot[0]} {plot[1]}\n')
f.write(f'\n\n')
print("Scenario 3a Complete")

# SCENARIO 3b: Choose binary stars to circle the origin and rotate coordinate system with stars (set two)
time = 0
pos = [0.03, -0.054]
vel = [0.01, 0.15]

f.write(f'{pos[0]} {pos[1]}\n')
while time < runtime:
    pos, vel, time = forest_ruth(pos, vel, time, res)
    plot = r_pos(pos, time)
    f.write(f'{plot[0]} {plot[1]}\n')
f.close()
print("Scenario 3b Complete")

