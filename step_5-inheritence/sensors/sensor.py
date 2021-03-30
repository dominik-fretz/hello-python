# sensor.py
class Sensor:
    def __init__(self, _sensorType):
        self.sensorType = _sensorType
        self.name = ""

    def __str__(self):
        return "Type: {} - Name: {} - value: {}".format(
            self.sensorType, self.name, self.get_value()
        )

    def get_value(self):
        return {}

    def read_sensor(self):
        value = self.get_value()
        return {"type": self.sensorType, "name": self.name, "value": value}
