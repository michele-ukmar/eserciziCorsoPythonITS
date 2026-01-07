import string

def sommaLista(lista):
    listaSomma = 0
    for i in lista:
        listaSomma += i
    return listaSomma

def sostituzioneVocali(inputString):
    vocali = "aeiouAEIOU"
    for vocale in vocali:
        inputString = inputString.replace(vocale, "-")
    return inputString

def intersezioneListe(lista1, lista2):
    elementiComuni = []
    for i in lista1:
        if i in lista2:
            elementiComuni.append(i)
    return elementiComuni

if __name__ == "__main__":
    listaSomma = []

    while True:
        listaSomma.append(int(input("Inserisci un numero (0 per terminare): ")))
        if 0 in listaSomma:
            listaSomma.remove(0)
            break

    parolaDaSostituire = input("Inserisci una frase: ")
    lista1 = []
    lista2 = []
    while True:
        lista1.append(int(input("Inserisci un numero per la prima lista (0 per terminare): ")))
        if 0 in lista1:
            lista1.remove(0)
            break
    for i in lista1:
        lista2.append(int(input("Inserisci un numero per la seconda lista: ")))


    listaNuova = sommaLista(listaSomma)
    fraseNuova = sostituzioneVocali(parolaDaSostituire)
    elementiComuni = intersezioneListe(lista1, lista2)

    print(listaNuova)
    print("---")
    print(fraseNuova)
    print("---")
    print(elementiComuni)
