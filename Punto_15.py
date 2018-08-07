import numpy as np
import matplotlib.pyplot as plt


# Definición de la función auxiliar.
def g(x):
    return (1+np.exp(x))/5


# Definición de la función que se quiere resolver.
def f(x):
    return 5*x-np.exp(x)+1

#Inicialización de las variables de interés:
p_0=0
tol=1e-5
salida=[]

i=0
while (i<5):
    p=g(p_0)
    print(np.exp(p)/5)
    if abs(p-p_0)<=tol:
        salida=p
    p_0=p
    i+=1

print(salida)
print(p)
print(f(p))

c=np.arange(0,2,0.001)
y=f(c)
plt.figure()
plt.plot(c,y)
plt.plot([p], [f(p)], marker='X', markersize=4, color="red")
plt.grid()
plt.title("Ecuación Integral")
plt.savefig("Punto_15.png")
plt.show()



