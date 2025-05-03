import numpy as np
import matplotlib.pyplot as plt

# Step 1: Take input from user
print("Enter 4 points (x, y) in increasing order of x:")

x = []
y = []
for i in range(4):
    xi = float(input(f"Enter x[{i+1}]: "))
    yi = float(input(f"Enter y[{i+1}]: "))
    x.append(xi)
    y.append(yi)

x = np.array(x)
y = np.array(y)

# Step 2: Compute intervals h
h = np.diff(x)   #hi = xi+1 - xi

# Step 3: Set up the linear system for solving c1 and c2
A = np.zeros((2, 2))
rhs = np.zeros(2)

A[0, 0] = 2 * (h[0] + h[1])
A[0, 1] = h[1]
A[1, 0] = h[1]
A[1, 1] = 2 * (h[1] + h[2])

rhs[0] = 3 * ((y[2] - y[1]) / h[1] - (y[1] - y[0]) / h[0])
rhs[1] = 3 * ((y[3] - y[2]) / h[2] - (y[2] - y[1]) / h[1])

# Step 4: Solve for c1 and c2, and set natural spline boundaries
c = np.zeros(4)
c[1:3] = np.linalg.solve(A, rhs)  # solves A.c=rhs

# Step 5: Compute b, d, and a
a = y[:-1]
b = np.zeros(3)
d = np.zeros(3)

for i in range(3):
    d[i] = (c[i+1] - c[i]) / (3 * h[i])
    b[i] = ((y[i+1] - y[i]) / h[i]) - h[i] * (2 * c[i] + c[i+1]) / 3

# Step 6: Define a function for the spline segments
def spline_piece(i, xi):   #calculates y value at an x value
    dx = xi - x[i]
    return a[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3

# Step 7: Evaluate and plot the spline
xs = np.linspace(x[0], x[3], 200)  #creates 200 equal spaces between the first and last input
ys = np.zeros_like(xs)   # initialises a similar array with 0

for i in range(3):  #3 intervals
    mask = (xs >= x[i]) & (xs <= x[i+1]) #finds x values in the 200 values that lie in the intervals ( total 3 intervals)
    ys[mask] = spline_piece(i, xs[mask]) # gives y value for each of 200 xvalues

plt.plot(x, y, 'ro', label='Given Points')
plt.plot(xs, ys, 'b-', label='Cubic Spline Interpolation')
plt.title("Natural Cubic Spline Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()