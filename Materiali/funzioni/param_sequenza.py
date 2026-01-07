# In questo caso, la funzione può accettare qualsiasi numero di argomenti posizionali.

def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# In questo caso, l'operatore * prima del parametro numbers indica che la 
# funzione può accettare un numero variabile di argomenti posizionali. 
# In pratica, quando viene chiamata la funzione, possiamo passare uno o più argomenti separati da virgola, 
# e tutti questi argomenti verranno raccolti nella tupla numbers. Ad esempio:

sum_numbers(1, 2, 3)
# output: 6

sum_numbers(4, 5, 6, 7, 8)
# output: 30 

