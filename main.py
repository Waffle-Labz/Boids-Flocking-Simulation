import pygame
from random import random, randint

from boid import Boid
from obstacle import Obstacle
from rules import cohesion, separation, alignment
from config import *

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boid Simulation")

# Create a list of Obstacle instances
obstacles = [
    Obstacle(400, 400, 30),
    Obstacle(200, 200, 20),
    Obstacle(600, 600, 25)
]

# Create a list of Boid instances
boids = [Boid(randint(0, WIDTH), randint(0, HEIGHT), obstacles) for _ in range(50)]
s = 3
for boid in boids:
    boid.v_x = random() * 2 * s - s
    boid.v_y = random() * 2 * s - s

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (RGB)
    screen.fill(BACKGROUND_COLOR)

    # Draw each obstacle
    for obstacle in obstacles:
        obstacle.draw(screen)

    # Update and draw each boid
    for boid in boids:
        alignment(boid, boids)
        cohesion(boid, boids)
        separation(boid, boids)

        boid.update()
        boid.draw(screen)

    # Update the display
    pygame.display.flip()
pygame.quit()