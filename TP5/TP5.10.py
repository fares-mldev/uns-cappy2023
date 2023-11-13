# Dada una tupla con información de círculos en el plano, implemetente 
# funciones para realizar las siguientes consultas de interés:
# a) Determinar cuál es el círculo cuyo centro se encuentra más cercano a un (x,y) dado y a qué cuadrante pertenece.
# b) Determinar cuántos círculos dentro de la estructura se encuentran centrados sobre los ejes de coordenadas.
#    circulos = (c1, c2, . . . , cn), donde cada ci = (ri, (xi, yi)) es otra tupla con la magnitud del radio 
#    y las coordenadas #del centro del círculo en el plano XY.

circulos=((1,(1,1)),
          (1,(-1,1)),
          (1,(1,-1)),
          (1,(-1,-1)),
          (1,(0,1))
          )

punto=(4,5)

# a) Determinar cuál es el círculo cuyo centro se encuentra más cercano a un (x,y) dado y a qué cuadrante pertenece.

def identificar_cuadrante(p):
    x, y = p
    if x>=0 and y>=0:
        return 1
    if x<=0 and y>=0:
        return 2
    if x<=0 and y<=0:
        return 3
    if x>=0 and y<=0:
        return 4

def calcular_distacia(p1,p2):
    import math
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def encontrar_mas_cercano(circulos,p):
    distancias = [(calcular_distacia(circulo[1],punto),circulo) for circulo in circulos ]
    mas_cercano = distancias[0]
    for distancia in distancias:
        if distancia[0] < mas_cercano[0]:
            mas_cercano = distancia
    return mas_cercano[1]

mas_cercano=encontrar_mas_cercano(circulos,punto)
cuadrante=identificar_cuadrante(mas_cercano[1])
print(f'a) El círculo mas cercano a {punto} es {mas_cercano} y  se encuentra en el cuadrante {cuadrante}')

#b) Determinar cuántos círculos dentro de la estructura se encuentran centrados sobre los ejes de coordenadas.

def sobre_eje(p): 
    x, y = p
    return x == 0 or y == 0

def contar_sobre_eje(circulos):
    cant_sobre_eje=0
    for circulo in circulos:
        cant_sobre_eje += 1 if sobre_eje(circulo[1]) else 0
    return cant_sobre_eje

print(f'b) La cantidad de circulos centrados sobre ejes coordenados es: {contar_sobre_eje(circulos)}')