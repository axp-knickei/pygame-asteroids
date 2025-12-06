from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            "white", 
            self.position, 
            self.radius, 
            LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        # 1. kill this asteroid
        self.kill()

        # 2. if too small, return
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20, 50)
            velocity_vector1 = self.velocity.rotate(split_angle)
            velocity_vector2 = self.velocity.rotate(-split_angle)
            splitted_aste_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, splitted_aste_radius)
            asteroid1.velocity = velocity_vector1 * 1.2
            
            asteroid2 = Asteroid(self.position.x, self.position.y, splitted_aste_radius)
            asteroid2.velocity = velocity_vector2 * 1.2



