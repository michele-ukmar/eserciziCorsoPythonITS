
class Persona:

    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza

    @classmethod
    def costruttore_alternativo(cls):
        pass


class Persona:

    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza

    @classmethod
    def from_string(cls, stringa_persona):
        nome, cognome, età, residenza = stringa_persona.split("-")
        return cls(nome, cognome, età, residenza)
    
persona_prova = "Dario-Rossi-34-Napoli"
persona_uno = Persona.from_string(persona_prova)
print(persona_uno.scheda_personale())
