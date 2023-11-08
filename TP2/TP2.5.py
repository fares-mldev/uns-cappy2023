# Escribir un script que pida al usuario un número entero y
# muestre por pantalla un pino de asteriscos cuya altura es el
# dato introducido.

#   *
#  ***
# *****

n=10
n = int(input('N ('+ str(n)+  '):') or n)

for lvl in range(n):
    str=' '*(n-1-lvl) + '*'*(2*lvl+1)
    print(str)