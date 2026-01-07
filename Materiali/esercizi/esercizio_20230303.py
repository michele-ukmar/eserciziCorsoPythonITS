import requests

# Scarichiamo il dizionario italiano dal sito web
response = requests.get("https://raw.githubusercontent.com/napolux/paroleitaliane/master/paroleitaliane/60000_parole_italiane.txt")
dizionario_scaricato = response.content.decode().splitlines()

import random
import numpy as np
import requests

def genera_griglia(dizionario_scaricato):
    # Definiamo le lettere disponibili nella griglia
    lettere_disponibili = "".join(set("".join(dizionario_scaricato)))

    # Generiamo una matrice 2D di lettere casuali
    griglia = np.array([[random.choice(lettere_disponibili) for _ in range(50)] for _ in range(50)])
    np.savetxt("griglia.txt", griglia, fmt="%s")

    return griglia

griglia = genera_griglia(dizionario_scaricato)


def trova_parole(griglia, dizionario):
    parole_trovate = []

    # Convertiamo la griglia in una lista di stringhe
    righe = ["".join(riga) for riga in griglia]

    # Aggiungiamo le colonne alla lista
    colonne = ["".join([riga[i] for riga in griglia]) for i in range(len(griglia[0]))]

    # Aggiungiamo le diagonali principali alla lista
    diagonali_principali = []
    for i in range(len(griglia)):
        diagonale = "".join([griglia[i+j][j] for j in range(len(griglia)-i)])
        diagonali_principali.append(diagonale)
        diagonale = "".join([griglia[j][i+j] for j in range(len(griglia)-i)])
        diagonali_principali.append(diagonale)

    # Aggiungiamo le diagonali secondarie alla lista
    diagonali_secondarie = []
    for i in range(len(griglia)):
        diagonale = "".join([griglia[i-j][j] for j in range(i+1)])
        diagonali_secondarie.append(diagonale)
        diagonale = "".join([griglia[len(griglia)-1-j][i+j-len(griglia)+1] for j in range(len(griglia)-i-1)])
        diagonali_secondarie.append(diagonale)

    # Uniamo tutte le possibili parole in una lista
    possibili_parole = righe + colonne + diagonali_principali + diagonali_secondarie

    # Troviamo le parole italiane nella lista
    for parola in possibili_parole:
        if parola in dizionario:
            parole_trovate.append(parola)
        elif parola[::-1] in dizionario:
            parole_trovate.append(parola[::-1])

    return parole_trovate

print(trova_parole(griglia, dizionario_scaricato))