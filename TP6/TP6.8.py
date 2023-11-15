#Construya un diccionario a partir de la información
#contenida en la tupla del ejercicio del ejercicio 9 del
#Trabajo Práctico 5. Su diccionario será de la forma
#nacimientos={‘enero’: [(dia, año),..], ‘febrero’:. . . .}.
#Vuelva a implementar las funciones teniendo en cuenta
#la nueva estructura

meses={1:'enero',
       2:'febrero',
       3:'marzo',
       4:'abril',
       5:'mayo',
       6:'junio',
       7:'julio',
       8:'agosto',
       9:'septiembre',
       10:'octubre',
       11:'noviembre',
       12:'diciembre'}

fechas=[( 10, 1,1981),
        (20, 2,2008),
        ( 9,12,1976),
        ( 9, 1,1981),
        (22, 3,2011),
        ( 10, 5,1981),
        (20, 3,2008),
        (19, 2,2008)]

dict_fechas={}
for d,m,a in fechas:
    if meses[m] in dict_fechas:
        dict_fechas[meses[m]].append((d,a))
    else:
        dict_fechas[meses[m]]=[(d,a)]

print(f'Se genera un diccionario que organiza los cumpleaños por mes: {dict_fechas}')