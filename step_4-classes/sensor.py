"""sensor.py"""


class Sensor:
    def __init__(self):
        self.sensorName = "sensor-01"

    def read_sensor(self):
        return {"source": self.sensorName, "value": 4.2}
