import numpy as np


def calculate_quadratic_roots(a, b, c):
  discriminant = b**2 - 4*a*c

  
  if discriminant >= 0:
   root_1 = (-b + np.sqrt(discriminant)) / (2*a)
   root_2 = (-b - np.sqrt(discriminant)) / (2*a)
   return root_1, root_2
  elif discriminant == 0:
    root = -b / (2*a)
    return root,
  else:
    real = -b / (2*a)
    imaginary = np.sqrt(-discriminant) / (2*a)
    root_1 = complex(real, imaginary)
    root_2 = complex(real, -imaginary)
    return root_1, root_2


def test_single_root():
  a, b, c = 1, 2, 1
  # expected_output = (-1.0)
  roots = calculate_quadratic_roots(a,b,c)
  print(f'x^2 + 2x + 1 = 0: x = 1;calculate_quadratic_roots({a},  {b},  {c}) = {roots}')


def test_roots_float():
  a, b, c = 1, -2, -3
  # expected_output = (3.0, -1.0)
  roots = calculate_quadratic_roots(a,b,c)
  print(f'x^2 - 2x - 3 = 0: x = 3, -1.; calculate_quadratic_roots({a}, {b}, {c}) =  \
  {roots}')


def test_roots_complex():
  a, b, c = 1, 0, 1
 # expected_output = (1j, -1j)
  roots = calculate_quadratic_roots(a,b,c)
  print(f'x^2 + 0x + 1 = 0: x = i, -i ; calculate_quadratic_roots({a},  {b}, {c}) = \
  {roots}')


if __name__ == '__main__':
  test_single_root()
  test_roots_float()
  test_roots_complex()
  