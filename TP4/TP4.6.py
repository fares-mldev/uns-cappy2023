#Dada una tupla con valores enteros, determine:
#a) Si los valores se encuentran ordenados de mayor a menor.
#b) Si un elemento n ingresado por el usuario pertenece a la secuencia.
#c) Si contiene los primeros términos de la serie de fibonacci.

t=(9,7,5,2,1)

#a) Si los valores se encuentran ordenados de mayor a menor.
prev=None
ordered=True
for i in t:
    print(i,prev,ordered)
    ordered= prev>=i if prev is not None else True
    prev=i
    if not ordered:
        break

#b) Si un elemento n ingresado por el usuario pertenece a la secuencia.
n = 4
belongs= n in t
print(f'{n} {"pertenece" if belongs else "no pertenece"} a {t}')

#c) Si contiene los primeros términos de la serie de fibonacci.

n = 4 # 4 primeros términos de fibonacci

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

print(f'{t} {"contiene" if contains else "no contiene"} los primeros {n} numeros de la secuencia de fibonacci')
