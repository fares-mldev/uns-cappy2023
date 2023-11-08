
x=-1

n=10

e_x=0
factorial=1

for i in range(n+1):
    
    if i==0:
        i_factorial=1
    else:
        i_factorial=i_factorial*i

    e_x += x**i / i_factorial


print(f'e**{x}={e_x}')
