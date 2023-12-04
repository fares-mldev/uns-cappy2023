#Se desea representar un mapa con algunas de las principales
#ciudades del país y la comunicación entre las mismas. A
#partir de una lista de ciudades y un diccionario con una
#ciudad como clave y un conjunto de cuidades aledañas a
#ella como valor, implemente una función para determinar
#todas las ciudades que se pueden alcanzar desde una ciudad
#dada

mapa_ciudades = {
    'CiudadA': {'CiudadB', 'CiudadC'},
    'CiudadB': {'CiudadA', 'CiudadD'},
    'CiudadC': {'CiudadA'},
    'CiudadD': {'CiudadE','CiudadF'},
    'CiudadE': {'CiudadF','CiudadD'},
    'CiudadF': {'CiudadE'}
}

def ciudades_alcanzables(mapa, ciudad_inicial):
    # Inicializar un conjunto para almacenar las ciudades alcanzables
    alcanzables = set()

    # Función recursiva para explorar las ciudades alcanzables
    def explorar(ciudad_actual):
        # Agregar la ciudad actual al conjunto de alcanzables
        alcanzables.add(ciudad_actual)

        # Recorrer las ciudades aledañas a la ciudad actual
        for ciudad_adyacente in mapa.get(ciudad_actual, []):
            # Si la ciudad adyacente no ha sido visitada, explorarla
            if ciudad_adyacente not in alcanzables:
                explorar(ciudad_adyacente)

    # Llamar a la función explorar con la ciudad inicial
    explorar(ciudad_inicial)

    return alcanzables

for ciudad in mapa_ciudades:
    print(ciudades_alcanzables(mapa_ciudades,ciudad))