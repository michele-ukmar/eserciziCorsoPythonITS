
from UFS02.class_ereditarieta import Circle, Rectangle

c=Circle(4)
print('Area del cerchio:', c.area)
print('Perimetro del cerchio:', c.perimeter)
print('Nome:', c.name)
print(type(c))

# Area del cerchio: 50.2654824574
# Perimetro del cerchio: 25.1327412287
# Nome: Untitled
# <class '__main__.Circle'>

r=Rectangle(10,20)
print('Area del rettangolo:', r.area)
print('Perimetro del rettangolo:', r.perimeter)
print('Nome:', r.name)
print(type(r))

# Area del rettangolo: 200
# Perimetro del rettangolo: 60
# Nome: A rectangle
# <class '__main__.Rectangle'>