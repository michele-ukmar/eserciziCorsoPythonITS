from colorama import Fore

class rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza
    
    def print(self):
        for i in range(self.altezza):
            if (i == 0 or i == self.altezza - 1):
                print("_" * self.base)
            else:
                print("|" + " " * (self.base - 2) + "|")

if __name__ == "__main__":
    r = rettangolo(10, 5)
    r.print()
# Path: UFS02/classe_cerchio.py
