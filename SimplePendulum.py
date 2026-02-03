import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 
print("USE SI UNITS ONLY FOR ALL INPUTS")
# Parameters
length = float(input("Enter the effective length of pendulum: "))
g = 9.81
omega = np.sqrt(g/length)
dt = 0.01
steps = int(input("Enter the number of time steps: "))

# Arrays
x = np.zeros(steps)
v = np.zeros(steps)
t = np.linspace(0, dt * (steps - 1), steps)
assert len(t) == len(x)



# Initial conditions
x[0] = float(input("Enter the initial angular position: "))
v[0] = float(input("Enter the initial angular velocity: "))

#Verlet Integration
for i in range(steps - 1):
    a = - (g / length) * np.sin(x[i])
    x[i + 1] = x[i] + v[i] * dt + 0.5 * a * dt**2
    a_next = - (g / length) * np.sin(x[i + 1])
    v[i + 1] = v[i] + 0.5 * (a + a_next) * dt

# Plot setup
r = length
fig, ax = plt.subplots()
ax.set_xlim(-1.5*r, 1.5*r)
ax.set_ylim(-1.5*r, 1.5*r)
ax.set_title("Simple Pendulum Animation")

x_pos = r * np.sin(x)
y_pos = -r * np.cos(x)

#penulum drawing   
pendulum, = ax.plot([], [], lw = 2, ms=12)  

# Initialization
def init():
    pendulum.set_data([], [])
    return pendulum,

#Update function
def update(frame):
    pendulum.set_data([0, x_pos[frame]], [0, y_pos[frame]])
    return pendulum, 

# Animation,
ani = FuncAnimation(fig, update, frames=steps, interval=30, blit=True, init_func=init)
plt.show()

#Plot of position vs time graph
plt.figure()
plt.plot(t, x)
plt.xlabel("Time (s)")
plt.ylabel("Angular Position (radians)")
plt.title("Angular Position vs Time Graph for Simple Pendulum")
plt.show()

