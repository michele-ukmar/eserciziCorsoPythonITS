nParole = int(input("Quante parole vuoi inserire? "))
parole = [None] * nParole
for i in range(nParole):
    print("inserisci parola numero", i + 1)
    parola = input()
    parole[i] = parola
for i in range(nParole-1):
    for j in range(i+1,nParole):
        if parole[i]>parole[j]:
            sostituzione = parole[i]
            parole[i] = parole[j]
            parole[j] = sostituzione
            
print("Le parole in ordine alfabetico sono:")
for i in range(nParole):
    print(parole[i])

