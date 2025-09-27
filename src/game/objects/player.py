import arcade

class Player(arcade.Sprite):
    def __init__(self, lanes, width, height, health):
        super().__init__(filename=None, hit_box_algorithm="None")
        self.color = arcade.color.BLUE
        self.width = width
        self.height = height
        self.lanes = lanes
        self.health = health
        self.current_lane = 0
        self.center_x = self.lanes[self.current_lane].x_start
        self.center_y = 0
        self.dead = False

    def move_left(self):
        if self.current_lane > 0:
            self.current_lane -= 1
            self.center_x = self.lanes[self.current_lane].x_start

    def move_right(self):
        if self.current_lane < len(self.lanes) - 1:
            self.current_lane += 1
            self.center_x = self.lanes[self.current_lane].x_start
            
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.dead = True
            
    def punch_forward(self):
        pass

    def draw(self):
        arcade.draw_lbwh_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color
        )

    def get_lane(self):
        return self.current_lane
