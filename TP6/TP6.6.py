# Implemente los siguientes diccionarios que a cada clave entera le asocie los siguiente valores:
# a) El máximo divisor entero distinto de si mismo.

def max_div(n):
    for i in range(n-1,1,-1):
        if n % i == 0:
            return i
    return None

test_a = range(2,20)

dict_max_div={i:max_div(i) for i in test_a}

print(f'a) El máximo divisor entero distinto de si mismo. {dict_max_div}')

# b) La lista completa de divisores del número.

def all_divs(n):
    divs=[]
    for i in range(n-1,1,-1):
        if n % i == 0:
            divs.append(i)
    return divs

dict_all_divs={i:all_divs(i) for i in test_a}

print(f'a) La lista completa de divisores del número. {dict_all_divs}')