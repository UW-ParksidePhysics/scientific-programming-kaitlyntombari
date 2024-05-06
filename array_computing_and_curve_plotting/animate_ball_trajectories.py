import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation


def x(t, angle, initial_velocity):
    return initial_velocity * np.cos(angle) * t


def y(t, angle, initial_velocity, g):
    return initial_velocity * np.sin(angle) * t - 0.5 * g * t**2


if __name__ == "__main__":
    initial_conditions = np.array([[1, 10, np.pi/4], [2, 5, np.pi/6], [3, 20, np.pi/3]])
    colors = ["blue", "green", "red"]
    g = 9.81  # m/s²
    times_of_flight = 2 * initial_conditions[:, 1] * np.sin(initial_conditions[:, 2]) / g
    maximum_heights = initial_conditions[:, 1] ** 2 * \
    np.sin(initial_conditions[:, 2])**2 / (2 * g)


    figure, axes = plt.subplots()
    axes.set_ylim(0, maximum_heights.max() * 1.1)
    axes.set_xlim(0, x(times_of_flight, initial_conditions[:, 2], \
initial_conditions[:, 1]).max() * 1.1)
    lines = []
    for index, (maximum_height, color) in enumerate(zip(maximum_heights, colors)):
        line, = axes.plot([], [], lw=2, color=color)  
        lines.append(line)
        axes.axhline(y=maximum_height, color=color)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    