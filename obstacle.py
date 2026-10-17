import pygame

from config import *

class Obstacle:
    def __init__(self, x, y, radius):
        self.x = float(x)
        self.y = float(y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, OBSTACLE_COLOR, (int(self.x), int(self.y)), self.radius)