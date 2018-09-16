import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent alient on fleet"""
    
    def __init__(self, settings, screen):
        """Initialize alien"""
        super().__init__()
        self.screen = screen
        self.settings = settings
        # Load alien image and set its rect
        self.image = pygame.image.load('assets/alien.bmp')
        self.rect = self.image.get_rect()
        # Start each new alien at top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien at its current location"""
        self.screen.blit(self.image, self.rect)
