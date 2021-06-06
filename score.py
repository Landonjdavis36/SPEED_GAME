import random
from game.player import player
from game.point import Point

class Score(player):
   
    def __init__(self):
        
        super().__init__()
        self._points = 0
        position = Point(1, 0)
        self.set_position(position)
        self.set_text(f"Score: {self._points}")
    
    def add_points(self, points):
       
        self._points += points
        self.set_text(f"Score: {self._points}")







from game import constants
from game.player import player
from game.point import Point
