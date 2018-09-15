import pygame

class Ship():

    def __init__(self, screen):
        """Initialize ship and set starting position"""
        self.screen = screen

        # Load ship and rectangle attributes
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start ship position at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Initialize movement flag to false
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update ship's position based on movement flags"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw ship using bit-boundary block transfer (blit)"""
        self.screen.blit(self.image, self.rect)
