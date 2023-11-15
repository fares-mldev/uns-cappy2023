# Implemente funciones que dada una lista de la forma del ejercicio 2.b, determine o retorne:
# a) Si todos sus elementos son impares.
# b) Si los valores negativos de la lista solo se encuentran en posiciones pares.
# c) Una nueva lista que contenga sólo los valores positivos ordenados de menor a mayor.
# d) Si el contenido de la lista es monótono creciente


def create_randint_list(n,a,b):
    import random 
    return [random.randint(a,b) for i in range(n)]    

def create_odd_sorted(n):
    return [2*i+1 for i in range(n,-1,-1)]    

n = 10

l = create_randint_list(n,-10,10)

# a) Si todos sus elementos son impares.

def are_all_odd(l):
    for i in l:
        if i%2 == 0:
            return False
    return True

test_a=[[9,-5,7],
      [-1,9,2]]

print('a) True si todos sus elementos son impares.')
for tst in test_a:
    print(f'{tst}: {are_all_odd(tst)}')

# b) Si los valores negativos de la lista solo se encuentran en posiciones pares.

def neg_in_even(l):
    for idx,i in enumerate(l):
        if i < 0 and idx%2 != 0:
            return False
    return True

test_b=[[ 1, 2,-3],
        [-1,-4,-3]]

print('a) True si los valores negativos de la lista solo se encuentran en posiciones pares.')
for tst in test_b:
    print(f'{tst}: {neg_in_even(tst)}')

# c) Una nueva lista que contenga sólo los valores positivos ordenados de menor a mayor.

test_c = create_randint_list(n,-10,10)

def pos_sorted(l):
    l_pos=[]
    for i in l:
        if i>=0:
            l_pos.append(i)
    return sorted(l_pos)

print('c) Una nueva lista que contenga sólo los valores positivos ordenados de menor a mayor.')
print(f'Lista original: {test_c}')
print(f'Valores positivos ordenados de menor a mayor: {pos_sorted(test_c)}')

# d) Si el contenido de la lista es monótono creciente

def monotonic_increasing(l):
    for idx,i in enumerate(l):
        if idx>0 and i<=prev:
            return False
        prev=i
    return True

test_d=[[ -1, 3, 5 ],
        [  1, 1, 2 ],
        [  1, 2, 1 ]]

print('d) Si el contenido de la lista es monótono creciente')
for l in test_d:
    print(f'{l}: {monotonic_increasing(l)}')