import arcade
import random
block_type = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
tile_life_points = [5,5,5,5,5]
class BuildingTiles ():
    def __init__(self):

        self.sprite_list = None
        self.physics_engine = None
        self.floors = []
        
    
    def GenerateFloor(self):

        street = arcade.Sprite("assets/street.png")
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
            for index, coordinate in enumerate(coordinate_list):
                num = random.randint(1, 1000)
                if(coordinate[0] == 672 and flag == False):
                    self.build = arcade.Sprite("assets/block8.png")
                    block_type[index+5] = 0
                    flag = True

                else:
                    if(num < 200):
                        self.build = arcade.Sprite("assets/block1.png")
                        block_type[index+i*5] = 0
                    elif(num >= 200 and num < 400):
                        self.build = arcade.Sprite("assets/block2.png")
                        block_type[index+i*5] = 0
                    elif(num >= 400 and num < 600):
                        self.build = arcade.Sprite("assets/block3.png")
                        block_type[index+i*5] = 0
                    elif(num >= 600 and num < 700):
                        self.build = arcade.Sprite("assets/block4.png")
                        block_type[index+i*5] = 1
                    elif(num >= 700 and num < 800):
                        self.build = arcade.Sprite("assets/block5.png")
                        block_type[index+i*5] = 1
                    elif(num >= 800 and num < 900):
                        self.build = arcade.Sprite("assets/block6.png")
                        block_type[index+i*5] = 1
                    else:
                        self.build = arcade.Sprite("assets/block7.png")
                        block_type[index+i*5] = 1


                print(f"Iteration {index}: coordinate = {block_type}")
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


    def drawNewFloor(self):
        tile_life_points = [5,5,5,5,5]
        coordinate_list = [[288, 1500], [480, 1550], [672, 1600], [864, 1650], [1056, 1700]]
        for index, coordinate in enumerate(coordinate_list):
            
            num = random.randint(1, 1050)
            if(num < 200):
                self.build = arcade.Sprite("assets/block1.png")
                block_type.append(0)
            elif(num >= 200 and num < 400):
                self.build = arcade.Sprite("assets/block2.png")
                block_type.append(0)
            elif(num >= 400 and num < 600):
                self.build = arcade.Sprite("assets/block3.png")
                block_type.append(0)
            elif(num >= 600 and num < 700):
                self.build = arcade.Sprite("assets/block4.png")
                block_type.append(1)
            elif(num >= 700 and num < 800):
                self.build = arcade.Sprite("assets/block5.png")
                block_type.append(1)
            elif(num >= 800 and num < 900):
                self.build = arcade.Sprite("assets/block6.png")
                block_type.append(1)
            else:
                self.build = arcade.Sprite("assets/block7.png")
                block_type.append(1)

            
             
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
        print(f"Iteration {index}: coordinate = {block_type}")   

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
        
        del block_type[:5]

        
    def checkIfCrystalFloor(self):
        pass

    def lowestFloorLifeCount(self,tile):
        if(tile == 0):
            tile_life_points[tile] = tile_life_points[tile] -1
        elif(tile == 1):
            tile_life_points[tile] = tile_life_points[tile] -1
        elif(tile == 2):
            tile_life_points[tile] = tile_life_points[tile] -1
        elif(tile == 3):
            tile_life_points[tile] = tile_life_points[tile] -1
        elif(tile == 4):
            tile_life_points[tile] = tile_life_points[tile] -1

        print(f"{tile_life_points}")

        if all(x <= 0 for x in tile_life_points):
            BuildingTiles.destroyLowestFloor(self)
            BuildingTiles.drawNewFloor(self)
            tile_life_points[0] = 5
            tile_life_points[1] = 5
            tile_life_points[2] = 5
            tile_life_points[3] = 5
            tile_life_points[4] = 5

        