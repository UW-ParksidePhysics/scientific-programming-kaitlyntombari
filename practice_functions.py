mass = 12 #kg
velocity = 15 # m/s
height = 10 # m
acceleration_due_to_gravity = 9.81 #m/s^2

def total_mechanical_energy(mass, velocity, height, acceleration_due_to_gravity):
  energy = .5 * mass * velocity**2 \
  + mass * acceleration_due_to_gravity * height
  return energy


total_energy = total_mechanical_energy(mass, velocity, height, acceleration_due_to_gravity)

print(f' The mass is {mass} kg')
print(f' The velocity is {velocity} m/s')
print(f' The height is {height} m')
print(f' the acceleration due to gravity is {acceleration_due_to_gravity} m/s^2')
print(f' The total mechanical energy is {total_energy} J')