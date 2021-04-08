import sensors

# from .temperature import TemperatureSensor


def print_sensor_value(sensor):
    print("Sensor name: '{}' value: {}".format(sensor.name, sensor.get_value()))


firstSensor = sensors.PressureSensor("Pressure sensor 1")
secondSenor = sensors.TemperatureSensor("Temperature Sensor 1")
thirdSensor = sensors.PressureSensor("Pressure sensor 2")


print_sensor_value(firstSensor)
print_sensor_value(secondSenor)
print_sensor_value(thirdSensor)