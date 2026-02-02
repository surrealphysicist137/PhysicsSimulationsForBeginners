import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
print("USE SI UNITS FOR ALL INPUTS")
L = int(input("Enter the length of the rod: "))
alpha = float(input("Enter the thermal diffusivity: "))
T_left = float(input("Enter the left boundary temperature: "))
T_right = float(input("Enter the right boundary temperature: "))
T_0 = float(input("Enter the initial temperature throughout the rod: "))

Nx = 1000  # Number of spatial points
dx = L / (Nx - 1)
dt = 0.1 * dx**2 / alpha   

#Stability check
if dt > 0.5 * dx**2 / alpha:
    print("Warning: The entered value of thermal diffusivity may lead to instability in the simulation.")

# Arrays
x = np.linspace(0, L, Nx)
T = np.zeros(Nx)
T[:] = T_0

# Boundary conditions
T[0] = T_left
T[-1] = T_right

# Figure setup
fig, ax = plt.subplots()
line, = ax.plot(x, T, lw=2)
ax.set_xlim(0, L)
ax.set_ylim(0, max(T_left, T_right, T_0) + 10)
ax.set_xlabel("Position (m)")
ax.set_ylabel("Temperature (K)")
ax.set_title("Heat Flow in a Rod")
time_text = ax.text(0.02, 0.9, '', transform=ax.transAxes)

# Update function
def update(frame):
    global T
    T_new = T.copy()

    # Finite difference method
    for i in range(1, Nx - 1):
        T_new[i] = T[i] + alpha * dt / dx**2 * ( T[i+1] - 2*T[i] + T[i-1] )

    # Apply boundary conditions
    T_new[0] = T_left
    T_new[-1] = T_right

    T = T_new

    line.set_ydata(T)
    time_text.set_text(f"Time = {frame*dt:.2f} s")

    return line, time_text


# Animation
ani = FuncAnimation(fig, update, frames=500, interval=50, blit=False)
plt.show()
