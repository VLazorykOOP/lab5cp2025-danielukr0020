import numpy as np
import matplotlib.pyplot as plt

def compute_hermite_points(p1, p2, v1, v2, resolution=100):
    t = np.linspace(0, 1, resolution)
    h = [
        2 * t**3 - 3 * t**2 + 1,
        -2 * t**3 + 3 * t**2,
        t**3 - 2 * t**2 + t,
        t**3 - t**2
    ]
    x_vals = h[0] * p1[0] + h[1] * p2[0] + h[2] * v1[0] + h[3] * v2[0]
    y_vals = h[0] * p1[1] + h[1] * p2[1] + h[2] * v1[1] + h[3] * v2[1]
    return x_vals, y_vals

def draw_hermite(p1, p2, v1, v2, scale=1.5):
    x, y = compute_hermite_points(p1, p2, v1, v2)

    x *= scale
    y *= scale

    points = {
        'P1': np.array(p1) * scale,
        'P2': np.array(p2) * scale,
        'V1': np.array(v1) * scale,
        'V2': np.array(v2) * scale
    }

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'b', label='Крива Ерміта')
    plt.scatter([points['P1'][0], points['P2'][0]], [points['P1'][1], points['P2'][1]], color='red', label='Точки')
    plt.quiver(*points['P1'], *points['V1'], angles='xy', scale_units='xy', scale=1, color='green', label='Вектор V1')
    plt.quiver(*points['P2'], *points['V2'], angles='xy', scale_units='xy', scale=1, color='orange', label='Вектор V2')

    plt.title("Гладка крива Ерміта")
    plt.legend()
    plt.axis('equal')
    plt.grid(True)
    plt.show()

# Демонстрація
if __name__ == "__main__":
    draw_hermite((0, 1), (4, 4), (2, -5), (4, -2), scale=-3)
