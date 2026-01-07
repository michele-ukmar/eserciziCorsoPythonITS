import json
import math
import random
import time
from dataclasses import dataclass, asdict, field
from typing import Dict, Optional

# ---------- Modelli ----------
@dataclass
class Business:
    id: str
    name: str
    level: int = 0
    base_cost: float = 10.0
    base_income_per_sec: float = 1.0
    cost_multiplier: float = 1.15  # scaling per upgrade
    manager_hired: bool = False
    last_collected: float = field(default_factory=time.time)

    def current_upgrade_cost(self) -> float:
        # cost to raise level by 1
        return self.base_cost * (self.cost_multiplier ** self.level)

    def income_per_sec(self) -> float:
        # income scales roughly linearly with level; tweak as desired
        return self.base_income_per_sec * (1 + 0.5 * self.level)

    def collect(self, now: Optional[float] = None) -> float:
        """Calcola e ritorna quanto è maturato dall'ultima raccolta (o dal last_collected)."""
        if now is None:
            now = time.time()
        elapsed = max(0.0, now - self.last_collected)
        amount = self.income_per_sec() * elapsed
        self.last_collected = now
        return amount

    def to_dict(self):
        d = asdict(self)
        # time as float OK
        return d

    @staticmethod
    def from_dict(d):
        return Business(**d)


@dataclass
class Player:
    money: float = 50.0
    businesses: Dict[str, Business] = field(default_factory=dict)
    prestige_points: int = 0
    last_global_collect: float = field(default_factory=time.time)

    def collect_all(self) -> float:
        """Raccoglie manualmente tutti i guadagni non ancora raccolti (anche dai manager se non automatici)."""
        now = time.time()
        total = 0.0
        for b in self.businesses.values():
            # if manager hired, we assume continuous collection into player's money on collect_all
            if b.manager_hired:
                # manager auto-collects into money continuously: still we compute elapsed since last_collected
                total += b.collect(now)
            else:
                # manual businesses only produce but must be collected explicitly; we still compute matured amount
                total += b.collect(now)
        self.money += total
        self.last_global_collect = now
        return total

    def passive_income_since(self, timestamp: float) -> float:
        """Calcola quanto sarebbe stato guadagnato da manager tra timestamp e ora (senza mutare last_collected)."""
        now = time.time()
        total = 0.0
        for b in self.businesses.values():
            if b.manager_hired:
                # income per sec * elapsed
                elapsed = max(0.0, now - max(timestamp, b.last_collected))
                total += b.income_per_sec() * elapsed
        return total

    def to_dict(self):
        return {
            "money": self.money,
            "businesses": {k: v.to_dict() for k, v in self.businesses.items()},
            "prestige_points": self.prestige_points,
            "last_global_collect": self.last_global_collect,
        }

    @staticmethod
    def from_dict(d):
        p = Player(money=d.get("money", 0.0),
                   prestige_points=d.get("prestige_points", 0))
        p.last_global_collect = d.get("last_global_collect", time.time())
        bs = d.get("businesses", {})
        p.businesses = {k: Business.from_dict(v) for k, v in bs.items()}
        return p

