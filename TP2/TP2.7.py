#Escriba un bloque de sentencias que permita generar todos
#los números de la forma ABAB  con 1 ≤A ≤9 y 9 ≥B > 0

for a in range(1,10):
    for b in range(1,10):
        print(a,b,a,b)