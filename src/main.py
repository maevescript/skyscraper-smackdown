import arcade
from game.systems.debris_generator import DebrisGenerator
from game.world.lane import Lane
from game.objects.player import Player

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Skyscraper Smackdown"
LANE_COUNT = 7
LANE_WIDTH = WINDOW_WIDTH / LANE_COUNT


class GameView(arcade.Window):
    def __init__(self):
        # Call the parent class to set up the window
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.background_color = arcade.csscolor.CORNFLOWER_BLUE

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        self.debris_generator = DebrisGenerator()

        self.lanes = []
        for i in range(LANE_COUNT):
            x_start = LANE_WIDTH * i
            self.lanes.append(Lane(i, x_start, LANE_WIDTH))

        self.player = Player(self.lanes, LANE_WIDTH, LANE_WIDTH, 100)

        pass

    def on_draw(self):
        """Render the screen."""

        # The clear method should always be called at the start of on_draw.
        # It clears the whole screen to whatever the background color is
        # set to. This ensures that you have a clean slate for drawing each
        # frame of the game.
        self.clear()
        self.debris_generator.draw()

        # Para mostrar las lineas de los carriles
        for lane in self.lanes:
            arcade.draw_line(
                lane.x_center - LANE_WIDTH // 2,
                0,
                lane.x_center - LANE_WIDTH // 2,
                WINDOW_HEIGHT,
                arcade.color.GRAY,
                2,
            )

        self.player.draw()
        # self.debris.draw()

        # Code to draw other things will go here

    def on_update(self, delta_time: float) -> None:
        self.debris_generator.on_update(delta_time)
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.move_left()
        elif key == arcade.key.RIGHT:
            self.player.move_right()


def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
