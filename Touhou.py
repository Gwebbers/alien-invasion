import pygame
from pygame.sprite import Group
from Settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize a game and create a screen object.
    pygame.init()  # 1
    tou_settings = Settings()
    screen = pygame.display.set_mode((tou_settings.screen_width, tou_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship, a group of bullets and a group of aliens
    ship = Ship(tou_settings, screen)
    aliens = Group()
    bullets = Group()

    # Make a group of stars
    stars = Group()

    # Create a fleet of aliens
    gf.create_fleet(tou_settings, screen, ship, aliens)

    # Create the sky
    gf.create_sky(tou_settings, stars, screen)

    # Start the main loop of the game
    while True:
        gf.check_events(tou_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(tou_settings, aliens)
        gf.update_screen(tou_settings, screen, ship, aliens, bullets, stars)

run_game()

# M'k so first!  We import the pygame and sys modules.  The pygame module contains the functionality we need to make a
# game.  We'll use the sys module to exit the game when the player quits.

# Our game starts as the function run_game().  The line pygame.init() on marker 1 initializes the background settings that
# Pygame needs to work properly.  Then on the following line we call pygame.display.set_mode() to create a display
# window called screen, on which we'll draw all of the graphical elements.  The argument (1200,800) is a tuple that
# defines the dimensions of the game window.  By passing these dimensions to pygame.display.set_mode() we create a game
# window that is 1200 pixels wide and 800 pixels tall.

# The screen object is called a surface.  A surface in Pygame is a part of the screen that displays a game element.
# Each element in the game, like the ships and bullets are surfaces.  The surface returned by display.set_mode()
# represents the entire game window.  When we activate the game's animation loop, this surface is automatically redrawn
# on every pass through the loop.

# The game is controlled by a while loop, which we can see on marker 2.  This contains an event loop and code which
# manages screen updates.  An event is an action that the user performs when playing the game, such as a key press or
# moving the mouse.  To make our program respond to events, we'll write an event loop to listen for an event and
# perform an appropriate task depending on the kind of event occured.  The for loop on line 14 is an event loop.

# To access the events detected by Pygame, we'll use the pygame.event.get() method.  Any keyboard or mouse event will
# cause the for loop to run.  Inside the loop we'll write a series of if statements to detect and respond to specific
# events.  For example, when the player clicks the game's window close button, a pygame.QUIT event is detected and we
# call sys.exit() to exit the game.

# The call to pygame.display.flip() on marker 3 tells the game to make the most recently drawn screen visible.  In this
# case it draws an empty screen each time through the while loop to erase the old screen so that only the new screen is
# visible.  When we move the game elements around, pygame.display.flip() will continually update the display to show the
# new positions and hide the old ones, creating the illusion of smooth movement.

# The last line in the base calls run_game(), which initializes the game and starts the main loop.

# Pygame uses a black screen by default, which is boring.  Let's change that.
# First we need to create a background color and store it in bg_color.  This color needs to be specified only once,
# so we determine its value before entering the main while loop.

# Colors in Pygame are specified as RGB colors: a mix of red, green and blue.  Each color value can range from 0 to
# 255.  The color value (255, 0, 0) is red, (0, 255, 0) is green and (0, 0, 255) is blue.  You can mix the values for
# 16 million colors.  The color value (230, 230, 230) mixes equal amounts of each color which provides a light gray
# background.

# Then at marker 4 we fill the screen with this color with screen.fill() which only takes the color as an argument.

# We imported Settings into the main program file, then created an instance of Settings to store it into tou_settings
# after the pygame_init()

# Phew, made our Ship class too.  Lets add it to our main code.

# Now that we have a ship on our screen lets do some refactoring!  Refactoring is when we simplify the structure of the
# code we've already written, making it easier to build on.

# We'll start by moving the code that manages events to a seperate function called check_events().  This will simplify
# run_game() and isolate the events seperately from the other aspects of the game, like updating the screen.
# We'll plonk it into a seperate module.

# Now we no longer need to import sys directly into the main program file, because it's only being used in the
# game_functions module.  We give the imported module the alias gf.

# Now lets create another refactoring for updating the screen.  We'll call this update_screen()

# These two new functions make the whole while loop much simpler and will make further development easier.  Instead of
# working inside run_game(), we can do most of our editing in the module game_functions.

# Because we wanted to start out working with code in a single file, we didn't introduce the game_functions module
# right away.  This is a realistic development process.  Writing our code then refactoring it!

# M'kay so now let's add steering to our ship!  First let's work on moving it right and left.  To do this we'll write
# code that responds when the player presses the right or left arrow key.  We'll focus on movement to the right first,
# then we'll follow the same principles for left-bound movement.  Now lets learn how to control the movements of images
# on our screen.

# Whenever the player presses a key, that keypress is registered in Pygame as an event.  Each event is picked up by the
# pygame.event.get() method, so we need to specify in our check_events() function what kind of events to check for.
# Each keypress is registered as a KEYDOWN event.

# When a KEYDOWN event is detected, we need to check whether the key that was pressed down triggers a certain event.
# For example, if the right arrow key was pressed we need to increase the ship's rect.centerx value to move the ship to
# the right.

# Now that we've done that we see our ship move one pixel to the right every time we press the right arrow key. That's
# technically correct but we can do a lot better.  Let's improve this by allowing continuous movement.

# When the player holds the right arrow key, we want our ship to continue moving to the right until the player releases
# that key.  We'll have our game detect a pygame.KEYUP event, so we'll know when the right arrow is released; then
# we'll use the KEYUP and KEYDOWN features together with a flag called moving_right to implement continuous motion.

# When the ship is motionless the moving_right flag will be False.  When the right arrow key is pressed we'll set the
# flag to True, and set it to False when the button is released again.

# The Ship class controls all attributes of the ship, so we'll give it an attribute called moving_right and an
# update() method will change the position of the ship if the flag is set to True.

# Now with a quick modification to the Ship class and the check_events() function we can move ourselves left too!

# Now that the ship can move in two directions and is motionless when both keys are pressed, it's time to further refine
# our movement, including changing our speed and making sure the ship doesn't go off the screen.

# Currently the ship moves one pixel per cycle through the while loop, but we can take finer control of the ship's
# speed by adding a ship_speed_factor attribute to the Settings class.  We'll use this attribute to determine how far
# to move the ship on each pass through the loop.

# Now that we've adjusted the speed a bit, let's limit our ship's range so it can't fly off the screen.
# We can do this by modifying our update method.

# Now to give us the ability to shoot, we'll write code that fires a bullet when the player presses the spacebar.
# Bullets will then travel to the top of the screen then disappear.

# First lets add the settings of our bullet to settings

# New update!  We imported Group from pygame.sprite.  Which we made an instance of and called it bullets.  This group
# is created outside the while loop so we don't create a new group of bullets every loop cycle.

# This would make thousands of different groups and slow the game to a crawl, freezing it and possibly crashing the
# computer.

# We then pass bullets to check_events() and update_screen().  We'll need to work with bullets in check_events() when
# the spacebar is pressed, and we'll need to update the bullets being drawn on screen to update_screen().  When you call
# update() on a group, the group automatically calls update for each sprite in the group.  The line bullets.update()
# calls bullet.update() for each bullet we place in the group bullets.

# Now we get to the part where we fire the bullets.  In game_functions.py we need to modify check_keydown_events() to
# fire a bullet when the spacebar is pressed.

# Phew, we can now fire bullets, but we have a problem.  The bullets disappear when they reach the top of the screen
# but they're not actually deleted.  They continue to exist and continue to go up, burning memory and processing power.

# We need to get rid of these old bullets, or the game will slow down from all this pointless work.  To do this, we need
# to check when the bottom value of a bullet's rect is less than or equal to 0, indicating that it is no longer on the
# screen.

# We shouldn't remove items from a list or group within a for loop, so we have a copy of the loop that we go over.
# We use the copy() method to set up the for loop, which enables us to modify bullets inside the loop.  We check each
# bullet to see if it's disappeared off the top of the screen, and if it has to delete it off bullets.  Then we create
# a print statement to show how many bullets are in the game and verify that they're being deleted.

# Note that even though we're using a copy() for our loop, we delete the bullets off of the main list.

# If this code works correctly, we can watch the terminal output while firing bullets and see if the number of bullets
# is decreasing or not.  After we verify that the code works we will delete this line however.

# Now that we're deleting the bullets lets move on to limiting the amount of bullets at a time.
# This will encourage the player to shoot accurately.  To do this lets go back to settings.py

# We've made it so our main loop contains only minimal code so we can quickly read through it when needed.  The main
# loop checks for player input, updates the position of the ship and the bullets as well as cleaning away the old ones
# and then we use these updated positions to draw a new screen.

# Now lets do another piece of refactoring over in game_functions.py

# M'k Let's go!  First thing's first, let's add a key that exits out of the game immediately.  Like "q".

# Here we're just importing the alien class and creating an instance of it before entering the main while loop.  We're
# not changing its position yet, so we're not going to add anything new inside the loop; however, we do modify
# update_screen() to pass it to the alien instance.

# Now lets edit the code for update_screen()

# Now that we have one alien showing up, we need to figure out how many aliens can fit across the screen.  First we'll
# figure the horizontal spacing between aliens and create a row; then we'll determine the vertical spacing and create
# a fleet.

# To figure out how many aliens fit in a row, let's look at how much horizontal space we have.  The screen width is
# stored in ai_settings.screen_width, but we need an empty margin on either side of the screen.  We'll make this margin
# the width of one alien.  Because we have two margins, the avaliable space for aliens on the screen width minus
# two aliens is:
# avaliable_space_x = tou_settings.screen_width - (2 * alien_width)

# We also need to set the spacing between aliens; we'll make it one alien width.  The space needed to display one alien
# is twice its width: one width for the alien and one width for an empty space between them on the right.  To find
# the number of aliens that fit across the screen, we divide the avaliable width by two times the width of the aliens.

# number_aliens = avaliable_space_x / (2 * alien_width)

# Now lets create a row of aliens.

# I changed it so we're no longer creating our aliens directly inside Touhou.py, we no longer need to import Alien into
# this file.
# We also created an empty group to hold all the aliens in the game.  Then call the new function create_fleet(), which
# we will write after this, passing it tou_settings, the screen object and the empty group called aliens.  Next we
# modified update_screen() to give it access to the aliens group.

# The first row is offset to the left, which is a positive for gameplay, because we want the fleet to move right until
# it hits the edge of the screen, then drop down a bit and head in the opposite direction and loop back and forth.
# Like the classic game Space Invaders, this movement is better then having the fleet just drop straight down.  We'll
# continue this motion until all the aliens have been destroyed or until an alien hits the ship or the bottom of the
# screen.

# Now time for some more refactoring!  Let's cleen up create_fleet()

# M'kay now lets work on making our fleet move!  Let's make it move to the right until it hits an edge, then it will
# drop a set amount and move left.  Continuing until one reaches the bottom of the screen or hits the player.

# To move the aliens right, we'll use an update() method in our Alien class.  Which we'll call for each alien in
# alien.py

# We also need to add something into settings.py to choose the alien speed.
