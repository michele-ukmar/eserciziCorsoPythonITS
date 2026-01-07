#!/usr/bin/env python3
"""
Business Empire GUI (Tkinter Edition)
Autore: ChatGPT (esempio)
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json, time, random, math, os
from dataclasses import dataclass, field, asdict
from typing import Dict, Optional

# ======= LOGICA DI GIOCO =======

@dataclass
class Business:
    id: str
    name: str
    level: int = 0
    base_cost: float = 10.0
    base_income_per_sec: float = 1.0
    cost_multiplier: float = 1.15
    manager_hired: bool = False
    last_collected: float = field(default_factory=time.time)

    def current_upgrade_cost(self) -> float:
        return self.base_cost * (self.cost_multiplier ** self.level)

    def manager_cost(self, multiplier: int = 10) -> float:
        """Costo per assumere il manager (default multiplier=10)."""
        return self.current_upgrade_cost() * multiplier

    def income_per_sec(self) -> float:
        return self.base_income_per_sec * (1 + 0.5 * self.level)

    def collect(self, now: Optional[float] = None) -> float:
        if now is None:
            now = time.time()
        elapsed = max(0.0, now - self.last_collected)
        amount = self.income_per_sec() * elapsed
        self.last_collected = now
        return amount

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(d):
        return Business(**d)


@dataclass
class Player:
    money: float = 50.0
    businesses: Dict[str, Business] = field(default_factory=dict)

    def collect_all(self) -> float:
        now = time.time()
        total = 0.0
        for b in self.businesses.values():
            total += b.collect(now)
        self.money += total
        return total

    def to_dict(self):
        return {
            "money": self.money,
            "businesses": {k: v.to_dict() for k, v in self.businesses.items()},
        }

    @staticmethod
    def from_dict(d):
        p = Player(money=d.get("money", 0.0))
        bs = d.get("businesses", {})
        p.businesses = {k: Business.from_dict(v) for k, v in bs.items()}
        return p


class Game:
    def __init__(self):
        self.player = Player()
        # elenco completo delle imprese disponibili nello shop:
        # id -> (nome, base_cost, base_income_per_sec, cost_multiplier)
        # ho aggiunto alcune imprese extra (cinema, hotel, bank, airline)
        self.available_businesses = {
            "lemonade": ("Stand di limonate", 10, 0.5, 1.10),
            "news": ("Giornale locale", 50, 2.0, 1.12),
            "cafe": ("Caffetteria", 200, 8.0, 1.13),
            "shop": ("Negozio", 1000, 40.0, 1.14),
            "factory": ("Fabbrica", 5000, 200.0, 1.15),
            "tech": ("Startup tech", 20000, 1200.0, 1.16),
            "cinema": ("Cinema multiplex", 500, 25.0, 1.13),
            "hotel": ("Hotel 3* centro", 3000, 150.0, 1.14),
            "bank": ("Banca locale", 15000, 900.0, 1.15),
            "airline": ("Compagnia aerea", 50000, 4000.0, 1.18),
        }
        self.init_businesses()

    def init_businesses(self):
        # se non ci sono imprese possedute, dare inizio al giocatore con una sola impresa di partenza
        if self.player.businesses:
            return
        starting = ["lemonade"]  # id delle imprese iniziali possedute
        for bid in starting:
            if bid in self.available_businesses:
                name, cost, income, mult = self.available_businesses[bid]
                self.player.businesses[bid] = Business(
                    id=bid, name=name, base_cost=float(cost),
                    base_income_per_sec=float(income),
                    cost_multiplier=float(mult)
                )

    def purchase_business(self, business_id: str) -> str:
        """Acquista una nuova impresa dallo shop se il giocatore ha abbastanza soldi."""
        if business_id in self.player.businesses:
            return "Impresa già posseduta."
        info = self.available_businesses.get(business_id)
        if not info:
            return "Impresa non disponibile."
        name, base_cost, income, mult = info
        cost = float(base_cost)  # costo di acquisto semplice (puoi cambiare formula)
        if cost > self.player.money:
            return f"Non hai abbastanza soldi per acquistare '{name}' ({cost:.2f}€)."
        # applica acquisto
        self.player.money -= cost
        self.player.businesses[business_id] = Business(
            id=business_id,
            name=name,
            base_cost=float(base_cost),
            base_income_per_sec=float(income),
            cost_multiplier=float(mult),
        )
        return f"Hai acquistato l'impresa '{name}' per {cost:.2f}€."

    def buy_business_level(self, business_id: str, levels: int = 1) -> str:
        # Fixed: compute total cost without mutating level, then apply purchase atomically
        b = self.player.businesses[business_id]
        total_cost = 0.0
        temp_level = b.level
        for i in range(levels):
            total_cost += b.base_cost * (b.cost_multiplier ** (temp_level + i))
        if total_cost > self.player.money:
            return f"Non hai abbastanza soldi ({total_cost:.2f}€ richiesti)."
        # applica l'acquisto
        self.player.money -= total_cost
        b.level += levels
        return f"Hai acquistato {levels} livello/i di '{b.name}'!"

    def hire_manager(self, business_id: str) -> str:
        # usa il metodo Business.manager_cost con un moltiplicatore ragionevole (10)
        b = self.player.businesses[business_id]
        if b.manager_hired:
            return "Manager già assunto."
        cost = b.manager_cost(multiplier=10)
        if cost > self.player.money:
            return f"Non hai abbastanza soldi per il manager ({cost:.2f}€)."
        self.player.money -= cost
        b.manager_hired = True
        b.last_collected = time.time()  # evita che i guadagni automatici vengano raccolti di nuovo
        return f"Manager assunto per '{b.name}' (costo {cost:.2f}€)."

    def wait_seconds(self, seconds: int = 1):
        # Fixed: aggiornare anche last_collected delle attività con manager per evitare doppi conteggi
        now = time.time()
        total = 0.0
        for b in self.player.businesses.values():
            if b.manager_hired:
                # calcola guadagno manager per il periodo e aggiorna last_collected
                earned = b.income_per_sec() * seconds
                total += earned
                b.last_collected = now
        self.player.money += total
        return total

    def save(self, filename="save_game.json"):
        data = {"player": self.player.to_dict()}
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self, filename="save_game.json"):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.player = Player.from_dict(data["player"])


# ======= INTERFACCIA GRAFICA =======

class BusinessEmpireGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Business Empire")
        self.geometry("800x600")
        self.resizable(False, False)

        self.game = Game()
        self.images = {}          # thumbnail images per business id (tk.PhotoImage / ImageTk)
        self.big_images = {}      # larger images per business id
        self.create_widgets()
        self.update_ui()
        self.after(1000, self.tick)

    def create_widgets(self):
        # Sezione superiore: denaro e comandi globali
        top_frame = ttk.Frame(self)
        top_frame.pack(pady=10)

        self.money_label = ttk.Label(top_frame, text="Soldi: 0 €", font=("Arial", 16, "bold"))
        self.money_label.grid(row=0, column=0, padx=10)

        ttk.Button(top_frame, text="Raccogli", command=self.collect_all).grid(row=0, column=1, padx=5)
        ttk.Button(top_frame, text="Salva", command=self.save_game).grid(row=0, column=2, padx=5)
        ttk.Button(top_frame, text="Carica", command=self.load_game).grid(row=0, column=3, padx=5)
        ttk.Button(top_frame, text="Negozio", command=self.open_shop).grid(row=0, column=4, padx=5)

        # layout principale: left = lista attività, right = dettaglio
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=5)

        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side="left", fill="both", expand=True)

        # Treeview con colonna principale (#0) per icona+nome e colonne per i valori
        self.tree = ttk.Treeview(left_frame, columns=("livello", "reddito", "costo", "manager"),
                                 show="tree headings", height=15, selectmode="browse")
        self.tree.heading("#0", text="Nome")
        self.tree.heading("livello", text="Livello")
        self.tree.heading("reddito", text="Reddito/s")
        self.tree.heading("costo", text="Costo Upgrade")
        self.tree.heading("manager", text="Manager")
        self.tree.column("#0", width=260)
        self.tree.column("livello", width=70, anchor="center")
        self.tree.column("reddito", width=100, anchor="e")
        self.tree.column("costo", width=140, anchor="e")
        self.tree.column("manager", width=80, anchor="center")
        self.tree.pack(fill="both", expand=True)
        # assegna bindings per selezione e doppio click
        self.tree.bind("<Button-1>", self.on_tree_click)
        self.tree.bind("<Double-1>", self.on_tree_double_click)

        # pannello dettaglio a destra
        right_frame = ttk.Frame(main_frame, width=260)
        right_frame.pack(side="right", fill="y")
        # immagine grande
        self.detail_image_label = ttk.Label(right_frame)
        self.detail_image_label.pack(pady=8)
        self.detail_name = ttk.Label(right_frame, text="", font=("Arial", 14, "bold"))
        self.detail_name.pack(pady=(0,6))
        self.detail_info = ttk.Label(right_frame, text="", justify="left")
        self.detail_info.pack(pady=(0,10))
        # azioni nel pannello dettaglio
        ttk.Button(right_frame, text="Compra livello", command=self.buy_level).pack(fill="x", padx=10, pady=3)
        ttk.Button(right_frame, text="Assumi manager", command=self.hire_manager).pack(fill="x", padx=10, pady=3)
        ttk.Button(right_frame, text="Raccogli", command=self.collect_all).pack(fill="x", padx=10, pady=3)

        # carica immagini (cerca in images/<id>.png). Vedi commento sotto su dove metterle.
        self.load_images()

        # Pulsanti di controllo sotto la tabella
        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(pady=8)
        ttk.Button(btn_frame, text="Aspetta 10s", command=lambda: self.wait_time(10)).grid(row=0, column=0, padx=5)

        # Log eventi
        self.log_text = tk.Text(self, height=8, width=80, state="disabled", bg="#f9f9f9")
        self.log_text.pack(pady=5)

    def load_images(self):
        """
        Carica immagini dalla cartella di immagini del progetto.
        Esempio di percorso (usare slash): c:/Users/MicheleUkmarMorlacch/Downloads/progetto/images/<business_id>.png
        Se Pillow è disponibile, le ridimensiona a thumbnails 48x48 e big 128x128.
        Se i file non esistono viene creato un placeholder semplice.
        Metti le tue immagini in: c:/Users/MicheleUkmarMorlacch/Downloads/progetto/images/
        con nomi: lemonade.png, news.png, cafe.png, shop.png, factory.png, tech.png
        """
        try:
            from PIL import Image, ImageTk
            pil_ok = True
        except Exception:
            pil_ok = False

        # costruisci percorso in modo portabile; usa le immagini sia per imprese possedute che disponibili
        base = os.path.join(os.path.dirname(__file__), "images")
        # iterate union of available and owned ids
        all_ids = set(self.game.available_businesses.keys()) | set(self.game.player.businesses.keys())
        for bid in all_ids:
            img_path = os.path.join(base, f"{bid}.png")
            try:
                if pil_ok:
                    img = Image.open(img_path).convert("RGBA")
                    thumb = img.resize((48, 48), Image.LANCZOS)
                    big = img.resize((128, 128), Image.LANCZOS)
                    self.images[bid] = ImageTk.PhotoImage(thumb)
                    self.big_images[bid] = ImageTk.PhotoImage(big)
                else:
                    # senza Pillow prova tk.PhotoImage (no resize)
                    self.images[bid] = tk.PhotoImage(file=img_path)
                    self.big_images[bid] = tk.PhotoImage(file=img_path)
            except Exception:
                # placeholder: piccolo rettangolo colorato
                ph_small = tk.PhotoImage(width=48, height=48)
                # riempi con un colore semplice (put richiede list of lists; usa single pixel replicate)
                ph_small.put(("gray",), to=(0,0,47,47))
                ph_big = tk.PhotoImage(width=128, height=128)
                ph_big.put(("lightgray",), to=(0,0,127,127))
                self.images[bid] = ph_small
                self.big_images[bid] = ph_big

    def update_ui(self):
        # aggiorna etichetta soldi
        self.money_label.config(text=f"Soldi: {self.game.player.money:.2f} €")

        # aggiorna lista attività (include immagine e nome nella colonna #0)
        # conserva selezione precedente
        prev_sel = self.tree.selection()
        self.tree.delete(*self.tree.get_children())
        for b in self.game.player.businesses.values():
            # testo nella colonna #0 e image=thumb
            img = self.images.get(b.id)
            self.tree.insert("", "end", iid=b.id, text=b.name, image=img, values=(
                b.level,
                f"{b.income_per_sec():.2f}",
                f"{b.current_upgrade_cost():.2f}",
                "Sì" if b.manager_hired else "No",
            ))
        # ripristina selezione se possibile
        if prev_sel:
            try:
                self.tree.selection_set(prev_sel)
            except Exception:
                pass
        # aggiorna pannello dettaglio con selezione corrente
        sel = self.tree.selection()
        if sel:
            self.show_selected_business(sel[0])
        else:
            # pulisci dettaglio
            self.detail_image_label.config(image="")
            self.detail_name.config(text="")
            self.detail_info.config(text="")

    def log(self, text):
        self.log_text.config(state="normal")
        self.log_text.insert("end", text + "\n")
        self.log_text.config(state="disabled")
        self.log_text.see("end")

    def on_tree_click(self, event):
        # seleziona la riga sotto il cursore al momento della pressione del mouse
        item = self.tree.identify_row(event.y)
        if item:
            # setta la selezione singola sulla riga trovata
            self.tree.selection_set(item)
            # anche sposta il focus (utile per keyboard navigation)
            self.tree.focus(item)
            # mostra dettagli
            self.show_selected_business(item)
        # permette anche al widget di gestire il resto dell'evento
        return

    def on_tree_double_click(self, event):
        # su double click assicuriamo la selezione dalla posizione e poi chiamiamo buy_level
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.tree.focus(item)
            # chiama direttamente la logica di acquisto (stesso effetto del pulsante)
            self.buy_level()
        return

    def show_selected_business(self, business_id):
        """Aggiorna il pannello dettaglio con i dati dell'impresa selezionata."""
        b = self.game.player.businesses.get(business_id)
        if not b:
            return
        big = self.big_images.get(b.id)
        if big:
            self.detail_image_label.config(image=big)
            # necessario per mantenere il riferimento
            self.detail_image_label.image = big
        else:
            self.detail_image_label.config(image="")
        self.detail_name.config(text=b.name)
        info = f"Livello: {b.level}\nReddito/s: {b.income_per_sec():.2f} €\nCosto prossimo upgrade: {b.current_upgrade_cost():.2f} €\nManager: {'Sì' if b.manager_hired else 'No'}"
        self.detail_info.config(text=info)

    # --- Azioni ---
    def collect_all(self):
        gained = self.game.player.collect_all()
        self.log(f"Raccolti {gained:.2f} € da tutte le attività.")
        self.update_ui()

    def buy_level(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Info", "Seleziona un'attività da potenziare.")
            return
        bid = selected[0]
        msg = self.game.buy_business_level(bid)
        self.log(msg)
        self.update_ui()
        # aggiorna pannello dettaglio
        self.show_selected_business(bid)

    def hire_manager(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Info", "Seleziona un'attività.")
            return
        bid = selected[0]
        msg = self.game.hire_manager(bid)
        self.log(msg)
        self.update_ui()
        self.show_selected_business(bid)

    def wait_time(self, sec=10):
        earned = self.game.wait_seconds(sec)
        self.log(f"Hai guadagnato {earned:.2f} € in {sec}s grazie ai manager.")
        self.update_ui()

    def save_game(self):
        self.game.save()
        self.log("Gioco salvato con successo.")

    def load_game(self):
        try:
            self.game.load()
            self.log("Partita caricata correttamente.")
            self.update_ui()
        except Exception as e:
            messagebox.showerror("Errore", f"Impossibile caricare: {e}")

    def open_shop(self):
        """Apri una finestra con le imprese acquistabili."""
        shop = tk.Toplevel(self)
        shop.title("Negozio - Acquista nuove imprese / livelli")
        shop.geometry("640x480")
        frame = ttk.Frame(shop)
        frame.pack(fill="both", expand=True, padx=8, pady=8)
        # elenca tutte le imprese disponibili (sia possedute che no)
        row = 0
        for bid, info in self.game.available_businesses.items():
            name, base_cost, income, mult = info
            img = self.images.get(bid)
            # immagine
            lbl_img = ttk.Label(frame, image=img)
            lbl_img.grid(row=row, column=0, padx=4, pady=6, sticky="n")
            lbl_img.image = img
            # nome e descrizione
            ttk.Label(frame, text=f"{name}\nReddito/s: {income}").grid(row=row, column=1, sticky="w")
            # costo base impresa
            ttk.Label(frame, text=f"Prezzo azienda: {base_cost:.2f} €").grid(row=row, column=2, padx=8, sticky="w")

            if bid in self.game.player.businesses:
                # se posseduta, mostra pulsanti per comprare livelli 1,10,50,100
                btns_frame = ttk.Frame(frame)
                btns_frame.grid(row=row, column=3, padx=8)
                for levels in (1, 10, 50, 100):
                    # testo semplice; il messaggio con il costo verrà mostrato dopo il tentativo
                    b = ttk.Button(btns_frame, text=f"+{levels}", width=6,
                                   command=(lambda b=bid, l=levels: self.purchase_levels(b, l)))
                    b.pack(side="left", padx=2)
                # metti anche un'etichetta con stato posseduta
                ttk.Label(frame, text="Posseduta", foreground="green").grid(row=row, column=4, padx=8)
            else:
                # non posseduta: mostra bottone per comprare l'impresa
                def make_buy(bid=bid):
                    def _buy():
                        msg = self.game.purchase_business(bid)
                        self.log(msg)
                        # ricarica immagini (nel caso fosse nuovo id)
                        self.load_images()
                        self.update_ui()
                        # refresh shop: chiudi e riapri (semplice)
                        shop.destroy()
                        self.open_shop()
                    return _buy
                ttk.Button(frame, text="Compra impresa", command=make_buy()).grid(row=row, column=3, padx=6)
            row += 1
        if row == 0:
            ttk.Label(frame, text="Nessuna impresa disponibile nello shop.").pack(pady=20)
        # pulsante chiudi
        ttk.Button(shop, text="Chiudi", command=shop.destroy).pack(pady=6)

    def purchase_levels(self, business_id: str, levels: int):
        """Acquista N livelli per l'impresa selezionata (usato dal negozio)."""
        if business_id not in self.game.player.businesses:
            messagebox.showinfo("Info", "Devi prima acquistare l'impresa.")
            return
        msg = self.game.buy_business_level(business_id, levels)
        self.log(msg)
        self.update_ui()

    def tick(self):
        """Chiamata ogni secondo per accumulare income automatico."""
        earned = self.game.wait_seconds(1)
        if earned > 0:
            self.log(f"+{earned:.2f} € (manager)")
        self.update_ui()
        self.after(1000, self.tick)


if __name__ == "__main__":
    app = BusinessEmpireGUI()
    app.mainloop()
