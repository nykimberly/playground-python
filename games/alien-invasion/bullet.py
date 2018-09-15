import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage bullets fired from ship"""

    def __init__(self, settings, screen, ship):
        """Initialize bullet at ship position"""
        super().__init__()
        self.screen = screen

        # Build bullet with pygame's Rect class
        self.rect = pygame.Rect(0, 0, 
                    settings.bullet_width, settings.bullet_height)

        # Position it at top of ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Give it a float y position value
        self.y = float(self.rect.y)

        # Assign qualities
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
        
    def update(self):
        """Move bullet up screen"""
        self.y -= 1 * self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Pass pygame.draw our rect object, its color, and canvas"""
        pygame.draw.rect(self.screen, self.color, self.rect)
