
#somma di due numeri
add_numbers = lambda x, y: x + y
print(add_numbers(3, 5))  # Output: 8


#moltiplicazione di due numeri
multiply_numbers = lambda x, y: x * y
print(multiply_numbers(3, 5))  # Output: 15

# ordina una lista di tuple in base al secondo elemento della tupla
my_list = [(1, 4), (2, 1), (3, 5), (4, 2)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)  # Output: [(2, 1), (4, 2), (1, 4), (3, 5)]

def extractor(s):
    return s[1]
print(sorted(my_list, key=extractor))

# extractor = lambda s: s[1]
print(sorted(my_list, key=lambda s: s[1]))

# filtra una lista di numeri pari
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(filtered_list)  # Output: [2, 4, 6, 8, 10]

# mappa una funzione ad una lista di numeri
my_list = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x**2, my_list))
print(squared_list)  # Output: [1, 4, 9, 16, 25]
