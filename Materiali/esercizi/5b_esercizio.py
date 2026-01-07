
dati = []
nome = "-"
eta =0

while nome !="" and eta !="" :
    nome = input("Inserisci nome, a capo due volte per finire")
    eta =  input("Inserisci eta, a capo due volte per finire")
    if nome !="" and eta !="" :
        dati.append((nome,eta))

dizionario={}
for nome, eta in dati:
    if eta not in dizionario:
        dizionario[eta] = []
    dizionario[eta].append(nome)
    # lista = dizionario[eta]
    # lista.append(nome)
    # dizionario[eta] = lista
    
    # if eta not in dizionario:
    #     dizionario[eta] = [nome]
    # else:
    #     dizionario[eta].append(nome)

    for eta in list(dizionario.keys()):
        print("Età " + eta + "\n")
        for nome in dizionario[eta]:
            print ("- " + nome + "\n")

