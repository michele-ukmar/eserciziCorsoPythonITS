# tests/main/test_main.py - test per il modulo principale main.py
import os
import sys

# Otteniamo il percorso assoluto della cartella `project`
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

# Aggiungiamo la cartella `project` al percorso di ricerca di Python
sys.path.append(project_path)

from unittest.mock import patch
import io
import main

def test_main():
    file_path = os.path.join(project_path, 'test/data/input.txt') 
    with patch('sys.stdout', new=io.StringIO()) as fake_output:
        main.main(file_path)
        assert fake_output.getvalue().strip() == 'Il file data/input.txt contiene 3 righe.'

# In questo esempio, abbiamo creato una funzione di test test_main 
# che utilizza la funzione main del modulo main.py e verifica che la 
# stringa di output prodotta dalla funzione corrisponda alla stringa 
# attesa "Il file data/input.txt contiene 3 righe.".

# Per catturare l'output prodotto dalla funzione main, abbiamo 
# utilizzato il modulo io per creare un oggetto StringIO, 
# che rappresenta un file di testo in memoria, e abbiamo 
# utilizzato la funzione patch del modulo unittest.mock 
# per sostituire lo standard output di Python con il nostro 
# oggetto StringIO. In questo modo, possiamo verificare l'output prodotto 
# dalla funzione main senza stamparlo effettivamente a schermo.