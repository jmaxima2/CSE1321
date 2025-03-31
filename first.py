import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FONT = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Health System Example")

player_health = 100

def take_damage(amount):
    global player_health
    player_health -= amount
    if player_health <= 0:
        game_over()

def game_over():
    print("Game Over! You have lost all your health.")
    pygame.quit()
    exit()

def draw_health():
    health_text = FONT.render(f"Health: {player_health}", True, RED)
    screen.blit(health_text, (10, 10))

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # Simulate damage when 'D' is pressed
                take_damage(10)
    
    draw_health()
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
