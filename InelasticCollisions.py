import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

print("USE SI UNITS FOR ALL INPUTS")
# Parameters
BOX_SIZE = float(input("Enter the size of the box: "))
dt = 0.05
RADIUS = float(input("Enter the radius of the particle: "))

# Energy loss factor (0 < e < 1)
RESTITUTION = float(input("Enter the restitution coefficient (0 < e < 1): "))


# Initial position
x = float(input("Enter the initial x-position of the particle: "))
y = float(input("Enter the initial y-position of the particle: "))

# Initial velocity
vx = float(input("Enter the initial x-component of velocity of the particle: "))
vy = float(input("Enter the initial y-component of velocity of the particle: "))

# Setup plot
fig, ax = plt.subplots()

ax.set_xlim(0, BOX_SIZE)
ax.set_ylim(0, BOX_SIZE)
ax.set_aspect("equal")

ax.set_title("Inelastic Particle in a Box")

# Box
ax.plot(
    [0, BOX_SIZE, BOX_SIZE, 0, 0],
    [0, 0, BOX_SIZE, BOX_SIZE, 0],
    "k"
)

# Particle
particle = plt.Circle((x, y), RADIUS, color="blue")
ax.add_patch(particle)


# Animation update
def update(frame):
    global x, y, vx, vy

    # Move
    x += vx * dt
    y += vy * dt

    # Left / Right wall
    if x - RADIUS <= 0:
        x = RADIUS
        vx = -vx * RESTITUTION

    if x + RADIUS >= BOX_SIZE:
        x = BOX_SIZE - RADIUS
        vx = -vx * RESTITUTION

    # Bottom / Top wall
    if y - RADIUS <= 0:
        y = RADIUS
        vy = -vy * RESTITUTION

    if y + RADIUS >= BOX_SIZE:
        y = BOX_SIZE - RADIUS
        vy = -vy * RESTITUTION

    particle.center = (x, y)

    return particle,


# Animate
anim = FuncAnimation(fig, update, frames=1000, interval=30, blit=True)

plt.show()
