import string

file = open ("fileProva.txt", "r")
fileDispari = open ("fileDispari.txt", "w")
filePari = open ("filePari.txt", "w")

for i, line in enumerate(file):
    if i % 2 == 0:
        filePari.write(line)
    else:
        fileDispari.write(line)
        

file.close()
filePari.close()
fileDispari.close()
