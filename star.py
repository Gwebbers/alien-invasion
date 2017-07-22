import pygame
from pygame.sprite import Sprite
import random


class Star(Sprite):
    """A star in the sky"""

    def __init__(self, tou_settings, screen):
        """Create the star"""
        super(Star, self).__init__()
        self.tou_settings = tou_settings
        self.screen = screen

        # load the star image
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # Finds the screen height and width
        self.screen_width = self.tou_settings.screen_width
        self.screen_height = self.tou_settings.screen_height

        # Randomly generates star positions
        star_x = random.randint(0, self.screen_width)
        star_y = random.randint(0, self.screen_height)

        # Creates the star based on the random positions
        self.rect.x = star_x
        self.rect.y = star_y

    def blitme(self):
        """Draw the star to its location"""
        self.screen.blit(self.image, self.rect)
