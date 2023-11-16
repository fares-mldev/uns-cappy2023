#Implemente un script que a partir de un archivo de texto
#con números enteros positivos genere una archivo de salida
#con la siguiente información:
# a) Cada uno de los enteros del archivo de entrada junto a su máximo divisor entero distinto de si mismo.
# b) Cada uno de los enteros del archivo de entrada junto a la lista completa de divisores del número.

archivo_entrada='./TP7/TP7.1.in'
archivo_salida_a='./TP7/TP7.1.a.out'
archivo_salida_b='./TP7/TP7.1.b.out'

# Generar archivo de entrada
with open(archivo_entrada, 'w') as archivo:
    for n in range(2,101):
        archivo.write(f'{n}\n')

# funciones auxiliares
def max_div(n):
    for i in range(n-1,1,-1):
        if n % i == 0:
            return i
    return None

def all_divs(n):
    divs=[]
    for i in range(n-1,1,-1):
        if n % i == 0:
            divs.append(i)
    return divs
        
# a) Cada uno de los enteros del archivo de entrada junto a su máximo divisor entero distinto de si mismo.

dict_max_div={}
with open(archivo_entrada, 'r') as archivo:
    for linea in archivo:
        n = int(linea.strip())
        dict_max_div[n] = max_div(n)

with open(archivo_salida_a, 'w') as archivo:
    for n in dict_max_div:
        max_div=dict_max_div[n]
        archivo.write(f'{n} {max_div if max_div is not None else ""}\n')

# b) Cada uno de los enteros del archivo de entrada junto a la lista completa de divisores del número.

dict_all_divs={}
with open(archivo_entrada, 'r') as archivo:
    for linea in archivo:
        n = int(linea.strip())
        dict_all_divs[n] = all_divs(n)

with open(archivo_salida_b, 'w') as archivo:
    for n in dict_all_divs:
        all_divs=dict_all_divs[n]
        archivo.write(f'{n} {" ".join(map(str, all_divs))}\n')