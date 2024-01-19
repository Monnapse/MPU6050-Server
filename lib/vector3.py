"""
    Made by Monnapse
"""

class new:
    # CREATING
    def __init__(self, X:int = 0, Y:int = 0, Z:int = 0) -> None:
        self.X = X
        self.Y = Y
        self.Z = Z
    
    def __str__(self):
        return f"{self.X}, {self.Y}, {self.Z}"
    
    def __repr__(self):
        return "vector3"
    
    # MATHEMATICAL FUNCTIONS
    def __add__(self, vector):
        if not vector: return
        if not vector.X or not vector.Y or not vector.Z: return
        return new(self.X + vector.X, self.Y + vector.Y, self.Y + vector.Y)

    def __sub__(self, vector):
        if not vector: return
        if not vector.X or not vector.Y or not vector.Z: return
        return new(self.X - vector.X, self.Y - vector.Y, self.Y - vector.Y)