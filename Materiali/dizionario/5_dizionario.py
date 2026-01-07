italian = {'cane':'dog', 'gatto':'cat', 'mucca':'cow'}
print(italian)
# Output: {'cane': 'dog', 'gatto': 'cat', 
# 'mucca': 'cow'}

milanese = italian
print(milanese)
# Output: {'cane': 'dog', 'gatto': 'cat', 
# 'mucca': 'cow'}


italian['ragno']='spider'
print(italian)
# Output: {'cane': 'dog', 'gatto': 'cat', 
# 'mucca': 'cow', 'ragno': 'spider'}

milanese['cane'] = 'cagnol'
print(milanese)
print(italian)
# Output: {'cane': 'cagnol', 'gatto': 'cat', 
# 'mucca': 'cow', 'ragno': 'spider'}

