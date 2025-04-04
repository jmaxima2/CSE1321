import pygame, sys
from pygame.locals import *
pygame.init()

#creates screen and loads in images
screen = pygame.display.set_mode((1280, 720))
boppi = pygame.image.load("BoppiFront.png").convert_alpha()
boppiRect = pygame.Rect(0,115,44,40)
arrow = pygame.image.load("Arrow for Game.png").convert_alpha()
arrowRect = pygame.Rect(1222.5,315,30,15)
running = True
clock = pygame.time.Clock()

level1Background = pygame.Surface((1280,720))
level1Background.fill((204,255,204))
level1Flag = False

#creates all platforms and flowers
plat1 = pygame.Surface((100, 10))
plat1Rect = pygame.Rect(0,150,100,10)
plat1.fill((0, 51, 0))
plat2 = pygame.Surface((100, 10))
plat2Rect = pygame.Rect(200,250,100,10)
plat2.fill((0, 51, 0))
plat3 = pygame.Surface((100, 10))
plat3Rect = pygame.Rect(60,350,100,10)
plat3.fill((0, 51, 0))
plat4 = pygame.Surface((100, 10))
plat4Rect = pygame.Rect(200,550,100,10)
plat4.fill((0, 51, 0))
plat5 = pygame.Surface((100, 10))
plat5Rect = pygame.Rect(100,70,100,10)
plat5.fill((0, 51, 0))
plat6 = pygame.Surface((100, 10))
plat6Rect = pygame.Rect(350,150,100,10)
plat6.fill((0, 51, 0))
plat7 = pygame.Surface((100, 10))
plat7Rect = pygame.Rect(550,200,100,10)
plat7.fill((0, 51, 0))
plat8 = pygame.Surface((100, 10))
plat8Rect = pygame.Rect(850,175,100,10)
plat8.fill((0, 51, 0))
plat9 = pygame.Surface((100, 10))
plat9Rect = pygame.Rect(1100,70,100,10)
plat9.fill((0, 51, 0))
plat10 = pygame.Surface((100, 10))
plat10Rect = pygame.Rect(700,300,100,10)
plat10.fill((0, 51, 0))
plat11 = pygame.Surface((100, 10))
plat11Rect = pygame.Rect(575,400,100,10)
plat11.fill((0, 51, 0))
plat12 = pygame.Surface((100, 10))
plat12Rect = pygame.Rect(650,600,100,10)
plat12.fill((0, 51, 0))
plat13 = pygame.Surface((100, 10))
plat13Rect = pygame.Rect(1000,600,100,10)
plat13.fill((0, 51, 0))
plat14 = pygame.Surface((100, 10))
plat14Rect = pygame.Rect(1180,350,100,10)
plat14.fill((0, 51, 0))
plat15 = pygame.Surface((40,10))
plat15Rect = pygame.Rect(40,650,40,10)
flower1 = pygame.Surface((10,10))
flower1Rect = pygame.Rect(105,325,10,10)
flower1.fill((255,102,178))
flower2 = pygame.Surface((10,10))
flower2Rect = pygame.Rect(55,625,10,10)
flower2.fill((255,102,178))
flower3 = pygame.Surface((10,10))
flower3Rect = pygame.Rect(145,45,10,10)
flower3.fill((255,102,178))
flower4 = pygame.Surface((10,10))
flower4Rect = pygame.Rect(1145,45,10,10)
flower4.fill((255,102,178))
flower5 = pygame.Surface((10,10))
flower5Rect = pygame.Rect(995,250,10,10)
flower5.fill((255,102,178))
flower6 = pygame.Surface((10,10))
flower6Rect = pygame.Rect(875,525,10,10)
flower6.fill((255,102,178))
ground = pygame.Surface((1280,10))
groundRect = pygame.Rect(0,720,1280,10)
ground.fill((0,0,0))

#creates a list of all platforms as rects to use later
plats = [plat1Rect, plat2Rect, plat3Rect, plat4Rect, plat5Rect, plat6Rect, plat7Rect, plat8Rect, plat9Rect, plat10Rect, plat11Rect, plat12Rect, plat13Rect, plat14Rect, plat15Rect]

#creates a list of all flowers as rects to be used later
flowerRect_list = [flower1Rect, flower2Rect, flower3Rect, flower4Rect, flower5Rect, flower6Rect]

#creates a list of all flowers as surfaces to be used later
flower_list = [flower1, flower2, flower3, flower4, flower5, flower6]

#creates a list of the location of all flowers to be used later
flower_location = [(105,325), (55,625), (145,45), (1145,45), (995,250), (875,525)]

