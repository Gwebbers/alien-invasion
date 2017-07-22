import sys
import pygame
from bullet import Bullet
from alien import Alien
from star import Star
import random


def check_keydown_events(event, tou_settings, screen, ship, bullets):
    # event is an event that's being checked
    # tou_settings is an instance of Settings
    # screen is the screen that we're using for our game
    # ship is an instance of Ship
    # bullets is a group of bullets

    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(tou_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(tou_settings, screen, ship, bullets):
    # If the amount of bullets is less than or equal to the amount listed in settings...
    if len(bullets) <= tou_settings.bullet_limit:
        # Create a new bullet and add it to the bullet group
        new_bullet = Bullet(tou_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(tou_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():  # 2
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, tou_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

# This module imports sys and pygame, which are used in our event checking loop.  The function needs no parameters at
# this stage.  Now lets import it back into our main file.


def update_screen(tou_settings, screen, ship, aliens, bullets, stars):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass of the loop
    screen.fill(tou_settings.bg_color)  # 4
    # Redraw all of our bullets behind our ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Draws the stars to the screen
    for star in stars:
        star.blitme()
    aliens.draw(screen)

    # Make the most recently drawn screen visible
    pygame.display.flip()  # 3


def update_bullets(bullets):
    """Update the position of bullets and delete old ones"""
    # Update bullet positions
    bullets.update()

    # Get rid of bullets that have disappeared off the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_aliens_x(tou_settings, alien_width):
    """Determine how many aliens can fit in a row"""
    # Create an alien and find the number of aliens on a row
    # Spacing is equal to one alien width
    # Calculate how much space we have using the screen width
    avaliable_space_x = tou_settings.screen_width - 2 * alien_width
    # Caculate the number of aliens we can store on a row
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    print(number_aliens_x)
    return number_aliens_x


def create_alien(tou_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in its row"""
    alien = Alien(tou_settings, screen)
    # Calculate the width of an alien and store it
    alien_width = alien.rect.width
    # Place the alien based on how wide they are
    alien_x = alien_width + ((2 * alien_width) * alien_number)
    alien.rect.x = alien_x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    # add the alien to the aliens group
    aliens.add(alien)


def create_fleet(tou_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    # Create an alien and find the number of aliens in the row
    alien = Alien(tou_settings, screen)
    number_aliens_x = get_number_aliens_x(tou_settings, alien.rect.width)
    number_rows = get_number_rows(tou_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        # for each row of aliens
        for alien_number in range(number_aliens_x):
            # Create an alien and place it on a row
            create_alien(tou_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(tou_settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(tou_settings, aliens)
            break

def change_fleet_direction(tou_settings, aliens):
    """Drop the entire fleet and change direction"""
    for alien in aliens.sprites():
        alien.rect.y += tou_settings.fleet_drop_speed
        tou_settings.fleet_direction = -1


def update_aliens(tou_settings, aliens):
    """Check if the fleet has hit an edge, and update position of all aliens"""
    check_fleet_edges(tou_settings, aliens)
    aliens.update()


def get_number_rows(tou_settings, ship_height, alien_height):
    # calculates the number of rows of aliens we can have.
    avaliable_space_y = (tou_settings.screen_height - (7 * alien_height) - ship_height)
    number_rows = int(avaliable_space_y /(2 * alien_height))
    return number_rows


def create_star(tou_settings, screen, stars, star_row, star_column):
    """Create a star and place it on a grid"""
    star = Star(tou_settings, screen)
    # Place the star based on a grid with deviation
    star_x = (100 * star_column) + random.randint(1, 10)
    star_y = (100 * star_row) + random.randint(1, 10)
    # adjusts the star's rect to these calculations
    star.rect.x = star_x + 100
    star.rect.y = star_y + 100
    # Add the star to the group
    stars.add(star)


def find_star_grid(tou_settings):
    # Find the usable space of the screen
    space_x = tou_settings.screen_width
    space_y = tou_settings.screen_height
    # Calculate the rows for our grid
    number_rows = int(space_x / 100)
    number_columns = int(space_y / 100)
    # Create the grid as a list and return it
    star_grid = [number_rows, number_columns]
    print(star_grid)
    return star_grid


def create_sky(tou_settings, stars, screen):
    """Creates a background full of randomly placed stars"""
    # Calls find_star_grid to get our grid stats
    star_grid = find_star_grid(tou_settings)
    # Creates stars in rows and columns
    for star_row in range(0, star_grid[0]):
        for star_column in range(0, star_grid[1]):
            create_star(tou_settings, screen, stars, star_row, star_column)


# The new update_screen() function takes three parameters: tou_settings, screen and ship.

# We edited check_events() to check for right key presses now.
# First we made it so check_events() accepts a new parameter, a ship parameter.  This is because the ship needs to move
# right when the right arrow key is pressed.  Inside check_events() we add an elif block to the event loop to respond
# when Python detects a KEYDOWN event.  We check if the key pressed is the right arrow key (pygame.K_RIGHT) by reading
# the event.key attribute.  If the right key was pressed, we move the ship to the right by increasing the value of
# ship.rect.centerx by 1.

# Now lets update the call in Touhou.py so it gives a ship argument in the call.

# And we modified it a bit again :P
# Now instead of directly moving the ship right, it trips our ship's flag for moving right, causing it to move right.

# Then we add a new elif block, which responds to KEYUP events.  When the player releases the right arrow key (K_RIGHT),
# we set moving_right to False.

# Finally we modify the while loop in Touhou.py to call the ship's update() method on each loop pass.

# With some more edits now if a KEYDOWN event occurs for the K_LEFT key, we set moving_left to True.  If a KEYUP event
# occurs for the K_LEFT key, we set moving_left to False.  We can use elif blocks here because each event is only
# connected to one key.  If the player presses two keys at once, two seperate events will be detected.

# check_events() is getting pretty big so lets refactor it into two separate functions: one that handles KEYDOWN events
# and another that handles KEYUP events.

# We make two new functions: check_keydown_events() and check_keyup_events().  Each needs an event parameter and a
# ship parameter.  The bodies of these two functions are copied down from check_events(), and we've replaced the old
# code to calls to the new functions.

# Now time to add bullet firing capability!  We don't need to change check_keyup_events() because nothing happens when
# the key is released.  We also need to modify update_screen() to make sure each bullet it being drawn to the screen
# before we call flip().

# This is pretty confusing yeah?  The group bullets is passed down to check_keydown_events().  When the player presses
# the spacebar, we create a new bullet ( a Bullet instance that we name new_bullet) and add it to the group bullets
# using the add() method; the code bullets.add(new_bullet) stores the new bullet into the group bullets.
# We need to add bullets as a parameter of check_events(), as well as pass it as an argument in the call of
# check_keydown_events().

# We give the bullets parameter to update_screen(), which draws the bullets to the screen.  The bullets.sprites()
# method returns a list of all sprites in the group bullets.  To draw all fired bullets on screen we loop through all
# the sprites in the group bullets and call draw_bullet() on each one.

# Now lets head back to the main file for a bit

# Okay we integrated the bullet limit into the game_functions.  Now when the spacebar is pressed, we check the length of
# bullets and if len(bullets) is less than three, we create a new bullet.  But if there are already three the player
# will not fire another bullet.  We can now only fire bullets in groups of three max.

# Let's do some more refactoring in the main code by creating a new function here called update_bullets()
# Now we fix up the main code and bam!

# We created fire_bullet() to help clean up our check_keydown_events() code.

# In check_keydown_events() we edited it so the alien appears correctly now.

# When you call draw() on a group, Pygame automatically draws each element in the group at the position defined by its
# rect attribute.  In this case, aliens.draw(screen) draws each alien in the group to the screen.

# Now we can create our fleet!  Here's the new function create_fleet(), which we'll place at the end of game_functions
# We also need to import the Alien class in.

# We've already gone through some of this code.  We need to know the alien's width and height in order to place the
# aliens, so we create an alien before we perform calculations.  This alien won't be part of the fleet, so don't add it
# to the group aliens.  Then we get the alien's width from its rect attribute and store this value in alien_width so
# we don't have to keep wortking through the rect attribute.  Next we calculate the horizontal space avaliable for
# aliens and the number of aliens we can fit in that space.

# The only change here from our original formula is that we're using int() to ensure we end up with an integer number of
# aliens because we don't want to create partial aliens, and the range() function needs an integer.  The int() function
# drops the decimal part of a number, effectively rounding it down.  (This is helpful since a little extra space is
# preferred to overcrowding.

# Next we set up a loop that counts from 0 to the number of aliens we need to make.  In the main body of the loop,
# create a new alien and set its x-coordinate value to place it on the row.  Each alien is pushed to the right by a
# margin of one alien width from the left margin.  Next, we multiply the alien width by 2 to account for the space
# each alien takes up, including the empty space to its right and we multiply this amount by the alien's position on the
# row.  Then we add the alien to the aliens group.

# Refactoring!  The body of get_number_aliens_x() is exactly as it was in create_fleet().  The body of create_alien()
# is also unchanged from the create_fleet() excerpt that we use the alien that was just created to get alien_width.
# in create_fleet() we replace the code for determining the horizontal spacing with a call to get_number_aliens_x(),
# and we removed the line referring to alien_width, because that's now only used in create_alien().  Then later we call
# create_alien to create our aliens in our fleet.

# But how do we make rows?  We must determine the amount of rows we can fit on screen and repeat the loop for each row
# of space.  To determine the amount of usable vertical space by subtracting the alien_height from the top, the ship
# height from the bottom and two alien heights from the new bottom.

# avaliable_space_y = tou_settings.screen_height - 3 * alien_height - ship_height

# The result will create some empty space above the ship, so the player has some time to start shooting aliens at the
# beginning of each level.  Each row needs some empty space below it, we'll make it equal to the height of one alien.
# To find the number of rows, we divide the avaliable space by two times the height of an alien.  One for the row, and
# another for the spacing. (If the calculations are off we can adjust this later)

# number_rows = avaliable_space_y /(2 * alien_height)

# Now lets actually make our code

# To calculate the number of rows we can fit on screen, we write our avaliable_space_y and number_rows calculations into
# a function named get_number_rows(), which is similar to get_number_aliens_x().  The calculation is wrapped in
# parenthesis so the calculation can be split over two lines.  We also use int on number_rows because we don't want
# partial rows.

# To create multiple rows, we use two nested loops: one outer and one inner loop.  The inner loop creates aliens on a
# row.  The outer loop counts from 0 to the number of rows we want; Python will use the code for making a single row
# a number of times equal to number_rows

# To nest the loops, write a new for loop and indent the code you want to repeat.  Now when we call create_alien(), we
# include an argument for the row number so each row can be placed farther down the screen.

# The definition of create_alien() needs a parameter to hold the row number.  Within create_alien(), we change an
# alien's y-coordinate value when it's not in the first row by starting with one alien's height to create an empty
# space at the top of the screen.  Each row starts two alien heights below the last, so we multiply the alien height
# by two and then by its row number.  The first row number is 0 so the vertical placement of the first row is unchanged.

# Finally create_fleet() has a new parameter for the ship object, which means we need to add it into the call in our
# main code.

# We use the update() method on the aliens group, which automatically calls each alien's update() method.  When you
# run the file now, the aliens should continue right until they go off the screen once you call update_aliens() in the
# main file

# When the alien reaches the edge, the entire fleet needs to drop down and change direction.  We therefore need to
# make some substantial changes in game_functions because that's where we're going to do the edge checking.  We'll make
# this happen by writing two functions, check_fleet_edges() and change_fleet_direction() as well as modifying
# check_aliens.


