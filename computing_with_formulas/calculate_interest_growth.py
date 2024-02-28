initial_amount_A = 1000 # dollars
interest_rate_P = 4.45 # percent, taken Feb 23, 2024
years_n = 3 # years
growth_amount = initial_amount_A * (1 + interest_rate_P / 100) ** years_n

print(f'The initial amount is {initial_amount_A} dollars')
print(f'The interest rate is {interest_rate_P} percent')
print(f'The growth amount is {growth_amount:.2f} dollars')