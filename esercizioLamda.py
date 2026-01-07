from math import log

filter([1,2,3,4,5], key=lambda x: x > 3)

filter(["Ciao", "come", "Stai", "Oggi"], key=lambda x : x[0].isUpper())

map([1,2,3,4,5], key=lambda x: log(x))
