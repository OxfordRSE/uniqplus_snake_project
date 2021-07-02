import pygame

pygame.init()

# Create screen
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Define colours in red-green-blue form
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Run game loop
game_over=False
while not game_over:
    for event in pygame.event.get():
        print("event = ", event)
        if event.type==pygame.QUIT:
            game_over=True
    
    # Draw black canvas
    screen.fill(BLACK)
    # Draw rectangle
    size = 20
    pygame.draw.rect(
            screen, WHITE,
      			[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20, 20]
        )
    
    # Draw text
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render("UNIQ+ rocks!", True, WHITE)
    screen.blit(mesg, [SCREEN_WIDTH // 2, 0])
    
    # Update display
    pygame.display.update()

pygame.quit()