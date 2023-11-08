
# defaults
l1=2
l2=6
l3=7

# input
l1 = int(input(f'M ({l1}):') or l1)
l2 = int(input(f'M ({l2}):') or l2)
l3 = int(input(f'M ({l3}):') or l3)

# compute
es_triangulo= (l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2
es_isoceles= es_triangulo and (l1 == l2 or l2 == l3 or l1 == l3)
es_equilatero= es_triangulo and (l1 == l2 and l2 == l3 and l1 == l3)
es_escaleno= es_triangulo and (l1 != l2 and l2 != l3 and l1 != l3)

# output
print(f'Es triangulo: {es_triangulo}')    
print(f'Es isoceles: {es_isoceles}')    
print(f'Es equilatero: {es_equilatero}')    
print(f'Es escaleno: {es_escaleno}')    