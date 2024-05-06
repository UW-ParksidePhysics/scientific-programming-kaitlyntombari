import numpy as np
import matplotlib.pyplot as plt


def calculate_trajectory(ground_position, angle, initial_velocity, initial_ball_position, gravitational_acceleration):
    trajectory = ground_position * np.tan(angle) - (1 / 2 * initial_velocity ** 2) * ((gravitational_acceleration * ground_position ** 2) / (2 * np.cos(angle) ** 2)) + initial_ball_position
    return trajectory


def plot_trajectory(angle, initial_velocity, initial_ball_position, gravitational_acceleration):
    x_values = np.linspace(0, 10, 100)
    y_values = calculate_trajectory(x_values, angle, initial_velocity, initial_ball_position, gravitational_acceleration)
  
    plt.plot(x_values, y_values)  
    plt.title('Trajectory of a ball')
    plt.xlabel('Horizontal Distance (m)')
    plt.ylabel('Vertical Distance (m)')  
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    angle = np.radians(45)  # radians
    initial_velocity = 10  # m/s
    initial_ball_position = 0  # m
    gravitational_acceleration = 9.81  # m/s^2

  
    plot_trajectory(angle, initial_velocity, initial_ball_position, gravitational_acceleration)
