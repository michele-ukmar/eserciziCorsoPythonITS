
list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
print(list_comp)
print(gen_exp)

from sys import getsizeof
my_comp = [x * 5 for x in range(1000)]
my_gen = (x * 5 for x in range(1000))

print(getsizeof(my_comp))
print(getsizeof(my_gen))