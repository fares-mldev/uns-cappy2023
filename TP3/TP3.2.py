# Empleando dos dígitos distintos, A y B, escriba un script
# para inicializar al entero M siguiendo las siguientes reglas:
# a) El mayor número entero de dos cifras.
# b) El menor número de 4 dígitos intercalando los mismos.
# c) El menor número capicúa de tres cifras.
# d) El mayor número capicúa de 5 dígitos.

a=1
b=2

#a = int(input('M ('+ str(a)+  '):') or a)
#b = int(input('M ('+ str(b)+  '):') or b)

# a) El mayor número entero de dos cifras.
print(f'El mayor número de dos cifras es {max(a,b)}{min(a,b)}')

# b) El menor número de 4 dígitos intercalando los mismos.
print(f'El menor número de 4 dígitos intercalando los mismos es {min(a,b)}{max(a,b)}{min(a,b)}{max(a,b)}')

# c) El menor número capicúa de tres cifras.
print(f'El menor número capicúa de tres cifras es {min(a,b)}{max(a,b)}{min(a,b)}')

# d) El mayor número capicúa de 5 dígitos.
print(f'El mayor número capicúa de 5 dígitos es {max(a,b)}{min(a,b)}{max(a,b)}{min(a,b)}{max(a,b)}')
