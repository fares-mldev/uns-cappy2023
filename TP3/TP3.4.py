# Determine el cuadrante al cuál pertenece un punto en el plano representado por una tupla de reales de la forma (x,y). 
# ¿Qué resultado se obtendría si el punto se encuentra sobre alguno de los ejes cartesianos o ambos?

x=0
y=0
p=(x,y)

x,y=p

if x>=0 and y>=0:
    print('Cuandrante 1')

if x<=0 and y>=0:
    print('Cuandrante 2')

if x<=0 and y<=0:
    print('Cuandrante 3')

if x>=0 and y<=0:
    print('Cuandrante 4')
