import numpy as np


def gaussian(position):
  gaussian = (1 / (np.sqrt(2 * np.pi)) * np.e ** (-0.5 * (position ** 2)))
  return gaussian


if __name__ == '__main__':
  x_values = np.linspace(-4, 4, 41)
  y_values = gaussian(x_values)
  
  print("Positions:", x_values)
  print("Gaussian Values:", y_values)
