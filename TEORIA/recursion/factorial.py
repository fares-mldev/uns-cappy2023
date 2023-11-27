def factorial_recursivo(n):
    #Tiempo O(N)
    #Memoria O(N)
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

def factorial_iterativo(n):
    #Tiempo O(N)
    #Memoria O(1)
    result=1
    for i in range(1,n+1):
        result*=i
    return result

print(factorial_iterativo(10),factorial_recursivo(10))
        