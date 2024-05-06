import numpy as np


def gaussian(position):
  gaussian = (1 / (np.sqrt(2 * np.pi)) * np.e ** (-0.5 * (position ** 2)))
  return gaussian


if __name__ == '__main__':
  positions = np.linspace(-4, 4, 41)
  gaussian_values = gaussian(positions)
  
  print('Positions:', positions)
  print('Gaussian Values:', gaussian_values)
  