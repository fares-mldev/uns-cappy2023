
t=(True,False,True)

a,b,c=t    
print(f'a:{a} b:{b} c:{c} -- r1:{bool(a or b and c)} r2:{bool(a and not c)}')
    