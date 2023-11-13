#Analice los siguientes bloques de código, verifique la salida
#en pantalla y determine a qué variable a hace referencia en
#cada caso:

# a) 

print('a)')
def subrutina():
    a = 2
    print(a)    # se refiere a la variable interna

a = 5
subrutina()
print(a)

# b)
del(a) # Para independizar del ejemplo a)
print('b)')

def subrutina():
    print(a)    # se refiere a la variable global

subrutina() # no existe la variable
a = 5
print(a)