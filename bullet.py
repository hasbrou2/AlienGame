import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manages Bullets fired from ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullter object at the ship's current position"""
        super().__init__()
        self.screen = screen

        #Create a bullet rect at (0,0) and the set correct position.
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store bullet position as a decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move bullet up screen"""
        #Update bullet decimal position
        self.y -= self.speed_factor
        #update rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)