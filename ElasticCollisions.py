import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

input("USE SI UNITS FOR ALL INPUTS")
# Simulation Parameters
BOX_SIZE = float(input("Enter the size of the box: "))
N = int(input("Enter the number of particles: "))
MASS = float(input("Enter the mass of each particle: "))
RADIUS = float(input("Enter the radius of each particle: "))
dt = 0.01
np.random.seed(1)
positions = np.random.uniform(
    RADIUS,
    BOX_SIZE - RADIUS,
    (N, 2)
)

velocities = np.random.uniform(-50, 50, (N, 2))

# Wall Collisions
def wall_collision():

    for i in range(N):

        # Left / Right walls
        if positions[i, 0] <= RADIUS or positions[i, 0] >= BOX_SIZE - RADIUS:
            velocities[i, 0] *= -1

        # Top / Bottom walls
        if positions[i, 1] <= RADIUS or positions[i, 1] >= BOX_SIZE - RADIUS:
            velocities[i, 1] *= -1


# Disc-Disc Collisions
def disc_collision():

    for i in range(N):
        for j in range(i + 1, N):

            r = positions[i] - positions[j]
            dist = np.linalg.norm(r)

            if dist < 2 * RADIUS:

                # Unit normal vector
                n = r / dist

                # Relative velocity
                v_rel = velocities[i] - velocities[j]

                # Velocity along normal
                v_n = np.dot(v_rel, n)

                # Only collide if moving toward each other
                if v_n < 0:

                    # Elastic collision (equal masses)
                    impulse = -2 * v_n / (1 / MASS + 1 / MASS)

                    velocities[i] += (impulse / MASS) * n
                    velocities[j] -= (impulse / MASS) * n


# Update Function
def update(frame):

    global positions

    # Move discs
    positions += velocities * dt

    # Handle collisions
    wall_collision()
    disc_collision()

    # Update plot
    scatter.set_offsets(positions)

    return scatter,


# Plot Setup
fig, ax = plt.subplots()
ax.set_xlim(0, BOX_SIZE)
ax.set_ylim(0, BOX_SIZE)
ax.set_aspect("equal")

ax.set_title("Elastic Collisions: Discs in a Box")

scatter = ax.scatter(
    positions[:, 0],
    positions[:, 1],
    s=(RADIUS * 4000),
    color="blue"
)

# Animation
anim = FuncAnimation(fig, update, frames=1000, interval=20, blit=True)
plt.show()
