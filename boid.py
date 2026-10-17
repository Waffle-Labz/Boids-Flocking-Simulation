import pygame
from random import randint

from config import *

class Boid:
    def __init__(self, x, y, obstacles = []):
        self.x = float(x)
        self.y = float(y)
        self.v_x = 0.0
        self.v_y = 0.0
        self.a_x = 0.0
        self.a_y = 0.0
        self.speed = 0.0
        self.obstacles = obstacles

    def update(self):

        self.avoid_obstacles()

        self.x += self.v_x
        if self.x < 0: self.x += WIDTH
        if self.x > WIDTH: self.x -= WIDTH

        self.y += self.v_y
        if self.y < 0: self.y += HEIGHT
        if self.y > HEIGHT: self.y -= HEIGHT

        self.v_x += self.a_x
        self.v_y += self.a_y

        self.a_x = 0.0
        self.a_y = 0.0

        self.speed = (self.v_x ** 2 + self.v_y ** 2) ** 0.5
        if self.speed > MAX_SPEED:
            self.v_x = (self.v_x / self.speed) * MAX_SPEED
            self.v_y = (self.v_y / self.speed) * MAX_SPEED

        elif self.speed < MIN_SPEED:
            self.v_x = (self.v_x / self.speed) * MIN_SPEED
            self.v_y = (self.v_y / self.speed) * MIN_SPEED

    def avoid_obstacles(self):
        for obstacle in self.obstacles:
            dist_x = obstacle.x - self.x
            dist_y = obstacle.y - self.y
            distance = (dist_x ** 2 + dist_y ** 2) ** 0.5

            if distance == 0:
                self.a_x -= self.v_x
                self.a_y -= self.v_y
                continue

            detection_distance = OBSTACLE_AVOIDANCE_RADIUS + obstacle.radius

            if distance >= detection_distance:
                continue

            # Unit vector towards the obstacle
            dir_x = dist_x / distance
            dir_y = dist_y / distance

            # Only react if moving towards the obstacle
            heading_dot = self.v_x * dir_x + self.v_y * dir_y

            if heading_dot <= 0:
                continue

            speed = (self.v_x ** 2 + self.v_y ** 2) ** 0.5

            # Increase avoidance strength rapidly near the obstacle
            # proximity = 1 - distance / detection_distance
            proximity = 10 - 1 / distance
            avoid_strength = (
                OBSTACLE_AVOIDANCE_STRENGTH * proximity * speed
            )

            # Scale by how directly the boid is heading towards it
            heading_strength = heading_dot / max(self.speed, 0.001)
            avoid_strength *= heading_strength

            # Steer away from the obstacle
            self.a_x -= dir_x * avoid_strength
            self.a_y -= dir_y * avoid_strength

            # Relocate if a collision has already occurred
            if distance < obstacle.radius:
                self.x = randint(0, WIDTH)
                self.y = randint(0, HEIGHT)
                break
    
    def draw(self, screen):
        speed_ratio = (self.speed - MIN_SPEED) / (MAX_SPEED - MIN_SPEED)
        speed_ratio = max(0.0, min(1.0, speed_ratio))

        color = tuple(
            int(min_channel + (max_channel - min_channel) * speed_ratio)
            for min_channel, max_channel in zip(MIN_COLOR, MAX_COLOR)
        )

        pygame.draw.polygon(screen, color, [
            (self.x + (7 * BOID_SIZE) * self.v_x / self.speed,
            self.y + (7 * BOID_SIZE) * self.v_y / self.speed),
            (self.x - (3 * BOID_SIZE) * self.v_y / self.speed,
            self.y + (3 * BOID_SIZE) * self.v_x / self.speed),
            (self.x + (3 * BOID_SIZE) * self.v_y / self.speed,
            self.y - (3 * BOID_SIZE) * self.v_x / self.speed)
        ])



    