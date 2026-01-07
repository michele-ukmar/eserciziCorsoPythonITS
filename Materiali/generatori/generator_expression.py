
def potenzadi2(length):
    for n in range(length):
        yield n ** 2

for i in potenzadi2(10):
    print(i)

potenzedi2 = (n** 2 for n in range(10))

for i in potenzedi2:
    print(i)


