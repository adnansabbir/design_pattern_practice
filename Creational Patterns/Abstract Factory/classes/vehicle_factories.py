from .abs_vehicle_factory import VehicleFactory
from .abs_vehicle import Bike, Car
from .cars import FuelCar, ElectricCar
from .bikes import FuelBike, ElectricBike


class FuelVehicleFactory(VehicleFactory):
    """This factory creates vehicles driven with fuel"""

    def create_bike(self) -> Bike:
        return FuelBike()

    def create_car(self) -> Car:
        return FuelCar()


class ElectricVehicleFactory(VehicleFactory):
    """This factory creates electric vehicles"""

    def create_bike(self) -> Bike:
        return ElectricBike()

    def create_car(self) -> Car:
        return ElectricCar()