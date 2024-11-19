import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk

ALPHA = 0.1
BETA = 0.01
GAMMA = 0.2
DELTA = 0.02

INITIAL_PREY = 50
INITIAL_PRED = 10

def dydt(t, y):
    x, z = y  # x is prey, z is predator
    dxdt = alpha.get() * x - beta.get() * x * z  # Prey equation
    dzdt = delta.get() * x * z - gamma.get() * z  # Predator equation
    return [dxdt, dzdt]

# solve diff eq
def solve_equations():
    global solution
    y_0 = [initial_prey.get(), initial_pred.get()]  # Read initial conditions from input
    timespan = (0, 100) #time axis - can be longer ?
    solution = solve_ivp(dydt, timespan, y_0, method='RK45', t_eval=np.linspace(0, 100, 500)) #method is rk45 !! 

# make figs
def update_plot():
    solve_equations()

    # update pvsp
    pvp_line.set_data(solution.y[0], solution.y[1])  # x is prey, y is predator
    ax1.set_xlim(0, max(solution.y[0]) * 1.1)
    ax1.set_ylim(0, max(solution.y[1]) * 1.1)

    # update ppvstime 
    prey_line.set_data(solution.t, solution.y[0])  # Time on x, prey on y
    pred_line.set_data(solution.t, solution.y[1])  # Time on x, predator on y
    ax2.set_xlim(0, max(solution.t))
    ax2.set_ylim(0, max(max(solution.y[0]), max(solution.y[1])) * 1.1)

    fig.canvas.draw_idle()

#update the plot and parameter labels
def update_parameters(event=None):
    update_plot()
    alpha_value_label.config(text=f"{alpha.get():.3f}")
    beta_value_label.config(text=f"{beta.get():.3f}")
    gamma_value_label.config(text=f"{gamma.get():.3f}")
    delta_value_label.config(text=f"{delta.get():.3f}")


def update_initial_conditions():
    try:
        initial_prey.set(float(prey_input.get()))
        initial_pred.set(float(pred_input.get()))
        update_plot()
    except ValueError:
        print("Invalid input for initial conditions")

# init tk
root = tk.Tk()
root.title("Predator-Prey Parameter Adjustment")

# param control values
alpha = tk.DoubleVar(value=ALPHA)
beta = tk.DoubleVar(value=BETA)
gamma = tk.DoubleVar(value=GAMMA)
delta = tk.DoubleVar(value=DELTA)

initial_prey = tk.DoubleVar(value=INITIAL_PREY)
initial_pred = tk.DoubleVar(value=INITIAL_PRED)

# sliders and value labels of param
controls_frame = ttk.Frame(root)
controls_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# alpha
ttk.Label(controls_frame, text="Alpha (Prey Growth Rate)").pack(pady=5)
alpha_slider = ttk.Scale(controls_frame, from_=0, to=1, orient='horizontal', variable=alpha, command=update_parameters)
alpha_slider.pack()
alpha_value_label = ttk.Label(controls_frame, text=f"{ALPHA:.3f}")
alpha_value_label.pack()

# beta
ttk.Label(controls_frame, text="Beta (Predator-Prey Interaction)").pack(pady=5)
beta_slider = ttk.Scale(controls_frame, from_=0, to=0.1, orient='horizontal', variable=beta, command=update_parameters)
beta_slider.pack()
beta_value_label = ttk.Label(controls_frame, text=f"{BETA:.3f}")
beta_value_label.pack()

# gamma
ttk.Label(controls_frame, text="Gamma (Predator Death Rate)").pack(pady=5)
gamma_slider = ttk.Scale(controls_frame, from_=0, to=1, orient='horizontal', variable=gamma, command=update_parameters)
gamma_slider.pack()
gamma_value_label = ttk.Label(controls_frame, text=f"{GAMMA:.3f}")
gamma_value_label.pack()

# delta
ttk.Label(controls_frame, text="Delta (Predator Reproductive Rate)").pack(pady=5)
delta_slider = ttk.Scale(controls_frame, from_=0, to=0.1, orient='horizontal', variable=delta, command=update_parameters)
delta_slider.pack()
delta_value_label = ttk.Label(controls_frame, text=f"{DELTA:.3f}")
delta_value_label.pack()

# start conditions 
ttk.Label(controls_frame, text="Initial Prey Population").pack(pady=5)
prey_input = ttk.Entry(controls_frame)
prey_input.insert(0, str(INITIAL_PREY))
prey_input.pack()

ttk.Label(controls_frame, text="Initial Predator Population").pack(pady=5)
pred_input = ttk.Entry(controls_frame)
pred_input.insert(0, str(INITIAL_PRED))
pred_input.pack()

# Button to update initial conditions
ttk.Button(controls_frame, text="Set Initial Conditions", command=update_initial_conditions).pack(pady=10)

#figure 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# pvsp 
pvp_line, = ax1.plot([], [], color='purple')
ax1.set_xlabel('Prey Population')
ax1.set_ylabel('Predator Population')
ax1.set_title("Predator vs. Prey")

# pvst
prey_line, = ax2.plot([], [], label='Prey (x)', color='blue')
pred_line, = ax2.plot([], [], label='Predator (z)', color='red')
ax2.set_xlabel('Time')
ax2.set_ylabel('Population')
ax2.set_title("Predator and Prey vs. Time")
ax2.legend()

# Embed Matplotlib in tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Initial plot setup
solve_equations()
update_plot()

# Start the GUI event loop
root.mainloop()
