import os

scriptDir = os.path.dirname(__file__)
# __file__ serve a dare nome al file corrente
relPath = "eserciziFile/test.txt"

absFilePath = os.path.join(scriptDir, relPath)
print(absFilePath)

fileProva = open(absFilePath, "w")
fileProva.write("Questo è un testo di prova")
fileProva.close()

