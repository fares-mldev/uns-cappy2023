#Dada una tupla de enteros (-2,14,5,-7,25,18,30)
#a) Determine la cantidad de enteros positivos.
#b) El mínimo valor.

t= (-2,14,5,-7,25,18,30)

n_enteros_positivos=0
min_val=None

for i in t:
    if i>0: n_enteros_positivos+=1 
    
    if min_val is None:
        min_val=i
    elif i < min_val:
        min_val=i
        
print(f'a) La cantidad de enteros positivos es {n_enteros_positivos}')
print(f'b) El valor mínimo es {min_val}')