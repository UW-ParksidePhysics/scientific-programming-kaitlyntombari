"""
Create a combined scatter and curve plot for the data and the fit polynomial, \
respectively, using Pyplot's plot function.
"""

__author__ = "Kaitlyn Tombari"

import matplotlib.pyplot as plt
import numpy as np


def plot_data_with_fit(data: np.ndarray, fit_curve: np.ndarray, data_format: str = \
'x', fit_format: str = '-') -> list:
    """Function used to create a combined scatter and curve plot for the data \
    and the fit polynomial."""
    data_plot = plt.scatter(data[0], data[1], s=50, marker=data_format) 
    fit_plot = plt.plot(fit_curve[0], fit_curve[1], fit_format)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Combined Scatter and Curve Plot')
    plt.legend(['Data', 'Fit']) 
    return [data_plot, fit_plot] 


if __name__ == "__main__":
    data = np.array([[-2, -2, 0, 1, 2], [4, 1, 0, 1, 4]])
    fit_curve = np.array([np.linspace(-2, 2), np.linspace(-2, 2) ** 2])
    combined_plot = plot_data_with_fit(data, fit_curve, data_format='o', 
    fit_format='--')
    plt.show()
