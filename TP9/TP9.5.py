
#Realice una función recursiva para verificar si una lista de
#N elementos enteros esta ordenada de mayor a menor.

def esta_ordenada_de_mayor_a_menor(lista):
    if len(lista) <= 1:
        return True  # Una lista vacía o con un solo elemento está siempre ordenada

    # Verificar si el primer elemento es mayor o igual que el segundo
    if lista[0] >= lista[1]:
        # Llamada recursiva para el resto de la lista
        return esta_ordenada_de_mayor_a_menor(lista[1:])
    else:
        return False

# Ejemplo de uso
lista_ejemplo = [5, 4, 3, 2, 1]
if esta_ordenada_de_mayor_a_menor(lista_ejemplo):
    print("La lista está ordenada de mayor a menor.")
else:
    print("La lista no está ordenada de mayor a menor.")
