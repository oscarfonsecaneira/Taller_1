# Primer Taller Análisis Numérico.

## Punto 1. 


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

<img alt="tex: f(x) = \frac1{\sigma\sqrt{2\pi}} 
    \int_{-\infty}^x e^{-\frac{(t-\mu)^2}{2\sigma^2}}dt">

## Punto 14. 

## Punto 15. 

Se propone resolver la integral con el método del punto fijo: 

<img src="https://latex.codecogs.com/svg.latex?\Large&space; e^{u} "/>


```
a := Lower Limit 
b := Upper Limit. 
n := Number of Divisions. 
tol := Desired Tolerance of the Answer. 
```



```
a = -8; b =5 ; n=5  tol=1e-8
```
Results: 
```
 x   = -6.000000000983039
f(x) =  8.847354849706364e-09 
```

<img src="https://latex.codecogs.com/svg.latex?\Large&space; f(c)=\frac{gm}{c}(1-e^{-(\frac{c}{m})t)})-v(t)"/>

```
m=68.1; g=9.8 ; v=40 ; t=10
a = 1; b =20 ; n=3  tol=1e-8
```
Results: 
```
x    = 14.78020382951945
f(x) = 4.175156220753706e-09
```



