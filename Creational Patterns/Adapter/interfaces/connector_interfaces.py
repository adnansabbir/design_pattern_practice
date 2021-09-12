from abc import ABC, abstractmethod, ABCMeta


class ElectricInterface(ABC):
    """An interface that determines an electric device"""

    __metaclass__ = metaclass = ABCMeta

    @abstractmethod
    def voltage(self) -> float:
        """Returns the voltage at what the device runs"""
        pass

    @abstractmethod
    def ampere(self) -> float:
        """Returns the voltage at what the device runs"""
        pass

    def wattage(self) -> float:
        """Returns the total wattage required"""
        return self.voltage() * self.ampere()


class PlugInterface(ElectricInterface, ABC):
    """A Plug interface that determines voltage, current and wattage to be provided"""

    def connect(self, device):
        """Method to connect a device"""
        device.plug(self)


class DeviceInterface(PlugInterface, ABC):
    """A Device interface that determines voltage, current and wattage required"""

    def plug(self, plug: PlugInterface):
        """Method to use the device"""
        if plug.voltage != self.voltage():
            raise ValueError(f"Voltage mismatch Source: {plug.voltage}v, required: {self.voltage()}v")
        if plug.ampere != self.ampere():
            raise ValueError(f"amp mismatch Source: {plug.voltage}amp, required: {self.voltage()}amp")

        print(f'Device plugged in and is running at {self.wattage()} watt')
