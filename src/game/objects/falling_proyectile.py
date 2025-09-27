import arcade
from abc import ABC, abstractmethod

class FallingProyectile(ABC):
    def __init__(self):
        self.sprite.center_x = 0
        self.sprite.center_y = 0
        self.speed = 0
        self.radius = 0
        self.color = arcade.color.GRAY
        self.change_y = 0
        self.lanes = 0
    
    def get_speed(self):
        return self.speed
    
    def set_speed(self, new_speed):
        self.speed = new_speed
        self.change_y = -new_speed
    
    def on_update(self, delta_time: float):
        # self.sprite.center_y += self.sprite.change_y * delta_time
        pass
    
    def get_position(self):
        return (self.sprite.center_x, self.sprite.center_y)
    
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def on_floor_hit(self):
        pass
    
    @abstractmethod
    def on_player_hit(self):
        pass
    