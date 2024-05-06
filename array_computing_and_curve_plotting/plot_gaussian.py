import numpy as np
import matplotlib.pyplot as plt


def gaussian(position):
  gaussian = (1 / (np.sqrt(2 * np.pi)) * np.e ** (-0.5 * (position ** 2)))
  return gaussian


if __name__ == '__main__':
  positions = np.linspace(-4, 4, 41)
  gaussian_values = gaussian(positions)

  plt.plot(positions, gaussian_values)
  plt.title('Gaussian Function')
  plt.xlabel('Position')
  plt.ylabel('Gaussian Value')
  plt.grid(True)
  plt.show()
  