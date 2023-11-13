# Implemente funciones que retornen las siguientes listas de enteros:
# a) Los primeros n términos de la sucesión de Fibonacci.
# b) Todos los números primos comprendidos entre 1 y un valor n.
# c) Todos los divisores de n comprendidos en el intervalo cerrado [1, n].

# a) Los primeros n términos de la sucesión de Fibonacci.

def fibonacci(n):
    ret_val=[]
    
    for i in range(0,n):
        if i == 0 or i == 1:
            ret_val.append(1)
        else:
            ret_val.append(ret_val[i-1]+ret_val[i-2])
    
    return ret_val

print(f'a) {fibonacci(10)}')

# b) Todos los números primos comprendidos entre 1 y un valor n.

def es_primo(n):
    import math
    
    if n<2:
        return False
    elif n==2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3,int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True
    
def listar_primos(n_max):
    primos=[]
    
    for n in range(1,n_max+1):
        if es_primo(n):
            primos.append(n)
    
    return primos

print(f'b) Los primos menores a 100 son: {listar_primos(100)}')

# c) Todos los divisores de n comprendidos en el intervalo cerrado [1, n].

def listar_divisores(n):
    divisores=[]
    for i in range(1,n):
        if n % i == 0:
            divisores.append(i)
    return divisores

print(f'c) Los divisores de 54 son: {listar_divisores(54)}')
