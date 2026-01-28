import numpy as np
import matplotlib.pyplot as plt
print("USE SI UNITS ONLY FOR ALL INPUTS")

#initial conditions and parameters
v0 = float(input("Enter initial velocity of the body: "))
x0 = float(input("Enter initial position of the body: "))
m = float(input("Enter mass of the body: "))
q = float(input("Enter charge of the body: "))
E = float(input("Enter magnitude of the electric field: "))
steps = int(input("Enter the number of time steps for the simulation: "))*100
dt = 0.01

#Arrays
t = np.linspace(0, (steps-1) * dt, steps)
x = np.zeros(len(t))
v = np.zeros(len(t))
gamma = np.zeros(len(t))
a = np.zeros(len(t))

#Initial Values
x[0] = x0
v[0] = v0

#Euler's Method
for i in range(steps-1):
    gamma[i] = 1 / np.sqrt(1 - (v[i]**2 / 299792458**2))
    a[i] = (q * E) / (m * gamma[i]**3)
    v[i+1] = v[i] + a[i] * dt
    x[i+1] = x[i] + v[i] * dt

#Plotting of x-t graph of particle motion
plt.plot(t, x)
plt.title("Relativistic Charged Particle in Electric Field")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid()
plt.show()