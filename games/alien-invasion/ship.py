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

    def blitme(self):
        """Draw ship using bit-boundary block transfer (blit)"""
        self.screen.blit(self.image, self.rect)
