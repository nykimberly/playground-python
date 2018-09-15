import pygame
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    # Initialize background settings for pygame functionality
    pygame.init()

    # Initialize settings object
    settings = Settings()

    # Initialize screen object of 1200x800 and add caption
    screen = pygame.display.set_mode((settings.screen_w, settings.screen_h))
    pygame.display.set_caption("Alien Invasion")
    
    # Initialize ship
    ship = Ship(screen, settings)

    # Main loop for game
    # Surfaces are redrawn on every pass of our loop
    while True:

        # Check for events
        gf.check_events(ship)

        # Update ship
        ship.update(settings)

        # Flip to new screen, ship position, etc.
        gf.update_screen(settings, screen, ship)

# call program
run_game()
