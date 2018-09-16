import sys
import pygame
from classes.bullet import Bullet
from classes.alien import Alien

def check_events(screen, settings, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit() 
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < settings.screen_bullet_limit:
            fire_bullets(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship, bullets, alien):
    """Keep display upto date"""
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Draw each alien of group to screen
    alien.draw(screen)
    ship.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(settings, screen, ship, bullets):
    new_bullet = Bullet(settings, screen, ship)
    bullets.add(new_bullet)

def create_fleet(settings, screen, aliens):
    """Create a fleet of aliens"""
    # Instantiate alien
    alien = Alien(settings, screen)
    # Define attributes
    alien_width = alien.rect.width
    # Calculate number of aliens that can fit on screen
    available_space_x = settings.screen_w - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    # Create a row of aliens
    for alien_number in range(number_aliens_x):
        alien = Alien(settings, screen)
        # Use alien_number in position calculation
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

