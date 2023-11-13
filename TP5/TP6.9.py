#Realice funciones apropiadas para realizar cada una de
#las siguientes consultas a partir de una tupla de fechas de
#nacimientos que contiene las fechas de nacimiento de
#un grupo de personas con el formato (dia, mes, año).
#Ayuda: Es posible identificar unívocamente a una fecha
#a partir de un número entero de la forma Año*10000+
#Mes*100+ Día.
#a) ¿Existe algún mes sin cumpleaños? De no existir retorne None.
#b) Todos los meses sin cumpleaños.
#c) El promedio de edad del grupo.
#d) El último y el primer cumpleaños del año

fechas=((9,12,1976),
        (9,1,1981),
        (20,3,2008),
        (22,3,2011),
        (13,11,2000))

#a) ¿Existe algún mes sin cumpleaños? De no existir retorne None.

def hay_mes_sin_cumple(fechas):
    ret_val=[]
    meses_con_cumple=[]
    for fecha in fechas:
        meses_con_cumple.append(fecha[1])
    for mes in range(1,13):
        if not (mes in meses_con_cumple):
           return True 
    return False

print(f'a) {"Hay" if hay_mes_sin_cumple(fechas) else "NO hay"} mes sin cumple')
    
#b) Todos los meses sin cumpleaños.
def meses_sin_cumple(fechas):
    ret_val=[]
    meses_con_cumple=[]
    for fecha in fechas:
        meses_con_cumple.append(fecha[1])
    for mes in range(1,13):
        if not (mes in meses_con_cumple):
           ret_val.append(mes) 
    return ret_val

print(f'b) Meses sin cumple: {meses_sin_cumple(fechas)}')

#c) El promedio de edad del grupo.

def hoy():
    import datetime
    current_time = datetime.datetime.now()
    return (current_time.day, current_time.month, current_time.year)    

def calcular_edad(fecha):
    
    fecha_hoy=hoy()
    delta_years= fecha_hoy[2]-fecha[2]
    delta_months= fecha_hoy[1]-fecha[1]
    delta_days= fecha_hoy[0]-fecha[0]

    if delta_years > 0:
        edad = delta_years
        if delta_months < 0:
            edad -= 1
        elif delta_months == 0:
            if delta_days < 0:
                edad -= 1
    else:
        edad = 0
    
    return edad

def calcular_edad_promedio(fechas):
    edades = [calcular_edad(fecha) for fecha in fechas ]
    suma=0
    for edad in edades:
        suma += edad
    return suma / len(edades)
    
print(f'c) La edad promedio es: {calcular_edad_promedio(fechas)}')

#d) El último y el primer cumpleaños del año

def cumple_despues(f1,f2):
    
    if f1[1] > f2[1]:
        return True
    elif f1[1] == f2[1] and f1[0] > f2[0]:
        return True
    else:
        return False

def primer_cumple(fechas):
    
    primer=fechas[0]
    
    for fecha in fechas:
        if cumple_despues(primer,fecha):
            primer=fecha
    
    return primer

def ultimo_cumple(fechas):
    
    ultimo=fechas[0]
    
    for fecha in fechas:
        if cumple_despues(fecha,ultimo):
            ultimo=fecha
    
    return ultimo

print(f'd) El primer cumpleaños del año es {primer_cumple(fechas)} y el último es {ultimo_cumple(fechas)}')
    
    