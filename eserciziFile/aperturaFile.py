import random
import string

file = open("fileProva.txt", "w")

for i in range (1000):
    file.write("linea numero "+ str(i) + " ".join(random.choices(string.ascii_letters, k = 100)) + "\n")
    
file.close()
