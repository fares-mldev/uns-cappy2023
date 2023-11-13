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
    edad_years= fecha_hoy[2]-fecha[2]
    edad_months= fecha_hoy[1]-fecha[1]
    edad_days= fecha_hoy[0]-fecha[0]

    if edad_years > 0:
        edad = edad_years
        if edad_months > 0:
            edad = edad
        elif edad_months < 0:
            edad -= 1
        elif edad_months == 0:
            if edad_days >= 0:
                edad = edad 
            else:
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
    
print(f'c La edad promedio es: {calcular_edad_promedio(fechas)}')

#d) El último y el primer cumpleaños del año

