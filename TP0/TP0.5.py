
m=100
p=5
n=12

m = int(input('M ('+ str(m)+  '):') or m)
p = int(input('P ('+ str(p)+  '):') or p)
n = int(input('N ('+ str(n)+  '):') or n)

#a) Tiene dos dígitos.
if -99 <= n <= 99:
    print(n, 'Tiene dos dígitos')

#b) Pertenece al intervalo semiabierto [0,37).
if 0 <= n <= 37:
    print(n, 'Pertenece al intervalo semiabierto [0,37)')

#c) Tiene al menos tres dígitos.
if n >= 1000 or n <= -1000 :
    print(n, 'Tiene al menos tres dígitos')

#d) Es el predecesor del entero M.
if n == m-1 :
    print(n, 'Es el predecesor de',m)

#e) Es el sucesor o el predecesor del entero M.
if n == m-1 or n == m+1:
    print(n, 'Es el sucesor o el predecesor de',m)

#f) Es par.
if n % 2 == 0:
    print(n, 'Es par')

#g) Es impar y positivo.
if n % 2 != 0 and n > 0:
    print(n, 'Es impar y positivo')

#h) Es divisor de M y múltiplo de P (donde M y P también
#son números enteros).
if m % n == 0 and n % p == 0:
    print(n, 'Es divisor de', m, 'y múltiplo de', p)

#i) No es múltiplo de 3 pero sí de 5.
if n % 3 != 0 and n % 5 == 0:
    print(n, 'No es múltiplo de 3 pero sí de 5')
    
#j) Es múltiplo de 3 y no de 5 o es múltiplo de 5 y no de 3.
if (n % 3 == 0 and n % 5 != 0) or (n % 3 != 0 and n % 5 == 0):
    print(n, 'Es múltiplo de 3 y no de 5 o es múltiplo de 5 y no de 3')