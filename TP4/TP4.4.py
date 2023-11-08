#Implemente un script para determinar:
#a) Si un número entero positivo es primo.
#b) El máximo divisor entero de un número.

import math

n=10451

es_primo=True

if n<2:
    es_primo=False
elif n==2:
    es_primo=True
elif n % 2 == 0:
    es_primo=False
else:
    for i in range(3,int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            es_primo=False
            break
    
print('a) Es primo' if es_primo else 'No es primo')

max_divisor=1
for i in range(2,int(math.sqrt(n)) + 1, 1):
    if n % i == 0 and i > max_divisor:
        max_divisor=i

print(f'b) El divisor máximo es: {max_divisor}')
