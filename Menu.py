import pygame
import buttons
import time

pygame.font.init()

game_volume = 0.1

def show_menu(screen, res_x, res_y, score):
    # Game variables
    game_paused = True
    menu_state = "main"
    global game_volume
    # Defining screen/window:
    # Load background image and re-size it
    BGImg = pygame.transform.scale(pygame.image.load("img/BG1.png"), (res_x, res_y))

    # Define colors
    TEXT_COL = (0, 0, 0)

    # Define fonts
    font = pygame.font.SysFont("arialblack", 50)
    # Define the font for the score display
    score_font = pygame.font.SysFont("arialblack", 30)
    
    # Load background sound
    pygame.mixer.music.load("sounds/background.wav")
    # -1 indicates the music should loop indefinitely
    pygame.mixer.music.play(-1)  
    # Set volume
    pygame.mixer.music.set_volume(game_volume)

    # Load button images
    resume_img = pygame.image.load("img/PlayButton.png").convert_alpha()
    options_img = pygame.image.load("img/OptionsButton.png").convert_alpha()
    quit_img = pygame.image.load("img/QuitButton.png").convert_alpha()
    audio_img = pygame.image.load('img/AudioButton.png').convert_alpha()
    muteAudio_img = pygame.image.load('img/MuteAudioButton.png').convert_alpha()
    ctrl_img = pygame.image.load('img/ControlsButton.png').convert_alpha()
    back_img = pygame.image.load('img/BackButton.png').convert_alpha()
    

    # Create button instances
    resume_button = buttons.Button(res_x / 2.5, (res_y / 2) - 150, resume_img, 0.5)
    options_button = buttons.Button(res_x / 2.5, res_y / 2, options_img, 0.5)
    quit_button = buttons.Button(res_x / 2.5, (res_y / 2) + 150, quit_img, 0.5)
    ctrl_button = buttons.Button(res_x / 2.5, (res_y / 2) - 150, ctrl_img, 0.5)
    audio_button = buttons.Button(res_x / 2.5, (res_y / 2) + 50, audio_img, 0.5)
    muteAudio_button = buttons.Button(res_x / 2.5 + 200, (res_y / 2) + 50, muteAudio_img, 0.5)
    back_button = buttons.Button(res_x / 2.5, (res_y / 2) + 250, back_img, 0.5)

    

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    # Function to draw the score on the screen
    def draw_score(highScore, font, text_col, x, y):
        highScore = score
        score_text = font.render(f"High Score: {round(highScore)}s", True, text_col)
        screen.blit(score_text, (x, y))

    run = True
    # Game loop, runs forever
    while run:
        # Clears the screen with the same background image
        screen.blit(BGImg, (0, 0))
        # Check if the game is paused
        if game_paused:
            # Check menu state
            if menu_state == "main":
                # Draw pause screen buttons only
                draw_text("Cannon Dodge!!", font, TEXT_COL, (res_x / 2) - 200, 200)
                # Draw the updated score on the screen
                draw_score(score, score_font, TEXT_COL, res_x / 2 - 100, res_y / 2 + 300)
                if resume_button.draw(screen):
                    game_paused = False
                    return "Play"
                if options_button.draw(screen):
                    menu_state = "options"
                if quit_button.draw(screen):
                    run = False

            # Check if the options menu is open
            if menu_state == "options":
                # Draw options screen buttons only
                draw_text("OPTIONS", font, TEXT_COL, (res_x / 2) - 110, 200)
                if ctrl_button.draw(screen):
                    menu_state = "controls"
                if muteAudio_button.draw(screen):
                    print("Mute")
                    game_volume == 0
                if audio_button.draw(screen):
                    print("Unmute")
                    game_volume += 0.5
                if back_button.draw(screen):
                    menu_state = "main"

            # Check if the controls menu is open
            if menu_state == "controls":
                # Draw controls screen buttons only
                ## Show the "How to play" controls
                draw_text("CONTROLS:", font, TEXT_COL, (res_x / 2) - 110, 200)
                draw_text("Use the < and > arrow keys to Move.", font, TEXT_COL, 200, 300)
                draw_text("Use the ^ arrow key to Jump.", font, TEXT_COL, 200, 400)
                draw_text("´P´to open the Pause menu.", font, TEXT_COL, 200, 500)
                draw_text("Survive for as long as you can!", font, TEXT_COL, 200, 600)
                if back_button.draw(screen):
                    menu_state = "options"

        else:
            draw_text("Press SPACE to pause", font, TEXT_COL, (res_x / 3), (res_y / 2))

        # Process events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if event.type == pygame.QUIT:
                # Exits the application immediately
                run = False
            # Checks user input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    game_paused = True

        # Update screen
        pygame.display.update()

    pygame.quit()