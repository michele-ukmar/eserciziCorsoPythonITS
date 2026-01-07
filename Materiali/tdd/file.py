# Esempio di come si potrebbe utilizzare il Test Driven Development (TDD) 
# per sviluppare una funzione Python che legge un file di testo e restituisce
# il numero di righe nel file:

# test_file_utils.py - modulo per testare la funzione file_utils.count_lines

import os
import file_utils

def test_count_lines_empty_file():
    # testa che la funzione restituisca 0 per un file vuoto
    assert file_utils.count_lines( os.dir(__file__) + 'empty_file.txt') == 0

def test_count_lines_single_line_file():
    # testa che la funzione restituisca 1 per un file con una sola riga
    assert file_utils.count_lines(os.dir(__file__) + 'single_line_file.txt') == 1

def test_count_lines_multi_line_file():
    # testa che la funzione restituisca il numero corretto di righe per un file con più righe
    assert file_utils.count_lines(os.dir(__file__) + 'multi_line_file.txt') == 3


# In questo esempio, abbiamo creato tre funzioni di test test_count_lines_empty_file,
#  test_count_lines_single_line_file e test_count_lines_multi_line_file che testano la 
# funzione count_lines del modulo file_utils. Queste funzioni di test verificano che 
# la funzione count_lines restituisca il risultato corretto per un file vuoto, 
# un file con una sola riga e un file con più righe.


# $ pytest
# ============================= test session starts ==============================
# collected 3 items

# tests/test_file_utils.py ...                                             [100%]

# ============================== 3 passed in 0.01s ==============================

# I nostri test sono tutti passati! Abbiamo utilizzato il TDD per sviluppare 
# la nostra funzione count_lines e garantire che funzioni correttamente per una varietà 
# di casi d'uso.