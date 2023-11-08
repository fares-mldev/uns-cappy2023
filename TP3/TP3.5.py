#Implemente un script que a partir de una tupla de la forma
#(día,mes,año) determine si corresponde a una fecha váli-
#da. Recuerde que los meses de abril, junio, septiembre y
#noviembre tienen 30 días; el mes de febrero puede tener
#29 o 28 días dependiendo de si se trata de un año bisiesto
#o no; y los meses restantes poseen 31 días. Nota: Un año
#es bisiesto si verifica las siguientes condiciones: es divisible
#por 4 pero no por 100 o, es múltiplo de 400

t=(29,2,400)

d,m,a=t

es_bisiesto= ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0)
es_mes_valido= m in range(1,13)

max_d=0
if m in (1,3,5,7,8,10,12):
    max_d=31 
elif m in (4,6,9,11):
    max_d=31 
elif m==2:
    max_d=28 if es_bisiesto else 29

es_dia_valido= d in range(1,max_d+1)


es_fecha_valida = es_mes_valido and es_dia_valido

if es_fecha_valida:
    print('La fecha es válida')
else:
    print('La fecha NO es válida')
    