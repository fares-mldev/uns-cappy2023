#Determine el valor aproximado de ex con un error menor
#a un valor ingresado por el usuario (rever ejercicio 3 del
#Trabajo Práctico 2). Imprima en pantalla la cantidad de
#términos necesarios para alcanzar la precisión deseada.

x=1
min_decimales=3

e_x=0
i_factorial=1

n_decimales=-1
decimales=''
es_periodico=False

i= 0
while n_decimales < min_decimales or es_periodico:
    
    if i==0:
        i_factorial=1
    else:
        i_factorial=i_factorial*i

    e_x += x**i / i_factorial

    decimales=str(e_x).split('.')[1]
    if len(decimales) > 1: es_periodico=decimales[-2]==decimales[-3]
    n_decimales= len(decimales)
    print(e_x,decimales,es_periodico)
    
    i+=1
    
print(f'e**{x}={e_x}')