"""
dati cliente 
pt. iva, nome azienda, cap, città, provincia, codice fiscale, indirizzo, telefono, email

opzione di aggiunta cliente e ricerca cliente
"""

registroClienti = { "ptIVA" : ["01234567890","09876543210","02345678901","03456789012","04567890123"],
                    "nomeAzienda" : ["Alfa Srl", "Beta Consulting S.p.A.", "Gamma Tech SRL", "Delta Logistica SNC", "Epsilon Design SRLS"],
                    "cap" : ["20121", "00184", "50123", "80133", "35121"],
                    "città" : ["Milano", "Roma", "Firenze", "Napoli", "Padova"],
                    "provincia" : ["MI", "RM", "FI", "NA", "PD"],
                    "codiceFiscale" : ["LFA12345A01F205Z", "BTC98765B02H501Y", "GMT23456C03E783P", "DLT34567D04L781X", "EPS45678E05P397Z"],
                    "indirizzo" : ["Via Roma 10", "Piazza Venezia 5", "Via dei Calzaiuoli 15", "Corso Umberto I 45", "Via Dante Alighieri 23"],
                    "telefono" : ["0234567890", "0667890123", "0551234567", "0812345678", "0498765432"],
                    "email" : ["info@alfasrl.it", "contatti@betaconsulting.it", "info@gammatech.it", "amministrazione@deltalogistica.it", "hello@epsilondesign.it"]
                }

def aggiungiCliente():
    registroClienti.get("ptIVA").append(input("Inserisci la partita IVA: "))
    registroClienti.get("nomeAzienda").append(input("Inserisci il nome dell'azienda: "))
    registroClienti.get("cap").append(input("Inserisci il CAP: "))  
    registroClienti.get("città").append(input("Inserisci la città: "))
    registroClienti.get("provincia").append(input("Inserisci la provincia: "))
    registroClienti.get("codiceFiscale").append(input("Inserisci il codice fiscale: "))
    registroClienti.get("indirizzo").append(input("Inserisci l'indirizzo: "))
    registroClienti.get("telefono").append(input("Inserisci il numero di telefono: "))
    registroClienti.get("email").append(input("Inserisci l'email: "))
    

def ricercaCliente(chiaveRicerca, datoRicerca):
    riga = registroClienti.get(chiaveRicerca).index(datoRicerca)
    if riga is not None:
        print ("-----")
        print("Cliente trovato:")
        print ("-----")
        for key, value in registroClienti.items():
            print(f"{key}: {value[riga]}")
        print ("-----")
    else:
        print("Cliente non trovato, controllare i dati inseriti.")
        print ("-----")
        aggiunta = int(input("Vuoi aggiungere questo cliente al registro? (1 = si)(2 = no)  "))
        if aggiunta == 1:
            aggiungiCliente()

chiavi = ["ptIVA", "nomeAzienda", "cap", "città", "provincia", "codiceFiscale", "indirizzo", "telefono", "email"]
while True:
    print("""benvenuto nel registro clienti
          seleziona un'opzione:
          1. aggiungi cliente
          2. ricerca cliente
          3. esci""")
    scelta = int(input("inserisci il numero dell'opzione scelta: "))
    print ("-----")
    if scelta == 1:
        aggiungiCliente()
    elif scelta == 2:
        while True:
            sceltaRicerca = input("""inserisci la tipologia di dato con la quale vuoi fare la ricerca (scrivere il nome completo):
                - ptIVA
                - nomeAzienda
                - cap    
                - città
                - provincia
                - codiceFiscale
                - indirizzo
                - telefono
                - email
                """)
            if sceltaRicerca in chiavi:
                break
        print ("-----")
        ricerca = input("inserisci il dato con cui vuoi fare la ricerca")
        ricercaCliente(sceltaRicerca, ricerca)
    elif scelta == 3:
        break
    else:
        print("opzione non valida, riprova")
        continue
