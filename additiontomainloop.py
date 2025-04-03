import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAVITY = 0.8
JUMP_STRENGTH = -15
SPEED = 7

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boppi's Adventure")

# Load Boppi's sprite
boppi = pygame.image.load("BoppiFront.png").convert_alpha()
boppi = pygame.transform.scale(boppi, (50, 70))  # Resize Boppi

# Player properties
player_health = 100  # Using same health variable as first.py
player_x, player_y = WIDTH // 2, HEIGHT - 100
velocity_x, velocity_y = 0, 0
on_ground = False

def take_damage(amount):
    """Reduce player's health when taking damage."""
    global player_health
    player_health -= amount
    if player_health <= 0:
        game_over()

def game_over():
    """End game when player health reaches zero."""
    print("Game Over! You have lost all your health.")
    pygame.quit()
    exit()

def handle_movement(keys):
    """Handle left, right movement and jumping."""
    global velocity_x, velocity_y, on_ground

    velocity_x = 0  # Reset horizontal velocity

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Move left
        velocity_x = -SPEED
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Move right
        velocity_x = SPEED
    if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and on_ground:  # Jump
        velocity_y = JUMP_STRENGTH
        on_ground = False

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle movement
    keys = pygame.key.get_pressed()
    handle_movement(keys)

    # Apply gravity
    velocity_y += GRAVITY
    player_y += velocity_y

    # Simulate ground collision
    if player_y >= HEIGHT - 100:
        player_y = HEIGHT - 100
        velocity_y = 0
        on_ground = True

    # Keep Boppi within screen bounds
    player_x = max(0, min(WIDTH - 50, player_x))  # Prevent going off-screen

    # Update position
    player_x += velocity_x

    # Draw player
    screen.blit(boppi, (player_x, player_y))

    # Draw health
    font = pygame.font.Font(None, 36)
    health_text = font.render(f"Health: {player_health}", True, RED)
    screen.blit(health_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
