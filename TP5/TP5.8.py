#Escriba una función que realice la operación CamelCase
#de una cadena de caracteres. Su función deberá retornar
#una nueva cadena de caracteres sin espacios y con las pala-
#bras de la cadena original formateada con la primera letra
#en mayúscula y todas las restantes en minúscula. Ejemplo:
#Entrada = "hola mundO" Salida = "HolaMundo"

t = ('hola mundO','Camel case')

def to_camel_case(s):
    
    ret_val=''
    words=s.split(' ')
    
    for wrd in words:
        wrd_camel=wrd[0].upper()+wrd[1:].lower()
        ret_val+=wrd_camel
    return ret_val

for txt in t:
    print(to_camel_case(txt))