# ---------- Logica di gioco ----------
class Game:
    def __init__(self):
        self.player = Player()
        self.event_chance_per_min = 0.2  # probabilità per evento casuale ogni minuto simulato
        self.init_businesses()
        self.start_time = time.time()

    def init_businesses(self):
        if self.player.businesses:
            return
        # Definisci un set di attività iniziali
        base_list = [
            ("lemonade", "Stand di limonate", 10, 0.5, 1.10),
            ("news", "Giornale locale", 50, 2.0, 1.12),
            ("cafe", "Caffetteria", 200, 8.0, 1.13),
            ("shop", "Negozio", 1000, 40.0, 1.14),
            ("factory", "Fabbrica", 5000, 200.0, 1.15),
            ("tech", "Startup tech", 20000, 1200.0, 1.16),
        ]
        for id_, name, cost, income, mult in base_list:
            self.player.businesses[id_] = Business(
                id=id_, name=name, base_cost=float(cost),
                base_income_per_sec=float(income),
                cost_multiplier=float(mult)
            )

    # --- Azioni giocatore ---
    def buy_business_level(self, business_id: str, levels: int = 1) -> str:
        b = self.player.businesses.get(business_id)
        if not b:
            return "Attività non trovata."
        total_cost = 0.0
        # prezzo progressivo: somma geometricamente
        for i in range(levels):
            cost = b.current_upgrade_cost()
            total_cost += cost
            # temporaneamente increment level to compute next cost
            b.level += 1
        # revert levels (we only change if can pay)
        b.level -= levels
        if total_cost > self.player.money + 1e-9:
            return f"Non hai abbastanza soldi. Serve {total_cost:.2f} €."
        # paga e applica livelli
        self.player.money -= total_cost
        b.level += levels
        return f"Hai comprato {levels} livello(i) per '{b.name}' per {total_cost:.2f} €."

    def hire_manager(self, business_id: str) -> str:
        b = self.player.businesses.get(business_id)
        if not b:
            return "Attività non trovata."
        if b.manager_hired:
            return "Manager già assunto per questa attività."
        # manager cost could be e.g. 25x base_cost of first upgrade
        cost = b.base_cost * 25 * (1 + 0.1 * b.level)
        if cost > self.player.money + 1e-9:
            return f"Non hai abbastanza soldi per assumere il manager ({cost:.2f} €)."
        self.player.money -= cost
        b.manager_hired = True
        b.last_collected = time.time()
        return f"Hai assunto un manager per '{b.name}' per {cost:.2f} €."

    def manual_collect(self) -> str:
        gained = self.player.collect_all()
        return f"Hai raccolto {gained:.2f} € da tutte le attività."

    def wait_seconds(self, seconds: int) -> str:
        """Simula il passare del tempo (senza thread): aggiorna last_collected e assegna guadagni automatici."""
        if seconds <= 0:
            return "Inserisci un numero di secondi positivo."
        now = time.time() + seconds  # simulate future time
        total = 0.0
        events = []
        for b in self.player.businesses.values():
            if b.manager_hired:
                # accumula guadagno nel player
                elapsed = max(0.0, now - b.last_collected)
                total += b.income_per_sec() * elapsed
                b.last_collected = now
            else:
                # no manager: it still accumulates but only given when manual collect is called.
                # We'll advance its last_collected as time passed, but not add to player's money.
                b.last_collected = now
        # gestisci eventi casuali durante il periodo
        # probabilità evento ~ event_chance_per_min * minutes
        minutes = seconds / 60.0
        prob = 1 - math.exp(-self.event_chance_per_min * minutes)  # approx
        if random.random() < prob:
            ev_text, ev_money = self.random_event()
            total += ev_money
            events.append(ev_text)
        self.player.money += total
        return f"Sono passati {seconds} secondi. Guadagni automatici: {total:.2f} €. Eventi: {'; '.join(events) if events else 'nessuno'}"

    def random_event(self):
        """Genera un evento casuale e restituisce (descrizione, delta_money)."""
        roll = random.random()
        if roll < 0.4:
            # piccolo bonus
            bonus = random.uniform(1.0, 50.0)
            return (f"Piccolo contratto ottenuto: +{bonus:.2f} €", bonus)
        elif roll < 0.7:
            # grande bonus
            bonus = random.uniform(100.0, 2000.0)
            return (f"Grande opportunità! +{bonus:.2f} €", bonus)
        else:
            # multa / perdita
            loss = -random.uniform(10.0, 500.0)
            return (f"Spesa imprevista: {loss:.2f} €", loss)

    def status(self) -> str:
        lines = []
        lines.append(f"Soldi: {self.player.money:.2f} € | Prestige: {self.player.prestige_points}")
        lines.append("Attività:")
        for b in self.player.businesses.values():
            lines.append(f" - [{b.id}] {b.name}: livello {b.level}, reddito/s {b.income_per_sec():.2f}, next_upgrade {b.current_upgrade_cost():.2f} €, manager: {'Sì' if b.manager_hired else 'No'}")
        # stima income passivo per sec
        passive = sum(b.income_per_sec() for b in self.player.businesses.values() if b.manager_hired)
        lines.append(f"Reddito passivo totale: {passive:.2f} €/s")
        # stima guadagni in 1 ora
        lines.append(f"Guadagno stimato in 1 ora (solo manager attivi): {passive * 3600:.2f} €")
        return "\n".join(lines)

    # --- Salvataggio/Caricamento ---
    def save(self, filename: str = "save_game.json") -> str:
        data = {
            "player": self.player.to_dict(),
            "saved_at": time.time(),
        }
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            return f"Salvataggio effettuato in '{filename}'."
        except Exception as e:
            return f"Errore nel salvataggio: {e}"

    def load(self, filename: str = "save_game.json") -> str:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.player = Player.from_dict(data["player"])
            return f"Caricato salvataggio da '{filename}'."
        except FileNotFoundError:
            return f"File '{filename}' non trovato."
        except Exception as e:
            return f"Errore nel caricamento: {e}"

    # --- Utility ---
    def find_business_by_prefix(self, pref: str) -> Optional[str]:
        pref = pref.lower()
        matches = [id_ for id_ in self.player.businesses if id_.startswith(pref) or self.player.businesses[id_].name.lower().startswith(pref)]
        if not matches:
            return None
        if len(matches) == 1:
            return matches[0]
        # se più corrispondenze, prendi la prima
        return matches[0]


