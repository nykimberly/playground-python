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

def get_number_aliens_x(settings, alien_w):
    """Determine number of aliens that can fit in row"""
    # Calculate number of aliens that can fit on screen
    available_space_x = settings.screen_w - 2 * alien_w
    number_aliens_x = int(available_space_x / (2 * alien_w))
    return number_aliens_x

def create_alien(settings, screen, aliens, alien_number):
    """Instantiate an alien and place it in row"""
    alien = Alien(settings, screen)
    # Define attributes
    alien_w = alien.rect.width
    # Use alien_number in position calculation
    alien.x = alien_w + 2 * alien_w * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(settings, screen, aliens):
    """Create a fleet of aliens"""
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    # Create a row of aliens
    for alien_number in range(number_aliens_x):
        create_alien(settings, screen, aliens, alien_number)
