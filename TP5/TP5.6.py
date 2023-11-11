#Escriba una función que dada la altura y un caracter dibuje
#un pinito de dicho caracter siguiendo las especificaciones
#del ejercicio 5 del Trabajo Práctico 2. En caso de que el usua-
#rio no especifique un caracter al momento de la invocación
#utilice * por defecto.


n=10
c='|'
n = int(input('N ('+ str(n)+  '):') or n)
c = input('c ('+ c+  '):') or c

def pyramid(n,c='*'):
    for lvl in range(n):
        str=' '*(n-1-lvl) + c[0]*(2*lvl+1)
        print(str)
        
pyramid(n,c)

pyramid(n)
