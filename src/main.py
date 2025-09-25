import arcade
from building import BuildingTiles

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Skyscraper Smackdown"



class GameView(arcade.Window):
    def __init__(self):

        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.sprite_list = None
        self.physics_engine = None

    def setup(self):

        self.sprite_list = arcade.SpriteList()
        self.physics_engine = arcade.PymunkPhysicsEngine(gravity=(0, -900))

        BuildingTiles.GenerateFloor(self)
        BuildingTiles.StartUpBuilding(self)


    def on_draw(self):
        
        self.clear()
        BuildingTiles.drawStartBuild(self)
    
    def on_update(self, delta_time):

        self.physics_engine.step()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            BuildingTiles.drawNewFloor(self)
            if self.sprite_list[1]:  
                self.physics_engine.remove_sprite(self.sprite_list[1])
                self.sprite_list[1].remove_from_sprite_lists()
                self.sprite_list[1] = None
            
            


def main():
    """Main function"""
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
