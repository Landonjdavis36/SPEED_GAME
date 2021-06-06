class Point:
    
    
    def __init__(self, x, y):
        
        self._x = x
        self._y = y

    def add(self, other):
        

        Args:
            self (Point): An instance of Point.
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
      
      
      
      Gets the horizontal distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The horizontal distance.
        
        return self._x

    def get_y(self):
     
        return self._y

    def reverse(self):
      
        x = self._x * -1
        y = self._y * -1
        return Point(x, y)

