class triangulo:
    def __init__(self, a, b, c) -> None:
        lados = [a,b,c]
        lados.sort()
        if lados[0]+lados[1] < lados[2]:
            raise ValueError('Triángulo mal conformado!')
        self.a = a
        self.b = b
        self.c = c
try:
    t = triangulo(1,2,5)    
except Exception as ex:
    print(f'{type(ex).__name__}: {ex}')