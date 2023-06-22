import pygame

pygame.init()

# Defining screen/window:
## Define the size/resolution of our window
res_x, res_y = 1400, 1000
## Create a window and a display surface
screen = pygame.display.set_mode((res_x, res_y))
## Set the pygame window name
pygame.display.set_caption("Main Menu")
## Load background image and re-size it 
BGImg = pygame.transform.scale(pygame.image.load("img/BG1.png"), (res_x, res_y))

# Defining fonts 
font = pygame.font.SysFont("arialblack", 40)

# Define colors
TEXT_COL = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
# Game loop, runs forever
while run:
        
    # Clears the screen with the same backgroung image
    screen.blit(BGImg, (0, 0))

    draw_text ("Press SPACE to pause", font, TEXT_COL, (res_x / 3), (res_y / 2))

    # Process events
    for event in pygame.event.get():
        # Checks if the user closed the window
        if (event.type == pygame.QUIT):
            # Exits the application immediately
            run = False
        #checks user input
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                run = False
        
    # Update screen
    pygame.display.update()
pygame.quit()