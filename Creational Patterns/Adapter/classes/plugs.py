import sys

sys.path.append("..")
from interfaces.connector_interfaces import PlugInterface


# from ..interfaces.connector_interfaces import PlugInterface, ElectricInterface


class Plug110(PlugInterface):
    def ampere(self) -> float:
        return 2

    def voltage(self) -> float:
        return 110

    def __str__(self):
        return f'{self.voltage()}v Plug'


class Plug220(PlugInterface):
    def ampere(self) -> float:
        return 1

    def voltage(self) -> float:
        return 220

    def __str__(self):
        return f'{self.voltage()}v Plug'


class Plug440(PlugInterface):
    def ampere(self) -> float:
        return .25

    def voltage(self) -> float:
        return 440

    def __str__(self):
        return f'{self.voltage()}v Plug'


class PlugAdapter220(PlugInterface):
    def __init__(self, plug: PlugInterface):
        self.plug_to_convert = plug
        self.ratio = 220 / plug.voltage()

    def ampere(self) -> float:
        return self.plug_to_convert.ampere() / self.ratio

    def voltage(self) -> float:
        return self.plug_to_convert.voltage() * self.ratio

    def __str__(self):
        return f'110v to 220v plug Adapter'


def test():
    print("Creating a 110v Plug")
    device110 = Plug110()
    print(f"Created {device110.voltage()}v Plug")

    print("Creating a 220v plug")
    device220 = Plug220()
    print(f"Created {device220.voltage()}v Plug")

    print("Creating a 220v plug")
    device440 = Plug440()
    print(f"Created {device440.voltage()}v Plug")

    print("Creating a 220V plug from 440v plug")
    device_220_adap = PlugAdapter220(device440)
    print(f"Created {device_220_adap.voltage()}v Plug with Voltage: {device_220_adap.ampere()}amp")


if __name__ == "__main__":
    test()
