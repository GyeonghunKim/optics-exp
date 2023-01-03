from .abstract_component import AbstractComponent
from .surface import Surface

import numpy as np
from numpy.typing import NDArray

class LensComponent(AbstractComponent):
    def __init__(self, component_name: str):
        """LensComponent which contains one lens and pivot.

        Args:
            component_name (str): Initialize lens component with its name. 
        """
        super().__init__(component_name)
        self.surface_1: Surface = None
        self.surface_2: Surface = None
        self.surface_1_distance: float = None
        self.surface_2_distance: float = None

    def set_lens_from_zmx(self, file_name: str):
        """Setup lens from Zemax *.zmx file

        Args:
            file_name (str): zmx file name
        """
        pass

    def set_custom_surfaces(self, surface_1: Surface, surface_2: Surface, surface_1_distance: float, surface_2_distance: float):
        """Setup Custom surfaces for lens component

        Args:
            surface_1 (Surface): Surface 1
            surface_2 (Surface): Surface 2
            surface_1_distance (float): Surface 1 distance
            surface_2_distance (float): Surface 2 distance
        """
        self.surface_1 = surface_1
        self.surface_2 = surface_2
        self.surface_1_distance = surface_1_distance
        self.surface_2_distance = surface_2_distance

    def C0_to_C1(self, C0: NDArray):
        """ Change optical axis coordinate to surface 1 coordinate

        Args:
            C0 (NDArray): Points (x, y) from Surface 1 coordinate with shape (n_points, 3)
        """
        x_0 = C0[:, 0]
        y_0 = C0[:, 1]
        z_0 = C0[:, 2]

        x_1 = self.pivot[0] + (self.parameter[0] + self.surface_1_distance) * np.cos(self.parameter[1]) + x_0 * np.cos(self.parameter[1]) - y_0 * np.sin(self.parameter[1])
        y_1 = self.pivot[1] + (self.parameter[0] + self.surface_1_distance) * np.sin(self.parameter[1]) + x_0 * np.sin(self.parameter[1]) + y_0 * np.cos(self.parameter[1])
        z_1 = z_0

        return np.array([x_1, y_1, z_1]).T


    def C0_to_C2(self, C0: NDArray):
        """ Change optical axis coordinate to surface 2 coordinate

        Args:
            C0 (NDArray): Points (x, y) from Surface 1 coordinate with shape (n_points, 3)
        """
        x_0 = C0[:, 0]
        y_0 = C0[:, 1]
        z_0 = C0[:, 2]

        x_2 = self.pivot[0] + (self.parameter[0] + self.surface_2_distance) * np.cos(self.parameter[1]) + x_0 * np.cos(self.parameter[1]) - y_0 * np.sin(self.parameter[1])
        y_2 = self.pivot[1] + (self.parameter[0] + self.surface_2_distance) * np.sin(self.parameter[1]) + x_0 * np.sin(self.parameter[1]) + y_0 * np.cos(self.parameter[1])
        z_2 = z_0

        return np.array([x_2, y_2, z_2]).T