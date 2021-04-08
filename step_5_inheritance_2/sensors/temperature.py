from .sensor import Sensor


class TemperatureSensor(Sensor):
    def __init__(self, name):
        Sensor.__init__(self, name)

    def get_value(self):
        # Go and get the temperature from the Hardware sensor
        return 42
