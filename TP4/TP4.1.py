#Imprima en pantalla la siguiente serie de enteros:

#a) 1, 4, 9, 16....10000

i=1
res=''
while i <= 100:
    res+=str(i**2)+' '
    i+=1

print(res)

#b) 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25
i=-5
res=''
while i <= 5:
    res+=str(i**2)+' '
    i+=1

print(res)

#c) 100, 95, 90, ...., 0

i=100
res=''
while i >= 0:
    res+=str(i)+' '
    i-=5

print(res)