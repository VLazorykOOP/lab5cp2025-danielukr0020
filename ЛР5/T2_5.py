import matplotlib.pyplot as plt
import numpy as np
import random

plt.figure(figsize=(6, 6))
for i, a in enumerate(np.linspace(0, 2*np.pi, 6, endpoint=False)):
    x = y = 0
    points = []
    for _ in range(1500):
        r = random.random()
        if r < 0.01: x, y = 0, 0.16*y
        elif r < 0.86: x, y = 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
        elif r < 0.93: x, y = 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
        else: x, y = -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44
        points.append((x, y))
    pts = np.array(points)
    rot = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
    rot_pts = pts @ rot
    plt.plot(rot_pts[:,0], rot_pts[:,1], '.', ms=0.5, color=plt.cm.hsv(i/6))

plt.axis('off')
plt.show()
