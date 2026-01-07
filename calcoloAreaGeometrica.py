scelta = 0
while (scelta < 1 or scelta > 5):
    scelta = int(input("""secgliere cosa si vuole calcolare
                1 = area quadrato
                2 = area rettangolo
                3 = area triangolo
                4 = area cerchio
                5 = area rombo """))
if scelta == 1:
    lato = float(input("calcolo area quadrato, inserire valore del lato"))
    areaQuadrato = lato * lato
    print ("l'area del quandrato è:", areaQuadrato)
elif scelta == 2:
    base = float(input("calcolo area rettangolo, inserire valore della base"))
    altezza = float(input("inserire valore dell'altezza"))
    areaRettangolo = base * altezza
    print ("l'area del rettangolo è:", areaRettangolo)
elif scelta == 3:
    base = float(input("calcolo area triangolo, inserire il valore della base"))
    altezza = float(input("inserire il valore dell'altezza"))
    areaTriangolo = (base * altezza)/2
    print("l'area del triangolo è: ", areaTriangolo)
elif scelta == 4:
    raggio = float(input("calcolo area cerchio, inserire valore del raggio"))
    areaCerchio = 3,14 * raggio * raggio
    print("l'area del cerchio è:", areaCerchio)
elif scelta == 5:
    diagonaleMaggiore = float(input("calcolo area rombo, inserire valore della diagonale maggiore"))
    diagonaleMinore = float(input("inserire valore della diagonale minore"))
    areaRombo = (diagonaleMaggiore * diagonaleMinore)/2
    print("l'area del rombo è:", areaRombo)
