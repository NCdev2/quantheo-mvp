from vpython import *
import numpy as np

# Constants
G = 6.674e-11  # Gravitational constant
M_earth = 5.972e24  # Mass of Earth (kg)
M_moon = 7.348e22   # Mass of Moon (kg)
distance = 3.844e8  # Initial distance between Earth and Moon (m)
dt = 1000  # Time step (seconds)

# Create the scene
scene = canvas(title="Earth-Moon Gravitational Simulation")

# Create Earth
earth = sphere(pos=vector(0, 0, 0), radius=6.37e6 * 5, color=color.blue, make_trail=True)

# Create Moon
moon = sphere(pos=vector(distance, 0, 0), radius=1.737e6 * 5, color=color.gray(0.7), make_trail=True)

# Initial velocity of Moon (circular orbit approximation)
v_moon = vector(0, 1022, 0)  # Moon's orbital velocity (m/s)

# Simulation loop
while True:
    rate(1000)  # Control speed

    # Compute gravitational force
    r_vec = earth.pos - moon.pos
    r = mag(r_vec)
    F_grav = (G * M_earth * M_moon) / r**2
    force_dir = norm(r_vec)  # Unit vector

    # Update velocity and position using Euler's method
    acceleration = force_dir * F_grav / M_moon
    v_moon += acceleration * dt
    moon.pos += v_moon * dt
