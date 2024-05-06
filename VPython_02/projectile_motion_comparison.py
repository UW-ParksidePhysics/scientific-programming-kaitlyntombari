import vpython as vp

# Define gravitational accelerations on Earth, Mars, and Moon
gravitational_acceleration_earth = 9.8  # m/s^2
gravitational_acceleration_mars = 3.7  # m/s^2
gravitational_acceleration_moon = 1.6  # m/s^2

def calculate_range_and_time_of_flight(initial_velocity, angle, \
gravitational_acceleration):
    """Function used to calculate the range and the time of flight."""
    initial_velocity_x = initial_velocity * vp.cos(angle)
    initial_velocity_y = initial_velocity * vp.sin(angle)
    time_flight = (2 * initial_velocity_y) / gravitational_acceleration
    range_x = initial_velocity_x * time_flight
    return range_x, time_flight

# Create the colored fields for Earth, Mars, and Moon
field_earth = vp.box(pos=vp.vector(0, 0, 0), size=vp.vector(20, 0.1, 20), \
color=vp.color.green)
field_mars = vp.box(pos=vp.vector(50, 0, 0), size=vp.vector(20, 0.1, 20), \
color=vp.color.red)
field_moon = vp.box(pos=vp.vector(-50, 0, 0), size=vp.vector(20, 0.1, 20), \
color=vp.color.gray(0.5))

# Extra credit: Create the text labels for Earth, Mars, and Moon
vp.label(pos=vp.vector(0, -5, 0), text="EARTH", color=vp.color.green)
vp.label(pos=vp.vector(60, -5, 0), text="MARS", color=vp.color.red)
vp.label(pos=vp.vector(-60, -5, 0), text="MOON", color=vp.color.gray(0.5))

# Create initial position, velocity, and angle for the balls
initial_position_earth = vp.vector(-10, 0, -5)
initial_position_mars = vp.vector(40, 0, -5)
initial_position_moon = vp.vector(-70, 0, -5)
initial_velocity = 20 # m/s
ball_radius = 1 # m
angle = vp.radians(40)

# Calculate the range and time of flight for Earth, Mars, and Moon
range_earth, earth_time_of_flight = calculate_range_and_time_of_flight\
(initial_velocity, angle, gravitational_acceleration_earth)
range_mars, mars_time_of_flight = calculate_range_and_time_of_flight\
(initial_velocity, angle, gravitational_acceleration_mars)
range_moon, moon_time_of_flight = calculate_range_and_time_of_flight\
(initial_velocity, angle, gravitational_acceleration_moon)

# Create the ball for Earth
ball_earth = vp.sphere(pos=initial_position_earth, radius=ball_radius, \
color=vp.color.blue)
velocity_earth = vp.vector(initial_velocity * vp.cos(angle), initial_velocity * \
vp.sin(angle), 0)
ball_earth.trail = vp.curve(color=vp.color.blue)

# Create the ball for Mars
ball_mars = vp.sphere(pos=initial_position_mars, radius=ball_radius,
                      color=vp.vector(1, 0.5, 0.5))
velocity_mars = vp.vector(initial_velocity * vp.cos(angle), initial_velocity * \
vp.sin(angle), 0)
ball_mars.trail = vp.curve(color=vp.vector(1, 0.4, 0.6))

# Create the ball for Moon
ball_moon = vp.sphere(pos=initial_position_moon, radius=ball_radius, \
color=vp.color.white)
velocity_moon = vp.vector(initial_velocity * vp.cos(angle), initial_velocity * \
vp.sin(angle), 0)
ball_moon.trail = vp.curve(color=vp.color.white)


def update_position(ball, velocity, time_flight, gravitational_acceleration):
    """Function used to update the ball's position."""
    dt = time_flight / 1000
    time = 0
    while time < time_flight:
        vp.rate(1000)
        acceleration = vp.vector(0, -gravitational_acceleration, 0)
        velocity += acceleration * dt
        ball.pos += velocity * dt
        ball.trail.append(pos=ball.pos)
        time += dt

# Update the positions for the three balls
update_position(ball_earth, velocity_earth, earth_time_of_flight,\
gravitational_acceleration_earth)
update_position(ball_mars, velocity_mars, mars_time_of_flight, \
gravitational_acceleration_mars)
update_position(ball_moon, velocity_moon, moon_time_of_flight, \
gravitational_acceleration_moon)
