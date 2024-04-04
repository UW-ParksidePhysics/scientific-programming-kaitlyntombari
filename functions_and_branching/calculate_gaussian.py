import numpy as np

def gaussian(position, mean=0.0, standard_deviation=1.0):
    coefficient = 1 / np.sqrt(2 * np.pi * standard_deviation ** 2)
    exponent = -0.5 * ((position - mean) / standard_deviation) ** 2
    return coefficient * np.exp(exponent)


if __name__ == "__main__":
  average = 2.0
  standard_deviation = 1.0
  n = 15

  start_x = average - 5 * standard_deviation
  end_x = average + 5 * standard_deviation
  step = (end_x - start_x) / (n - 1)

  print('x\t\tf(x)')
 
  for i in range(n):
    x = start_x + i * step
    f_x = gaussian(x, average, standard_deviation)
    print(f'{x:.4f}\t\t{f_x:.6f}')
  