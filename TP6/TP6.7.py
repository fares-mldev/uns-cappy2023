#Dado un diccionario del tipo (dato: máximo divisor entero
#distinto de si mismo) construya un nuevo diccionario que
#no contenga a los números primos

def max_div(n):
    for i in range(n-1,1,-1):
        if n % i == 0:
            return i
    return None # primo

test_a = range(2,20)

dict_max_div={i:max_div(i) for i in test_a if max_div(i) is not None}

print(f'Construya un nuevo diccionario que no contenga a los números primos. {dict_max_div}')
