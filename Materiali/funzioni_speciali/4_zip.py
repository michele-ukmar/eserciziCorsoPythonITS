#esempio di utilizzo di zip
#zip() prende due o piu' sequenze e le combina in una sequenza 
# di coppie

#zip() prende due o piu' sequenze e le combina in una sequenza
#di coppie


x = [1,2,3]
y = ['4','5','6']
risultato_zip = zip(x,y)

a, b = zip(*risultato_zip)
print("x={0}, y={1}".format(a,b))
# Output: x=(1, 2, 3), y=('4', '5', '6')

print(list(risultato_zip))
# Output: []