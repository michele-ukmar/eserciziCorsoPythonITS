# apertura di un file di testo in una path assoluta
import os
script_dir = os.path.dirname(__file__)
rel_path = "test/data.txt"

abs_file_path = os.path.join(script_dir, rel_path)
print(abs_file_path)

abs_file_path = os.path.join(script_dir,"test","data.txt")
print(abs_file_path)

file_prova = open(abs_file_path, 'w')
file_prova.write('ciao')
file_prova.close()