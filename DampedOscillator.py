import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
print("USE SI UNITS ONLY FOR ALL INPUTS")
# Damped Oscillator's Differential Equation of Motion: d^2x/dt^2 + gamma*dx/dt + omega^2*x = 0
# Parameters
omega = float(input("Enter the angular frequency: "))
gamma = float(input("Enter the damping coefficient: "))
dt = 0.01
steps = int(input("Enter the number of time steps: "))*100

# Arrays
x = np.zeros(steps)
v = np.zeros(steps)
t = np.linspace(0, dt * (steps - 1), steps)
assert len(t) == len(x)



# Initial conditions
x[0] = float(input("Enter the initial position: "))
v[0] = float(input("Enter the initial velocity: "))

# Euler's Method
for i in range(steps - 1):
    v[i + 1] = v[i] - (omega**2 * x[i] + gamma * v[i]) * dt
    x[i + 1] = x[i] + v[i + 1] * dt

# Plot setup
r = v[0]
fig, ax = plt.subplots()
ax.set_xlim(-1.4*r, 1.4*r)
ax.set_ylim(-1.4*r, 1.4*r)
ax.set_title("Damped Oscillator Animation")
ax.axvline(0, linestyle="--", alpha=0.5)


block, = ax.plot([], [], 's', markersize=20)

def update(frame):
    block.set_data([x[frame]], [0])
    return block,

# Animation
ani = FuncAnimation(fig, update, frames=steps, interval=30, blit=True)
plt.show()

#Plot of position vs time graph
import matplotlib.pyplot as pt
pt.figure()
pt.plot(t, x)
pt.xlabel("Time (s)")
pt.ylabel("Position (m)")
pt.title("Position vs Time Graph for Damped Oscillator")
pt.show()
