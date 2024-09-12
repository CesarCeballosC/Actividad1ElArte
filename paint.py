"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


# Se crea función para dibujar una linea desde un punto de inicio a un punto final
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


# Se crea función para dibujar un cuadrado desde un punto de inicio a un punto final
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4): # Se dibuja un cuadrado
        forward(end.x - start.x)
        left(90)

    end_fill()


# Se crea función para dibujar un círculo con un tamaño designado por la persona
def circlef(start, end):
    up()
    goto(start.x, start.y) # Se mueve el cursor a la posición de inicio
    down()   

    begin_fill() # Se inicia a dibujar el círculo
    circle((end.x - start.x)/2)
    end_fill()


# Se crea función para dibujar un rectángulo desde un punto de inicio a un punto final
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()             
    goto(start.x,start.y) #Se mueve el cursor a la posición de inicio
    down()           
    begin_fill()        

    for i in range(2): # Se dibuja un rectángulo
        forward(start.x)  
        left(90)
        forward(end.y) 
        left(90)

    end_fill()  

# Se crea función para dibujar un triángulo desde un punto de inicio a un punto final
def triangle(start, end):
    """Draw triangle from start to end."""

    up() 
    goto(start.x, start.y) # Se mueve el cursor a la posición de inicio
    down()
    
    begin_fill() # Se inicia a dibujar el triángulo
    x1, y1 = start.x, start.y
    x2, y2 = end.x, start.y
    x3, y3 = (start.x + end.x) / 2, end.y

    
    goto(x2, y2) 
    goto(x3, y3)  
    goto(x1, y1)  
    end_fill() 



def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']  

    if start is None:
        state['start'] = vector(x, y) # Se guarda el punto de inicio
    else:
        shape = state['shape'] # Se guarda la forma
        end = vector(x, y)
        shape(start, end)
        state['start'] = None



def store(key, value):
    """Store value in state at key."""
    state[key] = value # Se guarda el valor en el estado de la llave


# Se crea función para cambiar el color de la forma
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0) # Se configura la ventana
onscreenclick(tap)
listen()
onkey(undo, 'u') # Se deshace la última acción

# Se crean las teclas para cambiar el color de la forma
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')

# Se crean las teclas para cambiar la forma de la figura
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circlef), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

