def prova_solo_keyword(a,*,b, c):
    print(a,b,c)

prova_solo_keyword(1,2,3,4,5,6,7,8,9, c=10)
# genera errore

prova_solo_keyword(a =1, c=2)
# genera errore

prova_solo_keyword(1,2,3)
# genera errore

prova_solo_keyword(1,b=2, c=3)

prova_solo_keyword(a=1,b=2, c=3)