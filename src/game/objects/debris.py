import arcade
from game.objects.falling_proyectile import FallingProyectile

class Debris(FallingProyectile):
    def __init__(self, x=0, y=0, speed=1, radius=20, color=arcade.color.GRAY):
        self.center_x = x
        self.center_y = y
        self.speed = speed
        self.radius = radius
        self.color = color
        self.change_y = -speed
    
    def draw(self):
        arcade.draw_circle_filled(
            self.center_x, 
            self.center_y, 
            self.radius, 
            self.color
        )
    
    def on_floor_hit(self):
        return super().on_floor_hit()
    
    def on_player_hit(self):
        return super().on_player_hit()