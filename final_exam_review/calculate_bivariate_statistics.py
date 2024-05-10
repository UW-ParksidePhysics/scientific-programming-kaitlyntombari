"""
Calculate statistical characteristics of a data set using SciPy's stats.describe \
function.
"""

__author__ = "Kaitlyn Tombari"

import numpy as np
from scipy import stats


def calculate_bivariate_statistics(data: np.ndarray) -> np.ndarray:
    """Function used to calculate the statistical characteristics of a data set."""
    if data.shape[0] != 2 or data.shape[1] <= 1:
        raise IndexError(f"Data array has inappropriate dimensionsL {data.shape}.")
    mean_y = np.mean(data[1])
    standard_deviation_y = np.std(data[1])
    minimum_x_value = np.min(data[0])
    maximum_x_value = np.max(data[0])
    minimum_y_value = np.min(data[1])
    maximum_y_value = np.max(data[1])
    return np.array([mean_y,standard_deviation_y, minimum_x_value, maximum_x_value, \
    minimum_y_value, maximum_y_value])


if __name__ == "__main__":
  x_values = np.linspace(-10, 10, 100)
  y_values = x_values ** 2
  data = np.array([x_values, y_values])
  try:
      data = np.loadtxt("final_exam_review/volumes_energies.dat").T
      statistics = calculate_bivariate_statistics(data)
      print(f'Mean of y: {statistics[0]:.2f}')
      print(f'Standard deviation of y: {statistics[1]:.2f}')
      print(f'Minimum x-value: {statistics[2]:.2f}')
      print(f'Maximum x-value: {statistics[3]:.2f}')
      print(f'Minimum y-value: {statistics[4]:.2f}')
      print(f'Maximum y-value: {statistics[5]:.2f}')
      print(stats.describe(statistics))
      print(stats.describe(data))
  except IndexError as e:
    print(e)
