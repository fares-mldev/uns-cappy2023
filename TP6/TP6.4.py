# Dada una lista de números enteros con repeticiones ordenado en forma descendente, 
# se desea generar otra lista con pares (número, frecuencia) con la información de la 
# frecuencia de aparición de cada uno. 
# Por ejemplo, si l tiene los números [9,7,7,6,5,3,3,3,1,1,1] la lista frecuencia 
# debe contener los pares [(9,1),(7,2) ,(6,1) ,(5,1) ,(3,3) ,(1,3)].

def contar_ocurrencias(l):
    f={}
    for i in l:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    return [(k,f[k]) for k in f]

test=[9,7,7,6,5,3,3,3,1,1,1]

print(contar_ocurrencias(test))