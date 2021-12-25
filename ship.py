import pygame

class Ship():

    def __init__(self,ai_settings ,screen):
        """Initialize Ship and set its starting position"""

        self.screen = screen
        self.ai_settings = ai_settings


        #Load in the ship image and get its rect.
        self.image = pygame.image.load('/home/aaronhasbrouck/Documents/AlienGame/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store Decimal for ships center/position
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #Movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update Ship Position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor


        #Update rect oject from self.center
        self.rect.centerx = self.centerx


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)