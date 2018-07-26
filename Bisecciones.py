import numpy as np
import matplotlib.pyplot as plt

def function(c):
    m=68.1; g=9.8 ; v=40 ; t=10
    #return (c-3)*(c+6)
    return (g*m/c)*(1-np.exp(-(c/m)*t))-v

def limits(a,b,n):
    limits=[]
    sum=a;
    while(sum<=b):
        limits.append(sum)
        sum=sum+(b-a)/n
    return np.array(limits)


def main():
    
    c=np.arange(0,20,0.1)
    f=function(c)
    plt.figure()
    plt.plot(c,f)
    
    a= 1           #Limite inferior del intervalo de búsqueda Inicial.
    b= 20           #Limite superior del interval de búsqueda inicial.
    n= 5            #Número de divisiones.
    tol = 1e-8      #Toleracia de la Respuesta
    solucion=0      #Inicialización de la Solucion.
    valor=0         #Valor final de la función en la Solución.
    
    candidatos=np.zeros(n+1)
    
    if function(a)*function(b)<=0:
    
        while (True):
            
            candidatos=limits(a,b,n)
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
                    i+=1
                
                a=candidatos[i-1]
                b=candidatos[i]
    else:
        print("El intervalo no funciona")

    plt.plot([solucion], [valor], marker='X', markersize=4, color="red")
    plt.grid()
    plt.title("Root Finding")
    plt.savefig("f2.png")
    plt.show()


if __name__=='__main__':
    main()
