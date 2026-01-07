
import tkinter
from ModuloCerchio import Cerchio


mioCerchio = Cerchio([10,30], 20)
myOtherCircle = Cerchio([4,60], 10)

canvas = tkinter.Canvas(width=200, height=200)
mioCerchio.draw(canvas)
canvas.pack()
mioCerchio.draw(canvas)
mioCerchio.move(100, 100)