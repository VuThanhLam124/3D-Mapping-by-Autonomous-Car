import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import lidar_process as lp
#plot data in 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
x = [lp.coordinates(angle, distance)[0] for angle, distance in lp.data]
y = [lp.coordinates(angle, distance)[1] for angle, distance in lp.data]
z = [0]*len(x)
ax.scatter(x, y,z, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
