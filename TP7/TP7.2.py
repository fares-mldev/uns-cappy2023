#Dada una lista de enteros positivos ordenada con repeticio-
#nes (Ver el ejercicio 4 del Trabajo Práctico 6, implemente
#una función que guarde en un archivo la información de
#los pares dato-frecuencia.

archivo_entrada='./TP7/TP7.2.in'
archivo_salida='./TP7/TP7.2.out'

# Generar archivo de entrada
import random
with open(archivo_entrada, 'w') as archivo:
    for n in range(101):
        archivo.write(f'{random.randint(0,10)}\n')

# funciones auxiliares
def contar_ocurrencias(l):
    f={}
    for i in l:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    return {k:f[k] for k in f}

# Leer archivo de entrada y escribir lista
numeros=[]
with open(archivo_entrada, 'r') as archivo:
    for linea in archivo:
        numeros.append(int(linea.strip()))

# computar ocurrencias
dict_ocurrencias=contar_ocurrencias(numeros)

# Escribir en archivo de salida
with open(archivo_salida, 'w') as archivo:
    for n in sorted(dict_ocurrencias):
        ocurrencias=dict_ocurrencias[n]
        archivo.write(f'{n} {ocurrencias}\n')