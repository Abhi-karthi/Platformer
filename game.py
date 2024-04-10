import pygame
import random
import time


def show_text(msg, x, y, color, size, font):
    fontobj = pygame.font.SysFont(font, size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x, y))


x = 325
y = 400
start = False
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
grey = (127, 127, 127)
black = (0, 0, 0)
skyBlue = (120, 206, 255)
pygame.init()
colors = [white, red, green, blue, purple, skyBlue]
screen = pygame.display.set_mode((750,500))
pygame.display.set_caption("Zombie Apocalypse")
walkright = []
walkleft = []
jumpright = []
jumpleft = []
idleright = []
idleleft = []
slideright = []
slideleft = []
glideright = []
glideleft = []
attackright = []
attackleft = []
deadright = []
deadleft = []
pause = False
up = False
right = False
left = False
side = False
down = False
gliding = False
death = False
title = pygame.image.load("Good_Title.png")
bg = pygame.image.load("graveyardtilesetnew/png/BG.png")
bg = pygame.transform.scale(bg, (750, 500))
deadbush = pygame.image.load("graveyardtilesetnew/png/Objects/DeadBush.png")
deadbush = pygame.transform.scale(deadbush, (50, 50))
skeleton = pygame.image.load("graveyardtilesetnew/png/Objects/Skeleton.png")
bush = pygame.image.load("graveyardtilesetnew/png/Objects/Bush (1).png")
bush = pygame.transform.scale(bush, (100, 50))
sign = pygame.image.load("graveyardtilesetnew/png/Objects/Sign.png")
sign = pygame.transform.scale(sign, (50, 50))
for i in range(0, 9):
    image = pygame.image.load(f"png-3 less/Glide_00{i}.png")
    image = pygame.transform.scale(image, (95, 95))
    glideright.append(image)
    image = pygame.transform.flip(image, True, False)
    glideleft.append(image)

    image = pygame.image.load(f"png-3 less/Run__00{i}.png")
    image = pygame.transform.scale(image, (75, 100))
    walkright.append(image)
    image = pygame.transform.flip(image, True, False)
    walkleft.append(image)

    image = pygame.image.load(f"png-3 less/Jump__00{i}.png")
    image = pygame.transform.scale(image, (75, 100))
    jumpright.append(image)
    image = pygame.transform.flip(image, True, False)
    jumpleft.append(image)

    image = pygame.image.load(f"png-3 less/Idle__00{i}.png")
    image = pygame.transform.scale(image, (48, 96))
    idleright.append(image)
    image = pygame.transform.flip(image, True, False)
    idleleft.append(image)

    image = pygame.image.load(f"png-3 less/Slide__00{i}.png")
    image = pygame.transform.scale(image, (80, 80))
    slideright.append(image)
    image = pygame.transform.flip(image, True, False)
    slideleft.append(image)

    image = pygame.image.load(f"png-3 less/Attack__00{i}.png")
    image = pygame.transform.scale(image, (105, 105))
    attackright.append(image)
    image = pygame.transform.flip(image, True, False)
    attackleft.append(image)

    image = pygame.image.load(f"png-3 less/Dead__00{i}.png")
    image = pygame.transform.scale(image, (105, 105))
    deadright.append(image)
    image = pygame.transform.flip(image, True, False)
    deadleft.append(image)
slide = 0
jumptime = 0
slidetime = 0
walk = 0
jump = 0
idle = 0
glide = 0
floor = 397
togglehitboxes = False
floorDifference = 0
animationTime = 0
randomGraphics = []
menuGraphics = []
player = screen.blit(idleright[idle], (x, y))
playerhitbox = pygame.draw.rect(screen, blue, player, 1)
score = 0
high_score = 0
toggle_graphics = True
for i in range(50):
    menuGraphics.append([random.randint(0, 748), random.randint(0, 498), random.randint(5, 15)/10])
