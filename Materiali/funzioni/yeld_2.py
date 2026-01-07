
def generate_numbers(n):
    yield 1
    yield 2
    yield 3
    yield 4

my_iter = iter(generate_numbers(10))
print(next(my_iter))
print(next(my_iter))

other_generator = generate_numbers(10)
print(next(other_generator))
print(next(other_generator))
