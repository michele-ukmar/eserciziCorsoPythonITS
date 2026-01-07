# usando la proprietà della classe

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # proprietà dell'oggetto
    temperature = property(get_temperature, set_temperature)



human = Celsius(37)
# Setting value...

print(human.temperature)
# Getting value...
# 37

print(human.to_fahrenheit())
# Getting value...
# 98.60000000000001

human.temperature = -300

# raise ValueError("Temperature below -273.15 is not possible")
# ValueError: Temperature below -273.15 is not possible