#Algunos números naturales de n dígitos de la forma N =
#dj, . . . , d1, d0 con di ̸= 0∀i ∈ [0, j], cumplen con una pro-
#piedad de divisibilidad como se describe a continuación.
#Sea N=362 verifica la propiedad dado que 362 es divisible
#por 2, 36 es divisible por 6 y 3 es divisible por 3 mientras
#que N=168 no la verifica. Implemente una función para
#determinar si un número entero positivo cumple con esta
#propiedad.

numbers=(362,168
         )
def test_property(n):
    passed=True
    str_n=str(n)
    n_digits=len(str_n)
    
    for i in range(n_digits):
        # build numbers
        a=int(str_n[:n_digits-i])
        b=int(str_n[:n_digits-i][-1])
        
        # test
        passed= a%b==0
        if not passed:
            break
         
    return passed    
        
for n in numbers:
    print(f'{n} { "passed" if test_property(n) else "didnt pass"}')