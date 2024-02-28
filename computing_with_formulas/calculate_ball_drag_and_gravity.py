import math

drag_coefficient = 0.2
air_density = 1.2 # kg/m^3
gravitational_acceleration = 9.81 # m/s^2

ball_velocity_hard_kick = 33.333 # m/s
ball_velocity_soft_kick = 2.778 # m/s
ball_mass = 0.43 # kg

cross_area = math.pi * (.11)**2 # cm^2

drag_force_hard_kick = 0.5 * drag_coefficient * air_density \
* cross_area * ball_velocity_hard_kick**2

drag_force_soft_kick = .5 * drag_coefficient * air_density \
* cross_area * ball_velocity_soft_kick**2

gravitational_force = ball_mass * gravitational_acceleration

ratio_hard_kick = drag_force_hard_kick / gravitational_force
ratio_soft_kick = drag_force_soft_kick / gravitational_force

print(f'The ball velocity for a hard kick is {ball_velocity_hard_kick:.1f} m/s')
print(f'The drag force of a hard kick is {drag_force_hard_kick:.1f} N')
print(f'The gravitational force is {gravitational_force:.1f} N')
print(f'The ratio of drag force for a hard kick and gravitational force is \
{ratio_hard_kick:.1f}')

print(f'The ball velocity for a soft kick is {ball_velocity_soft_kick:.1f} m/s)')
print(f'The drag force of a soft kick is {drag_force_soft_kick:.1f} N')
print(f'The gravitational force is {gravitational_force:.1f} N')
print(f'The ratio of drag force for a soft kick and gravitational force is \
{ratio_soft_kick:.1f}')