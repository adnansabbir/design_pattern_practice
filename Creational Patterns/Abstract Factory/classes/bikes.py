from .abs_vehicle import Bike


class FuelBike(Bike):

    def seats(self) -> int:
        return 2

    def tyres(self) -> int:
        return 2


class ElectricBike(Bike):

    def seats(self) -> int:
        return 1

    def tyres(self) -> int:
        return 3
