#Dado un entero positivo de cinco cifras n, escriba el bloque
#de sentencias necesarias para determinar si es capicúa.
#¿Qué sucedería si no conoce la cantidad de cifras de “n”?

n=12321

# primer metodo
n_string=str(n)

capicua = n_string[0] == n_string[-1] and n_string[1] == n_string[-2]

if capicua:
    print(f'{n} es capicúa')  
else:
    print(f'{n} NO es capicúa')  
