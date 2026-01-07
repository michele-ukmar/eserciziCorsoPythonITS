# Input example:
uomini = ["Mario", "Luigi", "Pippo", "Pluto"]
donne = ["Minnie", "Topolina", "Paperina", "Paperoga"]

# comprehension list
coppie = [(uomo, donna) for uomo in uomini for donna in donne]

# Output example:
print(coppie)

# comprehension list
coppie = [(uomo, donna) for uomo, donna in zip(uomini, donne)]

# Output example:
print(coppie)

maschi = ['Luca', 'Marco', 'Giovanni']
femmine = ['Anna', 'Maria', 'Lucia']

coppie = [[maschi[i], femmine[i]] for i in range(0, 3)]
print(coppie)

coppie = [[maschi[i], femmine[j]] for i in range(0, 3) for j in range(0, 3)]
print(coppie)