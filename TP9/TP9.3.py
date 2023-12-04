#Escriba una función recursiva que implemente la búsqueda binaria.

def busqueda_binaria_recursiva(lista, elemento, inicio=0, fin=None):
    # Si fin no se proporciona, establecerlo como la longitud del array
    if fin is None:
        fin = len(lista) - 1

    # Verificar si el elemento no está presente en el listaay
    if inicio > fin:
        return -1  # Elemento no encontrado

    # Calcular el índice medio
    medio = (inicio + fin) // 2

    # Verificar si el elemento está en la posición media
    if lista[medio] == elemento:
        return medio

    # Si el elemento es menor que el valor en la posición media, buscar en la mitad izquierda
    elif lista[medio] > elemento:
        return busqueda_binaria_recursiva(lista, elemento, inicio, medio - 1)

    # Si el elemento es mayor que el valor en la posición media, buscar en la mitad derecha
    else:
        return busqueda_binaria_recursiva(lista, elemento, medio + 1, fin)

# Ejemplo de uso
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_buscado = 5

indice_encontrado = busqueda_binaria_recursiva(lista_ordenada, elemento_buscado)

if indice_encontrado != -1:
    print(f"El elemento {elemento_buscado} está en la posición {indice_encontrado}.")
else:
    print(f"El elemento {elemento_buscado} no está en la lista.")