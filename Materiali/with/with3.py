import os

with os.scandir(".") as entries:
     for entry in entries:
         print(entry.name, "->", entry.stat().st_size, "bytes")

# consegna_1.rtf -> 914 bytes
# consegna_2.rtf -> 751 bytes
# file_1.txt -> 33 bytes
# .DS_Store -> 8196 bytes
# dir.py -> 24 bytes
# file_2.txt -> 95 bytes
# ese_1.py -> 1481 bytes
# UFS02 -> 1728 bytes
# blender.py -> 867 bytes
# test.py -> 181 bytes
# altro.py -> 1350 bytes
# esercizio.py -> 0 bytes
# altro1.py -> 1741 bytes
# .vscode -> 96 bytes