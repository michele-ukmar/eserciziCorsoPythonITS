class Duck:
    def __str__(self):
        return "I'm a duck!"

class Person:
    def __str__(self):
        return "I'm a person!"

def print_object(obj):
    print(obj)

# create a Duck instance
donald = Duck()

# create a Person instance
john = Person()

# pass the Duck instance to the function
print_object(donald) # Output: I'm a duck!

# pass the Person instance to the function
print_object(john) # Output: I'm a person!