# create a dictionary of products
prodotti= {}
while True:
    try:
        prodotto = input("Inserisci il nome del prodotto: ")
        try:
            quantita = int(input("Inserisci la quantità disponibile: "))
        except:
            raise ValueError("La quantità deve essere un numero intero.")
        
        if quantita <= 0:
            raise ValueError("La quantità disponibile deve essere maggiore di 0.")
        
        if prodotto in prodotti:
            raise ValueError("Il prodotto è già presente nell'inventario.")
        
        prodotti[prodotto] = quantita
        if input("Vuoi inserire un altro prodotto? (s/n): ").strip().lower() != 's':
            break
    except ValueError as e:
        print(f"Errore: {e}")
        continue

# Inizio script
print("Benvenuto al sistema di gestione ordini!")
print("Prodotti disponibili:")
for prodotto, quantita in prodotti.items():
    print(f"- {prodotto}: {quantita} disponibili")

while True:
    try:
        # Richiesta input utente
        prodotto = input("\nInserisci il prodotto (o 'esci' per terminare): ").strip().lower()
        
        if prodotto == 'esci':
            print("Uscita dal programma. Grazie per aver ordinato!")
            break

        if prodotto not in prodotti:
            raise ValueError(f"Il prodotto '{prodotto}' non è disponibile.")

        # Tipo di operazione
        tipo_operazione = input("Inserisci 'aggiungi' per aggiungere un prodotto, 'rimuovi' per rimuoverlo: ").strip().lower()
        if tipo_operazione not in ['aggiungi', 'rimuovi']:
            raise ValueError("Operazione non valida. Devi scegliere tra 'aggiungi' o 'rimuovi'.")

        try:
            # Quantità richiesta
            quantita = int(input(f"Inserisci la quantità da movimentare per '{prodotto}': "))
        except ValueError:
            raise ValueError("La quantità deve essere un numero intero.")
                
        if tipo_operazione == 'aggiungi':
            if quantita <= 0:
                raise ValueError("La quantità da aggiungere deve essere maggiore di 0.")
            prodotti[prodotto] += quantita
            print(f"Aggiunta confermata: {quantita} {prodotto}(i). Disponibili: {prodotti[prodotto]}.")
            continue

        if tipo_operazione == 'rimuovi':
            if quantita <= 0:
                raise ValueError("La quantità da rimuovere deve essere maggiore di 0.")
            if quantita > prodotti[prodotto]:
                raise ValueError(f"Quantità richiesta ({quantita}) maggiore della disponibilità ({prodotti[prodotto]}).")
            prodotti[prodotto] -= quantita
            print(f"Rimozione confermata: {quantita} {prodotto}(i). Rimanenti: {prodotti[prodotto]}.")

    except ValueError as e:
        print(f"Errore: {e}")
    except Exception as e:
        print(f"Errore inaspettato: {e}")

# Fine script
print("\nInventario aggiornato:")
for prodotto, quantita in prodotti.items():
    print(f"- {prodotto}: {quantita} disponibili")