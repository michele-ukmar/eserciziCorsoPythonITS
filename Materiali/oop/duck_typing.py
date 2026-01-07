class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_quack(object):
    object.quack()

# create a Duck instance
donald = Duck()

# create a Person instance
john = Person()

# pass the Duck instance to the function
make_quack(donald) # Output: Quack, quack!

# pass the Person instance to the function
make_quack(john) # Output: I'm quacking like a duck!