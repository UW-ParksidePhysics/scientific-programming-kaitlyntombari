a = [3,3] 
b = [5,3] 
a2 = a[0]**2 + a[1]**2
b2 = b[0]**2 + b[1]**2
ab = a[0]*b[0] + a[1]*b[1]

binomial_sum_squared_terms = a2 + 2 * ab + b2
binomial_difference_squared_terms = a2 - 2 * ab + b2
binomial_sum_squared = (a[0] + b[0])**2 + (a[1] + b[1])**2
binomial_difference_squared = (a[0] - b[0])**2 + (a[1] - b[1])**2

print(f'First equation:  {binomial_sum_squared:.1f} = {binomial_sum_squared_terms:.1f}')
print(f'Second equation: {binomial_difference_squared:.1f} = \
{binomial_difference_squared_terms:.1f}')