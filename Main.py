# import modules
import pygame
from pygame import FULLSCREEN, SCALED, mixer
import time, random
import Interface, Assets, Audio, Particles

# initiate pygame
pygame.init()
screen = pygame.display.set_mode((700,700), FULLSCREEN|SCALED)
Icon = pygame.image.load('images/Interface/1216.png')
pygame.display.set_caption("1216")
pygame.display.set_icon(Icon)

# clock
clock = pygame.time.Clock()

# player movement procedure to reduce code
def mouvement_code():
    global event, last_image, normal_stage, main
    last_image = chuck.img  # Keeps track of the last direction chuck looked at
    # Add event listener
    for event in pygame.event.get():
        pass
    # KEYDOWN CONDITIONS
    if event.type == pygame.KEYDOWN:
        # Exit game by clicking "ESCAPE"
        if event.key == pygame.K_ESCAPE:
            normal_stage, main = False, False

        # Player Mouvement
        if event.key == pygame.K_LEFT:
                chuck.velo = -5
                chuck.dir = -1
                Particles.dust.append(Particles.Dust([chuck.x,chuck.y+54]))
        elif event.key == pygame.K_RIGHT:
                chuck.velo = +5
                chuck.dir = 1
                Particles.dust.append(Particles.Dust([chuck.x+64,chuck.y+54]))
    # KEYUP CONDITIONS
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT and chuck.velo < 0:
            chuck.velo *= 0.75 # haha sex number
        if event.key == pygame.K_RIGHT and chuck.velo > 0:
            chuck.velo *= 0.75 # 
    # Collision with borders
    if chuck.x < 0:
        chuck.x = 0
    elif chuck.x > 321:
        chuck.x = 320
    # move
    chuck.move(last_image)

################################## MENU SCREEN ##################################
menu, index = True, 0
Audio.menu_theme.play(-1) # play background music in a loop
while menu:
    # Update
    pygame.display.update()
    clock.tick(60)
    # Draw
    screen.fill((31,32,34))
    fonth = pygame.font.Font("fonts/m23.ttf", 120)
    title = fonth.render("1216", fonth, (255, 71, 61))
    outline = fonth.render("1216", fonth, (255, 232, 130))
    title_center = title.get_rect(center = screen.get_rect().center)
    screen.blit(outline, (title_center[0]-6 ,title_center[1]))
    screen.blit(title, (title_center[0]+5,title_center[1]))
    fontt = pygame.font.Font("fonts/main_font.ttf", 15)
    text = fontt.render("Press Space To Start", fontt, (255,255,255))
    text_center = text.get_rect(center = screen.get_rect().center)
    # Blinking text effect
    if index == 60:
        index = 0
    elif index >= 30:
        screen.blit(text, (text_center[0], text_center[1]+85))
    index += 1
    # Leave menu loop when user presses space
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu  = False
                Audio.theme.play(-1)
                Audio.menu_theme.stop()

################################## SPRITES INITIATION ##################################
# Chuck McGill aka "not crazy"
chuck = Assets.Player(161, 636, 64)
# Initiate number objects in different collumns
col1 = Assets.Number(-35)
col2 = Assets.Number(-235)
col3 = Assets.Number(-435)
col4 = Assets.Number(-635)
col5 = Assets.Number(-835)
col6 = Assets.Number(-1035)
# Initiate Huell and his Battery
boss = Assets.Huell()
bat = Assets.Battery(boss) # Link it to its daddy

