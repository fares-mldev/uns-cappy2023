# Se desea almacenar la ruta de viaje de vehículos no tripula-
# dos que realizan una travesía de postas definidas a partir
# de las coordenadas cartesianas (x,y) expresadas en metros.
# Considerando que el desplazamiento entre postas sucesivas
# es lineal, defina un diccionario que le permita almacenar
# la información e implemente funciones apropiadas para
# identificar cuál de los vehículos:
# a) Recorrió la mayor distancia.
# b) Abarcó la menor superficie rectangular.

def generar_trayectoria(n):
    import random
    x , y = ( 0 , 0 )
    t = [(x,y)]
    for i in range(n):
        x+=random.randint(-2,2)
        y+=random.randint(-2,2)
        t.append((x,y))
    return t


def calcular_distancia(t):
    d = 0
    prev=t[0]
    for step in t:
        d += ((step[0]-prev[0])**2 + (step[1]-prev[1])**2)**0.5
        prev=step
    return d

t1 = generar_trayectoria(10)
t2 = generar_trayectoria(10)   

d1 = calcular_distancia(t1)
d2 = calcular_distancia(t2)

vehiculo_mayor_distancia = 1 if d1 > d2 else 2
print(f'a) El vehiculo que cubrió mayor distancia es el {vehiculo_mayor_distancia}')
print(f'distancia vehiculo 1: {d1:0.2f} m')
print(f'distancia vehiculo 2: {d2:0.2f} m')

# b) Abarcó la menor superficie rectangular.

def superficie_rectangular(t):
    x = [x for x,y in t]
    y = [y for x,y in t]
    return (max(x) - min(x)) * (max(y)- min(y)) 

s1 = superficie_rectangular(t1)
s2 = superficie_rectangular(t2)

vehiculo_menor_superficie = 1 if s1 > s2 else 2

print(f'a) El vehiculo que abarcó la menor superficie rectangular es {vehiculo_menor_superficie}')
print(f'superficie vehiculo 1: {s1:0.2f} m2')
print(f'superficie vehiculo 2: {s2:0.2f} m2')