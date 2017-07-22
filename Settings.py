# Now lets go over how to create a Settings class.
# Each time we introduce some functionality into our game, we'll typically introduce some new settings as well.
# Instead of adding settings all throughout our code lets write a module called settings to store all the settings in
# one place.  This allows us to pass around one settings object instead of many individual settings.  In addition, it
# makes our function calls simpler and makes it easier to modify as our project grows.  To modify the game, we'll
# simply change some values in settings.py instead of searching around our main file.

class Settings():
    """A class to store all of our settings"""

    def __init__(self):
        """Initialize the settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = .5

        # Bullet settings
        self.bullet_speed_factor = 1
        # Bullet width and height in pixels
        self.bullet_width = 3
        self.bullet_height = 15
        # Amount of bullets allowed at a time
        self.bullet_limit = 3
        # Bullet color in RGB
        self.bullet_color = (0, 160, 160)

        # Star count
        self.star_count = 50

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

# We've set up the initial value of ship_speed factor to 1.5.  When we want to move the ship, we'll adjust it's position
# by 1.5 pixels instead of just one.  We're using decimal values for the speed setting to give us finer control of
# the ship's speed when we increase the tempo of the game later on.  However rect attributes such as centerx only store
# integer values, so next we have to edit Ship.

# We added a bullet_limit setting that will limit the amount of bullets the player can fire at a time.  Now let's go to
# game_functions so we can use this new setting.

# The setting fleet_drop_speed controls how quickly the fleet drops down the screen each time an alien reaches either
# edge.  It's helpful to separate this speed from the alien's horizontal speed for extra customization.

# To implement the fleet_direction we could use strings such as "left" or "right", but we'd end up with elif statements
# trying to figure out the direction.  This way we only have two directions to deal with, and switch between them
# every time the fleet changes direction.
