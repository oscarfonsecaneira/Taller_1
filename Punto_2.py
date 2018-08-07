import numpy as np
import matplotlib.pyplot as plt

def function(c):
    return (0.32-2*c)*(0.24-2*c)*c-(0.001-1e-8)

def derivate(c):
    return 12*c**2-2.24*c+0.0768

def limits(a,b,n):
    limits=np.zeros(n+1)
    limits[n]=b
    sum=a
    for i in range(n):
        limits[i]=sum
        sum=sum+(b-a)/n
    return limits


def main():
    
    # ------------Método De las Bisecciones----------------------------
    c=np.arange(0,0.2,0.001)
    f=function(c)
    plt.figure()
    plt.plot(c,f)
    
    a= 0.1          #Limite inferior del intervalo de búsqueda Inicial.
    b= 0.2         #Limite superior del interval de búsqueda inicial.
    n= 10           #Número de divisiones.
    tol = 1e-8      #Toleracia de la Respuesta
    solucion=0      #Inicialización de la Solucion.
    valor=0         #Valor final de la función en la Solución.
    
    errores=[]
    n_iter=0
    
    candidatos=np.zeros(n+1)
    
    if function(a)*function(b)<=0:
        
        while (True):
            n_iter+=1
            
            candidatos=limits(a,b,n)
            resultados=function(candidatos)

            if (abs(resultados)<=tol).any():
                solucion=candidatos[abs(resultados)<=1e-8][0]
                valor=resultados[abs(resultados)<=1e-8][0]
                break
            else:
                i=0
                sign=1
                while(sign==1):
                    sign=np.sign(resultados[i]*resultados[i+1])
                    i+=1
                
                a=candidatos[i-1]
                errores.append(resultados[i-1]+resultados[i]/2)
                b=candidatos[i]
    else:
        print("El intervalo no funciona")


    plt.plot([solucion], [valor], marker='X', markersize=4, color="red")
    plt.plot([0.016962500000000012], [0], marker='X', markersize=4, color="red")
    plt.plot([0.0809325], [0], marker='X', markersize=4, color="red")
    plt.grid()
    plt.title("Root Finding")
    plt.savefig("f2.png")
    plt.show()

    print(solucion)
    print(solucion*(0.32-2*solucion)*(0.24-2*solucion))

    # ------------Método de Newton-Raphson----------------------------

    #Inicialización de las variables de interés:
    xn=0.075
    solution=0
    eps=30

    Iteraciones=[]

    while (eps>0.0000001):
        solution=xn-function(xn)/derivate(xn)
        xn=solution
        Iteraciones.append(xn)
        eps=abs(function(xn))

    print (solution)
    print(solution*(0.32-2*solution)*(0.24-2*solution))





if __name__=='__main__':
    main()
