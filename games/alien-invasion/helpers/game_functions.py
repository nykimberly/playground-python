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

def update_bullets(aliens, bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Get rid of both alien and bullet in case of collision
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def fire_bullets(settings, screen, ship, bullets):
    new_bullet = Bullet(settings, screen, ship)
    bullets.add(new_bullet)

def get_number_aliens_x(settings, alien_w):
    """Determine number of aliens that can fit in row"""
    # Calculate number of aliens that can fit on screen
    available_space_x = settings.screen_w - 2 * alien_w
    number_aliens_x = int(available_space_x / (2 * alien_w))
    return number_aliens_x

def get_number_rows(settings, ship_h, alien_h):
    """Determine number of rows that can fit on screen"""
    available_space_y = settings.screen_h - 3 * alien_h - ship_h
    number_rows = int(available_space_y / (2 * alien_h))
    return number_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    """Instantiate an alien and place it in row"""
    alien = Alien(settings, screen)
    # Define attributes
    alien_w = alien.rect.width
    # Use alien_number in position calculation
    alien.x = alien_w + 2 * alien_w * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(settings, screen, ship, aliens):
    """Create a fleet of aliens"""
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)
    # Create fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)

def update_aliens(settings, aliens):
    check_fleet_edges(settings, aliens)
    aliens.update()

def check_fleet_edges(settings, aliens):
    """Drop fleet when fleet hits edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    """Reverse fleet direction and drop fleet"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1
