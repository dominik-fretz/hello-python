# main
import sensors

temp = sensors.TemperatureSensor("Temp-1")
pressure = sensors.PressureSensor("Pressure-1")

print("Temperature: {}".format(temp))
print("Pressure: {}".format(pressure))
