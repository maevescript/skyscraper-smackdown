import arcade

class DebrisGenerator:
    def __init__(self):
        self.x = 640
        self.y = 360
        self.radius = 40
    
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, arcade.color.AO)