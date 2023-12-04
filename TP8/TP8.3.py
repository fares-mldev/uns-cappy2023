#La Criba de Eratóstenes es un algoritmo que permite hallar todos los números primos menores 
# que un número #natural dado. A partir del conjunto de números naturales #comprendidos entre 
# 2 y n escriba una función que retorne el conjunto de números primos menores que n empleando
#dicho algoritmo

def criba_eratostenes(n):
    multiplos = set()
    primos = set()
    for i in range(2, n+1):
        if i not in multiplos:
            primos.add(i)
            multiplos.update(range(i*i, n+1, i))
    return primos

n=100
n = int(input(f'Ingrese n ({n}):') or n)

print(f'{criba_eratostenes(n)}')