from .sensor import Sensor


class PressureSensor(Sensor):
    def __init__(self, name):
        Sensor.__init__(self, name)

    def get_value(self):
        # go and get pressure
        return 1080
