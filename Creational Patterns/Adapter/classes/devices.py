import sys

sys.path.append("..")
from interfaces.connector_interfaces import DeviceInterface


class Blender110(DeviceInterface):

    def ampere(self) -> float:
        return 2

    def voltage(self) -> float:
        return 110

    def __str__(self):
        return f'{self.voltage()}v Blender'


class Blender220(DeviceInterface):
    def ampere(self) -> float:
        return 1

    def voltage(self) -> float:
        return 220

    def __str__(self):
        return f'{self.voltage()}v Blender'


def test():
    print("Creating a 110v device")
    device1 = Blender110()
    print(f"Created {device1.voltage()}v device")

    print("Creating a 220v device")
    device2 = Blender220()
    print(f"Created {device2.voltage()}v device")


if __name__ == "__main__":
    test()
