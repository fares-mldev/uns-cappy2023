#Dado un número natural n, escriba funciones recursivas para:
#a) Imprimir en pantalla su cuenta regresiva.
#b) Sumar todos sus dígitos.
#c) Obtener su dígito más significativo.
#d) Determinar si todos sus dígitos están ordenados de menor a mayor.
#e) La cantidad de dígitos pares e impares que contiene.
#f) La cantidad de veces que se repite su dígito más significativo.

#a) Imprimir en pantalla su cuenta regresiva.

def cuenta_regresiva(n):
    print(n)
    if n > 0:
        cuenta_regresiva(n-1)

print('a) Dado un número natural n, imprimir en pantalla su cuenta regresiva.')
cuenta_regresiva(10)

#b) Sumar todos sus dígitos.

def sumar_digitos(numero):
    
    # Caso base: si el número es un solo dígito, simplemente retornar ese dígito
    if numero < 10:
        return numero

    # Caso recursivo: sumar el último dígito y llamar a la función con el resto del número
    ultimo_digito = numero % 10
    resto_numero = numero // 10
    return ultimo_digito + sumar_digitos(resto_numero)

n=12341
print('b) Dado un número natural n, Sumar todos sus dígitos. n={n}')
print(sumar_digitos(n))

#c) Obtener su dígito más significativo.

def digito_mas_significativo(numero):
    
    # Caso base: si el número es un solo dígito, simplemente retornar ese dígito
    if numero < 10:
        return numero

    # Caso recursivo: llamar a la función con el resto del número
    resto_numero = numero // 10
    return digito_mas_significativo(resto_numero)

print('b) Dado un número natural n, obtener su dígito más significativo')
for n in [12341, 789, 345, 54, 6]:
    print(f'n={n}, dms={digito_mas_significativo(n)}')

#d) Determinar si todos sus dígitos están ordenados de menor a mayor.

def digitos_ordenados(numero):
    # Convertir el número a una cadena para trabajar con los dígitos
    str_numero = str(numero)

    # Caso base: si la longitud de la cadena es 1, los dígitos están ordenados
    if len(str_numero) <= 1:
        return True

    # Verificar si el primer dígito es menor o igual al siguiente
    if int(str_numero[0]) <= int(str_numero[1]):
        # Llamada recursiva con el resto de la cadena
        return digitos_ordenados(int(str_numero[1:]))
    else:
        return False

print('b) Dado un número natural n, Determinar si todos sus dígitos están ordenados de menor a mayor')
for n in [12341, 789, 345, 54, 6]:
    print(f'n={n}, ordenados={digitos_ordenados(n)}')

#e) La cantidad de dígitos pares e impares que contiene.

def contar_par_impar(numero):
    
    # Caso base: si el número es un solo dígito, simplemente retornar ese dígito
    if numero < 10:
        
        return int(numero % 2 == 0) , int(numero % 2 != 0)
    
    # Caso recursivo: sumar el último dígito y llamar a la función con el resto del número
    resto_numero = numero // 10
    conteo_resto = contar_par_impar(resto_numero)

    ultimo_digito = numero % 10
    conteo_ultimo_digito = int(ultimo_digito % 2 == 0) , int(ultimo_digito % 2 != 0)
        
    return conteo_resto[0]+ conteo_ultimo_digito[0], conteo_resto[1]+ conteo_ultimo_digito[1]

print('b) Dado un número natural n, la cantidad de dígitos pares e impares que contiene.')
for n in [12341, 789, 345, 54, 6]:
    print(f'n={n}, (par,impar)={contar_par_impar(n)}')

#f) La cantidad de veces que se repite su dígito más significativo.

def contar_dms(numero, dms = None):
    
    # Convertir el número a una cadena para trabajar con los dígitos
    str_numero = str(numero)
    
    if dms is None:
        dms=str_numero[0]
    
    if len(str_numero) == 1:
        return 1 if str_numero[0] == dms else 0

    return int(str_numero[0] == dms) + contar_dms(str_numero[1:],dms)

print('b) Dado un número natural n, la cantidad de veces que se repite su dígito más significativo')
for n in [12341, 789, 34335, 54, 55, 6]:
    print(f'n={n}, repeticiones={contar_dms(n)}')
    