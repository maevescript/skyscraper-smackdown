import arcade
import random

class BuildingTiles ():
    def __init__(self):

        self.sprite_list = None
        self.physics_engine = None
        self.floors = []
        
    
    def GenerateFloor(self):

        street = arcade.Sprite("C:/Users/rhbtz/Desktop/skyscraper-smackdown/assets/street.png")
        street.center_x = 1280/2
        street.center_y = 15
        self.sprite_list.append(street)

        self.physics_engine.add_sprite(
            street,
            body_type=arcade.PymunkPhysicsEngine.STATIC
        )
    
    def StartUpBuilding(self):
        coordinate_list = [[288, 800], [480, 850], [672, 900], [864, 950], [1056, 1000]]
        flag = False
        for i in range(4):
            for coordinate in coordinate_list:
                num = random.randint(1, 10)
                if(coordinate[0] == 672 and flag == False):
                    self.build = arcade.Sprite("C:/Users/rhbtz/Desktop/skyscraper-smackdown/assets/block8.png")
                    flag = True

                else:
                    
                    self.build = arcade.Sprite("C:/Users/rhbtz/Desktop/skyscraper-smackdown/assets/block1.png")
                
                self.build.center_x = coordinate[0]
                self.build.center_y = coordinate[1] + i*300
                self.sprite_list.append(self.build)

                self.physics_engine.add_sprite(
                    self.build,
                    mass=2.0,
                    friction=0.6,
                    elasticity=0.2,
                    body_type=arcade.PymunkPhysicsEngine.DYNAMIC,
                    moment_of_inertia=arcade.PymunkPhysicsEngine.MOMENT_INF 
                )


    def drawStartBuild(self):
        self.sprite_list.draw()
        print
        
    def drawNewFloor(self):
        
        coordinate_list = [[288, 1500], [480, 1550], [672, 1600], [864, 1650], [1056, 1700]]
        for coordinate in coordinate_list:
            #num = random.randint(1, 7)
            self.build = arcade.Sprite("C:/Users/rhbtz/Desktop/skyscraper-smackdown/assets/block1.png")
            self.build.center_x = coordinate[0]
            self.build.center_y = coordinate[1]
            self.sprite_list.append(self.build)

            self.physics_engine.add_sprite(
                self.build,
                mass=2.0,
                friction=0.6,
                elasticity=0.5,
                body_type=arcade.PymunkPhysicsEngine.DYNAMIC,
                moment_of_inertia=arcade.PymunkPhysicsEngine.MOMENT_INF 
            )

    def destroyLowestFloor(self):
        self.physics_engine.remove_sprite(self.sprite_list[5])
        self.sprite_list.remove(self.sprite_list[5])

        self.physics_engine.remove_sprite(self.sprite_list[4])
        self.sprite_list.remove(self.sprite_list[4])

        self.physics_engine.remove_sprite(self.sprite_list[3])
        self.sprite_list.remove(self.sprite_list[3])

        self.physics_engine.remove_sprite(self.sprite_list[2])
        self.sprite_list.remove(self.sprite_list[2])

        self.physics_engine.remove_sprite(self.sprite_list[1])
        self.sprite_list.remove(self.sprite_list[1])
        


        