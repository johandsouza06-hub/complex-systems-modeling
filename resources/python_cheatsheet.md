# Python Cheatsheet for Complex Systems Modeling

## Basic Data Types
```python
# Numbers
x = 5          # integer
y = 3.14       # float

# Lists (sequences)
points = [1, 2, 3, 4]
coordinates = [(0, 0), (1, 1), (2, 0)]

# Strings
message = "Hello, complex world!"
```

## Control Flow
```python
# Loops
for i in range(10):
    print(f"Step {i}")

for point in coordinates:
    x, y = point
    print(f"Position: ({x}, {y})")

# Conditionals
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```

## Functions
```python
def midpoint(p1, p2):
    "Calculate midpoint between two points"
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 + x2) / 2, (y1 + y2) / 2)

# Usage
result = midpoint((0, 0), (2, 4))
```

## Essential Libraries
```python
import numpy as np
import matplotlib.pyplot as plt
import random

# NumPy arrays
arr = np.array([1, 2, 3, 4])
matrix = np.array([[1, 2], [3, 4]])

# Plotting
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Simple Plot')
plt.show()

# Random numbers
random_point = (random.random(), random.random())
random_choice = random.choice(['red', 'blue', 'green'])
```

## Common Patterns in Complex Systems
```python
# Chaos game step
def chaos_step(current, vertices, fraction=0.5):
    chosen = random.choice(vertices)
    new_x = current[0] + fraction * (chosen[0] - current[0])
    new_y = current[1] + fraction * (chosen[1] - current[1])
    return (new_x, new_y)

# Distance between points
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Visualization template
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x_coords, y_coords, s=1, alpha=0.7)
ax.set_aspect('equal')
ax.set_title('Complex System Visualization')
plt.show()
```
