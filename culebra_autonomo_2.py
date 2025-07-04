### --- Importamos desde la biblioteca interna de Python ---
from turtle import *
from random import randrange
bgcolor("black")
title("Culebreando Ando")

### ---PLANTILLA TOMADA DE CCE para Turtle ---
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def copy(self):
        return Vector(self.x, self.y)

    def move(self, other):
        self.x += other.x
        self.y += other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

### --- Función para dibujar cuadrados ---
def square(x, y, size, color_name):
    up()
    goto(x, y)
    down()
    color(color_name)
    begin_fill()
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()

### --- Variables del juego ---
manzana = Vector(0, 0)
culebra = [Vector(10, 0)]
ruta = Vector(0, -10)

### --- Función para cambiar la dirección ---
def change(x, y):
    ruta.x = x
    ruta.y = y

### --- Verifica si la cabeza está dentro de los límites ---
def inside(cabeza):
    return -200 < cabeza.x < 190 and -200 < cabeza.y < 190

### --- Movimiento principal del juego ---
def move():
    cabeza = culebra[-1].copy()
    cabeza.move(ruta)

    if not inside(cabeza) or cabeza in culebra:
        square(cabeza.x, cabeza.y, 9, 'orange')
        update()
        return

    culebra.append(cabeza)

    if cabeza == manzana:
        print("tamaño culebra:", len(culebra))
        manzana.x = randrange(-15, 15) * 10
        manzana.y = randrange(-15, 15) * 10
    else:
        culebra.pop(0)

    clear()

    for cuerpo in culebra:
        square(cuerpo.x, cuerpo.y, 9, 'white')

    square(manzana.x, manzana.y, 9, 'red')
    update()
    ontimer(move, 100)

### --- Configuración de la ventana y eventos ---
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
manzana.x = randrange(-15, 15) * 10
manzana.y = randrange(-15, 15) * 10
move()
done()
