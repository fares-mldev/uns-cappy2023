# Realice funciones apropiadas para realizar cada una de las siguientes 
# operaciones a partir de una lista de fechas nacimientos que contiene 
# las fechas de nacimiento de un grupo de personas (dia, mes, año). 
# 
# a) Extraer de la lista el cumpleaños de la persona más joven.
# b) Ordenar la lista por orden cronológico. Implemente su propio algoritmo de ordenamiento.

fechas=[( 9,12,1976),
        ( 9, 1,1981),
        (20, 3,2008),
        (22, 3,2011)]

def es_mas_joven(f1,f2):
    if f1[2] > f2[2]:
        return True
    elif f1[2] < f2[2]:
        return False
    elif f1[2] == f2[2]:
        if f1[1] > f2[1]:
            return True
        elif f1[1] == f2[1] and f1[0] > f2[0]:
            return True
        else:
            return False
    
def extraer_mas_joven(fechas):
    mas_joven=None
    for fecha in fechas:
        if mas_joven is not None:
            if es_mas_joven(fecha,mas_joven):
                mas_joven=fecha
        else:
            mas_joven=fecha
    return mas_joven


print(f'El listado es: {fechas}')
print(f'La fecha de nacimiento de la persona mas joven es: {extraer_mas_joven(fechas)}')

fechas.remove(extraer_mas_joven(fechas))

print(f'El listado resultante es: {fechas}')

# b) Ordenar la lista por orden cronológico. Implemente su propio algoritmo de ordenamiento.
# https://arxiv.org/pdf/2110.01111.pdf
def ordenar_fechas(l):
    n=len(l)
    for i in range(1,n):
        for j in range(i):
            if es_mas_joven(l[j],l[i]):
                l[i], l[j] = l[j], l[i]
    return l

fechas=[( 10, 1,1981),
        (20, 2,2008),
        ( 9,12,1976),
        ( 9, 1,1981),
        (22, 3,2011),
        ( 10, 5,1981),
        (20, 3,2008),
        (19, 2,2008)]

print('b) Ordenar la lista por orden cronológico. Implemente su propio algoritmo de ordenamiento.')
print(f'Las fechas desordenadas: {fechas}')
print(f'Las fechas ordenadas: {ordenar_fechas(fechas)}')