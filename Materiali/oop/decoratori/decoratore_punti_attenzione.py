from UFS02.decoratore_definizione import funzione_decoratore


def mia_funzione():
    print("Hello World!")

print(mia_funzione.__name__)

# mia_funzione

@funzione_decoratore
def mia_funzione():
    print("Hello World!")

print(mia_funzione.__name__)
# wrapper