import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship)

def check_keydown_events(ship):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship):
    """Keep display upto date"""
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()
