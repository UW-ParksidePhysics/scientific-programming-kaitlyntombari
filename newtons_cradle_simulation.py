"""Newton's Cradle demonstrates physics concepts through a series of swinging \
spheres, where momentum and kinetic energy are transferred from one end to the other \
in a pendulum motion. In this simulation of Newton's Cradle, functions are used to \
calculate the angle of the string, the angular velocity of the spheres, and the \
potential and kinetic energy transferred all over an interval of time. Values for \
the simulation time, mass of the spheres, and the length of the string are chosen and \
used in these functions. The script utilizes the NumPy and Matplotlib libraries to \
model and visualize the swinging spheres. Three plots are created to visulize the \
results of the simulation: "Angle vs. Time", "Angular Velocity vs. Time", and \
"Energy vs. Time"."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import g as gravitational_acceleration


def calculate_angle(time, string_length):
    """Function used to calculate the angle of the string at a certain time."""
    pendulum_frequency = np.sqrt(gravitational_acceleration / string_length)
    string_angle = (np.pi / 4) * np.cos(pendulum_frequency * time)
    return string_angle


def calculate_angular_velocity(time, string_length):
    """Function used to calculate the angular velocity of the pendulum at a certain \
    time."""
    pendulum_frequency = np.sqrt(gravitational_acceleration / string_length)
    angular_speed = (-np.pi / 4) * np.sin(pendulum_frequency * time) * pendulum_frequency
    return angular_speed


def calculate_kinetic_energy(time, ball_mass, string_length):
    """Function used to calculate kinetic energy at a certain time."""
    angular_speed = calculate_angular_velocity(time, string_length)
    kinetic_energy = 0.5 * ball_mass * (string_length ** 2) * (angular_speed ** 2)
    return kinetic_energy


def calculate_potential_energy(time, ball_mass, string_length):
    """Function used to calculate potential energy at a certain time."""
    string_angle = calculate_angle(time, string_length)
    potential_energy = ball_mass * gravitational_acceleration * string_length \
  * (1 - np.cos(string_angle))
    return potential_energy


def simulate_newtons_cradle():
    """Function used to simulate the motion of Newton's Cradle and visualize the \
    angle, angular velocity, kinetic energy, and potential energy over a period of \
    time."""
    # Define parameters
    maximum_time = 3  # Maximum time for simulation (s)
    ball_mass = 0.2  # kg
    string_length = 0.1  # m

    # Create a time array
    times = np.linspace(0, maximum_time, 1000)

    # Create a matrix to store pendulum values (angle and angular velocity) over time
    pendulum_values = np.zeros((len(times), 2))

    # Calculate and store angle and angular velocity over time
    for i, t in enumerate(times):
        # Calculate angle and angular velocity
        angular_frequency = np.sqrt(gravitational_acceleration / string_length)
        angle = (np.pi / 4) * np.cos(angular_frequency * t)
        angular_velocity = (-np.pi / 4) * np.sin(angular_frequency * t) * angular_frequency
        # Store angle and angular velocity in the matrix
        pendulum_values[i, 0] = angle
        pendulum_values[i, 1] = angular_velocity

    # Extract angle and angular velocity from the matrix
    angle_values = pendulum_values[:, 0]
    angular_velocity_values = pendulum_values[:, 1]

    # Calculate kinetic and potential energy over time
    kinetic_energy_values = np.array([calculate_kinetic_energy(t, ball_mass, \
    string_length) for t in times])
    potential_energy_values = np.array([calculate_potential_energy(t, ball_mass, \
    string_length) for t in times])

    # Create plots
    plt.figure()

    # Plot of Angle vs. Time
    plt.subplot(3, 1, 1)
    plt.plot(times, angle_values, color='black')
    plt.title('Angle vs. Time')
    plt.xlabel('t (s)')
    plt.ylabel('θ (rad)')
    plt.xlim([0, maximum_time])

    # Plot of Angular Velocity vs. Time
    plt.subplot(3, 1, 2)
    plt.plot(times, angular_velocity_values, color='black')
    plt.title('Angular Velocity vs. Time')
    plt.xlabel('t (s)')
    plt.ylabel('ω (rad/s)')
    plt.xlim([0, maximum_time])

    # Plot of Kinetic and Potential Energy vs. Time
    plt.subplot(3, 1, 3)
    plt.plot(times, kinetic_energy_values, label='Kinetic Energy', color='blue')
    plt.plot(times, potential_energy_values, label='Potential Energy', color='brown')
    plt.title('Energy vs. Time')
    plt.xlabel('t (s)')
    plt.ylabel('E (J)')
    plt.xlim([0, maximum_time])
    plt.legend()

    plt.subplots_adjust(hspace=2.0)
    plt.show()
    return


if __name__ == "__main__":
    simulate_newtons_cradle()
  