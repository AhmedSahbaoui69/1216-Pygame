import pygame
from pygame import FULLSCREEN, SCALED
import random

# Initiate pygame (necessary lol)
pygame.init()
screen = pygame.display.set_mode((700,700), FULLSCREEN|SCALED)

################################## PARTICLES ##################################
dust = []
class Particle:
    def __init__(self, pos):
        self.x, self.y = pos[0], pos[1]
        self.vx, self.vy = random.randint(-2, 2), random.randint(-10, 0)*.1
        self.rad = 5

    def draw(self, win):
        pygame.draw.circle(win, (233, 234, 245), (self.x, self.y), self.rad)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if random.randint(0, 100) < 40:
            self.rad -= 1
class Dust:
    def __init__(self, pos):
        self.pos = pos
        self.particles = []
        for i in range(10):
            self.particles.append(Particle(self.pos))

    def update(self):
        for i in self.particles:
            i.update()
            self.particles = [particle for particle in self.particles if particle.rad > 0]

    def draw(self, win):
        for i in self.particles:
            i.draw(win)
