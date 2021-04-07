"""main.py"""
import sensor


first_sensor = sensor.Sensor()
first_sensor_data = first_sensor.read_sensor()

# sensor.Sensor.read_sensor()

print(first_sensor_data)
