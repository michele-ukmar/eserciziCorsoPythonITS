import os

scriptDir = os.path.dirname(__file__)
relPath = "esercizio1\proverbio.txt"

absFilePath = os.path.join(scriptDir, relPath)
print(absFilePath)

fileRead = open(absFilePath, "r")

print(fileRead)

filePariW = open(os.path.join(scriptDir, "esercizio1\proverbioPari.txt"), "w")
fileDispariW = open(os.path.join(scriptDir, "esercizio1\proverbioDispari.txt"), "w")

for i, x in enumerate(fileRead):
    if i % 2 == 0:
        filePariW.write(x)
    else:
        fileDispariW.write(x)

fileRead.close()
filePariW.close()
fileDispariW.close()
