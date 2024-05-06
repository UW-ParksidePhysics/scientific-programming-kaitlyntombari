import vpython as vp

# Define parameters for ball 1
initial_position1 = vp.vector(-1., 0., 0.)
initial_velocity1 = vp.vector(1., 1., 1.)
ball1 = vp.sphere(pos=initial_position1, radius=0.1, color=vp.color.red, \
make_trail=True)

# Define parameters for ball 2
initial_position2 = vp.vector(1., 0., 0.)
initial_velocity2 = vp.vector(-2., 1., 1.)
ball2 = vp.sphere(pos=initial_position2, radius=0.1, color=vp.color.green, \
make_trail=True)

animation_time_step = 0.1  # seconds
rate_of_animation = 1 / animation_time_step
time_step = 0.05
stop_time = 10.

time = 0.
while time < stop_time:
    vp.rate(rate_of_animation)
    # Update the position of ball 1
    x1 = initial_position1.x + initial_velocity1.x * time
    y1 = initial_position1.y + initial_velocity1.y * time
    z1 = initial_position1.z + initial_velocity1.z * time
    ball1.pos = vp.vector(x1, y1, z1)

    # Update the position of ball 2
    x2 = initial_position2.x + initial_velocity2.x * time
    y2 = initial_position2.y + initial_velocity2.y * time
    z2 = initial_position2.z + initial_velocity2.z * time
    ball2.pos = vp.vector(x2, y2, z2)

    time += time_step
