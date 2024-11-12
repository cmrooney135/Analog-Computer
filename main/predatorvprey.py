import matplotlib.pyplot as plt 
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation

# Parameters (these will be read in from the MCU)
ALPHA = 0.1  
BETA = 0.01
GAMMA = 0.2 
DELTA = 0.02 

# Differential equation function
def dydt(t, y):
    x, z = y  # x is prey, z is predator
    dxdt = ALPHA * x - BETA * x * z  # Prey equation
    dzdt = DELTA * x * z - GAMMA * z  # Predator equation
    return [dxdt, dzdt]

# Initial conditions
y_0 = [50, 10]  

# Timespan
timespan = (0, 100)

# Solve the differential equations
solution = solve_ivp(dydt, timespan, y_0, method='RK45', t_eval=np.linspace(0, 100, 500))

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, max(solution.y[0]) * 1.1)  # x-axis for prey population
ax.set_ylim(0, max(solution.y[1]) * 1.1)  # y-axis for predator population

line, = ax.plot([], [], color='purple')
ax.set_xlabel('Prey Population')
ax.set_ylabel('Predator Population')
ax.set_title("Predator vs. Prey Population Dynamics")

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Update function for the animation
def update(frame):
    line.set_data(solution.y[0][:frame], solution.y[1][:frame])  # x is prey, y is predator
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(solution.t), init_func=init, blit=True, interval=50)

# Save the animation
ani.save('figs/Predator_vs_Prey.gif', writer='pillow')

plt.show()
