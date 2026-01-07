quadrati = []

for n in range(10):
    quadrati.append(n**2)

print(quadrati)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# in alternativa usando list comprehension
quadrati = [n**2 for n in range(10)]

print(quadrati)
# Output:   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

