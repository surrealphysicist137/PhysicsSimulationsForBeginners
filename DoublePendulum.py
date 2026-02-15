import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sp

# Define symbols
t = sp.symbols('t')
g, m1, m2, l1, l2 = sp.symbols('g m1 m2 l1 l2')

theta1 = sp.Function('theta1')(t)
theta2 = sp.Function('theta2')(t)

theta1_dot = sp.diff(theta1, t)
theta2_dot = sp.diff(theta2, t)

# Positions
x1 = l1 * sp.sin(theta1)
y1 = -l1 * sp.cos(theta1)

x2 = x1 + l2 * sp.sin(theta2)
y2 = y1 - l2 * sp.cos(theta2)

# Velocities
x1_dot = sp.diff(x1, t)
y1_dot = sp.diff(y1, t)

x2_dot = sp.diff(x2, t)
y2_dot = sp.diff(y2, t)

# Kinetic Energy
T1 = (1/2) * m1 * (x1_dot**2 + y1_dot**2)
T2 = (1/2) * m2 * (x2_dot**2 + y2_dot**2)
T = T1 + T2

# Potential Energy
V1 = m1 * g * y1
V2 = m2 * g * y2
V = V1 + V2

# Lagrangian
L = T - V

# Euler-Lagrange Equations
eq1 = sp.diff(sp.diff(L, theta1_dot), t) - sp.diff(L, theta1)
eq2 = sp.diff(sp.diff(L, theta2_dot), t) - sp.diff(L, theta2)

# Solve for second derivatives
theta1_ddot = sp.diff(theta1, t, t)
theta2_ddot = sp.diff(theta2, t, t)

solutions = sp.solve([eq1, eq2], (theta1_ddot, theta2_ddot), simplify=True)

theta1_ddot_expr = solutions[theta1_ddot]
theta2_ddot_expr = solutions[theta2_ddot]

# Convert symbolic expressions to numerical functions
params = (theta1, theta2, theta1_dot, theta2_dot, m1, m2, l1, l2, g)
f_theta1_ddot = sp.lambdify(params, theta1_ddot_expr, 'numpy')
f_theta2_ddot = sp.lambdify(params, theta2_ddot_expr, 'numpy')

#Numerical Simulation

# Constants and inputs
print("USE SI UNITS FOR ALL INPUTS")
g_val = 9.81
m1_val = float(input("Enter mass of first pendulum: "))
m2_val = float(input("Enter mass of second pendulum: "))
l1_val = float(input("Enter length of first pendulum: "))
l2_val = float(input("Enter length of second pendulum: "))

# Initial conditions
theta1_val = float(input("Enter initial angular displacement for first pendulum: "))
theta2_val = float(input("Enter initial angular displacement for second pendulum: "))
theta1_dot_val = float(input("Enter initial angular velocity for first pendulum: "))
theta2_dot_val = float(input("Enter initial angular velocity for second pendulum: "))

dt = 0.01
t_max = float(input("Enter total simulation time: "))
steps = int(t_max / dt)

theta1_vals = []
theta2_vals = []

for _ in range(steps):
    theta1_vals.append(theta1_val)
    theta2_vals.append(theta2_val)
 
# RK4 integration

# Define derivative function
def derivatives(state):
    th1, th2, w1, w2 = state
    a1 = f_theta1_ddot(th1, th2, w1, w2, m1_val, m2_val, l1_val, l2_val, g_val)
    a2 = f_theta2_ddot(th1, th2, w1, w2, m1_val, m2_val, l1_val, l2_val, g_val)

    return np.array([w1, w2, a1, a2], dtype=float)


# Initial state vector
state = np.array([theta1_val, theta2_val, theta1_dot_val, theta2_dot_val], dtype=float)

theta1_vals = []
theta2_vals = []

for _ in range(steps):
    theta1_vals.append(state[0])
    theta2_vals.append(state[1])

    k1 = derivatives(state)
    k2 = derivatives(state + 0.5 * dt * k1)
    k3 = derivatives(state + 0.5 * dt * k2)
    k4 = derivatives(state + dt * k3)

    state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)


# Animation
fig, ax = plt.subplots()
ax.set_xlim(-1.5*(l1_val+l2_val), 1.5*(l1_val+l2_val))
ax.set_ylim(-1.5*(l1_val+l2_val), 1.5*(l1_val+l2_val))
ax.set_aspect('equal')

line, = ax.plot([], [], 'o-', lw=2)

def update(frame):
    theta1 = theta1_vals[frame]
    theta2 = theta2_vals[frame]

    x1 = l1_val * np.sin(theta1)
    y1 = -l1_val * np.cos(theta1)

    x2 = x1 + l2_val * np.sin(theta2)
    y2 = y1 - l2_val * np.cos(theta2)

    line.set_data([0, x1, x2], [0, y1, y2])
    return line,

ani = FuncAnimation(fig, update, frames=len(theta1_vals), interval=dt*1000, blit=True)
plt.show()

#Graphs of angular displacements
time = np.linspace(0, t_max, steps)
plt.figure()
plt.plot(time, theta1_vals)
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement (rad)')
plt.title('Angular Displacement of First Pendulum in Double Pendulum')
plt.grid()
plt.show()

time = np.linspace(0, t_max, steps)
plt.figure()
plt.plot(time, theta2_vals)
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement (rad)')
plt.title('Angular Displacement of Second Pendulum in Double Pendulum')
plt.grid()
plt.show()
