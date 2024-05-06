import numpy as np


def gaussian(position):
  gaussian = (1 / (np.sqrt(2 * np.pi)) * np.e ** (-0.5 * (position ** 2)))
  return gaussian


if __name__ == '__main__':
  positions = np.linspace(-4, 4, 41)
  x_values = np.empty(41)
  y_values = np.empty(41)
  
  for i, pos in enumerate(positions):
    x_values[i] = pos
    y_values[i] = gaussian(pos)

  print('X Values:', x_values)
  print('Y Values:', y_values)
  