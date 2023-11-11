#Implemente funciones para modelar las operaciones lógicas
#xor, nand y nor.

def xor(a,b):
    return bool((a and not b) or (not a and b))

def nand(a,b):
    return bool(not (a and b))

def nor(a,b):
    return bool(not (a or b))

## test

print('a','b', '|' , f'xor\tnor\tnand')
    
n_bits=2
for i in range(2**n_bits):
   
    binary_str = format(i, '0{}b'.format(n_bits))
    
    a=int(binary_str[0])
    b=int(binary_str[1])

   
    print(a,b, '|' , f'{xor(a,b)}\t{nor(a,b)}\t{nand(a,b)}')
    