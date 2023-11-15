#Implemente funciones que retornen listas de enteros de n
#elementos de la forma:
#a) Valores aleatorios entre [0, 100].
#b) Valores aleatorios entre [-x, x].
#c) Los primeros n números impares ordenados de mayor a menor.

#a) Valores aleatorios entre [0, 100].

import random 

def create_randint_list(n,a,b):
    return [random.randint(a,b) for i in range(n)]    

n = 10

#a) Valores aleatorios entre [0, 100].
print(f'a) Lista de {n} valores aleatorios entre 0 y 100: {create_randint_list(n,0,100)}')

#b) Valores aleatorios entre [-x, x].
x = 1
print(f'b) Lista de {n} valores aleatorios entre {-x} y {x}: {create_randint_list(n,-1,1)}')

#c) Los primeros n números impares ordenados de mayor a menor.

def create_odd_sorted(n):
    return [2*i+1 for i in range(n,-1,-1)]    

print(f'c) Los primeros {n} números impares ordenados de mayor a menor: {create_odd_sorted(n)}')
