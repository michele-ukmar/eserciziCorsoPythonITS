#!/usr/bin/env python3
"""
Campo Minato - Interfaccia grafica con tkinter

Esegui: python campo_minato_gui.py

Caratteristiche:
- Selezione dimensioni e numero mine
- Prima mossa sempre sicura
- Click sinistro per scoprire, click destro per mettere/rimuovere bandiera
- Flood-fill per celle a 0
- Contatore mine/flag e pulsante reset
- Messaggi di vittoria/sconfitta

Nota: su macOS il tasto destro potrebbe richiedere Ctrl+Click.
"""
import tkinter as tk
import tkinter.font as tkfont
from tkinter import messagebox, simpledialog
import random
from functools import partial


class MinesweeperGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Campo Minato')
        self.resizable(False, False)
        # font per i pulsanti/numeri
        self.btn_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        self.info_font = tkfont.Font(family="Helvetica", size=10)
        # defaults
        self.rows = 9
        self.cols = 9
        self.mines = 10
        # preset map: nome -> (rows, cols, mines)
        self.presets = {
            "Custom": None,
            "Beginner 9x9 (10)": (9, 9, 10),
            "Intermediate 16x16 (40)": (16, 16, 40),
            "Expert 20x20 (99)": (20, 20, 99),
            "Large 24x24 (150)": (24, 24, 150),
        }
        self.preset_var = tk.StringVar(value="Beginner 9x9 (10)")
        self._create_controls()
        # applica preset iniziale (avvia partita)
        self.apply_preset(self.preset_var.get())

    def _create_controls(self):
        top = tk.Frame(self)
        top.pack(padx=6, pady=6, anchor='w')

        self.mine_label = tk.Label(top, text='Mine: 0', font=self.info_font)
        self.mine_label.pack(side='left', padx=(0,10))

        # OptionMenu per preset dimensioni
        preset_menu = tk.OptionMenu(top, self.preset_var, *self.presets.keys(), command=self.apply_preset)
        preset_menu.config(width=20)
        preset_menu.pack(side='left', padx=(0,8))

        btn_new = tk.Button(top, text='Nuova partita', command=self._on_new_game)
        btn_new.pack(side='left')

        btn_settings = tk.Button(top, text='Impostazioni', command=self._on_settings)
        btn_settings.pack(side='left', padx=(6,0))

        self.board_frame = tk.Frame(self)
        self.board_frame.pack(padx=6, pady=(0,6))

    def _on_settings(self):
        # Ora le impostazioni permettono solo di modificare il numero di mine
        max_mines = self.rows * self.cols - 1
        mines = simpledialog.askinteger('Mine', f'Numero mine (max {max_mines}):', initialvalue=self.mines, minvalue=1, maxvalue=max_mines)
        if mines is None:
            return
        self.mines = mines
        # aggiorna spinbox e avvia nuova partita
        try:
            self.mines_spin.config(to=max_mines)
        except Exception:
            pass
        self.mines_var.set(self.mines)
        self._start_new_game()

    def _on_new_game(self):
        self._start_new_game()

    def _start_new_game(self):
        # reset state
        self.first_click = True
        self.flags = set()
        self.revealed = set()
        self.mine_positions = set()
        self.buttons = {}
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        # clear frame
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        # create grid of buttons
        for r in range(self.rows):
            for c in range(self.cols):
                # pulsanti con font coerente; dimensione compatta ma leggibile
                btn = tk.Button(self.board_frame, width=3, height=1, text='', relief='raised',
                                font=self.btn_font, bg='SystemButtonFace', activebackground='#e6e6e6')
                btn.grid(row=r, column=c, padx=0, pady=0)
                # bind left and right click
                btn.bind('<Button-1>', partial(self._on_left_click, r=r, c=c))
                btn.bind('<Button-3>', partial(self._on_right_click, r=r, c=c))
                # macOS Ctrl-Click support
                btn.bind('<Control-Button-1>', partial(self._on_right_click, r=r, c=c))
                self.buttons[(r, c)] = btn

        self._update_mine_label()

    def _place_mines(self, safe_r, safe_c):
        forbidden = {(safe_r, safe_c)} | { (nr, nc) for nr in range(safe_r-1, safe_r+2) for nc in range(safe_c-1, safe_c+2) if 0 <= nr < self.rows and 0 <= nc < self.cols }
        all_cells = [(r, c) for r in range(self.rows) for c in range(self.cols) if (r, c) not in forbidden]
        mines = set(random.sample(all_cells, min(self.mines, len(all_cells))))
        self.mine_positions = mines
        # compute board numbers
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in mines:
                    self.board[r][c] = -1
                else:
                    count = 0
                    for nr in range(r-1, r+2):
                        for nc in range(c-1, c+2):
                            if (nr, nc) in mines:
                                count += 1
                    self.board[r][c] = count

    def _on_left_click(self, event, r, c):
        if (r, c) in self.flags or (r, c) in self.revealed:
            return
        if self.first_click:
            self._place_mines(r, c)
            self.first_click = False
        # if mine -> lose
        if self.board[r][c] == -1:
            self._reveal_mine(r, c)
            self._game_over(False)
            return
        self._reveal_cell(r, c)
        if self._check_victory():
            self._game_over(True)

    def _on_right_click(self, event, r, c):
        if (r, c) in self.revealed:
            return 'break'
        btn = self.buttons[(r, c)]
        if (r, c) in self.flags:
            self.flags.remove((r, c))
            btn.config(text='', fg='black')
        else:
            if len(self.flags) < self.mines:
                self.flags.add((r, c))
                # bandiera emoji
                btn.config(text='🚩', fg='red')
        self._update_mine_label()
        return 'break'

    def _update_mine_label(self):
        remaining = max(0, self.mines - len(self.flags))
        self.mine_label.config(text=f'Mine: {remaining}')

    def _reveal_cell(self, r, c):
        if (r, c) in self.revealed or (r, c) in self.flags:
            return
        btn = self.buttons[(r, c)]
        val = self.board[r][c]
        # aspetto per cella rivelata
        btn.config(relief='sunken', state='disabled', bg='#e9e9e9')
        if val > 0:
            btn.config(text=str(val))
            self._color_number(btn, val)
        else:
            btn.config(text=' ')
        self.revealed.add((r, c))
        # flood fill for zeros
        if val == 0:
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                for nr in range(cr-1, cr+2):
                    for nc in range(cc-1, cc+2):
                        if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in self.revealed and (nr, nc) not in self.flags:
                            nval = self.board[nr][nc]
                            nbtn = self.buttons[(nr, nc)]
                            nbtn.config(relief='sunken', state='disabled', bg='#e9e9e9')
                            if nval > 0:
                                nbtn.config(text=str(nval))
                                self._color_number(nbtn, nval)
                            else:
                                nbtn.config(text=' ')
                            self.revealed.add((nr, nc))
                            if nval == 0:
                                stack.append((nr, nc))

    def _color_number(self, btn, val):
        # colori più vividi per ogni numero; applica anche disabledforeground
        colors = {
            1: '#0000FF',  # blue
            2: '#008000',  # green
            3: '#FF0000',  # red
            4: '#00008B',  # darkblue
            5: '#8B4513',  # brown
            6: '#00CED1',  # dark turquoise
            7: '#000000',  # black
            8: '#808080',  # grey
        }
        color = colors.get(val, '#000000')
        # imposto sia fg (quando abilitato) sia disabledforeground (quando disabilitato)
        btn.config(fg=color, disabledforeground=color, font=self.btn_font)

    def _reveal_mine(self, r, c):
        # reveal all mines and mark the exploded one
        for (mr, mc) in self.mine_positions:
            b = self.buttons[(mr, mc)]
            # mostra mina come emoji e stile disabilitato
            b.config(text='💣', fg='black', relief='sunken', state='disabled', bg='#f2f2f2')
        # mark clicked mine
        btn = self.buttons[(r, c)]
        btn.config(text='💥', bg='red', fg='white')

    def _check_victory(self):
        total_cells = self.rows * self.cols
        return len(self.revealed) == total_cells - len(self.mine_positions)

    def _game_over(self, victory: bool):
        if victory:
            messagebox.showinfo('Vittoria', 'Hai vinto! Tutte le celle senza mine sono state rivelate.')
        else:
            messagebox.showinfo('Sconfitta', 'Hai colpito una mina. Gioco terminato.')
        # disable all buttons
        for btn in self.buttons.values():
            btn.unbind('<Button-1>')
            btn.unbind('<Button-3>')
            btn.unbind('<Control-Button-1>')
        # show mines count
        self._update_mine_label()

    def apply_preset(self, preset_name):
        """Applica preset di dimensione e numero mine; se 'Custom' non cambia nulla."""
        info = self.presets.get(preset_name)
        if info is None:
            return
        rows, cols, mines = info
        rows = max(5, min(60, int(rows)))
        cols = max(5, min(60, int(cols)))
        max_mines = rows * cols - 1
        mines = max(1, min(max_mines, int(mines)))
        self.rows, self.cols, self.mines = rows, cols, mines
        self._start_new_game()


if __name__ == '__main__':
    app = MinesweeperGUI()
    app.mainloop()
