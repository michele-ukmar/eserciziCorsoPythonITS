
# usando i metodi Getter and Setter
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

# crea un nuovo oggetto con il costruttore
human = Celsius(37)

# richiediamo la temperatura con il metodo getter
print(human.get_temperature())

# 37
# 98.60000000000001

# chiediamo la temperatura in gradi Fahrenheit
print(human.to_fahrenheit())

# imposta la temperatura con il metodo setter
human.set_temperature(-300)

# Output:
# Traceback (most recent call last):
#   File "<string>", line 30, in <module>
#   File "<string>", line 16, in set_temperature
# ValueError: Temperature below -273.15 is not possible.

# legge la temperatura con il metodo getter
print(human.to_fahrenheit())

