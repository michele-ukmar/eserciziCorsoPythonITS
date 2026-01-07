# =========================
# IMPORT LIBRERIE STANDARD
# =========================

# Tkinter per l'interfaccia grafica
import tkinter as tk
from tkinter import ttk, messagebox

# urllib per richieste HTTP senza librerie esterne
import urllib.request
import urllib.parse

# Threading per non bloccare la GUI
import threading

# Gestione byte stream (immagini)
import io

# =========================
# LIBRERIE ESTERNE CONSENTITE
# =========================

# Pillow per gestione immagini
from PIL import Image, ImageTk

# BeautifulSoup4 per il web scraping HTML
from bs4 import BeautifulSoup


# =========================
# URL BASE (RICERCA WEB)
# =========================

SCRYFALL_SEARCH_URL = "https://scryfall.com/search?q="


# =========================
# CLASSE PRINCIPALE
# =========================

class CardViewerApp:
    def __init__(self, root):
        # Finestra principale
        self.root = root
        self.root.title("Magic Card Viewer (Web Scraping)")
        self.root.geometry("1200x800")

        # Lista per mantenere immagini in memoria
        self.images = []

        # Costruisce la GUI
        self.build_ui()

    # =========================
    # INTERFACCIA GRAFICA
    # =========================

    def build_ui(self):
        """Costruisce l'interfaccia grafica"""

        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)

        self.entries = {}

        labels = [
            "Nome carta",
            "Colori (w u b r g)",
            "Tipo",
            "Testo regole"
        ]

        # Creazione campi di input
        for i, label in enumerate(labels):
            ttk.Label(input_frame, text=label).grid(row=i, column=0, sticky="w")
            entry = ttk.Entry(input_frame, width=30)
            entry.grid(row=i, column=1, padx=5)
            self.entries[label] = entry

        # Pulsante Cerca
        ttk.Button(
            input_frame,
            text="Cerca",
            command=self.start_search
        ).grid(row=len(labels), column=0, columnspan=2, pady=10)

        # Canvas per risultati scrollabili
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)

        self.results_frame = ttk.Frame(self.canvas)

        self.results_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.results_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    # =========================
    # AVVIO RICERCA
    # =========================

    def start_search(self):
        """Avvia la ricerca in un thread"""

        query = self.build_query()

        if not query:
            messagebox.showwarning("Attenzione", "Inserisci almeno un parametro")
            return

        # Pulizia risultati precedenti
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        self.images.clear()

        # Thread separato per scraping
        threading.Thread(
            target=self.search_cards,
            args=(query,),
            daemon=True
        ).start()

    # =========================
    # COSTRUZIONE QUERY
    # =========================

    def build_query(self):
        """Costruisce la query per il sito Scryfall"""

        parts = []

        name = self.entries["Nome carta"].get().strip()
        if name:
            parts.append(name)

        colors = self.entries["Colori (w u b r g)"].get().strip().lower().split()
        if colors:
            parts.append("c<=" + "".join(colors))

        card_type = self.entries["Tipo"].get().strip()
        if card_type:
            parts.append(f"type:{card_type}")

        oracle = self.entries["Testo regole"].get().strip().lower()
        if oracle:
            parts.append(" ".join(oracle.split()))

        return " ".join(parts)

    # =========================
    # WEB SCRAPING
    # =========================

    def search_cards(self, query):
        """Scarica la pagina HTML e ne estrae le carte"""

        try:
            url = SCRYFALL_SEARCH_URL + urllib.parse.quote(query)

            with urllib.request.urlopen(url) as response:
                html = response.read().decode("utf-8")

            soup = BeautifulSoup(html, "html.parser")

            # Ogni carta è contenuta in un tag <a> con class "card-grid-item"
            card_elements = soup.select("a.card-grid-item")

            if not card_elements:
                self.show_message("Nessuna carta trovata.")
                return

            cards = card_elements[:30]

            self.root.after(0, lambda: self.display_cards(cards))

        except Exception as e:
            self.show_message(f"Errore: {e}")

    # =========================
    # VISUALIZZAZIONE
    # =========================

    def display_cards(self, cards):
        """Mostra le carte in griglia"""

        max_cols = 3

        for index, card in enumerate(cards):
            row = index // max_cols
            col = index % max_cols

            frame = ttk.Frame(self.results_frame, padding=10)
            frame.grid(row=row, column=col, padx=10, pady=10)

            img_label = ttk.Label(frame, text="Caricamento...")
            img_label.pack()

            name = card.get("aria-label", "Carta sconosciuta")
            ttk.Label(frame, text=name, justify="center").pack(pady=5)

            image_url = card.get("data-card-image")

            threading.Thread(
                target=self.load_image,
                args=(image_url, img_label),
                daemon=True
            ).start()

    # =========================
    # CARICAMENTO IMMAGINI
    # =========================

    def load_image(self, image_url, label):
        """Scarica e mostra l'immagine"""

        try:
            if not image_url:
                self.root.after(0, lambda: label.config(text="Immagine non disponibile"))
                return

            with urllib.request.urlopen(image_url) as response:
                image_bytes = response.read()

            image = Image.open(io.BytesIO(image_bytes))
            image = image.resize((200, 280), Image.Resampling.LANCZOS)

            tk_image = ImageTk.PhotoImage(image)
            self.images.append(tk_image)

            self.root.after(0, lambda: label.config(image=tk_image, text=""))

        except Exception:
            self.root.after(0, lambda: label.config(text="Errore immagine"))

    # =========================
    # MESSAGGI
    # =========================

    def show_message(self, text):
        self.root.after(0, lambda: messagebox.showinfo("Info", text))


# =========================
# AVVIO APPLICAZIONE
# =========================

if __name__ == "__main__":
    root = tk.Tk()
    app = CardViewerApp(root)
    root.mainloop()
