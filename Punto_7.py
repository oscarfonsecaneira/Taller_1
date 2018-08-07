import numpy as np
import matplotlib.pyplot as plt

#Definición de la función del cuadrado de la distancia.
def distance(t):
    return (2*np.cos(t)-2)**2+(np.sin(t)-1)**2

# Definición de la función que se quiere resolver.
def function (t):
    return -3*np.sin(2*t)-2*np.cos(t)+8*np.sin(t)
                          
# Definicón de la derivada de la función que se quiere resolver.
def derivate(t):
    return -6*np.cos(2*t)+2*np.sin(t)+8*np.cos(t)

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

print (solution)
print (distance(solution)**(1/2))

#Gráficas de Resultados:

t=np.arange(0,5,0.1)
f=function(t)
plt.figure()
plt.plot(t,f)
valor=function(solution)

plt.plot([solution], [valor], marker='X', markersize=4, color="red")
plt.grid()
plt.title("Derivada del cuadrado de la Distancia")
plt.savefig("Derivada.png")

D=distance(t)
plt.figure()
plt.plot(t,D)
valor=distance(solution)
plt.plot([solution], [valor], marker='X', markersize=4, color="red")
plt.grid()
plt.title("Función del cuadrado de la distancia")
plt.savefig("Distancia.png")


iter=np.array(Iteraciones)
plt.figure()
plt.plot(iter)
plt.grid()
plt.title("Convergencia del Método")
plt.savefig("Convergencia.png")




