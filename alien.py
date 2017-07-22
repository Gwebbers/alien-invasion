import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent an alien"""

    def __init__(self, tou_settings, screen):
        """Initialize the alien and starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.tou_settings = tou_settings

        # Load the alien image and its rect value
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien right or left"""
        self.x += (self.tou_settings.fleet_direction * self.tou_settings.alien_speed_factor)
        self.rect.x = self.x

    def check_edge(self):
        """Returns True if an alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)


# Most of this class is like the ship class except for the placement of the alien.  We initially place each alien in
# the top-left corner of the screen, adding a space to the left of it that's equal to the alien's width and a space
# above it equal to its height.

# Now lets go to the main code to make our game create these bad boys.

# Each time we update an alien's position, we move it to the right by the amount stored in alien_speed_factor.  We
# track the alien's exact position with the self.x attribute, which can hold decimals.  We then use self.x to position
# the alien's self.rect.x

# Now in the main while loop we need to call our alien's positions after the bullets have been updated, because soon
# we'll also check to see if the bullets are hitting any aliens.

# Let's add a new function to game_functions that will update our aliens.

# We need to add a function to check for edges.

# We can call the new method check_edges() on any alien to see if it's at the left or right edge.  The alien is at the
# right edge if the right attribute of the rect is greater than or equal to the right rect attribute of the screen's
# rect.  It's at the left edge if the left attribute is less than or equal to 0

# We modify the update() method to allow motion to the left or right by multiplying the alien's speed factor by the
# fleet's direction.  Moving right if it's equal to 1 or left if it's equal to -1.
