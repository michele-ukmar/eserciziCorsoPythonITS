# creazione di un file di testo con 1000 righe
# aventi all'inizio di ogni riga il numero di riga
# e un testo composto da 100 caratteri casuali

import random as rd
import string

fileOut = open('file_di_prova.txt', 'w')
for i in range(1000):
    fileOut.write(str(i) + ' ' + \
        ''.join(rd.choices(string.ascii_letters, k=100)) + "\n")
    
fileOut.close()