import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 1. Define the vehicle dynamics (Kinematic Single-Track Model)
def vehicle_dynamics(x, t, u, p):
    """
    x: State vector [x, y, delta, v, psi] (pos_x, pos_y, steer, vel, yaw)
    u: Input [acceleration, steering_rate]
    p: Parameters [wheelbase]
    """
    pos_x, pos_y, delta, v, psi = x
    accel, steer_rate = u
    wheelbase = p

    # State derivatives
    dpos_x = v * np.cos(psi)
    dpos_y = v * np.sin(psi)
    dsteer = steer_rate
    dvel = accel
    dyaw = v * np.tan(delta) / wheelbase

    return [dpos_x, dpos_y, dsteer, dvel, dyaw]

# 2. Simulation Setup
params = 2.5 # Wheelbase in meters
initial_state = [0.0, 0.0, 0.0, 10.0, 0.0] # [x, y, steer, vel, yaw]
t = np.linspace(0, 5, 100) # 5 seconds
input_u = [1.0, 0.1] # Acceleration, Steering

# 3. Simulate
states = odeint(vehicle_dynamics, initial_state, t, args=(input_u, params))

# 4. Plot Results
plt.plot(states[:, 0], states[:, 1])
plt.title("Vehicle Path")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.show()
