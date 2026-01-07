class Calculator:
    def add(self, a, b):
        pass

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

class Calculator:
    def add(self, a, b):
        return a + b

def test_add_with_negative_numbers():
    calc = Calculator()
    assert calc.add(-2, 3) == 1

def test_add_with_zero():
    calc = Calculator()
    assert calc.add(0, 0) == 0


def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3


class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

def test_subtract_with_negative_numbers():
    calc = Calculator()
    assert calc.subtract(-2, -3) == 1

def test_subtract_with_zero():
    calc = Calculator()
    assert calc.subtract(0, 0) == 0



