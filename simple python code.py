Import numpy as np
Import matplotlib.pyplot as plt
Import control as ctrl
# Define the plant (system) transfer function
# Replace this with the actual transfer function of your soil system
Plant = ctrl.TransferFunction([1], [1, 5, 10]) # Example transfer function
# Initial PID controller parameters
Kp = 1.0
Ki = 0.1
Kd = 0.01
# Define the PID controller transfer function
Controller = ctrl.TransferFunction([Kp, Ki, Kd], [1, 0])
# Define simulation parameters
Time = np.linspace(0, 20, 1000)
Desired_moisture = np.ones_like(time) * 0.7 # Example desired moisture level
# Lists to store data for plotting
Time_data = []
Moisture_data = []
Kp_data = []
Ki_data = []
Kd_data = []
# Simulation loop
For t, setpoint in zip(time, desired_moisture):
 # Simulate the system’s response to the current controller gains
 Closed_loop_system = ctrl.feedback(controller * plant, 1)
 Time, response = ctrl.step_response(closed_loop_system, time)
# Calculate the current moisture error
Error = setpoint – response[-1]
 # Adjust PID gains based on the error (simple rule-based approach)
 If error > 0.1:
 Kp += 0.1
 Elif error < -0.1:
 Kp -= 0.1
If error > 0.01:
 Ki += 0.01
 Elif error < -0.01:
 Ki -= 0.01
If error > 0.001:
 Kd += 0.001
 Elif error < -0.001:
 Kd -= 0.001
# Update the PID controller with the new gains
 Controller = ctrl.TransferFunction([Kp, Ki, Kd], [1, 0])
# Store data for plotting
 Time_data.append(t)
 Moisture_data.append(response[-1])
 Kp_data.append(Kp)
 Ki_data.append(Ki)
 Kd_data.append(Kd)
# Plot results
Plt.figure(figsize=(12, 8))
Plt.subplot(2, 2, 1)
Plt.plot(time_data, desired_moisture, label=’Desired Moisture Level’, linestyle=’—‘)
Plt.plot(time_data, moisture_data, label=’Moisture Level’)
Plt.xlabel(‘Time’)
Plt.ylabel(‘Moisture Level’)
Plt.title(‘Moisture Control’)
Plt.legend()
Plt.grid(True)
Plt.subplot(2, 2, 2)
Plt.plot(time_data, Kp_data, label=’Kp’)
Plt.xlabel(‘Time’)
Plt.ylabel(‘Kp Value’)
Plt.title(‘Proportional Gain’)
Plt.grid(True)
Plt.subplot(2, 2, 3)
Plt.plot(time_data, Ki_data, label=’Ki’)
Plt.xlabel(‘Time’)
Plt.ylabel(‘Ki Value’)
Plt.title(‘Integral Gain’)
Plt.grid(True)
Plt.subplot(2, 2, 4)
Plt.plot(time_data, Kd_data, label=’Kd’)
Plt.xlabel(‘Time’)
Plt.ylabel(‘Kd Value’)
Plt.title(‘Derivative Gain’)
Plt.grid(True)
Plt.tight_layout()
Plt.show()                 