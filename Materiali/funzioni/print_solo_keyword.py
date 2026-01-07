import sys
def print30(*args, sep=' ', end='\n', file=sys.stdout, **kargs):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

print30(99)

def print30_2(*args, sep, end, file, **kargs):
    sep1 = kargs.pop('sep',' ')
    end1 = kargs.pop('end','\n')
    file1 = kargs.pop('file',sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

print30_2(99,sep=':',end=';',test='ciao')

def print30_1(*args,**kargs):
    sep = kargs.pop('sep',' ')
    end = kargs.pop('end','\n')
    file = kargs.pop('file',sys.stdout)
    if kargs: raise TypeError('extra keywords: %s' % kargs)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

print30_1(99,name='carlos')
# print30() got an unexpected keyword argument 'name'

print30_1(99,name='carlos')
# extra keywords: {'name': 'carlos'}