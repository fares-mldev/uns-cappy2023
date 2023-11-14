def filtrar(palabra):
    raros='".%(){}+,'
    while palabra[0] in raros: palabra = palabra[1:]
    while palabra[-1] in raros: palabra = palabra[:-1]
    return palabra.lower()

def agregar_palabra(palabra,d):
    if palabra in d:
        d[palabra] += 1
    else:
        d[palabra] = 1
      
texto="Each element of iterable, such as a list or a tuple, is assigned to variable_name and evaluated with expression. A new list is created with the result evaluated by expression as an element."  
diccionario ={}

palabras=texto.split(' ')

palabras=[filtrar(p) for p in palabras]

for p in palabras:
    agregar_palabra(p,diccionario)

for p,c in sorted(diccionario.items()):
    print(p,c)

print(type(diccionario.keys()))
# Librerias NLP
#nltk
#beautiful soup