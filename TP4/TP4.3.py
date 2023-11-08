# Escriba bloques de sentencias en un script que a partir de
# un entero positivo n ingresado por el usuario calcule:
# a) Sus dígitos más y menos significativos.
# b) La cantidad de dígitos del número.
# c) La cantidad de dígitos pares e impares.
# d) Un entero con sus dígitos en orden inverso.
# e) Un entero solo con los dígitos pares.

n=1234569

print(f'a) Dígito más significativo: {str(n)[0]}. Dígito menos significativo: {str(n)[-1]}')

print(f'b) Cantidad de dígitos: {len(str(n))}')

pares=0
impares=0
for c in str(n):
    pares+=1 if int(c) % 2 == 0 else 0
    impares+=1 if int(c) % 2 != 0 else 0

print(f'c) Cantidad de dígitos pares: {pares}. Cantidad de números impares: {impares}')

str_inv=''
for c in str(n):
    str_inv = c + str_inv

print(f'd) Número invertido: {str_inv}')

str_par=''
for c in str(n):
    str_par+=c if int(c) % 2 == 0 else ''

print(f'e) Sólo dígitos pares: {str_par}')