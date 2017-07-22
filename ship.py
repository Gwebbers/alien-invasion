import pygame

class Ship():

    def __init__(self, tou_settings, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.tou_settings = tou_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's movement based on the movement flag"""
        # Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.tou_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.tou_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

# Okay this is overwhelming.  First we import the pygame module.  Then the __init__() method of Ship takes two
# parameters, the self reference and the screen where we'll draw the ship.  To load the image, we call
# pygame.image.load().  This function returns a surface representing the ship, which we store in self.image.
# It also takes the ship.bmp file as an argument for which to create the surface with.

# Once the image is loaded, we get to use get_rect() to access the surface's rect attribute.  One reason Pygame is
# so efficient is that it lets you treat game elements like rectangles (rects), even when they're not exactly shaped
# like rectangles.  Treating an element as a rectangle is good because rectangles are very simple geometric shapes.
# Even though the shapes of the elements won't be exact, it's usually good enough for simple games like this.

# When working with a rect object, you can use the x and y-coordinates of the top, bottom, left and right edges of the
# rectangle, as well as the center.  You can set any of these values to determine the current position of the rect.

# When centering a game element, work with the center, centerx or centery attributes of a rect.  When you're working
# at an edge of a screen, work with the top, bottom, left or right attributes.  When you're adjusting the horizontal
# or vertical placement of the rect, you can just use the x and y attributes, which are the x- and y-coordinates at the
# top-left corner.  These attributes spare you from having to do calculations that earlier game designers had to do
# manually.

# The origin of the screen in Pygame is in the top-left corner.

# We'll position our ship at the bottom of the screen.  To do so, first store the screen's rect in self.screen.rect.
# We use the screen.get_rect() function to get the rect and store the it in the variable.  Then we make the value of
# self.rect.centerx (the x-coordinate of the ship's center) match the centerx attribute of the screen's rect.  Aka
# placing our ship in the center of the screen.  Next we make sure the value of self.rect.bottom (the y-coordinate of
# the ship's bottom) equal to the value of the screen rect's bottom attribute, Pygame will use these attributes to
# position the ship image so it's centered horizontally and aligned  with the bottom of the screen.

# Next we define the blitme() method, which will draw the image to the screen at the position specified by self.rect.

# We've added a self.moving_right attribute in the __init__() method and have it initially set to False initially.
# Then we add update(), which moves the ship right if the flag is True.

# Now lets modify check_events() so that moving_right is set to True when the right arrow key is pressed and False
# when the key is released.

# The ship's positioning will update after we've checked for keyboard events

# We added a new attribute for self.moving_left.  In update(), we use two seperate if blocks instead of an elif block
# To allow the ship's rect to be both increased and decreased if both are held down.  This results in the ship standing
# still.  If we used elif for motion to the left, the right arrow key would still have priority.  Doing it this way
# makes the movements more accurate when switching from left to right, when the player might momentarily press both
# keys.

# Now we have to make some adjustments to check_events()

# So we added ai_settings to the list of parameters for __init__() so the ship will have access to the speed setting.
# We then turn the tou_settings parameter into an attribute, so we can use it in update().  Now that we're adjusting
# The position of the ship by fractions of a pixel, we need to store the position in a variable that can store a
# decimal value.  You can use a decimal variable to set a rect's attribute, but the rect will only store the integer
# portion of that value.  To store  the ship's position accurately, we define a new attribute self.center, which can
# hold decimal values.  We use the float() function to convert the value of self.rect.centerx to a decimal and store
# this value in self.center.

# Now when we change the ship's position in update(), the value of self.center is adjusted by the amount stored in
# tou_settings.ship_speed_factor.  After self.center has updated we set the value of self.rect.centerx to self.center.
# Only the integer portion will be stored in self.rect.centerx but that's fine for display.

# Now let's pass the Ship class an argument for settings in the main file.

# Added some new code onto our update() method so that it checks the position of our ship before changing the value of
# self.center.  The code self.rect.right returns the x-coordinate value of the right edge of the ship's rect.  If the
# value returned is less then the value of the screen's right edge or self.screen.rect.right then the ship hasn't
# reached the right edge of the screen.  Same for the left side, except since the left edge of the screen's rect is 0
# we can just check to make sure that our ship's rect's left edge is greater than 0.  This makes sure our ship can't
# get out of the boundaries.

# Next lets refactor check_events()
