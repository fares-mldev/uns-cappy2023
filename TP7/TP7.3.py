# Implemente un script que a partir de un archivo de texto con fechas de la forma dia/mes/año
# 31/10/2013\n 31/11/2002\n 29/2/2019\n... realice las siguientes operaciones:
# a) Cargue la lista nacimientos solo con las fechas válidas incluidas en el archivo.
# Los meses de abril, junio, septiembre y noviembre tienen 30 días; el mes de febrero puede tener 29 o
# 28 días dependiendo de si se trata de un año bisiesto o no; y los meses restantes poseen 31 días. 
# Recuerde que un año es bisiesto si cumple con la condición de ser divisible por 4 pero no por 100 o, 
# es múltiplo de 400.
# b) Ordene la lista nacimientos con las fechas ordenadas cronológicamente.
# c) Guarde la lista ordenada en un archivo de texto.

import random
# generar 1000 fechas, algunas pueden ser inválidas
fechas_in = [(random.randint(1,31),random.randint(1,12),random.randint(2000,2023)) for i in range(1000)]
archivo_entrada='./TP7/TP7.3.in'

# Generar archivo de entrada
with open(archivo_entrada, 'w') as archivo:
    for d,m,a in fechas_in:
        archivo.write(f'{d}/{m}/{a}\n')

# funciones auxiliares
def fecha_valida(t):
    d,m,a=t

    es_bisiesto= ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0)
    es_mes_valido= m in range(1,13)

    max_d=0
    if m in (1,3,5,7,8,10,12):
        max_d=31 
    elif m in (4,6,9,11):
        max_d=31 
    elif m==2:
        max_d=28 if es_bisiesto else 29

    es_dia_valido= d in range(1,max_d+1)


    es_fecha_valida = es_mes_valido and es_dia_valido

    return es_fecha_valida

#a) Cargue la lista nacimientos solo con las fechas válidas incluidas en el archivo.

fechas=[]
with open(archivo_entrada, 'r') as archivo:
    for linea in archivo:
        
        # parsear linea 
        fecha = tuple(map(int,linea.strip().split('/')))
        
        # verifico si es válida
        if fecha_valida(fecha):
            # agrego a la nueva lista
            fechas.append(fecha)

# b) Ordene la lista nacimientos con las fechas ordenadas cronológicamente.

def es_mas_reciente(f1,f2):
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
        
def ordenar_fechas(l):
    n=len(l)
    for i in range(1,n):
        for j in range(i):
            if es_mas_reciente(l[j],l[i]):
                l[i], l[j] = l[j], l[i]
    return l

fechas_out = ordenar_fechas(fechas)

# c) Guarde la lista ordenada en un archivo de texto.

# Generar archivo de salida
archivo_salida='./TP7/TP7.3.out'
with open(archivo_salida, 'w') as archivo:
    for d,m,a in fechas_out:
        archivo.write(f'{d}/{m}/{a}\n')