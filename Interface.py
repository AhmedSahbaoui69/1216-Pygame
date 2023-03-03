import pygame
from pygame import FULLSCREEN, SCALED, mixer
import random

# initiate pygame
pygame.init()
screen = pygame.display.set_mode((700,700), FULLSCREEN|SCALED)

################################## DECORATIONS ##################################
court = pygame.image.load('images/interface/court.png').convert()
border = pygame.image.load('images/interface/border.png').convert_alpha()
speech = pygame.image.load('images/interface/speech.png').convert()
_1216_ = pygame.image.load('images/interface/1216.png').convert_alpha()
# hammer frames
hammer_0, hammer_1 = pygame.image.load("images/hammer/hammer_0.png").convert_alpha(), pygame.image.load("images/hammer/hammer_1.png").convert_alpha()
hammer = []
index = 0
# Let's animate it the hard way lol
for i in range(24):
    hammer.append(hammer_0)
for i in range(24):
    hammer.append(hammer_1)

################################## LIVE / SCORE UPDATE FUNCTIONS ##################################
def score_set(score):
    font = pygame.font.Font("fonts/main_font.ttf", 30)
    scored = font.render("Score: " + str(score), True, (74,246,38))
    screen.blit(scored, (464,615))
def lives_set(lives):
    font = pygame.font.Font("fonts/main_font.ttf", 30)
    lives = font.render("Lives: " + str(lives), True, (255, 0, 0))
    screen.blit(lives, (464,645))