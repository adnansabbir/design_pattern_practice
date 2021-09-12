from abc import ABC, abstractmethod
from .abs_vehicle import Car, Bike


class VehicleFactory(ABC):
    """
    Interface of a vehicle factory
    """

    @abstractmethod
    def create_car(self) -> Car:
        """
        Creates a car
        :return: Car
        """
        pass

    @abstractmethod
    def create_bike(self) -> Bike:
        """
        Creates a bike
        :return: Bike
        """
        pass
