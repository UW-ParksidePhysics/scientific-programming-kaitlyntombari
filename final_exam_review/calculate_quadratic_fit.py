"""Fit a quadratic polynomial to a two row NumPy array of x-y data using NumPy's \
polynomial class polyfit() method.

__Kaitlyn Tombari__
"""

import numpy as np


def calculate_quadratic_fit(data:np.ndarray) -> np.ndarray:
    """Function used to fit a quadradtic polynomial to a two row NumPy array of x-y \
    data."""
    if data.shape[0] != 2:
        raise IndexError("Input data should have exactly 2 rows and at least 2 columns.")

    x_data = data[0]
    y_data = data[1]
    quadratic_coefficients = np.polyfit(x_data, y_data, 2)
    return quadratic_coefficients

if __name__ == "__main__":
    data = np.array([np.linspace(-1,1), np.linspace(-1,1) ** 2])
    try:
        quadratic_coefficients = calculate_quadratic_fit(data)
        print(f'Quadratic polynomial coefficients: {quadratic_coefficients}')
    except IndexError as e:
        print(e)
