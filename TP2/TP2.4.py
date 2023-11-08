#Implemente un algoritmo que solicite al usuario un entero
#positivo n mayor que dos y calcule en enésimo término de
#la sucesión de Fibonnacci

n=3

n = int(input('N ('+ str(n)+  '):') or n)

f_k_2=1
f_k_1=1

print(f'f(1) {f_k_2}')
print(f'f(2) {f_k_1}')

for k in range(3,n+1):
    
    # f(k)
    f_k= f_k_2 + f_k_1
    
    # actualizo f(k-1) y f(k-2) 
    f_k_2=f_k_1
    f_k_1=f_k

    # salida    
    print(f'f({k}) {f_k}')

