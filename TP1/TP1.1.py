# Sabiendo que una empresa posee 100 autos con capacidad
# para 4 personas cada uno, y que en el día de la fecha se
# encuentran disponibles 30 choferes, determine la siguiente
# información para una lista de espera de 50 pasajeros: 
# La #cantidad de autos disponibles para el traslado de pasajeros. ok
# ¿Cuántos pasajeros más se podrían sumar durante el día? 
# ¿Cuál es la capacidad de pasajeros ociosa por falta de choferes?

n_coches=100
n_choferes=30
capacidad_coche=4
pasajeros_lista_espera=50

coches_disponibles=min(n_coches,n_choferes)
capacidad_total=coches_disponibles * capacidad_coche
pasajeros_adicionales= capacidad_total - pasajeros_lista_espera
capacidad_ociosa=(n_coches-coches_disponibles)*capacidad_coche

print(f'PROBLEMA: Hay {n_coches} coches, cada uno con una capacidad de {capacidad_coche} pasajeros. Hay {n_choferes} choferes y {pasajeros_lista_espera} pasajeros en lista de espera.')


print(f'Hay {coches_disponibles} coches disponibles')
print(f'Con una capacidad total de {capacidad_total} pasajeros')
print(f'Considerando que hay {pasajeros_lista_espera} pasajeros en lista de espera, se podrían sumar {pasajeros_adicionales} pasajeros adicionales')
print(f'Se tiene una capacidad ociosa de {capacidad_ociosa} pasajeros por falta de choferes')

