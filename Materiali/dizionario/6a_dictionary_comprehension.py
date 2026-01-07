
dizionario1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dizionario1)

# dizionario del doppio dei valori del dizionario1
dizionario1_doppio = {k:v*2 for (k,v) in dizionario1.items()}

print(dizionario1_doppio)