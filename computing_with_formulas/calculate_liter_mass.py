volume = 1000 #cm^3

density_iron = 7.87 #g/cm^3
density_air = .0012 #g/cm^3
density_gasoline = .755 #g/cm^3
density_ice = .9167 #g/cm^3
density_body = 1.096 #g/cm^3
density_silver = 10.5 #g/cm^3
density_platinum = 21.45 #g/cm^3

mass_iron = volume * density_iron
mass_air = volume * density_air
mass_gasoline = volume * density_gasoline
mass_ice = volume * density_ice
mass_body = volume * density_body
mass_silver = volume * density_silver
mass_platinum = volume * density_platinum

print(f'The mass of iron is {mass_iron:.2f} grams')
print(f'The mass of air is {mass_air:.2f} grams')
print(f'The mass of gasoline is {mass_gasoline:.2f} grams')
print(f'The mass of ice is {mass_ice:.2f} grams')
print(f'The mass of body is {mass_body:.2f} grams')
print(f'The mass of silver is {mass_silver:.2f} grams')
print(f'The mass of platinum is {mass_platinum:.2f} grams')