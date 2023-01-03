class Aperture:
    def __init__(self):
        pass

class RectangularAperture:
    def __init__(self, width: float, height: float):
        super().__init__()
        self.width = None
        self.height = None
        
    def set_width_height(self, width: float, height: float):
        self.width = width
        self.height = height

class CircularAperture:
    def __init__(self):
        super().__init__()
        self.diameter = None

    def set_diameter(self, diameter: float):
        self.diameter = diameter