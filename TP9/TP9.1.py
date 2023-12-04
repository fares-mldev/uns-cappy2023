#Escriba una función recursiva y otra iterativa para obtener
#el n-ésimo elemento de la sucesión de Fibonacci. Compare
#ambas implementaciones de acuerdo a la utilización de
#memoria, el tiempo de ejecución y la claridad del código
#en relación a la definición del problema.

def fib_recursivo(n):
    # Tiempo y memoria O(2**n)
    if n <= 1: return 1
    else: return fib_recursivo(n-1)+fib_recursivo(n-2)

def fib_memo(n,m={}):
    # Tiempo y memoria O(2**n)
    if n <= 1: return 1
    elif n in m: 
        return m[n]
    else: 
        result=fib_memo(n-1,m)+fib_memo(n-2,m)
        m[n]=result
        return result  

n=100
print(f'Método iterativo f(100): {fib_memo(n)}')
print(f'Método recursivo f(100): {fib_memo(n)}')