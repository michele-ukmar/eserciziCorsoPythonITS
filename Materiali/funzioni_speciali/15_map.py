# sintassi: map(funzione, oggetto)
# map(funzione, oggetto)

def raddoppia(num): 
    return num*2 

for n in map(raddoppia, [1,2,3]):
    print(n)

print(list(map(raddoppia, [1,2,3])))