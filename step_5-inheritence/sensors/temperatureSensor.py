# Temperatur sensor
from .sensor import Sensor


class TemperatureSensor(Sensor):
    def __init__(self, name):
        Sensor.__init__(self, "temperature")
        self.name = name

    def get_value(self):
        return 23.5
