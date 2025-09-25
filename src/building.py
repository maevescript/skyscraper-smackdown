import arcade

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
        
        self.build = arcade.Sprite("C:/Users/rhbtz/Desktop/skyscraper-smackdown/assets/build_1_1.png")
        self.build.center_x = 1280/2
        self.build.center_y = 700
        self.sprite_list.append(self.build)

        self.physics_engine.add_sprite(
            self.build,
            mass=2.0,
            friction=0.6,
            elasticity=0.5,
            body_type=arcade.PymunkPhysicsEngine.DYNAMIC,
            moment_of_inertia=arcade.PymunkPhysicsEngine.MOMENT_INF 
        )

        self.build2 = arcade.Sprite("C:/Users/rhbtz/Desktop/skyscraper-smackdown/assets/build_1_2.png")
        self.build2.center_x = 1280/2
        self.build2.center_y = 1000
        self.sprite_list.append(self.build2)
        
        self.physics_engine.add_sprite(
            self.build2,
            mass=1.5,
            friction=0.6,
            elasticity=0.5,
            body_type=arcade.PymunkPhysicsEngine.DYNAMIC,
            moment_of_inertia=arcade.PymunkPhysicsEngine.MOMENT_INF 
        )

        self.build3 = arcade.Sprite("C:/Users/rhbtz/Desktop/skyscraper-smackdown/assets/build_1_2.png")
        self.build3.center_x = 1280/2
        self.build3.center_y = 1300
        self.sprite_list.append(self.build3)
        
        self.physics_engine.add_sprite(
            self.build3,
            mass=1.0,
            friction=0.6,
            elasticity=0.5,
            body_type=arcade.PymunkPhysicsEngine.DYNAMIC,
            moment_of_inertia=arcade.PymunkPhysicsEngine.MOMENT_INF 
        )

        self.build4 = arcade.Sprite("C:/Users/rhbtz/Desktop/skyscraper-smackdown/assets/build_1_2.png")
        self.build4.center_x = 1280/2
        self.build4.center_y = 1600
        self.sprite_list.append(self.build4)
        
        self.physics_engine.add_sprite(
            self.build4,
            mass=1.0,
            friction=0.6,
            elasticity=0.5,
            body_type=arcade.PymunkPhysicsEngine.DYNAMIC,
            moment_of_inertia=arcade.PymunkPhysicsEngine.MOMENT_INF  
        )

    def drawStartBuild(self):
        self.sprite_list.draw()
        print
        
    def drawNewFloor(self):
        newFloor = arcade.Sprite("C:/Users/rhbtz/Desktop/skyscraper-smackdown/assets/build_1_2.png")
        newFloor.center_x = 640
        newFloor.center_y = 1500
        self.sprite_list.append(newFloor)

        tipo_cuerpo = arcade.PymunkPhysicsEngine.DYNAMIC 

        self.physics_engine.add_sprite(
            newFloor,
            mass=1.0, 
            friction=0.6,
            elasticity=0.7,
            body_type=tipo_cuerpo,
            moment_of_inertia=arcade.PymunkPhysicsEngine.MOMENT_INF
        )

    def destroyLowestFloor(self, floor):
        pass