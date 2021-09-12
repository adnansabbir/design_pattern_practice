from abc import ABC, abstractmethod


class Car(ABC):
    """
    This is a car interface which defines the characteristics of a car
    """

    @abstractmethod
    def tyres(self) -> int:
        """Returns the number of doors a car has"""
        pass

    @abstractmethod
    def seats(self) -> int:
        """Returns the number of seats a car has"""
        pass


class Bike(ABC):
    """
    This is a bike interface which defines the characteristics of a bike
    """

    @abstractmethod
    def tyres(self) -> int:
        """Returns the number of tyres a bike has"""
        pass

    @abstractmethod
    def seats(self) -> int:
        """Returns the number of seats a bike has"""
        pass
