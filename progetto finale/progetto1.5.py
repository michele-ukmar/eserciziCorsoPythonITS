# Import della libreria tkinter per creare interfacce grafiche
import tkinter as tk
# Import dei widget avanzati di tkinter (bottoni, label, frame, ecc.)e delle finestre di dialogo (messagebox)
from tkinter import ttk, messagebox
# urllib serve per effettuare richieste HTTP senza librerie esterne
import urllib.request      # per aprire URL
import urllib.parse        # per codificare correttamente le query
# json serve per interpretare la risposta dell'API Scryfall
import json
# threading permette di eseguire operazioni in parallelo evitando il blocco dell'interfaccia grafica
import threading
# io serve per gestire stream di byte (immagini scaricate)
import io
# PIL (Pillow) serve per aprire, modificare e visualizzare immagini
from PIL import Image, ImageTk

# URL base dell'API di Scryfall per cercare le carte
BASE_URL = "https://api.scryfall.com/cards/search?q="

# Classe principale dell'applicazione
class CardViewerApp:
    def __init__(self, root):
        # Riferimento alla finestra principale di tkinter
        self.root = root
        # Titolo della finestra
        self.root.title("Magic Card Viewer")
        # Dimensione iniziale della finestra (larghezza x altezza)
        self.root.geometry("1300x800")
        # Lista che mantiene i riferimenti alle immagini caricate
        # NECESSARIA per evitare che Python le elimini (garbage collection)
        self.images = []
        # Costruzione dell'interfaccia grafica
        self.build_ui()

    # ---------------- INTERFACCIA GRAFICA ----------------

    def build_ui(self):
        """Crea tutta l'interfaccia grafica dell'applicazione"""
        # Frame superiore che contiene i campi di ricerca
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)

        # Dizionario che conterrà tutte le Entry di input
        self.entries = {}

        # Etichette dei campi di ricerca
        labels = [
            "Nome carta",
            "Colori (w u b r g)",
            "Tipo",
            "Testo regole"
        ]

        # Creazione dinamica delle label e delle entry
        for i, label in enumerate(labels):
            # Label descrittiva
            ttk.Label(input_frame, text=label).grid(row=i, column=0, sticky="w")

            # Campo di input testuale
            entry = ttk.Entry(input_frame, width=30)
            entry.grid(row=i, column=1, padx=5)

            # Salvataggio dell'entry nel dizionario
            self.entries[label] = entry

        # Pulsante di ricerca che avvia la funzione start_search
        ttk.Button(
            input_frame,
            text="Cerca",
            command=self.start_search
        ).grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Canvas che conterrà i risultati (necessario per lo scrolling)
        self.canvas = tk.Canvas(self.root)

        # Scrollbar verticale collegata al canvas
        self.scrollbar = ttk.Scrollbar(
            self.root,
            orient="vertical",
            command=self.canvas.yview
        )

        # Frame interno al canvas dove verranno inserite le carte
        self.results_frame = ttk.Frame(self.canvas)

        # Aggiorna automaticamente l'area scrollabile quando il contenuto cambia
        self.results_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Inserisce il frame dei risultati dentro il canvas
        self.canvas.create_window((0, 0), window=self.results_frame, anchor="nw")

        # Collega scrollbar e canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Posizionamento canvas e scrollbar nella finestra
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    # ---------------- RICERCA ----------------

    def start_search(self):
        """Avvia la ricerca in un thread separato"""

        # Costruisce la query per Scryfall
        query = self.build_query()

        # Se non è stato inserito alcun parametro, mostra avviso
        if not query:
            messagebox.showwarning("Attenzione", "Inserisci almeno un parametro")
            return

        # Rimuove i risultati precedenti dalla GUI
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        # Pulisce la lista delle immagini precedenti
        self.images.clear()

        # Avvia la ricerca in un thread separato
        # (evita il congelamento dell'interfaccia)
        threading.Thread(
            target=self.search_cards,
            args=(query,),
            daemon=True
        ).start()

    def build_query(self):
        """Costruisce correttamente la query per l'API Scryfall"""

        parts = []  # parti della query

        # Ricerca per nome carta
        name = self.entries["Nome carta"].get().strip()
        if name:
            parts.append(f'name:"{name}"')

        # Ricerca per colore (at most questi colori)
        colors = self.entries["Colori (w u b r g)"].get().strip().lower().split()
        if colors:
            parts.append("color<=" + "".join(sorted(colors)))

        # Ricerca per tipo carta
        card_type = self.entries["Tipo"].get().strip()
        if card_type:
            parts.append(f"type:{card_type}")

        # Ricerca nel testo delle regole (oracle)
        oracle = self.entries["Testo regole"].get().strip().lower()
        if oracle:
            parole = oracle.split()
            # Ogni parola diventa oracle:parola (AND logico)
            parts.append("(" + " ".join(f"oracle:{p}" for p in parole) + ")")

        # Unisce tutte le parti della query
        return " ".join(parts)

    # ---------------- RICHIESTA API ----------------

    def search_cards(self, query):
        """Effettua la richiesta HTTP all'API Scryfall"""

        try:
            # Codifica correttamente la query per l'URL
            url = BASE_URL + urllib.parse.quote(query)

            # Apertura dell'URL e lettura risposta
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode())

            # Se non ci sono risultati
            if "data" not in data or not data["data"]:
                self.show_message("Nessuna carta trovata.")
                return

            # Limita a 30 carte per non sovraccaricare la GUI
            cards = data["data"][:30]

            # Aggiorna la GUI nel thread principale
            self.root.after(0, lambda: self.display_cards(cards))

        except Exception as e:
            # Gestione degli errori di rete o parsing
            self.show_message(f"Errore: {e}")

    # ---------------- VISUALIZZAZIONE ----------------

    def display_cards(self, cards):
        """Mostra le carte in una griglia (immagine + informazioni)"""

        max_cols = 3  # numero di carte per riga

        for index, card in enumerate(cards):
            # Calcolo riga e colonna
            row = index // max_cols
            col = index % max_cols

            # Frame che contiene una singola carta
            frame = ttk.Frame(self.results_frame, padding=10)
            frame.grid(row=row, column=col, padx=10, pady=10)

            # Label temporanea per l'immagine
            img_label = ttk.Label(frame, text="Caricamento...")
            img_label.pack()

            # Testo informativo della carta
            info = (
                f"{card.get('name','?')}\n"
                f"Set: {card.get('set_name','?')}\n"
                f"Rarità: {card.get('rarity','?')}"
            )
            ttk.Label(frame, text=info, justify="center").pack(pady=5)

            # Avvia il caricamento dell'immagine in un thread separato
            threading.Thread(
                target=self.load_image,
                args=(card, img_label),
                daemon=True
            ).start()

    # ---------------- IMMAGINI ----------------

    def load_image(self, card, label):
        """Scarica e visualizza l'immagine della carta usando PIL"""

        try:
            # Recupera l'URL dell'immagine
            image_url = card.get("image_uris", {}).get("normal")

            # Gestione carte con doppia faccia
            if not image_url and "card_faces" in card:
                image_url = card["card_faces"][0].get("image_uris", {}).get("normal")

            # Se non esiste un'immagine
            if not image_url:
                self.root.after(0, lambda: label.config(text="Immagine non disponibile"))
                return

            # Scarica l'immagine come byte
            with urllib.request.urlopen(image_url) as response:
                image_bytes = response.read()

            # Converte i byte in immagine PIL
            image = Image.open(io.BytesIO(image_bytes))

            # Ridimensiona l'immagine
            image = image.resize((200, 280), Image.Resampling.LANCZOS)

            # Converte l'immagine in formato compatibile con tkinter
            tk_image = ImageTk.PhotoImage(image)

            # Mantiene riferimento per evitare garbage collection
            self.images.append(tk_image)

            # Aggiorna la GUI nel thread principale
            self.root.after(0, lambda: label.config(image=tk_image, text=""))

        except Exception:
            # In caso di errore nel download o caricamento
            self.root.after(0, lambda: label.config(text="Errore immagine"))

    def show_message(self, text):
        """Mostra un messaggio informativo"""
        self.root.after(0, lambda: messagebox.showinfo("Info", text))



if __name__ == "__main__":
    # Creazione finestra principale
    root = tk.Tk()

    # Istanziazione dell'applicazione
    app = CardViewerApp(root)

    # Avvio del loop principale di tkinter
    root.mainloop()
