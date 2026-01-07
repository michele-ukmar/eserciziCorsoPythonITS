# scopo globale
variabile_globale = 78

def funzione(Y):
    # definizion di variabile globale dall'interno di una funzione
    global var_glob
    # scopo locale con accesso alla variabile globale
    variabile_locale = variabile_globale + Y
    var_glob = 8
    print(variabile_locale)

print(funzione(2))

print(var_glob)

# genera errore
# print(variabile_locale)

#esempio di funzione nonlocal

def funzione_prova():
  x = "Gianni"
  def funzione_prova_interna():
    # nonlocal x
    # x = "ciao"
    def funzione_prova_interna_2():
      # cerca x e la trova secondo la definizione di enclosed (LEGB)
      nonlocal x
      x = "ciao_2"
    funzione_prova_interna_2()
    print(x)
  funzione_prova_interna() 
  return x

print(funzione_prova())
