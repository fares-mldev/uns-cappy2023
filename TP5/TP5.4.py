#Implemente el ejercicio 3 del Trabajo Práctico 3 utilizando
#las funciones esTriangulo y tipoDeTriangulo. Esta
#última deberá invocarse solo si las longitudes de los seg-
#mentos ingresados por el usuario conforman un triángulo.

def es_triangulo(l1,l2,l3):
    return (l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2

def es_isoceles(l1,l2,l3):
    return l1 == l2 or l2 == l3 or l1 == l3

def es_equilatero(l1,l2,l3):
    return l1 == l2 and l2 == l3 and l1 == l3

def es_escaleno(l1,l2,l3):
    return l1 != l2 and l2 != l3 and l1 != l3

# defaults
l1=2
l2=3
l3=2

# input
l1 = int(input(f'M ({l1}):') or l1)
l2 = int(input(f'M ({l2}):') or l2)
l3 = int(input(f'M ({l3}):') or l3)

# compute

if es_triangulo(l1,l2,l3):
    print('Es triangulo')    

    if es_isoceles(l1,l2,l3):
        print('Es isóceles')    
        
        if es_equilatero(l1,l2,l3):
            print('Es equilátero')    
        else:
            pass
    elif es_escaleno(l1,l2,l3):
        print('Es escaleno')

