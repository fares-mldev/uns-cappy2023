# Escriba funciones para retornar el conjunto de:
# a) Palabras que aparecen en dos archivos de texto distintos.
# b) Todas las posiciones en las que un caracter dado aparece en una cadena.
# c) Las letras que aparecen en todas las líneas de un archivo de texto.

archivo_1='./TP8/TP8.2.in.1'
archivo_2='./TP8/TP8.2.in.2'

def clean_line(line):
    import re
    lowercase_line = line.lower()
    cleaned_line = re.sub(r'[^a-zA-Z0-9\s+]', '', lowercase_line.strip())

    return cleaned_line

def line_to_set(line):
    ret_val=set()
    for word in line.split(' '):
        ret_val.add(word)
    return ret_val
        
def read_file(fn):
    ret_val=set()
    with open(fn, 'r') as archivo:
        for linea in archivo:
            ret_val=ret_val.union(line_to_set(clean_line(linea)))
    return ret_val

set_1=read_file(archivo_1)
set_2=read_file(archivo_2)

# a) Palabras que aparecen en dos archivos de texto distintos.

print(f'# a) Palabras que aparecen en dos archivos de texto distintos: {set_1.intersection(set_2)}')

# b) Todas las posiciones en las que un caracter dado aparece en una cadena.

def buscar_posiciones(linea, caracter):
    posiciones = set()
    for i in range(len(linea)):
        if linea[i] == caracter:
            posiciones.add(i)
    return posiciones

def buscar_posiciones_archivo(fn,caracter):
    ret_val=set()
    with open(fn, 'r') as archivo:
        for linea in archivo:
            ret_val=ret_val.union(buscar_posiciones(linea,caracter))
    return ret_val

caracter='a'
archivo=archivo_1
posiciones=buscar_posiciones_archivo(archivo_1,'a')

print(f'b) Todas las posiciones en las que el caracter "{caracter}" aparece en una cadena del archivo {archivo} son: {posiciones}')

# c) Las letras que aparecen en todas las líneas de un archivo de texto.

def buscar_letras(linea):
    letras_str=''.join(char.lower() for char in linea if char.isalpha())
    letras_set=set(letras_str)
    return letras_set

def buscar_letras_archivo(fn):
    ret_val=set()
    with open(fn, 'r') as archivo:
        for linea in archivo:
            if not ret_val:
                ret_val=buscar_letras(linea)
            else:
                ret_val=ret_val.intersection(buscar_letras(linea))
    return ret_val

caracter='a'
archivo=archivo_1
letras=buscar_letras_archivo(archivo_1)

print(f'c) Las letras que aparecen en todas las líneas del un archivo de texto {archivo} son: {letras}')