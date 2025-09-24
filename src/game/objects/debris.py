from game.objects.falling_proyectile import FallingProyectile


class Debris(FallingProyectile):
    def update(self):
        return super().update()
    
    def on_floor_hit(self):
        return super().on_floor_hit()
    
    def on_player_hit(self):
        return super().on_player_hit()