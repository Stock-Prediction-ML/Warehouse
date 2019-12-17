"""AbstractAPI
This file contains the abstract API for the data collection packages
"""

from abc import ABC, abstractmethod

class AbstractAPI(ABC):
    """This abstract class creates a API contract for the data collection packages
    """
    def __init__(self):
        """Class constructor"""
        super().__init__()

    @abstractmethod
    def connect(self) -> None:
        """Read the API keys and connect to the API if available"""
        raise NotImplementedError

    @abstractmethod
    def get(self):
        """Pull data from API"""
        raise NotImplementedError