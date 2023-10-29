import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from pyswarm import pso  # You need to install the pyswarm package

# Define the plant (system) transfer function
Plant = ctrl.TransferFunction([1], [1, 5, 10])  # Example transfer function

# Define simulation parameters
time = np.linspace(0, 20, 1000)
desired_moisture = np.ones_like(time) * 0.7  # Example desired moisture level

# Function to be optimized by PSO
def pid_performance(K):
    Kp, Ki, Kd = K
    controller = ctrl.TransferFunction([Kp, Ki, Kd], [1, 0])

    time_data = []
    moisture_data = []

    for t, setpoint in zip(time, desired_moisture):
        closed_loop_system = ctrl.feedback(controller * Plant, 1)
        _, response = ctrl.step_response(closed_loop_system, time)

        time_data.append(t)
        moisture_data.append(response[-1])

    # Define a performance metric to minimize (e.g., Integral of Time-weighted Absolute Error, ITAE)
    error = np.abs(desired_moisture - moisture_data)
    ITAE = np.trapz(t * error, time)

    return ITAE

# PSO optimization
lb = [0.0, 0.0, 0.0]  # Lower bounds for Kp, Ki, Kd
ub = [10.0, 10.0, 10.0]  # Upper bounds for Kp, Ki, Kd

xopt, _ = pso(pid_performance, lb, ub)

# Extract the optimized parameters
Kp_opt, Ki_opt, Kd_opt = xopt

print(f"Optimized Kp: {Kp_opt}")
print(f"Optimized Ki: {Ki_opt}")
print(f"Optimized Kd: {Kd_opt}")
