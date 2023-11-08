#Una juguetería tiene mucho éxito con la venta de baldes
#de ladrillitos en sus presentaciones de 350 y 500 gr. El
#correo los obliga a armar bultos de no más de 10 unidades
#cuyo costo final se calcula en función de su peso. Escriba un
#programa que lea el número de baldes de cada presentación
#de un pedido y determine en forma automática el costo
#total del envío sabiendo que cada bulto tiene un costo fijo
#de 350$ más un proporcional de 125$ por kilo

import math

n_baldes_350=7
n_baldes_500=4
costo_por_bulto=350
costo_por_kilo=125

n_bultos= math.ceil((n_baldes_350 + n_baldes_500) / 10)
costo_bultos=n_bultos * costo_por_bulto

peso_bultos_kilos= n_baldes_350 * 0.350 + n_baldes_500 * 0.500
costo_peso= peso_bultos_kilos * costo_por_kilo

print(f'Bultos: {n_bultos} - Costo: {costo_bultos}')
print(f'Peso (kg): {peso_bultos_kilos:0.2f} - Costo: {costo_peso:0.2f}')
print(f'Costo total: {costo_bultos+costo_peso}')

