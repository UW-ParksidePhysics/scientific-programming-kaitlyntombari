import math

mass_small_egg = 47 # g
mass_large_egg = 67 # g
density = 1.038 # g/cm^3
specific_heat_capacity = 3.7 # J/g*K
thermal_conductivity = 0.0054 # W/cm*K

temperature_boiling_water = 100 # C
temperature_y = 70 # C
original_temperature_fridge = 4 # C
original_temperature_room = 20 # C

large_egg_frige_cook_time = ((mass_large_egg**(2/3)) * specific_heat_capacity \
  * (density**(1/3))) / (thermal_conductivity * (math.pi**2) * \
  (((4 * math.pi) / 3)**(2/3))) \
  * math.log(.76 * (original_temperature_fridge - temperature_boiling_water) \
  / (temperature_y - temperature_boiling_water))

large_egg_room_cook_time = ((mass_large_egg**(2/3)) * specific_heat_capacity \
  * (density**(1/3))) / (thermal_conductivity * (math.pi**2) * \
  (((4 * math.pi) / 3)**(2/3))) \
  * math.log(.76 * (original_temperature_room - temperature_boiling_water) \
  / (temperature_y - temperature_boiling_water))

# Compute cook times for small eggs from fridge and room temperature
small_egg_frige_cook_time = ((mass_small_egg**(2/3)) * specific_heat_capacity \
  * (density**(1/3))) / (thermal_conductivity * (math.pi**2) * \
  (((4 * math.pi) / 3)**(2/3))) \
  * math.log(.76 * (original_temperature_fridge - temperature_boiling_water) \
  / (temperature_y - temperature_boiling_water))

small_egg_room_cook_time = ((mass_small_egg**(2/3)) * specific_heat_capacity \
  * (density**(1/3))) / (thermal_conductivity * (math.pi**2) * \
  (((4 * math.pi) / 3)**(2/3))) \
  * math.log(.76 * (original_temperature_room - temperature_boiling_water) \
  / (temperature_y - temperature_boiling_water))

print(f'Large egg from fridge cook time = {large_egg_frige_cook_time:.0f} s = {large_egg_frige_cook_time/60:.1f} min')

print(f'Large egg from room temperature cook time = {large_egg_room_cook_time:.0f} s = {large_egg_room_cook_time/60:.1f}min')

print(f'Small egg from fridge cook time = {small_egg_frige_cook_time:.0f} s = {small_egg_frige_cook_time/60:.1f} min')

print(f'Small egg from room temperature cook time = {small_egg_room_cook_time:.0f} s = {small_egg_room_cook_time/60:.1f} min')