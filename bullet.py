import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, tou_settings, screen, ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet rect at (0, 0) and then set the correct positioning
        self.rect = pygame.Rect(0, 0, tou_settings.bullet_width, tou_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = tou_settings.bullet_color
        self.speed_factor = tou_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

# The Bullet class inherits from Sprite, which we import from the pygame.sprite module.  When you use sprites, you can
# group related elements in your game and act on all the grouped elements as one.  To create a bullet instance,
# __init__() needs the tou_settings, screen and ship instances.  And we call super() to inherit properties from Sprite.

# On line 13 we create the bullet's rect attribute.  The bullet is not based on an image so we have to build a rect
# from scratch using the pygame.Rect() class.  This class requires the x- and y-coordinates of the top-left corner of
# the rect, and the width and height of the rect.  We initialize the rect at (0, 0), but we'll move it to the current
# in the next two lines, where we set its location to the location of our ship using the centerx and top locations.
# We get the width and height of our bullet from tou_settings.

# On the following line we set the bullet's centerx to be the same as the ship's rect.centerx.  Centering the bullet on
# the ship. Then we set the top of the bullet's rect to the top of the ship's rect, making it look like it's firing out.

# We store a decimal value for the bullet's y-coordinate so we can make fine tune adjustments to the bullet's speed.
# (At self.y = float(self.rect.y)).  Then we store the bullet's color and speed settings in self.color and
# self.speed_factor

# The update() method manages the bullet's position.  When a bullet is fired, it moves up the screen, which corresponds
# to a decreasing y-coordinate value; so to update the position, we subtract the amount stored in self.speed_factor
# from self.y.  We then use the value of self.y to set the value of self.rect.y.  The speed_factor attribute lets us
# increase the speed of the bullets easily or modify it as the game goes on.  Once fired a bullet's x-value won't change
# so it'll always fire in a straight line.

# When we want to draw a bullet, we'll call draw_bullet().  The draw_rect() function fills part of the screen defined
# by the bullet's rect and color stored in self.color.

# Now that we have a Bullet class and the settings defined, we can write code to fire a bullet each time the player
# presses the spacebar.  First, we'll create a group in Touhou.py to store all the live bullets so we can manage all the
# bullets that have been fired.  The group will be an instance  of the class pygame.sprite.Group, which behaves like a
# list but with some extra functionality that's helpful for building games.  We'll use this group to draw bullets to the
# screen on each pass through the main loop and to update each bullet's position.


