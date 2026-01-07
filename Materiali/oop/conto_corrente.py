
def salva_su_file_fun(self):
    with open("saldo.txt", "w") as file:
        file.write(f"{self.nome} {self.cognome} {self.saldo}")
    return self

def preleva_fun(self, importo):
    if self.saldo >= importo:
        self.saldo -= importo
        self.prova = "A"
        print(f"Prelevati {importo} euro")
    else:
        print("Saldo Insufficiente")
    return self

class conto_corrente(object):
    def __init__(self, nome, cognome, saldo):
        self.nome = nome
        self.cognome = cognome
        self.saldo = saldo
    def preleva(self, importo):
        self = preleva_fun(self, importo)
        print(self.prova)

    def salva_su_file(self):
        self = salva_su_file_fun(self)


cc = conto_corrente("Mario", "Rossi", 1000)
cc.preleva(500)
cc.salva_su_file()
# print private attribute
print(cc.saldo) # 500