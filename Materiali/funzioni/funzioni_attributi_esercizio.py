
def prova_generatore():
    prova_generatore.count +=1
    yield "Hello"
    prova_generatore.count +=1
    yield "World"
    prova_generatore.count +=1
    yield "!"


prova_generatore.count = 0
for i in prova_generatore():
    print(i)
print(prova_generatore.count)



