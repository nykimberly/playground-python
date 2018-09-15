import pygame

class Ship():

    def __init__(self, screen, settings):
        """Initialize ship and set starting position"""
        self.screen = screen
        # Load ship and rectangle attributes
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start ship position at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Store position values as float and initialize
        self.center = float(self.rect.centerx)
        # Initialize movement flag to false
        self.moving_right = False
        self.moving_left = False
        # Set ship speed
        self.settings = settings
    
    def update(self, settings):
        """Update ship's position based on movement flags"""
        if self.moving_right:
            self.center += 1 * self.settings.ship_speed_factor
        if self.moving_left:
            self.center -= 1 * self.settings.ship_speed_factor
        # Adjust rect center to self center result
        self.rect.centerx = self.center

    def blitme(self):
        """Draw ship using bit-boundary block transfer (blit)"""
        self.screen.blit(self.image, self.rect)
