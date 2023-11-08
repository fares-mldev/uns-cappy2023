
n_bits=3

for i in range(2**n_bits):
    
    binary_str = format(i, '0{}b'.format(n_bits))
    
    a=int(binary_str[0])
    b=int(binary_str[1])
    c=int(binary_str[2])
    
    print(a,b,c, ' - ' , bool(a or b and c), ' - ' , bool(a and not c))
    