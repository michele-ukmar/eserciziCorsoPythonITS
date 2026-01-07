import os

scriptDir = os.path.dirname(__file__)
relPath = "paroleUtente.txt"

absFilePath = os.path.join(scriptDir, relPath)
print(absFilePath)

file = open(absFilePath, "w")

while True:
    parole = (input("Inserisci una parola: "))
    file.write(parole + "\n")
    if parole == "fine":
        break

file.close()