################################## MAIN GAME LOOP ##################################
huell_stage = False # Becomes "True" when Huell decides it's reasonable
main, normal_stage = True, True
# To prevent audios from repeating in a row
old_audio, new_audio = random.choice(Audio.scored), random.choice(Audio.scored)
while main:
    ################################## Normal Stage ##################################
    while normal_stage == True and huell_stage == False:
        boss.y = -144 # reset huell postion each time the player leaves his stage
        mouvement_code()
        chuck_rect = pygame.Rect(chuck.x, chuck.y, 64, 64) # Chuck rectangle
        # Generate numbers & their rectangles
        col1.generate()
        rect1 = pygame.Rect(col1.x, col1.y, 32, 38)
        col2.generate()
        rect2 = pygame.Rect(col2.x, col2.y, 32, 38)
        col3.generate()
        rect3 = pygame.Rect(col3.x, col3.y, 32, 38)
        col4.generate()
        rect4 = pygame.Rect(col4.x, col4.y, 32, 38)
        col5.generate()
        rect5 = pygame.Rect(col5.x, col5.y, 32, 38)
        col6.generate()
        rect6 = pygame.Rect(col6.x, col6.y, 32, 38)

        # Initiate/update score and lives
        Interface.score_set(chuck.score)
        Interface.lives_set(chuck.lives)

        # Prevent Chuck from playing the same sound in a row
        if Assets.j >= 4:
            Assets.j = 0
            while old_audio == new_audio:
                new_audio = random.choice(Audio.scored)
            pygame.mixer.Sound.play(new_audio)
            old_audio = new_audio
            chuck.score +=1
        
        # Restart if Chuck runs out of lives
        if chuck.lives <= 0:
            Audio.theme.stop() # Stop music
            time.sleep(3)
            Audio.theme.play(-1) # Replay music
            chuck.score, chuck.lives = 0, 3
            chuck.x, chuck.velo = 161, 0 # Reset Chuck's velocity and position
            col1.y, col2.y, col3.y, col4.y, col5.y, col6.y = -35, -235, -435, -235, -35, -635
            col6 = Assets.Number(-1035)
            Assets.j=0 # Reset pattern index
        
        # Check for collision with numbers
        Assets.collide_check(chuck, chuck_rect, rect1, col1)
        Assets.collide_check(chuck, chuck_rect, rect2, col2)
        Assets.collide_check(chuck, chuck_rect, rect3, col3)
        Assets.collide_check(chuck, chuck_rect, rect4, col4)
        Assets.collide_check(chuck, chuck_rect, rect5, col5)
        Assets.collide_check(chuck, chuck_rect, rect6, col6)
        
        current_time = pygame.time.get_ticks()
        
        # Chuck turns red when hit
        if current_time - Assets.hit_time > 1000:
            if chuck.dir == 1:
                chuck.img = Assets.chuck_r
            elif chuck.dir == -1:
                chuck.img = Assets.chuck_l

        # UPDATE
        pygame.display.update()
        clock.tick(60)

        # IGHT LETS DRAW!
        screen.fill( (50,50,50) )
        screen.blit(Interface.court, (0,0))
        if Interface.index == len(Interface.hammer):
            Interface.index = 0
        else:
            screen.blit(Interface.hammer[Interface.index], (150,110))
        Interface.index += 1
        font = pygame.font.Font("fonts/cool_font.ttf", 111)
        screen.blit(Interface._1216_, (446,25))
        screen.blit(Interface.speech, (395,130))
        
        # Dust particles loop
        for i in range(len(Particles.dust)):
            if len(Particles.dust[i].particles) > 0:
                Particles.dust[i].draw(screen)
                Particles.dust[i].update()
        
        # Check if Huell is horny
        if chuck.score%5 == 0 and chuck.score >= 2:
            bat.count = 0 # Reset battery counter
            normal_stage = False # Exit normal stage loop
            Audio.theme.stop() # Stop normal theme
            for s in Audio.scored:
                s.stop() # Stop all score audios
            huell_stage = True # Trigger Huell stage loop
            play_epic, Assets.bat_go, play_speech = True, False, True # Green light

        screen.blit(Interface.border, (0,0)) # Put border always on front
    
    ################################## Huell Stage ##################################
    while huell_stage == True and normal_stage == False: 
        if bat.count >= 15:
                Audio.epic_theme.stop()
                Audio.huell_s.stop()
                Audio.theme.play(-1)
                chuck.score += 1
                chuck.lives += 1
                huell_stage = False
                normal_stage = True
        else:    
            mouvement_code()
            chuck_rect = pygame.Rect(chuck.x, chuck.y, 64, 64) # Chuck rectangle
            # Play epic music
            if play_epic:
                Audio.epic_theme.play()
                Audio.huell_s.play()
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, 386, 700))
                play_epic = False
            # Update score and lives
            Interface.score_set(chuck.score)
            Interface.lives_set(chuck.lives)

            # Restart if Chuck runs out of lives
            if chuck.lives <= 0:
                Audio.epic_theme.stop() # Stop epic music
                Audio.huell_s.stop() # Stop Huell speech
                time.sleep(3)
                Audio.theme.play(-1) # Replay music
                chuck.score, chuck.lives = 0, 3
                chuck.x, chuck.velo = 161, 0 # Reset Chuck's velocity and position
                col1.y, col2.y, col3.y, col4.y, col5.y, col6.y = -35, -235, -435, -235, -35, -635
                col6 = Assets.Number(-1035)
                Assets.j=0 # Reset pattern index
                huell_stage, normal_stage = False, True

            if play_speech == True:
                pygame.mixer.Sound.play(Audio.huell_s)
                play_speech = False
            boss.generate()

            # Check for collision with batteries
            if Assets.bat_go == True:
                bat.generate(boss, chuck)
                bat_rect = pygame.Rect(bat.x, bat.y, bat.size[0], bat.size[1])
                Assets.collide_check(chuck, chuck_rect, bat_rect, bat)
            
            current_time = pygame.time.get_ticks()
            
            # Chuck turns red when hit
            if current_time - Assets.hit_time > 1000:
                if chuck.dir == 1:
                    chuck.img = Assets.chuck_r
                elif chuck.dir == -1:
                    chuck.img = Assets.chuck_l
            
            # UPDATE
            pygame.display.update()
            clock.tick(60)

            # IGHT LETS DRAW!
            screen.fill( (50,50,50) )
            screen.blit(Interface.court, (0,0))
            if Interface.index == len(Interface.hammer):
                Interface.index = 0
            else:
                screen.blit(Interface.hammer[Interface.index], (150,110))
            Interface.index += 1
            font = pygame.font.Font("fonts/cool_font.ttf", 111)
            screen.blit(Interface._1216_, (446,25))
            screen.blit(Interface.speech, (395,130))
            
            # Dust particles loop
            for i in range(len(Particles.dust)):
                if len(Particles.dust[i].particles) > 0:
                    Particles.dust[i].draw(screen)
                    Particles.dust[i].update()
            
            screen.blit(Interface.border, (0,0)) # Put border always on front

# quit pygame when exiting loop
pygame.quit()