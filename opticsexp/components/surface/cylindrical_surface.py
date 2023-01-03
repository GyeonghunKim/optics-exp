from .abstract_surface import AbstractSurface
from .aperture import RectangularAperture

class CylindricalSurface(AbstractSurface):
    def __init__(self):
        super().__init__(RectangularAperture())
        