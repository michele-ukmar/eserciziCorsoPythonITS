# L'operatore " ** " viene utilizzato per accettare un numero variabile di argomenti con nome. Ad esempio, 
# la seguente funzione "print_person" accetta un numero variabile di argomenti con nome e li stampa:

def print_person(**person):
    for key, value in person.items():
        print(key + ": " + value)
        
# In questo caso, la funzione può accettare qualsiasi numero di argomenti con nome, 
# come ad esempio "name", "age", "city", ecc.

