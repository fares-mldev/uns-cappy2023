
def nueva_linea(linea):

    if len(linea)==0:
        return [1]
        
    linea.insert(0,0)
    linea.append(0)
    
    nl = []
    
    for i in range(len(linea)-1):
        nl.append(linea[i]+linea[i+1])
    
    return nl

def pascal(n):
    linea=[]
    for nivel in range(10):
        linea=nueva_linea(linea)
        print(linea)
    

pascal(5)