import sys # to exit game when player decides to quit
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # Initialize background settings for pygame functionality
    pygame.init()

    # Initialize settings object
    ainvasion_settings = Settings()

    # Initialize screen object of 1200x800
    # These objects are called 'surfaces'
    screen = pygame.display.set_mode(
        (ainvasion_settings.screen_width, ainvasion_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Initialize ship
    ship = Ship(screen)

    # Main loop for game
    # Surfaces are redrawn on every pass of our loop
    while True:

        # event loop to listen for and respond to events
        for event in pygame.event.get():
            # pygame.QUIT is the exit button on our window
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Maintain background color
        screen.fill(ainvasion_settings.bg_color)
        
        # Update position of ship
        ship.blitme()

        # Keep display up to date; draws empty screen to hide old 
        # and redraws the new display
        pygame.display.flip()

# call program
run_game()