score = 0
clock = pygame.time.Clock()
while True:
    if not start:
        screen.fill((11, 11, 184))
        if toggle_graphics:
            for item in menuGraphics:
                pygame.draw.rect(screen, (250, 250, 77), (item[0], item[1], 4, 4))
                item[1] += item[2]
                if item[1] > 498:
                    item[1] = 0
        screen.blit(title, (30, 0))
        if score > high_score:
            high_score = score
        if score < 10000 and high_score < 10000:
            show_text(f"Prev. Score: {score}", 500, 175, white, 30, "Comic Sans")
            show_text(f"High Score: {high_score}", 500, 275, white, 30, "Comic Sans")
        else:
            show_text(f"Prev. Score: {score}", 400, 175, white, 30, "Comic Sans")
            show_text(f"High Score: {high_score}", 400, 275, white, 30, "Comic Sans")
        show_text("Difficulty:", 75, 175, white, 30, "Comic Sans")
        easy = pygame.draw.rect(screen, easy_button_color, (75, 225, 147, 51))
        show_text("Easy", 115, 225, black, 30, "Comic Sans")
        medium = pygame.draw.rect(screen, medium_button_color, (75, 290, 147, 51))
        show_text("Medium", 105, 290, black, 30, "Comic Sans")
        hard = pygame.draw.rect(screen, hard_button_color, (75, 355, 147, 51))
        show_text("Hard", 115, 355, black, 30, "Comic Sans")
        abhikarthi_mode = pygame.draw.rect(screen, abhikarthi_button_color, (75, 490, 147, 51))
        show_text("Abhikarthi Mode", 115, 490, black, 5, "Comic Sans")
        start_ = pygame.draw.rect(screen, (250, 250, 77), (300, 400, 147, 51))
        show_text("Start!", 325, 400, black, 30, "Comic Sans")
        quitter = pygame.draw.rect(screen, (250, 250, 77), (500, 350, 100, 50))
        show_text("Quit", 500, 350, black, 30, "Comic Sans")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy.collidepoint(pygame.mouse.get_pos()):
                    health = 300
                    max_health = 300
                    zombiespawntime = 4
                    easy_button_color = (200, 200, 27)
                    medium_button_color = (250, 250, 77)
                    hard_button_color = (250, 250, 77)
                    abhikarthi_button_color = (250, 250, 77)
                if medium.collidepoint(pygame.mouse.get_pos()):
                    health = 225
                    max_health = 225
                    zombiespawntime = 3.5
                    easy_button_color = (250, 250, 77)
                    medium_button_color = (200, 200, 27)
                    hard_button_color = (250, 250, 77)
                    abhikarthi_button_color = (250, 250, 77)
                if hard.collidepoint(pygame.mouse.get_pos()):
                    health = 150
                    max_health = 150
                    zombiespawntime = 3
                    easy_button_color = (250, 250, 77)
                    medium_button_color = (250, 250, 77)
                    hard_button_color = (200, 200, 27)
                    abhikarthi_button_color = (250, 250, 77)
                if abhikarthi_mode.collidepoint((pygame.mouse.get_pos())):
                    health = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                    max_health = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                    # zombiespawntime = 0
                    easy_button_color = (250, 250, 77)
                    medium_button_color = (250, 250, 77)
                    hard_button_color = (250, 250, 77)
                    abhikarthi_button_color = (200, 200, 27)
                if quitter.collidepoint((pygame.mouse.get_pos())):
                    quit()
                if start_.collidepoint(pygame.mouse.get_pos()):
                    score = 0
                    check_point = 0
                    damage = 71.42
                    zombiehealth = 150
                    zombiespawn = time.time()
                    pause = False
                    start = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    if toggle_graphics:
                        toggle_graphics = False
                    else:
                        toggle_graphics = True
    else:
        if not pause:
            screen.fill(black)
            screen.blit(bg, (0, 0))
            screen.blit(deadbush, (50, 450))
            screen.blit(skeleton, (360, 450))
            screen.blit(bush, (150, 450))
            screen.blit(sign, (500, 450))
            if time.time() - animationTime > 2:
                if len(randomGraphics) > 1:
                    for i in range(0, 50):
                        randomGraphics.pop(0)
                for i in range(0, 50):
                    randomGraphics.append([random.randint(0, 750), random.randint(0, 500), random.randint(1, 2)])
                animationTime = time.time()
            if toggle_graphics:
                for i in range(0, 49):
                    if time.time() - animationTime < 1:
                        if randomGraphics[i][2] == 1:
                            pygame.draw.rect(screen, green, (randomGraphics[i][0], randomGraphics[i][1], 1, 1))
                        else:
                            pygame.draw.rect(screen, green, (randomGraphics[i][0], randomGraphics[i][1], 2, 2))
                    else:
                        if randomGraphics[i][2] == 1:
                            pygame.draw.rect(screen, green, (randomGraphics[i][0], randomGraphics[i][1], 2, 2))
                        else:
                            pygame.draw.rect(screen, green, (randomGraphics[i][0], randomGraphics[i][1], 1, 1))
            show_text(f"Your score is {score}", 0, 0, white, 25, "freesans")
            show_text("Esc. to quit", 300, 0, white, 25, "Comic Sans")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        right = True
                        left = False
                    if event.key == pygame.K_a:
                        right = False
                        left = True
                    if event.key == pygame.K_w:
                        jump = 0
                        up = True
                        if not gliding:
                            down = False
                    if event.key == pygame.K_s:
                        if y >= floor + 31:
                            y += 30
                        down = True
                        up = False
                        left = False
                        right = False
                        slidetime = time.time()
                    if event.key == pygame.K_F4:
                        if togglehitboxes:
                            togglehitboxes = False
                        else:
                            togglehitboxes = True
                    if event.key == pygame.K_SPACE:
                        pause = True
                    if event.key == pygame.K_ESCAPE:
                        start = False
                    if event.key == pygame.K_g:
                        if toggle_graphics:
                            toggle_graphics = False
                        else:
                            toggle_graphics = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        right = False
                    if event.key == pygame.K_a:
                        left = False
                    if event.key == pygame.K_w:
                        up = False
                    if event.key == pygame.K_s:
                        down = False
                        gliding = False
            walk += 1
            jump += 1
            idle += 1
            slide += 1
            glide += 1
            dead += 1
            if y < floor + floorDifference and not gliding:
                y += 5
            if walk == 9:
                walk = 0
            if dead == 9:
                dead = 0
            if jump == 9:
                jump = 0
            if idle == 9:
                idle = 0
            if slide == 9:
                slide = 0
            if glide == 9:
                glide = 0
            if death:
                # screen.fill(black)
                # screen.blit(bg, (0, 0))
                # screen.blit(deadbush, (50, 450))
                # screen.blit(skeleton, (360, 450))
                # screen.blit(bush, (150, 450))
                # screen.blit(sign, (500, 450))
                # clock.tick(15)
                pygame.display.update()
                while start:
                    show_text("You Died!", 150, 50, red, 100, "freesans")
                    show_text(f"Score: {score}", 270, 170, black, 25, "freesans")
                    quit_button = pygame.draw.rect(screen, grey, (300, 250, 155, 40))
                    show_text("Esc. to quit", 300, 250, white, 25, "Comic Sans")
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                health = max_health
                                zombies = []
                                start = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if quit_button.collidepoint(pygame.mouse.get_pos()):
                                health = max_health
                                zombies = []
                                start = False
                    clock.tick(15)
                    pygame.display.update()
            if y > floor + floorDifference:
                y = floor + floorDifference
            if togglehitboxes:
                playerhitbox = pygame.draw.rect(screen, blue, player, 1)
            else:
                if right or left:
                    playerhitbox = pygame.rect.Rect((x, y, 75, 100))
                elif gliding:
                    playerhitbox = pygame.rect.Rect((x, y, 95, 95))
                elif down:
                    playerhitbox = pygame.rect.Rect((x, y, 80, 80))
                elif up:
                    playerhitbox = pygame.rect.Rect((x, y, 75, 100))
                elif idle:
                    playerhitbox = pygame.rect.Rect((x, y, 48, 96))
            if down:
                if right:
                    side = False
                if left:
                    side = True
                if y >= floor:
                    if time.time() - slidetime < 1.35:
                        if side:
                            player = screen.blit(slideleft[slide], (x, y))
                            if x > 0:
                                x -= 12
                            else:
                                down = False
                        else:
                            player = screen.blit(slideright[slide], (x, y))
                            if x < 675:
                                x += 12
                            else:
                                down = False
                    else:
                        down = False
                    floorDifference = 30
                else:
                    gliding = True
                    if side:
                        player = screen.blit(glideleft[glide], (x, y))
                        if x > 0:
                            x -= 10
                        else:
                            gliding = False
                            down = False
                    else:
                        player = screen.blit(glideright[glide], (x, y))
                        if x < 675:
                            x += 10
                        else:
                            gliding = False
                            down = False
                    y += 1
            elif up:
                y -= 15 - ((time.time() - jumptime) * 10)
                if right:
                    side = False
                    if x < 675:
                        x += 8
                if left:
                    side = True
                    if x > 0:
                        x -= 8
                if y > floor + floorDifference:
                    y = floor + floorDifference
                    jumptime = time.time()
                if side:
                    player = screen.blit(jumpleft[8], (x, y))
                else:
                    player = screen.blit(jumpright[8], (x, y))
                floorDifference = 10
            elif right:
                side = False
                if x < 675:
                    x += 8
                player = screen.blit(walkright[walk], (x, y))
                floorDifference = 7
            elif left:
                side = True
                if x > 0:
                    x -= 8
                player = screen.blit(walkleft[walk], (x, y))
                floorDifference = 7
            else:
                if side:
                    player = screen.blit(idleleft[idle], (x, y))
                else:
                    player = screen.blit(idleright[idle], (x, y))
                floorDifference = 4
            if x > 675:
                x = 11
            elif x < 10:
                x = 675
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False
                    if event.key == pygame.K_ESCAPE:
                        health = max_health
                        zombies = []
                        start = False
            show_text("Paused", 0, 300, grey, 25, "freesans")
            
                          
    pygame.display.update()