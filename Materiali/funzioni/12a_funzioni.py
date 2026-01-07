# esempio di funzione annidata
def funzione_esterna():
    print("funzione esterna")
    def funzione_interna():
        print("funzione interna")
    funzione_interna()

# esempio di funzione assegna a una variabile
def scrivi_file():
    def scrivi_file(nome_file, riga):
        """scrive una riga in un file"""
        file = open(nome_file, "a")
        file.write(riga + "\n")
        file.close()
    i = 0
    while True:
        valore = input("digita qualcosa e conferma con invio, due invii per uscire")
        i += 1
        if i % 2 == 0:
            scrivi_file_pari = scrivi_file
            scrivi_file_pari("file_1.txt", valore)
        else:
            scrivi_file_dispari = scrivi_file
            scrivi_file_dispari("file_2.txt", valore)
            def conta_caratteri(nome_file):
                file = open(nome_file, "r")
                righe = file.readlines()
                file.close()
                return "numero righe" + str(len(righe))
            print(conta_caratteri("file_2.txt"))
        if valore == "":
            break

scrivi_file()

