import pygame
import buttons

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

# Game variables
game_paused = True
menu_state = "main"

# Defining fonts 
font = pygame.font.SysFont("arialblack", 40)

# Define colors
TEXT_COL = (0, 0, 0)

# Load button images
resume_img = pygame.image.load("img/PlayButton.png").convert_alpha()
options_img = pygame.image.load("img/OptionsButton.png").convert_alpha()
quit_img = pygame.image.load("img/QuitButton.png").convert_alpha()
audio_img = pygame.image.load('img/AudioButton.png').convert_alpha()
ctrl_img = pygame.image.load('img/ControlsButton.png').convert_alpha()
back_img = pygame.image.load('img/BackButton.png').convert_alpha()

# Create button instances
resume_button = buttons.Button(res_x / 2.5, (res_y / 2) - 150 , resume_img, 0.5)
options_button = buttons.Button(res_x / 2.5, res_y / 2, options_img, 0.5)
quit_button = buttons.Button(res_x / 2.5, (res_y / 2) + 150, quit_img, 0.5)
ctrl_button = buttons.Button(res_x / 2.5, (res_y / 2) - 150, ctrl_img, 0.5)
audio_button = buttons.Button(res_x / 2.5, (res_y / 2), audio_img, 0.5)
back_button = buttons.Button(res_x / 2.5, (res_y / 2) + 150, back_img, 0.5)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
# Game loop, runs forever
while run:
        
    # Clears the screen with the same backgroung image
    screen.blit(BGImg, (0, 0))

    # Check if the game is paused
    if(game_paused):
        # Check menu state
        if menu_state == "main":
            # Draw pause screen buttons only
            draw_text ("PAUSED", font, TEXT_COL, (res_x / 2) - 75, 200)
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                pygame.quit()

        # Check if the options menu is open 
        if menu_state == "options":
            # Draw options screen buttons only
            draw_text ("OPTIONS", font, TEXT_COL, (res_x / 2) - 75, 200)
            if ctrl_button.draw(screen):
                menu_state = "controls"
            if options_button.draw(screen):
                menu_state = "options"
            if back_button.draw(screen):
                menu_state = "main"
                
        # Check if the controls menu is open 
        if menu_state == "controls":
            # Draw controls screen buttons only
            ## Show the "How to play" controls
            draw_text ("CONTROLS", font, TEXT_COL, (res_x / 2) - 75, 200)
            draw_text ("Use the RIGHT and LEFT arrow keys to move.", font, TEXT_COL, 300, 300)
            draw_text ("Use the UP arrow keys to move.", font, TEXT_COL, 300, 400)
            draw_text ("Survive for as long as you can!", font, TEXT_COL, 300, 500)
            if back_button.draw(screen):
                menu_state = "options"

    else:
        draw_text ("Press SPACE to pause", font, TEXT_COL, (res_x / 3), (res_y / 2))

    # Process events
    for event in pygame.event.get():
        # Checks if the user closed the window
        if (event.type == pygame.QUIT):
            # Exits the application immediately
            run = False
        # Checks user input
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                run = False
            if (event.key == pygame.K_SPACE):
                game_paused = True
        
    # Update screen
    pygame.display.update()
pygame.quit()