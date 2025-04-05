import pygame, sys
from pygame.locals import *
pygame.init()

# Setup screen
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Load images
boppi = pygame.image.load("BoppiFront2.png").convert_alpha()
arrow = pygame.image.load("Arrow for Game.png").convert_alpha()

# Setup initial position
boppiRect = pygame.Rect(0, 0, 44, 40)

# Background
level1Background = pygame.Surface((1280, 720))
level1Background.fill((204, 255, 204))

# Platforms
platRects = [
    pygame.Rect(-2, 150, 102, 10),
    pygame.Rect(198, 250, 102, 10),
    pygame.Rect(58, 350, 102, 10),
    pygame.Rect(198, 550, 102, 10),
    pygame.Rect(98, 70, 102, 10),
    pygame.Rect(348, 150, 102, 10),
    pygame.Rect(548, 200, 102, 10),
    pygame.Rect(848, 175, 102, 10),
    pygame.Rect(1098, 70, 102, 10),
    pygame.Rect(698, 300, 102, 10),
    pygame.Rect(573, 400, 102, 10),
    pygame.Rect(648, 600, 102, 10),
    pygame.Rect(998, 600, 102, 10),
    pygame.Rect(1178, 350, 102, 10),
    pygame.Rect(38, 650, 42, 10),
]

# Flowers
flowerRect_list = [
    pygame.Rect(105, 325, 10, 10),
    pygame.Rect(55, 625, 10, 10),
    pygame.Rect(145, 45, 10, 10),
    pygame.Rect(1145, 45, 10, 10),
    pygame.Rect(995, 250, 10, 10),
    pygame.Rect(875, 525, 10, 10),
]

# Ground
ground = pygame.Rect(0, 710, 1280, 10)

# Fonts and text
font = pygame.font.Font(None, 30)
lives = 6
flowers = 6

# Movement vars
velocity_x = 0
velocity_y = 0
on_plat = False
SPEED = 8
JUMP_FORCE = -15
GRAVITY = 1

# Start boppi on first platform
boppiRect.y = platRects[0].top - boppiRect.height

running = True
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

        # Horizontal movement
    boppiRect.x += velocity_x
    for plat in platRects:
        if boppiRect.colliderect(plat):
            if velocity_x > 0:
                boppiRect.right = plat.left
            elif velocity_x < 0:
                boppiRect.left = plat.right

    #keeping inside:

        if boppiRect.left < 0:
            boppiRect.left = 0
    if boppiRect.right > 1280:
        boppiRect.right = 1280

    # Prevent going off-screen vertically
    if boppiRect.top < 0:
        boppiRect.top = 0
    if boppiRect.bottom > ground.top:
        boppiRect.bottom = ground.top
        velocity_y = 0
        on_plat = True

    # Vertical movement
    boppiRect.y += velocity_y
    on_plat = False
    for plat in platRects:
        if boppiRect.colliderect(plat):
            if velocity_y > 0:
                boppiRect.bottom = plat.top
                velocity_y = 0
                on_plat = True
            elif velocity_y < 0:
                boppiRect.top = plat.bottom
                velocity_y = 0

    # Ground collision
    if boppiRect.bottom >= ground.top:
        boppiRect.bottom = ground.top
        velocity_y = 0
        on_plat = True

    # Top screen limit
    if boppiRect.top < 0:
        boppiRect.top = 0

    # Draw everything
    screen.blit(level1Background, (0, 0))

    # Draw platforms
    for plat in platRects:
        pygame.draw.rect(screen, (0, 51, 0), plat)

    # Draw flowers
    for flower in flowerRect_list:
        pygame.draw.rect(screen, (255, 102, 178), flower)

    # Draw ground
    pygame.draw.rect(screen, (0, 0, 0), ground)

    # Draw Boppi
    screen.blit(boppi, boppiRect.topleft)

    # Optional: draw blue outline to debug Boppi hitbox
    # pygame.draw.rect(screen, (0, 0, 255), boppiRect, 2)

    # Draw text
    screen.blit(font.render(f"Lives: {lives}", True, (0, 0, 0)), (1120, 680))
    screen.blit(font.render(f"Flowers: {flowers}", True, (0, 0, 0)), (1120, 700))

    pygame.display.flip()
