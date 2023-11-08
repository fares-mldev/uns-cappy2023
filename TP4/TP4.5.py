#Implemente un script para determinar si:
#a) Un número entero positivo es capicúa.
#b) Una cadena de caracteres cumple la condición de ser un palíndromo.

n= 12344321

str_n=str(n)
es_capicua=True
for d in range(len(str_n)//2):
    
    if str_n[d]!=str_n[-1-d]:
        es_capicua=False
        break
    
print('a) Es capicúa' if es_capicua else 'a) No es capicúa')

frase='Anita lava la tina'

es_palindromo= True
frase_limpia= frase.replace(" ", "").lower()
print(frase_limpia)
for d in range(len(frase_limpia)//2):
    
    if frase_limpia[d]!=frase_limpia[-1-d]:
        es_palindromo=False
        break
    
print('a) Es palíndromo' if es_palindromo else 'a) No es palíndromo')