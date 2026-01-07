
set1 = {'A','B','C'}
set2 = {'A','D','E'}

sd = set1.symmetric_difference(set2)
print(sd)
# output: {'C', 'B', 'E', 'D'}

si = set1.intersection(set2)
print(si)
# output: {'A'}
su = sd.union(si)
print(su)
# output: {'A', 'B', 'E', 'D', 'C'}
print(su == set1.union(set2))
#output: True

set0 = set(range(1, 10))
set3 = {2,3}
set4 = {2,3}


print(set0.issuperset(set3))
# output: True

# {2,3} è un sottoinsieme di {1,2,3,4,5,6,7,8,9}
print(set3.issuperset(set0))
# output: False

# {2,3} è un sottoinsieme di {1,2,3,4,5,6,7,8,9}
print(set3.issubset(set0))
# output: True

# {2,3} non è disgiunto da {1,2,3,4,5,6,7,8,9}
# vi è un elemento in comune
print(set3.isdisjoint(set0))
# output: False


print(set3.issubset(set4))
# output: True

print(set3.issuperset(set4))
# output: True

# {2,3} è disgiunto da {1,2,3,4,5,6,7,8,9}
# neghiamo l'esistenza di un elemento in comune
set3 = {0,10}

print(set3.isdisjoint(set0))
# output: True

lista = ["A","B","C","A"]
set1 = set(lista)
print(len(set1)!=len(lista))

tt = set({1:"ciao"},{"3":"prova"})