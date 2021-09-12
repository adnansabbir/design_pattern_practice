from classes.vehicle_factories import FuelVehicleFactory, ElectricVehicleFactory, VehicleFactory, Car, Bike


def manufacture_car(factory: VehicleFactory) -> Car:
    return factory.create_car()


def manufacture_bike(factory: VehicleFactory) -> Bike:
    return factory.create_bike()


if __name__ == "__main__":
    fuel_factory = FuelVehicleFactory()
    electric_factory = ElectricVehicleFactory()

    # Creating an Electric bike
    electric_bike = manufacture_bike(electric_factory)
    print(electric_bike)

    # Creating an Fuel car
    fuel_car = manufacture_car(fuel_factory)
    print(fuel_car)
