
languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

type(enumerate_prime)
# Output: <class 'enumerate'>

# convert enumerate object to list
print(list(enumerate_prime))

# Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]

print(list(enumerate_prime))

# Output: []    