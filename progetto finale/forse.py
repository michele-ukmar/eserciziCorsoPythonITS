# Import della libreria tkinter per creare interfacce grafiche
import tkinter as tk

# Import dei widget avanzati di tkinter e delle finestre di dialogo
from tkinter import ttk, messagebox

# requests permette di effettuare richieste HTTP in modo semplice
import requests

# json serve per interpretare le risposte dell'API Scryfall
import json

# io serve per gestire flussi di byte (necessari per le immagini)
import io

# PIL (Pillow) permette di aprire, ridimensionare e visualizzare immagini
from PIL import Image, ImageTk


# URL base dell'API di Scryfall per la ricerca delle carte
BASE_URL = "https://api.scryfall.com/cards/search"


# Classe principale dell'applicazione
class CardViewerApp:
    def __init__(self, root):
        # Riferimento alla finestra principale
        self.root = root

        # Titolo della finestra
        self.root.title("Magic Card Viewer")

        # Dimensioni iniziali della finestra
        self.root.geometry("1300x800")

        # Lista per mantenere riferimenti alle immagini
        # Necessaria per evitare la garbage collection
        self.images = []

        # Sessione HTTP persistente (più efficiente di requests.get singoli)
        self.session = requests.Session()

        # Costruzione dell'interfaccia grafica
        self.build_ui()

    # ---------------- INTERFACCIA GRAFICA ----------------

    def build_ui(self):
        """Costruisce tutta l'interfaccia grafica"""

        # Frame superiore che contiene i campi di ricerca
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)

        # Dizionario che conterrà i campi di input
        self.entries = {}

        # Etichette dei campi di ricerca
        labels = [
            "Nome carta",
            "Colori (w u b r g)",
            "Tipo",
            "Testo regole"
        ]

        # Creazione dinamica di label e entry
        for i, label in enumerate(labels):
            # Label descrittiva
            ttk.Label(input_frame, text=label).grid(row=i, column=0, sticky="w")

            # Campo di input testuale
            entry = ttk.Entry(input_frame, width=30)
            entry.grid(row=i, column=1, padx=5)

            # Salvataggio dell'entry
            self.entries[label] = entry

        # Pulsante di ricerca
        ttk.Button(
            input_frame,
            text="Cerca",
            command=self.start_search
        ).grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Canvas per visualizzare i risultati con scrolling
        self.canvas = tk.Canvas(self.root)

        # Scrollbar verticale
        self.scrollbar = ttk.Scrollbar(
            self.root,
            orient="vertical",
            command=self.canvas.yview
        )

        # Frame interno al canvas che conterrà le carte
        self.results_frame = ttk.Frame(self.canvas)

        # Aggiorna automaticamente l'area scrollabile
        self.results_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Inserisce il frame dei risultati nel canvas
        self.canvas.create_window((0, 0), window=self.results_frame, anchor="nw")

        # Collega scrollbar e canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Posizionamento nella finestra
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    # ---------------- RICERCA ----------------

    def start_search(self):
        """Avvia la ricerca delle carte"""

        # Costruisce la query per Scryfall
        query = self.build_query()

        # Controllo input vuoto
        if not query:
            messagebox.showwarning("Attenzione", "Inserisci almeno un parametro")
            return

        # Rimuove i risultati precedenti
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        # Pulisce la lista delle immagini
        self.images.clear()

        # Avvia direttamente la ricerca (senza thread)
        self.search_cards(query)

    def build_query(self):
        """Costruisce la query secondo la sintassi di Scryfall"""

        parts = []

        # Nome carta
        name = self.entries["Nome carta"].get().strip()
        if name:
            parts.append(f'name:"{name}"')

        # Colori (at most questi colori)
        colors = self.entries["Colori (w u b r g)"].get().strip().lower().split()
        if colors:
            parts.append("color<=" + "".join(sorted(colors)))

        # Tipo carta
        card_type = self.entries["Tipo"].get().strip()
        if card_type:
            parts.append(f"type:{card_type}")

        # Testo delle regole (oracle)
        oracle = self.entries["Testo regole"].get().strip().lower()
        if oracle:
            parole = oracle.split()
            parts.append("(" + " ".join(f"oracle:{p}" for p in parole) + ")")

        # Ritorna la query finale
        return " ".join(parts)

    # ---------------- API ----------------

    def search_cards(self, query):
        """Effettua la richiesta HTTP all'API Scryfall"""

        try:
            # Parametri della richiesta
            params = {
                "q": query
            }

            # Richiesta GET all'API
            response = self.session.get(BASE_URL, params=params, timeout=10)

            # Solleva eccezione in caso di errore HTTP
            response.raise_for_status()

            # Conversione JSON in dizionario Python
            data = response.json()

            # Controllo risultati
            if "data" not in data or not data["data"]:
                self.show_message("Nessuna carta trovata.")
                return

            # Limita a 30 carte
            cards = data["data"][:30]

            # Mostra le carte
            self.display_cards(cards)

        except Exception as e:
            self.show_message(f"Errore: {e}")

    # ---------------- VISUALIZZAZIONE ----------------

    def display_cards(self, cards):
        """Visualizza le carte in una griglia"""

        max_cols = 3  # carte per riga

        for index, card in enumerate(cards):
            row = index // max_cols
            col = index % max_cols

            # Frame della singola carta
            frame = ttk.Frame(self.results_frame, padding=10)
            frame.grid(row=row, column=col, padx=10, pady=10)

            # Label per immagine
            img_label = ttk.Label(frame, text="Caricamento...")
            img_label.pack()

            # Testo informativo
            info = (
                f"{card.get('name','?')}\n"
                f"Set: {card.get('set_name','?')}\n"
                f"Rarità: {card.get('rarity','?')}"
            )
            ttk.Label(frame, text=info, justify="center").pack(pady=5)

            # Carica l'immagine
            self.load_image(card, img_label)

    # ---------------- IMMAGINI ----------------

    def load_image(self, card, label):
        """Scarica e visualizza l'immagine della carta"""

        try:
            # Recupera URL immagine
            image_url = card.get("image_uris", {}).get("normal")

            # Gestione carte double-face
            if not image_url and "card_faces" in card:
                image_url = card["card_faces"][0].get("image_uris", {}).get("normal")

            if not image_url:
                label.config(text="Immagine non disponibile")
                return

            # Scarica l'immagine
            response = self.session.get(image_url, timeout=10)
            response.raise_for_status()

            # Converte byte in immagine PIL
            image = Image.open(io.BytesIO(response.content))

            # Ridimensionamento
            image = image.resize((200, 280), Image.Resampling.LANCZOS)

            # Conversione per tkinter
            tk_image = ImageTk.PhotoImage(image)

            # Mantiene riferimento
            self.images.append(tk_image)

            # Aggiorna label
            label.config(image=tk_image, text="")

        except Exception:
            label.config(text="Errore immagine")

    def show_message(self, text):
        """Mostra un messaggio informativo"""
        messagebox.showinfo("Info", text)


# ---------------- AVVIO APP ----------------

if __name__ == "__main__":
    # Creazione finestra principale
    root = tk.Tk()

    # Avvio applicazione
    app = CardViewerApp(root)

    # Loop principale tkinter
    root.mainloop()
