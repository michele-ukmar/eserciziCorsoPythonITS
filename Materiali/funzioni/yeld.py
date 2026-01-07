

def generate_numbers(n):
    for i in range(n):
        yield i


my_iter = iter(generate_numbers(10))
print(next(my_iter))
print(next(my_iter))

other_generator = generate_numbers(10)
print(next(other_generator))
print(next(other_generator))

def extract_string(s):
    for i in range(len(s)):
        yield s[0:i]

my_iter = iter(extract_string('ciao'))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))