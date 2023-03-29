import pygame
from pygame import FULLSCREEN, SCALED, mixer
import random
import Audio, Interface

# Initiate pygame (necessary lol)
pygame.init()
screen = pygame.display.set_mode((700,700), FULLSCREEN|SCALED)

################################## SPRITE IMAGES ##################################
# Load player images
chuck_r = pygame.image.load('images/Chuck/chuck_0.png').convert_alpha()
chuck_l = pygame.image.load('images/Chuck/chuck_1.png').convert_alpha()
ouch_r = pygame.image.load('images/Chuck/ouch_0.png').convert_alpha()
ouch_l = pygame.image.load('images/Chuck/ouch_1.png').convert_alpha()
# Load number images
num_1 = pygame.image.load('images/numbers/num_1.png').convert_alpha()
num_2 = pygame.image.load('images/numbers/num_2.png').convert_alpha()
num_6 = pygame.image.load('images/numbers/num_6.png').convert_alpha()
# Put numbers in nice lists
num_list = [num_1, num_2, num_6]
pattern = [num_1, num_2, num_1, num_6]
j = 0 # Index that goes through pattern
lanes = (36, 72, 108, 144, 180, 216, 252, 288, 324) # number lanes
# Huell related images
huell = pygame.image.load('images/Huell/huell.png').convert_alpha() # huell
battery = pygame.image.load('images/Huell/battery.png').convert_alpha() # battery

################################## SPRITE CLASSES ##################################
bat_go = False
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.velo = 0
        self.img = chuck_r
        self.lives = 3
        self.score = 0
        self.dir = 1
    
    def move(self, last_image):
        self.x += self.velo
        if self.velo > 0:
            if self.img == ouch_l or self.img == ouch_r:
                self.img = ouch_r
            else:
                self.img = chuck_r
            screen.blit(self.img, (self.x, self.y))
        elif self.velo < 0:
            if self.img == ouch_r or self.img == ouch_l:
                self.img = ouch_l
            else:
                self.img = chuck_l
            screen.blit(self.img, (self.x, self.y))
        elif self.velo == 0:
            self.img = last_image
            screen.blit(self.img, (self.x, self.y))
        elif self.velo == 0:
            self.img = last_image
            screen.blit(self.img, (self.x, self.y))

class Number(pygame.sprite.Sprite):
    def __init__(self, initial_y):
        self.num = random.choice(num_list)
        self.velo = random.randrange(2,10)
        self.x = random.choice(lanes)
        self.y = initial_y

    def generate(self):
        self.y += self.velo
        if self.num == num_1:
            screen.blit(num_1, (self.x, self.y))
        elif self.num == num_2:
            screen.blit(num_2, (self.x, self.y))
        elif self.num == num_6:
            screen.blit(num_6, (self.x, self.y))

        if self.y > 700:
            self.y = random.choice([-35,-235])
            self.x = random.choice(lanes)
            self.num = random.choice(num_list)
            self.generate()
            self.velo = random.randrange(4,8)
class Huell(pygame.sprite.Sprite):
    def __init__(self):
        self.dir = 1
        self.img = huell
        self.velo = 1
        self.x = 150
        self.y = -144
        self.x += self.velo
    
    def generate(self):
        global bat_go
        self.x += self.dir * self.velo
        if self.y != 0:
            self.y += 4
        if self.x < 0:
            self.dir = 1
        elif self.x > 386-179:
            self.dir = -1
        if self.y == 0:
            bat_go = True
        screen.blit(huell, (self.x, self.y))

class Battery(pygame.sprite.Sprite):
    def __init__(self, boss):
        self.size = [32,38]
        self.num = pygame.transform.scale(battery, self.size)
        self.velo = 6.9
        self.x = boss.x + 89
        self.y = 144
        self.count = 0
        self.scale = 1

    def generate(self, boss, chuck):
        self.y += self.velo
        self.size[0] += 0.25
        self.size[1] += 0.75
        self.num = pygame.transform.scale(battery, self.size)
        screen.blit(self.num, (self.x, self.y))
        self.x += (chuck.x - self.x)/36
        if self.y > 700:
            self.size = [32,38]
            self.count += 1
            self.y = 144
            self.x = boss.x + 89
            self.generate(boss, chuck)
            self.size = [32,38]

################################## CHECK FOR COLLISION ##################################
hit_time = 0 # helps turn Chuck red for 5 sec when he gets hit
j = 0 # Index that iterates pattern
def collide_check(player, player_rect, rect, col):
    global j, hit_time
    if rect.colliderect(player_rect):
        col.y = 700
        if pattern[j] == col.num:
                j += 1
                pygame.mixer.Sound.play(Audio.coin)
        else:
            if player.lives <= 1:
                # Game Over screen
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, 386, 700))
                font = pygame.font.Font("fonts/cool_font.ttf", 40)
                display = font.render("CHICANERED", True, (255,255,255))
                screen.blit(display, (72,330))
                font = pygame.font.Font("fonts/main_font.ttf", 9)
                display = font.render('Press "ESC" if you want to exit.', True, (255,255,255))
                screen.blit(display, (93,380))
                screen.blit(Interface.border, (0,0))
                # reset lives & score on sreen
                Interface.lives_set(3)
                Interface.score_set(0)
                player.score = 0
            else:
                pygame.draw.rect(screen, (255,0,0), pygame.Rect(0, 0, 386, 700))
            pygame.mixer.Sound.play(Audio.notcrazy)
            pygame.mixer.Sound.play(Audio.zap)
            hit_time = pygame.time.get_ticks()
            if player.dir == 1:
                player.img = ouch_r
            elif player.dir == -1:
                player.img = ouch_l
            player.lives -= 1