# ---------- Interfaccia testuale ----------
def print_help():
    print("""
Comandi disponibili:
  stato                       - Mostra stato attuale (soldi, attività, reddito passivo)
  compra <id> [n]             - Compra n livelli per l'attività <id> (default n=1)
  migliora <id> [n]           - sinonimo di compra
  assumi <id>                 - Assumi manager per l'attività <id>
  raccogli                    - Raccogli manualmente i guadagni da tutte le attività
  aspetta <sec>               - Fai passare <sec> secondi (simulazione)
  salva [file]                - Salva su file (default save_game.json)
  carica [file]               - Carica da file (default save_game.json)
  aiuto                       - Mostra questo aiuto
  esci                        - Esci dal gioco
  lista                       - Lista attività e relativi id
""")

def main_loop():
    game = Game()
    print("Benvenuto a Business Empire (testo). Digita 'aiuto' per i comandi.")
    while True:
        try:
            cmd = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nUscita. Salvataggio automatico...")
            print(game.save())
            break
        if not cmd:
            continue
        parts = cmd.split()
        action = parts[0].lower()

        if action in ("aiuto", "help"):
            print_help()
        elif action in ("stato", "status"):
            print(game.status())
        elif action in ("lista", "list"):
            for b in game.player.businesses.values():
                print(f"{b.id}: {b.name}")
        elif action in ("compra", "migliora", "buy", "upgrade"):
            if len(parts) < 2:
                print("Uso: compra <id> [n]")
                continue
            bid = game.find_business_by_prefix(parts[1])
            if not bid:
                print("ID attività non trovata.")
                continue
            n = 1
            if len(parts) >= 3:
                try:
                    n = int(parts[2])
                    if n < 1:
                        raise ValueError
                except ValueError:
                    print("Inserisci un numero intero positivo per [n].")
                    continue
            print(game.buy_business_level(bid, n))
        elif action in ("assumi", "hire"):
            if len(parts) < 2:
                print("Uso: assumi <id>")
                continue
            bid = game.find_business_by_prefix(parts[1])
            if not bid:
                print("ID attività non trovata.")
                continue
            print(game.hire_manager(bid))
        elif action in ("raccogli", "collect"):
            print(game.manual_collect())
        elif action in ("aspetta", "wait"):
            if len(parts) < 2:
                print("Uso: aspetta <sec>")
                continue
            try:
                sec = int(parts[1])
            except ValueError:
                print("Inserisci un numero intero di secondi.")
                continue
            print(game.wait_seconds(sec))
        elif action in ("salva", "save"):
            fname = parts[1] if len(parts) >= 2 else "save_game.json"
            print(game.save(fname))
        elif action in ("carica", "load"):
            fname = parts[1] if len(parts) >= 2 else "save_game.json"
            print(game.load(fname))
        elif action in ("esci", "quit", "exit"):
            print("Vuoi salvare prima di uscire? (s/N)")
            resp = input("> ").strip().lower()
            if resp in ("s", "si", "y", "yes"):
                print(game.save())
            print("Arrivederci!")
            break
        else:
            print("Comando non riconosciuto. Digita 'aiuto' per la lista comandi.")

if __name__ == "__main__":
    main_loop()
