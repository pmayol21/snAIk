"""
Platformer Game
"""
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = .3
TILE_SCALING = .3
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 64
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 16
GRAVITY = 0
PLAYER_JUMP_SPEED = 16

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 300

BOTTOM_VIEWPORT_MARGIN = 100



class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.coin_list = None
        self.wall_list = None
        self.background = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        # Load sounds


        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.background = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite("slime.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 96
        self.player_list.append(self.player_sprite)

        # --- Load in a map from the tiled editor ---

        # Name of map file to load
        map_name = "grid.tmx"
        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Walls'
        # Name of the layer that has items for pick-up
        coins_layer_name = 'Coins'
        # Name of background
        background = 'Background'

        # Read in the tiled map
        my_map = arcade.read_tiled_map(map_name, TILE_SCALING)

        # -- Walls
        # Grab the layer of items we can't move through
        map_array = my_map.layers_int_data[platforms_layer_name]

        # Calculate the right edge of the my_map in pixels
        self.end_of_map = len(map_array[0]) * GRID_PIXEL_SIZE

        # -- Platforms
        self.wall_list = arcade.generate_sprites(my_map, platforms_layer_name, TILE_SCALING)

        # -- Coins
        self.coin_list = arcade.generate_sprites(my_map, coins_layer_name, TILE_SCALING)

        # -- Back
        self.background = arcade.generate_sprites(my_map, background, TILE_SCALING)

        # --- Other stuff
        # Set the background color
        if my_map.backgroundcolor:
            arcade.set_background_color(my_map.backgroundcolor)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.background.draw()
        self.wall_list.draw()
        self.coin_list.draw()

        self.player_list.draw()


<<<<<<< HEAD
        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.WHITE, 18)
=======
>>>>>>> 05d789bd3e2842b00929999a9d3df004716c3ade

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = - PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_y = 0
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_y = 0
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED


    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            # Play a sound
            arcade.play_sound(self.collect_coin_sound)
            # Add one to the score
            self.score += 1

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False



        self.view_left = -100









            # Do the scrolling
        arcade.set_viewport(-100,SCREEN_WIDTH ,-400, SCREEN_HEIGHT)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
