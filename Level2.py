import pygame, sys
from pygame.locals import *
pygame.init()

# Setup screen
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Load images
boppi = pygame.image.load("BoppiFront2.png").convert_alpha()
arrow = pygame.image.load("Arrow for Game.png").convert_alpha()

#Position first
boppiRect = pygame.Rect(0, 0, 45, 68)

# Background - with waterfall area marked
level2Background = pygame.Surface((1280, 720))
level2Background.fill((204, 255, 204))
# waterfall 
pygame.draw.rect(level2Background, (100, 150, 255), (400, 0, 480, 720))

# Waterfall platforms (in center)
waterfall_platRects = [
    pygame.Rect(450, 50, 100, 20),
    pygame.Rect(550, 200, 100, 20),
    pygame.Rect(650, 350, 100, 20),
    pygame.Rect(450, 500, 100, 20),
    pygame.Rect(550, 650, 100, 20),
]

#  left side
left_platRects = [
    pygame.Rect(100, 100, 200, 20),
    pygame.Rect(50, 300, 200, 20),
    pygame.Rect(150, 500, 200, 20),
]

# on right side
right_platRects = [
    pygame.Rect(980, 150, 200, 20),
    pygame.Rect(1030, 350, 200, 20),
    pygame.Rect(930, 550, 200, 20),
]

# Combine all platforms for collision detection
all_platRects = left_platRects + waterfall_platRects + right_platRects

# Original waterfall 
original_waterfall_positions = [rect.y for rect in waterfall_platRects]

# Exit Arrow
arrowRect = pygame.Rect(1080, 315, 30, 15)

# Flowers
flowerRect_list = [
    pygame.Rect(150, 75, 10, 10),    # Left side
    pygame.Rect(500, 25, 10, 10),    # Waterfall
    pygame.Rect(1050, 125, 10, 10),  # Right side
    pygame.Rect(600, 325, 10, 10),    # Waterfall
    pygame.Rect(200, 475, 10, 10),    # Left side
    pygame.Rect(1000, 525, 10, 10),   # Right side
]

# Ground 
ground = pygame.Rect(0, 720, 1280, 10)

# Fonts and text
font = pygame.font.Font(None, 30)
lives = 6
flowers = 6
cannotContinueText = font.render("Cannot continue. Collect all of the flowers.", False, (0,0,0))
waterfallWarningText = font.render("You can't fall or hit the bottom in the waterfall!", False, (255,255,255))
mistWarningText = font.render("The mist pushes you up if you try to advance!", False, (255,255,255))

# Movement vars
velocity_x = 0
velocity_y = 0
on_plat = False
SPEED = 8
JUMP_FORCE = -15
GRAVITY = 1
WATERFALL_SPEED = 2  # How fast waterfall platforms move down
MIST_FORCE = -5      # Upward force when trying to advance without flowers

#starting point
boppiRect.midbottom = left_platRects[0].midtop

running = True
GameOverFlag = False
level3Flag = False
show_warning = False
warning_timer = 0
show_mist_warning = False
mist_timer = 0

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Input
    keys = pygame.key.get_pressed()
    velocity_x = 0
    if keys[K_a] or keys[K_LEFT]:
        velocity_x = -SPEED
    if keys[K_d] or keys[K_RIGHT]:
        velocity_x = SPEED
    if (keys[K_SPACE] or keys[K_UP]) and on_plat:
        velocity_y = JUMP_FORCE
        on_plat = False

    # Apply gravity
    velocity_y += GRAVITY
    if velocity_y > 20:
        velocity_y = 20

    # Downwards only
    for plat in waterfall_platRects:
        plat.y += WATERFALL_SPEED
        # Reset platform to top when it goes off screen
        if plat.top > 720:
            plat.y = -plat.height

    # Flower movement - only waterfall flowers move
    for i, flower in enumerate(flowerRect_list):
        # Check if flower is in waterfall area (x between 400-880)
        if 400 <= flower.x <= 880:
            for plat in waterfall_platRects:
                if abs(flower.x - plat.centerx) < 60:  # Rough association
                    flower.y = plat.y - 15  # Keep above platform
                    break

    # Horizontal movement
    boppiRect.x += velocity_x
    for plat in all_platRects:
        if boppiRect.colliderect(plat):
            if velocity_x > 0:
                boppiRect.right = plat.left
            elif velocity_x < 0:
                boppiRect.left = plat.right

    # Keep inside screen horizontally
    if boppiRect.left < 0:
        boppiRect.left = 0
    if boppiRect.right > 1280:
        boppiRect.right = 1280

    # Prevent going above screen
    if boppiRect.top < 0:
        boppiRect.top = 0
        velocity_y = 0

    # Vertical movement
    boppiRect.y += velocity_y
    on_plat = False
    for plat in all_platRects:
        if boppiRect.colliderect(plat):
            if velocity_y > 0:
                boppiRect.bottom = plat.top
                velocity_y = 0
                on_plat = True
            elif velocity_y < 0:
                boppiRect.top = plat.bottom
                velocity_y = 0

    # Check if player falls below screen (waterfall bottom)
    if boppiRect.top > 720:
        lives -= 1
        if lives <= 0:
            pygame.quit()
            sys.exit()
        # Reset position to starting platform
        boppiRect.midbottom = left_platRects[0].midtop
        # Reset waterfall platforms to original positions
        for i, plat in enumerate(waterfall_platRects):
            plat.y = original_waterfall_positions[i]
        # Show warning message
        show_warning = True
        warning_timer = 180  # 3 seconds at 60fps

    # Flower collection
    for flower in flowerRect_list[:]:  # Make a copy for iteration
        if boppiRect.colliderect(flower):
            flowers -= 1
            flowerRect_list.remove(flower)
            pygame.display.flip()

    # Check for level completion (arrow on right side)
    if boppiRect.colliderect(arrowRect):
        if flowers == 0:
            level3Flag = True
            running = False
        else:
            # Apply mist force (push player up)
            velocity_y = MIST_FORCE
            # Show mist warning
            show_mist_warning = True
            mist_timer = 120  # 2 seconds

    # Warning message timers
    if show_warning:
        warning_timer -= 1
        if warning_timer <= 0:
            show_warning = False
            
    if show_mist_warning:
        mist_timer -= 1
        if mist_timer <= 0:
            show_mist_warning = False

    #  everything
    screen.blit(level2Background, (0, 0))

    #  left platforms (green)
    for plat in left_platRects:
        pygame.draw.rect(screen, (0, 100, 0), plat)

    #  waterfall platforms (blue)
    for plat in waterfall_platRects:
        pygame.draw.rect(screen, (0, 100, 200), plat)

    #  right platforms (green)
    for plat in right_platRects:
        pygame.draw.rect(screen, (0, 100, 0), plat)

    #  flowers
    for flower in flowerRect_list:
        pygame.draw.rect(screen, (255, 102, 178), flower)

    screen.blit(arrow, arrowRect.topleft)

    #  Boppi
    screen.blit(boppi, boppiRect.topleft)

    #  text
    screen.blit(font.render(f"Lives: {lives}", True, (0, 0, 0)), (1120, 680))
    screen.blit(font.render(f"Flowers: {flowers}", True, (0, 0, 0)), (1120, 700))

    # Show warnings if needed
    if show_warning:
        screen.blit(waterfallWarningText, (400, 350))
    if show_mist_warning:
        screen.blit(mistWarningText, (400, 400))

    pygame.display.flip()
