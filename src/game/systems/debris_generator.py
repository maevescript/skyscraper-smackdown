import arcade
import random
import time

from game.objects.debris import Debris

class DebrisGenerator:
    def __init__(self, min_interval=1.0, max_interval=3.0, screen_width=1280, screen_height=720, lanes = 7):
        self.min_interval = min_interval
        self.max_interval = max_interval
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.lanes = lanes
        
        self.debris_list = []  # List to store all debris circles
        self.last_spawn_time = time.time()
        self.next_spawn_delay = random.uniform(self.min_interval, self.max_interval)
        
        self.radius = 40
    
    def on_update(self, delta_time, lane = 0):
        current_time = time.time()
        
        if current_time - self.last_spawn_time >= self.next_spawn_delay:
            self.spawn_debris(lane)
            self.last_spawn_time = current_time
            self.next_spawn_delay = random.uniform(self.min_interval, self.max_interval)

        for debris in self.debris_list:
            debris.on_update(delta_time)
    
    def spawn_debris(self, lane):
        # x = random.randint(self.radius, self.screen_width - self.radius)
        x = self.get_middle_lane_point(lane)
        y = self.screen_height - self.radius
        debris = Debris(x, y, 120, self.radius, arcade.color.AO)
        
        self.debris_list.append(debris)
    
    def draw(self):
        for debris in self.debris_list:
            debris.draw()
    
        self.debris_list = [debris for debris in self.debris_list if debris.get_position()[1] >= 100]
    
    def clear_debris(self):
        self.debris_list.clear()
    
    def get_debris_count(self):
        return len(self.debris_list)

    def get_middle_lane_point(self, lane):
        lane_width = self.screen_width / self.lanes
        left_edge = lane_width * lane
        middle_point = left_edge + (lane_width / 2)
        return middle_point

