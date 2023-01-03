import numpy as np
from numpy.typing import NDArray
class AbstractComponent:
    def __init__(self, component_name: str):
        """Initialize abstract component

        Args:
            component_name (str): component name
        """
        self.name: str = component_name
        self.pivot: NDArray[np.float64] = np.array([0., 0.]) # (x, y) coordinate with pivot
        self.parameter: NDArray[np.float64] = np.array([0., 0.]) # (r, \theta) parameters 

    def set_pivot(self, x: float, y: float):
        """Setup pivot points

        Args:
            x (float): pivot x coordinate
            y (float): pivot y coordinate
        """
        self.pivot = np.array([x, y])

    def set_parameter(self, r: float, theta: float):
        """Setup parameter values (r, theta)

        Args:
            r (float): moving distance 
            theta (float): tilting angle
        """
        self.parameter = np.array([r, theta])

