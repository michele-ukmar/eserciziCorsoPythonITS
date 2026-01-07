# usando il decoratore @property ed il decoratore @temperature.setter
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# crea un nuovo oggetto con il costruttore
human = Celsius(37)
# Setting value...

print(human.temperature)
# Getting value...
# 37

print(human.to_fahrenheit())
# Getting value...
# 98.60000000000001

coldest_thing = Celsius(-300)
# Setting value...
# Traceback (most recent call last):
#   File "", line 29, in 
#   File "", line 4, in __init__
#   File "", line 18, in temperature
# ValueError: Temperature below -273 is not possible