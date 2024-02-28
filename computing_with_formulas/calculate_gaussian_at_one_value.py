import math

mean = 0
standard_deviation = 2
input_value = 1

function_output = (1 / (math.sqrt(2 * math.pi) * standard_deviation)) \
**(-.5 * ((input_value - mean / standard_deviation)**2))
function_output = (1 / (math.sqrt(2 * math.pi) * standard_deviation)) * \
math.exp(-0.5 * ((input_value - mean) / standard_deviation)**2)

print(f'The mean is {mean}')
print(f'The standard deviation is {standard_deviation}')
print(f'The input value is {input_value}')
print(f'The function output is {function_output:.6f}')
