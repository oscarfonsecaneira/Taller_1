import numpy as np
import matplotlib.pyplot as plt

def function(c):
    m=68.1; g=9.8 ; v=40 ; t=10
    return (c-3)*(c+6)
    #return (g*m/c)*(1-np.exp(-(c/m)*t))-v

def limits(a,b,n):
    limits=np.zeros(n+1)
    limits[n]=b
    sum=a
    for i in range(n):
        limits[i]=sum
        sum=sum+(b-a)/n
    return limits


def main():
    
    c=np.arange(-10,10,0.1)
    f=function(c)
    plt.figure()
    plt.plot(c,f)
    
    a= -10          #Limite inferior del intervalo de búsqueda Inicial.
    b= -4.5         #Limite superior del interval de búsqueda inicial.
    n= 3            #Número de divisiones.
    tol = 1e-8      #Toleracia de la Respuesta
    solucion=0      #Inicialización de la Solucion.
    valor=0         #Valor final de la función en la Solución.
    
    candidatos=np.zeros(n+1)
    
    if function(a)*function(b)<=0:
        
        while (True):
            print("------Nueva Iteración------")
            
            candidatos=limits(a,b,n)
            print(candidatos)
            resultados=function(candidatos)

            if (abs(resultados)<=tol).any():
                solucion=candidatos[abs(resultados)<=1e-8][0]
                valor=resultados[abs(resultados)<=1e-8][0]
                print(solucion,valor)
                break
            else:
                i=0
                sign=1
                while(sign==1):
                    sign=np.sign(resultados[i]*resultados[i+1])
                    #print(sign)
                    i+=1
                
                a=candidatos[i-1]
                b=candidatos[i]
    else:
        print("El intervalo no funciona")

    plt.plot([solucion], [valor], marker='X', markersize=4, color="red")
    plt.grid()
    plt.title("Root Finding")
    plt.savefig("figure.png")
    plt.show()


if __name__=='__main__':
    main()

