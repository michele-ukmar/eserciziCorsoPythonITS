# Ora possiamo creare il modulo file_utils e implementare la funzione count_lines in modo 
# da soddisfare questi test:

# file_utils.py - modulo per gestire file di testo

def count_lines(file_path):
    with open(file_path, 'r') as file:
        return len(file.readlines())


# La funzione count_lines utilizza il costrutto with per garantire che il file venga 
# chiuso correttamente alla fine del blocco di codice. La funzione apre il file
#  specificato dal percorso file_path, legge tutte le righe del file usando il metodo 
# readlines() e restituisce il numero di righe usando la funzione len().

# Ora possiamo eseguire i nostri test utilizzando un framework di testing come 
# pytest e vedere se la nostra funzione count_lines passa tutti i test:
