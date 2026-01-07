class Studente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
        self.oreCrediti = 0
        self.puntiQualità = 0

    def setNome(self, newName):
        self.nome = newName

    def setCognome(self, newSurname):
        self.cognome = newSurname
    
    def setOreCrediti(self, newOreCrediti):
        self.oreCrediti = newOreCrediti
        
    def setPuntiQualità(self, newPuntiQualità):
        self.puntiQualità = newPuntiQualità
        
    def getNome(self):
        return self.nome
    
    def getCognome(self):
        return self.cognome
    
    def getOreCrediti(self):
        return self.oreCrediti
    
    def getPuntiQualità(self):
        return self.puntiQualità
    
    def calcolaGPA(self):
        if self.oreCrediti == 0:
            return 0
        punteggi = ["A", "B", "C", "D", "F"]
        return punteggi[round(self.puntiQualità / self.oreCrediti)]

    
    
    def getGPA(self):
        return self.calcolaGPA()

Studenti = [Studente("Studente", "Numero1", 127, 228), Studente("Cognome", "Studente2", 100, 400), Studente("Gio", "Bianchi", 18, 41.5), Studente("Rox", "Verde", 48.5, 155), Studente("Danni", "Amir", 37, 125.33)]

for i in Studenti:
    print(f"Nome: {i.getNome()}, Cognome: {i.getCognome()}, Ore Crediti: {i.getOreCrediti()}, Punti Qualità: {i.getPuntiQualità()}, GPA: {i.getGPA():.2f}")