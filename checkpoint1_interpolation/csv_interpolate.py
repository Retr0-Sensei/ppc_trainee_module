import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev

# Load the CSV
df = pd.read_csv('loop_track_waypoints.csv')

# Extract x and y coordinates
x = df['X'].values
y = df['Y'].values

# Ensure the path is closed by appending the first point to the end, here no need as already closed loop data given
#x = np.append(x, x[0])
#y = np.append(y, y[0])

# Perform spline interpolation
tck, u = splprep([x, y], s=0, per=True)
u_fine = np.linspace(0, 1, 500)
x_fine, y_fine = splev(u_fine, tck)

#plot only waypoints
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ro', label='Original Waypoints')
plt.legend()
plt.axis('equal')
plt.title('Only waypoints')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# Plot original waypoints and interpolated curve
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ro-', label='Original Waypoints')
plt.plot(x_fine, y_fine, 'b-', label='Interpolated Curve')
plt.legend()
plt.axis('equal')
plt.title('Path Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()