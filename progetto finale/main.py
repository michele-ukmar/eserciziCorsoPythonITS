# Import della libreria tkinter per creare interfacce grafiche
import tkinter as tk
# Import dei widget avanzati e delle finestre di dialogo
from tkinter import ttk, messagebox
# Libreria requests per effettuare richieste HTTP
import requests
# Libreria io per gestire flussi di byte (immagini)
import io
# Libreria PIL (Pillow) per aprire e visualizzare immagini
from PIL import Image, ImageTk

# URL base dell'API Scryfall (per cercare carte Magic)
BASE_URL = "https://api.scryfall.com/cards/search"

# Definizione della classe principale dell'applicazione
class CardViewerApp:
    def __init__(self, root):
        # Salva il riferimento alla finestra principale di Tkinter
        self.root = root
        # Imposta il titolo della finestra
        self.root.title("Magic Card Viewer")
        # Imposta la dimensione iniziale della finestra (larghezza x altezza)
        self.root.geometry("1300x800")
        # Lista per mantenere i riferimenti alle immagini caricate (evita garbage collection)
        self.images = []
        # Crea una sessione HTTP persistente per riutilizzare la connessione
        self.session = requests.Session()
        # Costruisce l'interfaccia grafica chiamando il metodo dedicato
        self.build_ui()

    # ---------------- INTERFACCIA GRAFICA ----------------

    def build_ui(self):
        """Crea l'interfaccia grafica"""
        # Crea un frame dentro la finestra principale per contenere i campi di input
        input_frame = ttk.Frame(self.root)
        # Lo posiziona con un po' di margine verticale
        input_frame.pack(pady=10)

        # Dizionario per salvare i riferimenti agli Entry (campi di input)
        self.entries = {}

        # Etichette dei campi di ricerca
        labels = [
            "Nome carta",
            "Colori (w u b r g)",
            "Tipo",
            "Testo regole"
        ]

        # Ciclo per creare dinamicamente le label e i campi di input
        for i, label in enumerate(labels):
            # Crea una label descrittiva e la mette nella griglia (riga i, colonna 0)
            ttk.Label(input_frame, text=label).grid(row=i, column=0, sticky="w")

            # Crea un campo di input testuale largo 30 caratteri
            entry = ttk.Entry(input_frame, width=30)
            # Lo posiziona nella colonna 1, stessa riga
            entry.grid(row=i, column=1, padx=5)

            # Salva il riferimento nel dizionario usando il testo della label come chiave
            self.entries[label] = entry

        # Crea un pulsante "Cerca" che quando premuto chiama il metodo start_search
        ttk.Button(
            input_frame,
            text="Cerca",
            command=self.start_search
        ).grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Crea un canvas dove mostrare i risultati della ricerca
        self.canvas = tk.Canvas(self.root)

        # Crea una scrollbar verticale collegata al canvas
        self.scrollbar = ttk.Scrollbar(
            self.root,
            orient="vertical",
            command=self.canvas.yview
        )

        # Crea un frame interno al canvas che conterrà i risultati
        self.results_frame = ttk.Frame(self.canvas)

        # Quando il frame cambia dimensione aggiorna l'area scrollabile del canvas
        self.results_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Inserisce il frame dei risultati nel canvas (in alto a sinistra)
        self.canvas.create_window((0, 0), window=self.results_frame, anchor="nw")

        # Collega la scrollbar al canvas (per scorrere verticalmente)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Posiziona il canvas a sinistra, riempiendo spazio disponibile e permettendo espansione
        self.canvas.pack(side="left", fill="both", expand=True)
        # Posiziona la scrollbar a destra, occupando tutta l'altezza verticale
        self.scrollbar.pack(side="right", fill="y")

    # ---------------- RICERCA ----------------

    def start_search(self):
        """Avvia la ricerca"""
        # Costruisce la query da inviare all'API a partire dai campi di input
        query = self.build_query()

        # Se la query è vuota (nessun parametro), mostra un messaggio di avviso e ritorna
        if not query:
            messagebox.showwarning("Attenzione", "Inserisci almeno un parametro")
            return

        # Pulisce eventuali risultati precedenti eliminando i widget figli del frame risultati
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        # Pulisce la lista delle immagini caricate
        self.images.clear()

        # Effettua la ricerca chiamando il metodo dedicato
        self.search_cards(query)

    def build_query(self):
        """Costruisce la query per Scryfall"""
        parts = []

        # Prende il valore inserito in "Nome carta" e rimuove spazi iniziali/finali
        name = self.entries["Nome carta"].get().strip()
        # Se è stato inserito un nome, aggiunge la parte corrispondente alla query
        if name:
            parts.append(f'name:"{name}"')

        # Prende i colori (esempio: "w u b"), li mette in minuscolo e li divide in lista
        colors = self.entries["Colori (w u b r g)"].get().strip().lower().split()
        # Se ci sono colori, aggiunge la parte "color<=" con i colori ordinati in query
        if colors:
            parts.append("color<=" + "".join(sorted(colors)))

        # Prende il tipo carta e aggiunge la parte alla query se presente
        card_type = self.entries["Tipo"].get().strip()
        if card_type:
            parts.append(f"type:{card_type}")

        # Prende il testo regole, lo divide in parole e costruisce query oracle:parola
        oracle = self.entries["Testo regole"].get().strip().lower()
        if oracle:
            parole = oracle.split()
            parts.append("(" + " ".join(f"oracle:{p}" for p in parole) + ")")

        # Unisce tutte le parti separate da spazi in una singola stringa
        return " ".join(parts)

    # ---------------- API ----------------

    def search_cards(self, query):
        """Effettua la richiesta all'API Scryfall"""
        try:
            # Parametri da inviare con la GET: la query costruita
            params = {"q": query}

            # Effettua la richiesta HTTP GET all'API con timeout di 10 secondi
            response = self.session.get(BASE_URL, params=params, timeout=10)
            # Se la risposta HTTP è un errore solleva eccezione
            response.raise_for_status()

            # Converte automaticamente la risposta JSON in dizionario Python
            data = response.json()

            # Se non ci sono risultati mostra messaggio e termina
            if "data" not in data or not data["data"]:
                self.show_message("Nessuna carta trovata.")
                return

            # Prende solo le prime 50 carte per non sovraccaricare la GUI
            cards = data["data"][:50]
            # Mostra le carte in interfaccia
            self.display_cards(cards)

        except Exception as e:
            # Se si verifica un errore (rete, timeout, JSON non valido...) mostra messaggio
            self.show_message(f"Errore: {e}")

    # ---------------- VISUALIZZAZIONE ----------------

    def display_cards(self, cards):
        """Mostra le carte"""
        max_cols = 4  # Numero massimo di carte per riga

        # Ciclo sulle carte enumerate (indice e carta)
        for index, card in enumerate(cards):
            # Calcola la riga
            row = index // max_cols
            # Calcola la colonna
            col = index % max_cols

            # Crea un frame per ogni carta con padding interno
            frame = ttk.Frame(self.results_frame, padding=10)
            # Posiziona il frame in griglia (row, col)
            frame.grid(row=row, column=col, padx=10, pady=10)

            # Crea una label temporanea per l'immagine (prima di scaricarla)
            img_label = ttk.Label(frame, text="Caricamento...")
            img_label.pack()

            # Testo informativo della carta (nome, set e rarità)
            info = (
                f"{card.get('name','?')}\n"
                f"Set: {card.get('set_name','?')}\n"
                f"Rarità: {card.get('rarity','?')}"
            )
            # Mostra le info in una label centrata con margine verticale
            ttk.Label(frame, text=info, justify="center").pack(pady=5)

            # Scarica e mostra l'immagine (sincrono, blocca GUI se lento)
            self.load_image(card, img_label)

    # ---------------- IMMAGINI ----------------

    def load_image(self, card, label):
        """Scarica e mostra l'immagine"""

        try:
            # Prova a recuperare l'url dell'immagine principale "normal"
            image_url = card.get("image_uris", {}).get("normal")

            # Se la carta ha doppia faccia, prende l'immagine della prima faccia
            if not image_url and "card_faces" in card:
                image_url = card["card_faces"][0].get("image_uris", {}).get("normal")

            # Se non c'è URL immagine, scrive messaggio nel label
            if not image_url:
                label.config(text="Immagine non disponibile")
                return

            # Scarica l'immagine con GET (timeout 10 secondi)
            response = self.session.get(image_url, timeout=10)
            response.raise_for_status()

            # Converte il contenuto byte in immagine PIL
            image = Image.open(io.BytesIO(response.content))

            # Ridimensiona l'immagine a 200x280 pixel con filtro di alta qualità
            image = image.resize((200, 280), Image.Resampling.LANCZOS)

            # Converte l'immagine PIL in formato compatibile Tkinter
            tk_image = ImageTk.PhotoImage(image)

            # Memorizza il riferimento all'immagine per evitare garbage collection
            self.images.append(tk_image)

            # Aggiorna la label con l'immagine (e rimuove il testo "Caricamento...")
            label.config(image=tk_image, text="")

        except Exception:
            # In caso di errore nel download o caricamento mostra messaggio
            label.config(text="Errore immagine")

    def show_message(self, text):
        """Mostra messaggi informativi"""
        # Mostra una finestra di dialogo con il messaggio fornito
        messagebox.showinfo("Info", text)

# ---------------- AVVIO ----------------

if __name__ == "__main__":
    # Crea la finestra principale Tkinter
    root = tk.Tk()
    # Crea l'applicazione passando la finestra
    app = CardViewerApp(root)
    # Avvia il loop principale dell'interfaccia grafica (evento)
    root.mainloop()
