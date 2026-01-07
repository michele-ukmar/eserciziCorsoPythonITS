# voler copiare le righe pari di un file di testo chiamato 
# file_di_prova.txt (già esistente!) su un file chiamato 
# pari.txt e le righe dispari su un file chiamato dispari.txt 

file_in = open('file_di_prova.txt', 'r')
file_out_pari = open('pari.txt', 'w')
file_out_dispari = open('dispari.txt', 'w')

for i, line in enumerate(file_in):
    if i % 2 == 0:
        file_out_pari.write(line)
    else:
        file_out_dispari.write(line)

file_in.close()
file_out_pari.close()
file_out_dispari.close()