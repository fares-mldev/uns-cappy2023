def potencia(b,n):
    # Tiempo y Memoria O(log(n))
    if b==0: return 0
    else:
        if n==0 : return 1
        elif n < 0 : return 1 / potencia(b,-n)
        elif n % 2 == 0:
            p= potencia(b,n//2)
            return p * p
        else:
            p = potencia(b,(n-1) //2)
            return p * p * b
        
print(potencia(2,4))