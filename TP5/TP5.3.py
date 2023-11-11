#Transforme los bloques de sentencias pedidos en los ejerci-
#cios 3 y 6 del Trabajo Práctico 4 en funciones

# TP4.3
# Escriba bloques de sentencias en un script que a partir de
# un entero positivo n ingresado por el usuario calcule:
# a) Sus dígitos más y menos significativos.
# b) La cantidad de dígitos del número.
# c) La cantidad de dígitos pares e impares.
# d) Un entero con sus dígitos en orden inverso.
# e) Un entero solo con los dígitos pares.

n=1234569

def msd(n):
    return str(n)[0]

def lsd(n):
    return str(n)[-1]

def n_dig(n):
    return len(str(n))

print(f'a) Dígito más significativo: {msd(n)}. Dígito menos significativo: {lsd(n)}')

print(f'b) Cantidad de dígitos: {n_dig(n)}')

def n_dig_even_odd(n):
    pares=0
    impares=0
    for c in str(n):
        pares+=1 if int(c) % 2 == 0 else 0
        impares+=1 if int(c) % 2 != 0 else 0

    return pares,impares

pares,impares=n_dig_even_odd(n)
print(f'c) Cantidad de dígitos pares: {pares}. Cantidad de números impares: {impares}')

def inv_n(n):
    str_inv=''
    for c in str(n):
        str_inv = c + str_inv
    return str_inv

print(f'd) Número invertido: {inv_n(n)}')

def even_dig(n):
    str_par=''
    for c in str(n):
        str_par+=c if int(c) % 2 == 0 else ''
    return str_par
    
print(f'e) Sólo dígitos pares: {even_dig(n)}')

# TP4.6
#a) Si los valores se encuentran ordenados de mayor a menor.
#b) Si un elemento n ingresado por el usuario pertenece a la secuencia.
#c) Si contiene los primeros términos de la serie de fibonacci.

t=(9,7,5,2,1)

#a) Si los valores se encuentran ordenados de mayor a menor.

def is_ordered(t):
    prev=None
    ordered=True
    for i in t:
        ordered= prev>=i if prev is not None else True
        prev=i
        if not ordered:
            break
    return ordered

print(f'a) {t}{"" if is_ordered(t) else "NO"} está ordenada de mayor a menor')

#b) Si un elemento n ingresado por el usuario pertenece a la secuencia.
n = 4

def belongs(n,t):
    return n in t

print(f'{n} {"pertenece" if belongs(n,t) else "no pertenece"} a {t}')

#c) Si contiene los primeros términos de la serie de fibonacci.

n = 4 # 4 primeros términos de fibonacci

def contains(n,t):

    contains = 1 in t

    f_k_2=1
    f_k_1=1
    for k in range(3,n+1):

        # stop condition
        if not contains:
            break
            
        # f(k)
        f_k= f_k_2 + f_k_1
        
        # actualizo f(k-1) y f(k-2) 
        f_k_2=f_k_1
        f_k_1=f_k

        contains = f_k in t

    return contains

print(f'{t} {"contiene" if contains(n,t) else "no contiene"} los primeros {n} numeros de la secuencia de fibonacci')