#deals with lives and flowers displays
font = pygame.font.Font(None, 30)
lives = 6
flowers = 6
livesText = font.render(f"Lives left: {lives}", False, (0,0,0))
flowerText = font.render(f"Flowers left: {flowers}", False, (0,0,0))
gameOverText = font.render(f"Game Over", False, (0,0,0))
retryText = font.render("Press S to Retry", False, (0,0,0))
cannotContinueText = font.render("Cannot continue. Collect all of the flowers.", False, (0,0,0))

#sets some constants and variables that will be used later
player_x, player_y = 0, 115
velocity_x, velocity_y = 0, 0
on_ground = False
on_plat = True
GRAVITY = 15
JUMP = 0
SPEED = 7
keys = pygame.key.get_pressed()

def reset_screen(x,y):
    global player_x, player_y
    # sets variables used to keep track of some for loop iterations
    num1 = 0
    num2 = 0
    # loads in all platforms, flowers, boppi, and the background
    screen.blit(level1Background, (0, 0))
    level1Background.blit(plat1, (0, 150))
    level1Background.blit(plat2, (200, 250))
    level1Background.blit(plat3, (60, 350))
    level1Background.blit(plat4, (200, 550))
    level1Background.blit(plat15, (40, 650))
    level1Background.blit(plat5, (100, 70))
    level1Background.blit(plat6, (350, 150))
    level1Background.blit(plat7, (550, 200))
    level1Background.blit(plat8, (850, 175))
    level1Background.blit(plat9, (1100, 70))
    level1Background.blit(plat10, (700, 300))
    level1Background.blit(plat11, (575, 400))
    level1Background.blit(plat12, (650, 600))
    level1Background.blit(plat13, (1000, 600))
    level1Background.blit(plat14, (1180, 350))
    level1Background.blit(arrow, (1222.5, 315))
    level1Background.blit(ground, (0, 720))
    level1Background.blit(livesText, (1120, 680))
    level1Background.blit(flowerText, (1120, 700))
    for flower in flower_list:
        level1Background.blit(flower, flower_location[num1])
        num1 = num1 + 1
    level1Background.blit(boppi, (player_x, player_y))
    pygame.display.flip()
# checks to see if player is on a platform or not
def check_on_plat(x,y):
    global velocity_y, on_plat
    if plat1Rect.collidepoint(player_x, player_y + 36) == True or plat2Rect.collidepoint(player_x, player_y + 36) == True or plat3Rect.collidepoint(player_x, player_y + 36) == True or plat4Rect.collidepoint(player_x, player_y + 36) == True or plat5Rect.collidepoint(player_x, player_y + 36) == True or plat6Rect.collidepoint(player_x, player_y + 36) == True or plat7Rect.collidepoint(player_x, player_y + 36) == True or plat8Rect.collidepoint(player_x, player_y + 36) == True or plat9Rect.collidepoint(player_x, player_y + 36) == True or plat10Rect.collidepoint(player_x, player_y + 36) == True or plat11Rect.collidepoint(player_x, player_y + 36) == True or plat12Rect.collidepoint(player_x, player_y + 36) == True or plat13Rect.collidepoint(player_x, player_y + 36) == True or plat14Rect.collidepoint(player_x, player_y + 36) == True or plat15Rect.collidepoint(player_x, player_y + 36) == True:
        on_plat = True
    else:
        on_plat = False
    return on_plat

def handle_movement(keys):
    global velocity_x, velocity_y, on_plat, JUMP, GRAVITY
    velocity_x = 0  # Reset horizontal velocity
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Move left
        velocity_x = -SPEED
        JUMP = 0
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Move right
        velocity_x = SPEED
        JUMP = 0
    if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and on_plat:  # Jump
        JUMP = 1
        on_plat = False



while running:
    GRAVITY = 15
    JUMP = 0
    reset_screen(player_x, player_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Handle movement
    keys = pygame.key.get_pressed()
    handle_movement(keys)
    if check_on_plat(player_x,player_y) == True:
        GRAVITY = 0
        if JUMP == 0:
            GRAVITY = GRAVITY
            velocity_y = GRAVITY
            player_y += velocity_y
            player_x += velocity_x
            reset_screen(player_x, player_y)
        elif JUMP == 1:
            for x in range(80):
                GRAVITY = -80 + 1
            velocity_y = GRAVITY
            player_y += velocity_y
            player_x += velocity_x
            reset_screen(player_x, player_y)
    elif check_on_plat(player_x,player_y) == False:
        # Apply gravity
        if JUMP == 0:
            GRAVITY = GRAVITY
            velocity_y = GRAVITY
            player_y += velocity_y
            player_x += velocity_x
            reset_screen(player_x,player_y)
        elif JUMP == 1:
            for x in range (80):
                GRAVITY = -80 + 1
            velocity_y = GRAVITY
            player_y += velocity_y
            player_x += velocity_x
            reset_screen(player_x,player_y)
    clock.tick(30)  # 60 FPS








