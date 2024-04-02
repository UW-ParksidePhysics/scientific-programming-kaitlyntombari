def compute_heaviside(position):
  if position < 0:
    return 0
  if position >= 0:
   return 1

if __name__ == '__main__':
  result1 = compute_heaviside(position=-10)
  result2 = compute_heaviside(position=-10-15)
  result3 = compute_heaviside(position=0)
  result4 = compute_heaviside(position=10-15)
  result5 = compute_heaviside(position=10)

  print(f'H(-10) = {result1}')
  print(f'H(-10-15) = {result2}')
  print(f'H(0) = {result3}')
  print(f'H(10-15) = {result4}')
  print(f'H(10) = {result5}')


