#Se desea implementar un simulador de plazo fijo. Realice un
#programa que pregunte al usuario una cantidad a invertir,
#el interés mensual, el período en meses a depositar y calcule
#el capital obtenido al finalizar la inversión.

monto_inicial=1
interes_mensual=1
periodo_meses=12

monto_inicial = float(input(f'Monto inicial ({monto_inicial}):') or monto_inicial)
interes_mensual = float(input(f'Interes mensual ({interes_mensual}):') or interes_mensual)
periodo_meses = float(input(f'Período plazo fijo ({periodo_meses}):') or periodo_meses)

coeficiente_interes_mensual= 1 + interes_mensual / 100
capital_final= monto_inicial + coeficiente_interes_mensual * periodo_meses

print(f'El capital final es {capital_final:.2f}')