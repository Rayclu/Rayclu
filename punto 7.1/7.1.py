"""7-1)Escribir una funcion que reciba una tupla de elementos e indique si se encuentran ordenados de mayor a menor"""
#secuencia=(1,-1)
def EstaOrdenado(secuencia):
    
    for i in range(0, len(secuencia)-1):
        if secuencia[i]>secuencia[i + 1]:
            return False
     
    return True
            
def main():
    secuencia=(6,1,2,3)
    print(EstaOrdenado(secuencia))
main()

