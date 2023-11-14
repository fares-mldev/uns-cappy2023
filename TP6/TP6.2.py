#Implemente funciones que retornen listas de enteros de n
#elementos de la forma:
#a) Valores aleatorios entre [0, 100].
#b) Valores aleatorios entre [-x, x].
#c) Los primeros n números impares ordenados de mayor a menor.

#a) Valores aleatorios entre [0, 100].

import random 

def create_randint_list(n):
    return [random.randint() for i in range(n)]    

print(f'a) Lista de{create_randint_list(n))'}