import numpy as np
import matplotlib.pyplot as plt


# Definición de la función que se quiere resolver.
def function (t):
    return np.cos(3*t)+np.exp(t)
                          
# Definicón de la derivada de la función que se quiere resolver.
def derivate(t):
    return -3*np.sin(3*t)+np.exp(t)

#Inicialización de las variables de interés:
xn=0
solution=0
eps=30

Iteraciones=[]

while (eps>0.0000001):
     solution=xn-function(xn)/derivate(xn)
     xn=solution
     Iteraciones.append(xn)
     eps=abs(function(xn))

print ("Solucion en Radianes: ", solution)
print ("Solucion en Grados: ", solution*180/np.pi)

#Gráficas de Resultados:

t1=np.arange(0,2*np.pi,0.01)
t2=np.arange(-np.pi/2,np.pi/2,0.01)

r1=2+np.cos(3*t1)
r2=2-np.exp(t2)

plt.figure()
plt.polar(t1, r1)
plt.polar(t2, r2)
plt.grid(True)

plt.title("A line plot on a polar axis", va='bottom')
plt.savefig("Polar plot.png")
plt.show()





