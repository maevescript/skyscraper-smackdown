import arcade
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from game.systems.debris_generator import DebrisGenerator

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Skyscraper Smackdown"


class GameView(arcade.Window):
    def __init__(self):

        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

        self.debris_generator = DebrisGenerator()

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()
        self.debris_generator.draw()

        # Code to draw other things will go here
    def on_update(self, delta_time: float) -> None:
        self.debris_generator.update(delta_time)


def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
