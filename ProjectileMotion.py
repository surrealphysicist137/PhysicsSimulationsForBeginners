import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
from scipy.optimize import minimize_scalar

print("USE SI UNITS ONLY FOR ALL INPUTS UNLESS OTHERWISE SPECIFIED")
#parameters and initial conditions
v0 = float(input("Enter launch speed: "))
m = float(input("Enter mass of projectile: "))
c = float(input("Enter drag coefficient: "))
print("Enter initial height of projectile:")
y_0 = float(input())
x_0 = 0.0
g = 9.81

#trajectory calculations
def projectile(t, Y):
    x, y, vx, vy = Y
    dxdt = vx
    dydt = vy
    dvxdt = -(c/m) * vx**2
    dvydt = -g - (c/m) * vy**2
    return [dxdt, dydt, dvxdt, dvydt]
# event to stop integration when projectile hits the ground
def hit_ground(t, Y):
    return Y[1]
hit_ground.terminal = True
hit_ground.direction = -1

# function to compute range for given angle
def range_for_angle(alpha):
    vx0 = v0 * np.cos(alpha)
    vy0 = v0 * np.sin(alpha)
    y0 = [0, 0, vx0, vy0]
    sol = spi.solve_ivp(projectile, t_span=(0, 10),y0 = y0, events=hit_ground, max_step=0.05)
    return sol.y[0, -1]  # final x position

# optimize angle for maximum range
res = minimize_scalar(lambda angle: -range_for_angle(angle), bounds=(0, np.pi/2), method='bounded')
optimal_angle = res.x
print(f"Optimal launch angle for maximum range (in degrees): {np.degrees(optimal_angle):.2f}")

theta = optimal_angle

# initial velocity components
vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)

# solve and extract results
y0 = [x_0, y_0, vx0, vy0]
sol = spi.solve_ivp(projectile, t_span=(0, 10), y0=y0, events=hit_ground, max_step=0.05)
x = sol.y[0]
y = sol.y[1]

# plot
plt.plot(x, y, label="Trajectory", color='blue')
plt.xlabel("Horizontal distance (m)")
plt.ylabel("Vertical height (m)")
plt.title("Projectile Trajectory")
plt.grid(True)
plt.show()
