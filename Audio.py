import pygame
from pygame import FULLSCREEN, SCALED, mixer
import random

# Initiate pygame (necessary lol)
pygame.init()
screen = pygame.display.set_mode((700,700), FULLSCREEN|SCALED)

################################## SOUND EFFECTS ##################################
# Fail sounds
notcrazy = pygame.mixer.Sound('sounds/collision_sounds/notcrazy.mp3')
zap = pygame.mixer.Sound('sounds/collision_sounds/zap.mp3')
zap.set_volume(0.1)
# Score sounds
iknewit = pygame.mixer.Sound('sounds/1216_collected/iknewit.mp3')
pocket = pygame.mixer.Sound('sounds/1216_collected/pocket.mp3')
sunroof = pygame.mixer.Sound('sounds/1216_collected/sunroof.mp3')
chicanery = pygame.mixer.Sound('sounds/1216_collected/chicanery.mp3')
shouldve = pygame.mixer.Sound('sounds/1216_collected/shouldve.mp3')
law = pygame.mixer.Sound('sounds/1216_collected/law.mp3')
huell_s = pygame.mixer.Sound('sounds/other/huell.mp3')
# Put scored_sounds in a nice list
scored = [iknewit, pocket, chicanery, law, sunroof, shouldve]
# Coin sound effect
coin = pygame.mixer.Sound('sounds/collision_sounds/coin.mp3')
coin.set_volume(0.1)
################################## BACKGROUND MUSIC ##################################
menu_theme = pygame.mixer.Sound("sounds/background_music/menu.mp3")
theme = pygame.mixer.Sound("sounds/background_music/theme.mp3")
theme.set_volume(0.15)
epic_theme = pygame.mixer.Sound("sounds/background_music/epic_theme.mp3")
epic_theme.set_volume(0.2)