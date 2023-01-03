from .aperture import Aperture

class AbstractSurface:
    def __init__(self, aperture: Aperture):
        self.aperture: Aperture = aperture