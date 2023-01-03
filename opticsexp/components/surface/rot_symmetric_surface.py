from .abstract_surface import AbstractSurface
from .aperture import CircularAperture

class RotSymmetricSurface(AbstractSurface):
    def __init__(self):
        super().__init__(CircularAperture())
