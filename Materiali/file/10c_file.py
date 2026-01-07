# Scrivere su un file 'proverbio.txt' un proverbio a scelta 
# Aprire il file proverbio.txt 
# Leggerne tutto il contenuto 
# Scrivere i caratteri in posizione pari su un file 'propari.txt' 
# Scrivere i caratteri in posizione dispari su un file 'prodisp.txt’ 

proverbio = '-'

file_proverbio = open('proverbio.txt', 'w')
while proverbio != '':
    proverbio = input('Inserisci un proverbio: ')
    if proverbio != '':
        file_proverbio.write(proverbio)

file_proverbio.close()

file_proverbio = open('proverbio.txt', 'r')
proverbio = file_proverbio.read()
file_proverbio_pari = open('file_proverbio_pari.txt', 'w')
file_proverbio_dispari = open('file_proverbio_dispari.txt', 'w')

for i, c in enumerate(proverbio):
    if i % 2 == 0:
        file_proverbio_pari.write(c)
    else:
        file_proverbio_dispari.write(c)

file_proverbio_pari.close()
file_proverbio_dispari.close()


