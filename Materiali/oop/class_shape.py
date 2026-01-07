
class Shape(object):
    '''Un oggetto di tipo Shape rappresenta una figura geometrica generica'''

    @property
    def area(self):
        '''Restituisce l'area della figura'''
        pass

    @property
    def perimeter(self):
        '''Restituisce il perimetro della figura'''
        pass

    @property
    def name(self):
        return getattr(self, '_name', 'Untitled')
        # restituisce l'attributo _name se esiste, altrimenti 'Untitled'
        