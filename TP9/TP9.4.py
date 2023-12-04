#Dada una cadena de caracteres, escriba funciones recursivas para:
#a) Determinar si es un palíndromo.
#b) Contar la cantidad de apariciones de una letra dada.
#c) Retornar la lista con las posiciones en las que aparece la letra.
#d) Retornar el conjunto de enteros con las posiciones en las que aparece la letra.

# a) Determinar si es un palíndromo
def es_palindromo(cadena):
    cadena = cadena.lower()  # Convertir la cadena a minúsculas para ignorar mayúsculas
    return es_palindromo_recursivo(cadena, 0, len(cadena) - 1)

def es_palindromo_recursivo(cadena, inicio, fin):
    if inicio >= fin:
        return True
    if cadena[inicio] != cadena[fin]:
        return False
    return es_palindromo_recursivo(cadena, inicio + 1, fin - 1)

# b) Contar la cantidad de apariciones de una letra dada
def contar_apariciones_letra(cadena, letra):
    cadena = cadena.lower()  # Convertir la cadena a minúsculas para ignorar mayúsculas
    letra = letra.lower()  # Convertir la letra a minúsculas para ignorar mayúsculas
    return contar_apariciones_letra_recursivo(cadena, letra, 0)

def contar_apariciones_letra_recursivo(cadena, letra, indice):
    if indice == len(cadena):
        return 0
    if cadena[indice] == letra:
        return 1 + contar_apariciones_letra_recursivo(cadena, letra, indice + 1)
    else:
        return contar_apariciones_letra_recursivo(cadena, letra, indice + 1)

# c) Retornar la lista con las posiciones en las que aparece la letra
def posiciones_letra(cadena, letra):
    cadena = cadena.lower()  # Convertir la cadena a minúsculas para ignorar mayúsculas
    letra = letra.lower()  # Convertir la letra a minúsculas para ignorar mayúsculas
    return posiciones_letra_recursivo(cadena, letra, 0, [])

def posiciones_letra_recursivo(cadena, letra, indice, posiciones):
    if indice == len(cadena):
        return posiciones
    if cadena[indice] == letra:
        posiciones.append(indice)
    return posiciones_letra_recursivo(cadena, letra, indice + 1, posiciones)

# d) Retornar el conjunto de enteros con las posiciones en las que aparece la letra
def conjunto_posiciones_letra_recursivo(cadena, letra, indice):
    if indice == len(cadena):
        return set()
    posiciones = conjunto_posiciones_letra_recursivo(cadena, letra, indice + 1)
    if cadena[indice] == letra:
        posiciones.add(indice)
    return posiciones

# Ejemplos de uso
cadena_ejemplo = "Anita lava la tina"
letra_ejemplo = "a"

print("Es palíndromo:", es_palindromo(cadena_ejemplo))
print("Cantidad de apariciones de la letra '{}': {}".format(letra_ejemplo, contar_apariciones_letra(cadena_ejemplo, letra_ejemplo)))
print("Posiciones de la letra '{}': {}".format(letra_ejemplo, posiciones_letra(cadena_ejemplo, letra_ejemplo)))
print("Conjunto de posiciones de la letra '{}': {}".format(letra_ejemplo, conjunto_posiciones_letra(cadena_ejemplo, letra_ejemplo)))
