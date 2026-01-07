# main.py - modulo principale del progetto
import file_utils

def main(file_path):
    # esempio di utilizzo del modulo file_utils
    num_lines = file_utils.count_lines(file_path)
    print(f"Il file {file_path} contiene {num_lines} righe.")