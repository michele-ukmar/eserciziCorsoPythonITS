"""
lista = [1, 1.3, "c"]

while (len(lista) > 0):
    print(lista.pop())

list = [range(0,10)]
    
for i in range (len(list)):
    if list[i] % 2 != 0:
        print(list[i])
        
"""

maschi = ["mario", "luigi", "pippo", "pluto"]
femmine = ["minnie", "topolina", "paperina", "paperoga"]
unione = [[maschi[i], femmine[i]] for i in range (len(maschi))]
print(unione)
print("-----")
unioneCompleta = [[maschi[i], femmine[j]] for i in  range(len(maschi)) for j in range(len(femmine))]
#unioneCompleta = [(i, j) for i in  maschi for j in femmine]
print(unioneCompleta)

