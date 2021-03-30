# pressureSensor.py
from .sensor import Sensor


class PressureSensor(Sensor):
    def __init__(self, name):
        Sensor.__init__(self, "pressure")
        self.name = name

    def get_value(self):
        return 1008.2
