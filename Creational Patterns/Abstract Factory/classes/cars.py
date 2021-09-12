from .abs_vehicle import Car


class FuelCar(Car):

    def seats(self) -> int:
        return 5

    def tyres(self) -> int:
        return 4


class ElectricCar(Car):

    def seats(self) -> int:
        return 2

    def tyres(self) -> int:
        return 4
