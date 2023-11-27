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

print(fib_memo(100))