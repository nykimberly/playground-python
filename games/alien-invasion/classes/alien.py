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

    def update(self):
        """Shimmy the aliens"""
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return true of alien hits edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def blitme(self):
        """Draw alien at its current location"""
        self.screen.blit(self.image, self.rect)
