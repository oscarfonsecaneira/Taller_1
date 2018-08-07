# Primer Taller Análisis Numérico.

## Punto 1. 

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{W}(A,f)&space;=&space;(T,\bar{f})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathcal{W}(A,f)&space;=&space;(T,\bar{f})" title="\mathcal{W}(A,f) = (T,\bar{f})" /></a>

## Punto 2. 

Se necesita un recipiente rectangular, sin tapa, de un litro de capacidad. Para construirlo se debe usar una lámina rectangular de 32 cm de largo y 24 cm de ancho. El procedimiento será recortar un cuadrado idéntico en cada una de las cuatro esquinas y doblar los bordes de la lámina para formar el recipiente. 

El código determina la medida del lado del cuadrado que se debe recortar en cada esquina para que el recipiente tenga la capacidad requerida. 

Solución. 

Un esquema del problema es como el que se muestra en la figura a continuación: 


El volumen de la caja se puede obtener mediante la siguiente expresión. 

Luego, basta con resolver la siguiente ecuación: 

Para resolver el problema usamos una variación de los métodos de bisecciones y Newton Rapson que permita aproximarse a la solución por la izquierda.

## Punto 3 o 4 o 5.  

## Punto 6. 
 
## Punto 7.  
Una partícula se mueve en el espacio con el siguiente vector posición: 

Se quiere conocer utilizando métodos numéricos, el tiempo en el que el objeto se encuentre más cercano del punto . Se utilizará el método de Newton Rapson, usando 4 decimales de precisión. 

Solución: 


Gráficamente, podemos verificar la convergencia del método. 



## Punto 10.

Se utilizará el método de Newton para encontrar una intersección de las siguientes ecuaciones en coordenadas polares. 

<a href="https://www.codecogs.com/eqnedit.php?latex=r=2&plus;\cos&space;(3t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r=2&plus;\cos&space;(3t)"/></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=r=2-e^{t}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r=2-e^{t}" title="r=2-e^{t}" /></a>
                                                                                              
Se igualan las dos ecuaciones y se obtiene la siguiente expresión. 


Para utilizar el método de Newton, derivamos la expresión: 

Se selecciona una solución en el siguiente intervalo: 

```
a = Lower Limit 
b := Upper Limit.  
tol := Desired Tolerance of the Answer. 
```

## Punto 14. 

## Punto 15. 

Se propone resolver la integral con el método del punto fijo: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\int_{0}^{x}&space;\left&space;(&space;5&space;-&space;e^{u}&space;\right&space;)&space;du" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int_{0}^{x}&space;\left&space;(&space;5&space;-&space;e^{u}&space;\right&space;)&space;du" title="\int_{0}^{x} \left ( 5 - e^{u} \right ) du" /></a>




