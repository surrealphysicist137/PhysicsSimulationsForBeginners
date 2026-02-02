import numpy as np
import matplotlib.pyplot as plt

print("USE SI UNITS ONLY FOR ALL INPUTS")
# Parameters and Initial Conditions
T_s = float(input("Enter the constant ambient temperature: "))
A = float(input("Enter the effective surface area of the substance: "))
T_0 = float(input("Enter the initial temperature of the substance: "))
E = float(input("Enter the emissivity of the substance: "))
m = float(input("Enter the mass of the substance: "))
c = float(input("Enter the specific heat capacity of the substance: "))
steps = int(input("Enter the time limit: "))*100
dt = 0.01
sigma = 5.67e-8 
p = A*sigma*E

#Arrays
t = np.linspace(0, dt*(steps-1), steps)
T = np.zeros(steps)
T[0] = T_0

#Euler's Method
for i in range(1, steps):
    dT_dt =  p*(T_s**4-T[i-1]**4) / (m*c)
    T[i] = T[i-1] + dt*dT_dt

# Plot
plt.plot(t, T, label="Temperature vs Time", color='green')
plt.xlabel("Time (s)")
plt.ylabel("Temperature (K)")
plt.title("Heat Transfer by Radiation")
plt.show()
