# Implemente funciones para realizar las siguientes consultas de interés.
# a) Determine la lista de países con un único país limítrofe independientemente del continente al que pertenezca.
# b) ¿Cuál es el país con menor densidad poblacional de cada continente?
# c) ¿Cúal es el continente con más países con mayor porcentaje de agua que de tierra?

# Continente es la clave del diccionario y su valor es una lista con los paises que lo integran.
# Pais es la clave del diccionario y su valor es una lista que
# contiene: la superficie en km2, la cantidad de habi-
# tantes en millones, la superficie cubierta por agua en
# porcentaje y la lista de sus países limítrofes

continentes = {
    'Africa': ['Egipto', 'Nigeria'],
    'America': ['Argentina', 'Canadá', 'Brasil', 'Chile', 'Perú'],
    'Asia': ['China', 'India', 'Malasia'],
    'Europa': ['Alemania', 'Italia', 'Polonia'],
    'Oceania': ['Australia', 'Nueva Zelanda', 'Islas Salomón']
}

paises = {
    'Argentina': [3761274, 40.11, 48, ['Bolivia', 'Brasil', 'Chile', 'Paraguay', 'Uruguay']],
    'Egipto': [1002450, 104.26, 0.6, ['Sudán', 'Israel', 'Libia']],
    'India': [3287263, 1380.00, 9.6, ['Pakistán', 'China', 'Bangladesh']],
    'Italia': [301340, 60.36, 2.4, ['Francia', 'Suiza', 'Austria', 'Eslovenia']],
    'Australia': [7692024, 25.36, 0.8, ['Indonesia', 'Timor Oriental', 'Papúa Nueva Guinea']],
    'Nigeria': [923768, 206.14, 1.3, ['Benín', 'Camerún', 'Chad']],
    'Canadá': [9976140, 38.01, 8.9, ['Estados Unidos']],
    'China': [9596961, 1443.78, 2.8, ['India', 'Rusia', 'Mongolia']],
    'Alemania': [357022, 83.02, 2.4, ['Francia', 'Polonia', 'Austria']],
    'Nueva Zelanda': [270467, 4.91, 2.2, ['Australia']],
    'Marruecos': [446550, 36.91, 0.03, ['Argelia', 'Mauritania']],
    'Perú': [1285216, 32.17, 0.1, ['Ecuador', 'Colombia', 'Brasil', 'Chile', 'Bolivia']],
    'Malasia': [330803, 32.40, 0.30, ['Tailandia', 'Indonesia', 'Brunéi']],
    'Noruega': [1487290, 5.41, 6.0, ['Suecia', 'Finlandia', 'Rusia']],
    'Singapur': [725.7, 5.85, 1.7, ['Malasia']],
    'Chile': [756950, 19.52, 1.0, ['Perú', 'Argentina', 'Bolivia']],
    'Grecia': [131957, 10.42, 0.8, ['Albania', 'Macedonia del Norte', 'Bulgaria', 'Turquía']],
    'Polonia': [312696, 38.26, 3.1, ['Alemania', 'República Checa', 'Eslovaquia', 'Ucrania', 'Bielorrusia']],
    'Islas Salomón': [28896, 0.7, 1.3, ['Papúa Nueva Guinea', 'Vanuatu']],
    'Brasil': [8515767, 214.13, 0.65, ['Argentina', 'Uruguay', 'Paraguay', 'Bolivia', 'Perú', 'Colombia', 'Venezuela', 'Guyana', 'Surinam', 'Guayana Francesa']]
}

# a) Determine la lista de países con un único país limítrofe independientemente del continente al que pertenezca.

paises_un_limitrofe=[]

for pais in paises:
    sup_total, hab, perc_agua, limitrofes = paises[pais]
    if len(limitrofes) == 1 : 
        paises_un_limitrofe.append(pais)

print(f'a) Los países con un solo país limítrofe son: {paises_un_limitrofe}')

# b) ¿Cuál es el país con menor densidad poblacional de cada continente?

pais_menor_densidad_por_continente = {}

for continente , paises_continente in continentes.items():

    menor_densidad=None
    pais_menor_densidad=None
    
    for pais in paises_continente:
        
        sup_total, hab, perc_agua, limitrofes = paises[pais]
        densidad = hab * 1e6 / sup_total 
        if menor_densidad is None or densidad < menor_densidad:
            menor_densidad = densidad
            pais_menor_densidad = pais
    
    pais_menor_densidad_por_continente[continente]=(pais_menor_densidad,menor_densidad)           
            
print('b) El país con menor densidad poblacional de cada continente es:')
for continente in pais_menor_densidad_por_continente:
    print(continente,':', pais_menor_densidad_por_continente[continente][0], pais_menor_densidad_por_continente[continente][1],'hab/km2' )
    
# c) ¿Cúal es el continente con más países con porcentaje de agua mayor a 1%?
# NOTA: Cambio un poco la consigna porque de los paises elegidos todos tienen sup < 50% 

max_cant_paises_porc_agua_gt1=None
continente_max_cant_paises_porc_agua_gt1=None

for continente , paises_continente in continentes.items():
    
    # sumar cantidad de paises con porc_agua > 1
    cant_paises_porc_agua_gt1=0
    for pais in paises_continente:
        sup_total, hab, porc_agua, limitrofes = paises[pais]
        cant_paises_porc_agua_gt1 += int(porc_agua > 1)

    if  max_cant_paises_porc_agua_gt1 is None or cant_paises_porc_agua_gt1 > max_cant_paises_porc_agua_gt1:
        max_cant_paises_porc_agua_gt1 = cant_paises_porc_agua_gt1
        continente_max_cant_paises_porc_agua_gt1 = continente
    
print(f'c) El continente con más países con porcentaje de agua mayor a 1% es: {continente_max_cant_paises_porc_agua_gt1} con {max_cant_paises_porc_agua_gt1} paises')