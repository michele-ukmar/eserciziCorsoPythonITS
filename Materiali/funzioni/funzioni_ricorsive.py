
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


# Questa funzione prende in input un intero positivo ne restituisce il valore del suo fattoriale.
# Se n è uguale a 1, la funzione restituisce 1 (il fattoriale di 1). Altrimenti, 
# la funzione restituisce il prodotto tra n e il risultato della chiamata ricorsiva alla funzione 
# factorial con argomento n-1.

# Ad esempio, se chiamiamo factorial(5), la funzione restituirà il valore 120 (poiché 5! = 5 x 4 x 3 x 2 x 1 = 120).
