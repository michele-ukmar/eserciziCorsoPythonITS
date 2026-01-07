n = int(input("inserisci quanti sono i numeri da confrontare"))
numero = int(input("inserisci il primo numero da confrontare"))
max = numero
for i in range (1, n, 1):
    numero = int(input("inserisci il prossimo numero da confrontare"))
    if max < numero:
        max = numero
    
print ("il numero massimo è", max)

stringa1 = "prova 1"
stringa2 = "prova2"

stringa1[1:5:2]
stringa1[1:3]