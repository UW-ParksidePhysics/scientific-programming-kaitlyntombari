import vpython as vp

# Define parameters for the first ball
initial_position1 = vp.vector(-10., 5., 5.) 
initial_velocity1 = vp.vector(25., -15., -15.) 
ball1 = vp.sphere(pos=initial_position1, radius=0.5, color=vp.color.blue, \
make_trail=True)

# Define parameters for the second ball
initial_position2 = vp.vector(-10., -5., 5.)
initial_velocity2 = vp.vector(25., 15., 15.)
ball2 = vp.sphere(pos=initial_position2, radius=0.5, color=vp.color.green, \
make_trail=True)

# Define parameters for the wall
wall_center = vp.vector(0., 0., 0.)
wall_dimensions = vp.vector(0.25, 10., 10.)
wall = vp.box(pos=wall_center, size=wall_dimensions, color=vp.color.red)

animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.005
stop_time = 1.

time = 0.
while time < stop_time:
    vp.rate(rate_of_animation)

    # Check for collision with the wall for ball 1
    if abs(ball1.pos.x - wall.pos.x) <= ball1.radius + 0.5 * wall_dimensions.x:
        initial_velocity1.x = -initial_velocity1.x
    ball1.pos += initial_velocity1 * time_step

    # Check for collision with the wall for ball 2
    if abs(ball2.pos.x - wall.pos.x) <= ball2.radius + 0.5 * wall_dimensions.x:
        initial_velocity2.x = -initial_velocity2.x
    ball2.pos += initial_velocity2 * time_step

    time += time_step
