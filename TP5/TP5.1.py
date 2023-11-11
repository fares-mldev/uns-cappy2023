#Realice una función para convertir un valor en kilómetros
#por hora [km/h] a metros por segundo [m/s] y otra con la
#operación inversa que convierta de [m/s] a [km/h]

def convert_kmh_ms(kmh):
    return 1000 * kmh / 3600

def convert_ms_kmh(ms):
    return 3600 * ms / 1000

kmh = 100
kmh = float(input('Ingrese velocidad en kmh ('+ str(kmh)+  '):') or kmh)

ms = convert_kmh_ms(kmh)
kmh = convert_ms_kmh(ms)

print(f'Valor convertido a m/s: {ms}')
print(f'Valor reconvertido a km/h: {kmh}')
