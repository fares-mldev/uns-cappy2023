#Implemente una función fecha_valida.


t=(29,2,400)

def fecha_valida(t):
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

    return es_fecha_valida

if fecha_valida(t):
    print(f'La fecha {t} es válida')
else:
    print(f'La fecha {t} NO es válida')
        