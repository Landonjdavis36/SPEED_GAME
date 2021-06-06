class word:
    
    def __init__(self):
        
        super().__init__()
        self._segments = []
        self._prepare_size()
    
    def get_all(self):
       
        return self._segments

    def word_size(self):
     
        return self._segments[1:]

    def word_move(self):
   
        return self._segments[0]

    def word(self):
       
        tail = self._segments[-1]
        offset = word.get_velocity().reverse()
        text = 
        position = word.get_position().add(offset)
        velocity = word.get_velocity()
        self._add_segment(text, position, velocity)
    
    def mword_move(self, direction):
        
        count = len(self._segments) - 1
        for n in range(count, -1, -1):
            segment = self._segments[n]
            if n > 0:
                leader = self._segments[n - 1]
                velocity = leader.get_velocity()
                segment.set_velocity(velocity)
            else:
                segment.set_velocity(direction)
            segment.move_next()

    def _add_segment(self, text, position, velocity):
        
        segment = player()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)

    def _prepare_body(self):
    
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        for n in range(constants):
            position = Point(x - n, y)
            velocity = Point(1, 0)
            self._add_segment(text, position, velocity)




import sys
from game import constants
from asciimatics.widgets import Frame
