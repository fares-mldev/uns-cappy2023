# Escribir un script que pida al usuario un dígito y muestre por
# pantalla un triángulo rectángulo de números cuya altura es
# el dato introducido.

# N = 4
# 1
# 31
# 531
# 7531

n=10
n = int(input('N ('+ str(n)+  '):') or n)

for lvl in range(n):
    line=''
    for i in range(2*lvl+1,0,-2):
        line+=str(i)
    print(line)