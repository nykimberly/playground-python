import sys
import pygame

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 

def update_screen(settings, screen, ship):
    """Keep display upto date"""
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()
