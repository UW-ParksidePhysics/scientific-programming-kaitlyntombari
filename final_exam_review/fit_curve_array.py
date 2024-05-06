"""Make fit curve using fit polynomial coefficients, NumPy's polynomial, and minimum \
and maximum x-values.

__Kaitlyn Tombari__
"""

import numpy as np


def fit_curve_array(quadratic_coefficients : np.ndarray, minimum_x_value: float, \
maximum_x_value: float, number_of_points: int = 100) -> np.ndarray:
    """Function used to make a fit curve."""
    if maximum_x_value < minimum_x_value:
        raise ArithmeticError("Maximum x-value must be greater than or equal to \
        minimum x-value.")
    if number_of_points <= 2:
        raise IndexError("Number of points must be greater than 2.")

    x_values = np.linspace(minimum_x_value, maximum_x_value, number_of_points)
    y_values = np.polynomial.polynomial.polyval(x_values, quadratic_coefficients)
    return np.array([x_values, y_values])


if __name__ == "__main__":
    quadratic_coefficients = np.array([0, 0, 1])
    minimum_x_value = -2
    maximum_x_value = 2
    try:
        fit_curve = fit_curve_array(quadratic_coefficients, minimum_x_value, \
        maximum_x_value)
        print("Fit curve array:")
        print(fit_curve)
    except (ArithmeticError, IndexError) as e:
        print(e)
      