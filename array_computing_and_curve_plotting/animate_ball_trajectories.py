from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


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

    fig, ax = plt.subplots()
    ax.set_ylim(0, maximum_heights.max() * 1.1)
    ax.set_xlim(0, x(times_of_flight.max(), initial_conditions[:, 2].max(), \
        initial_conditions[:, 1].max()) * 1.1)
    lines = []
    for idx, (maximum_height, color) in enumerate(zip(maximum_heights, colors)):
        line, = ax.plot([], [], lw=2, color=colors[idx])  
        lines.append(line)
        ax.axhline(y=maximum_height, color=color)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    
    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    
    def update(frame):
        t = np.linspace(0, times_of_flight[frame], 1000)
        for idx, (_, initial_velocity, angle) in \
        enumerate(initial_conditions):
            x_vals = x(t, angle, initial_velocity)
            y_vals = y(t, angle, initial_velocity, g)
            valid_indices = np.where(y_vals >= 0)
            lines[idx].set_data(x_vals[valid_indices], y_vals[valid_indices])
        return lines

    
    anim = FuncAnimation(fig, update, frames=len(times_of_flight), init_func=init, \
    blit=True)

    plt.show()
