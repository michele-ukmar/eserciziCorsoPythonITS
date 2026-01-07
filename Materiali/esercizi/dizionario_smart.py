nome = "-"
eta =0

dizionario={}
while nome !="" and eta !="" :
    nome = input("Inserisci nome, a capo due volte per finire")
    eta =  input("Inserisci eta, a capo due volte per finire")
    if nome !="" and eta !="" :
        if eta not in dizionario:
            dizionario[eta] = []
        dizionario[eta].append(nome)    


    for eta in list(dizionario.keys()):
        print("Età " + eta + "\n")
        for nome in dizionario[eta]:
            print ("- " + nome + "\n")

