from abc import ABC, abstractmethod


class FallingProyectile(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def on_floor_hit(self):
        pass

    @abstractmethod
    def on_player_hit(self):
        pass