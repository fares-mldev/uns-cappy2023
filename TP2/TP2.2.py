
n=1000

suma_1=0
for i in range(n+1):
    suma_1 += (-1)**i / (i + 1)

print(f'Suma 1: {suma_1}')

suma_2=0
for i in range(n+1):
    suma_2 += i**(-i)

print(f'Suma 2: {suma_2}')