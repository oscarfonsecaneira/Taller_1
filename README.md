# Primer Taller Análisis Numérico.

## Punto 1. 
Evaluar el polinomio en cada valor indicado y el número de operaciones mínimo para hacerlo, para los siguientes polinomios junto con sus derivadas.

<a href="https://www.codecogs.com/eqnedit.php?latex=P(x)=7x^{5}+6x^{4}-6x^{3}+3x-4" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(x)=7x^{5}+6x^{4}-6x^{3}+3x-4" title="P(x)=7x^{5}+6x^{4}-6x^{3}+3x-4" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=x0=3" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x0=3" title="x0=3" /></a>

A través de la implementación del método de horner en Python, se obtuvieron los siguientes resutados.

Con <a href="https://www.codecogs.com/eqnedit.php?latex=x0=3" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x0=3" title="x0=3" /></a>

Para el polinomio: <a href="https://www.codecogs.com/eqnedit.php?latex=P(x)=7x^{5}+6x^{4}-6x^{3}+3x-4" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(x)=7x^{5}+6x^{4}-6x^{3}+3x-4" title="P(x)=7x^{5}+6x^{4}-6x^{3}+3x-4" /></a>

Se obtuvo como resultado: 2030 y como mínimo número de operaciones: 10

Para la primera derivada: <a href="https://www.codecogs.com/eqnedit.php?latex=P'(x)=35x^4+24x^3-18x^2+3" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P'(x)=35x^4+24x^3-18x^2+3" title="P'(x)=35x^4+24x^3-18x^2+3" /></a>

Se obtuvo como resultado: 3324 y como mínimo número de operaciones: 8

Para la segunda derivada: <a href="https://www.codecogs.com/eqnedit.php?latex=P''(x)=140x^3+72x^2-36x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P''(x)=140x^3+72x^2-36x" title="P''(x)=140x^3+72x^2-36x" /></a>

Se obtuvo como resultado: 4320 y como mínimo número de operaciones: 6

Para la tercera derivada: <a href="https://www.codecogs.com/eqnedit.php?latex=P'''(x)=420x^2+144x-36" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P'''(x)=420x^2+144x-36" title="P'''(x)=420x^2+144x-36" /></a>

Se obtuvo como resultado: 4176 y como mínimo número de operaciones: 4

Para la cuarta derivada: <a href="https://www.codecogs.com/eqnedit.php?latex=P''''(x)=840x+144" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P''''(x)=840x+144" title="P''''(x)=840x+144" /></a>

Se obtuvo como resultado: 2664 y como mínimo número de operaciones: 2

## Punto 2. 

Se necesita un recipiente rectangular, sin tapa, de un litro de capacidad. Para construirlo se debe usar una lámina rectangular de 32 cm de largo y 24 cm de ancho. El procedimiento será recortar un cuadrado idéntico en cada una de las cuatro esquinas y doblar los bordes de la lámina para formar el recipiente. 

El código determina la medida del lado del cuadrado que se debe recortar en cada esquina para que el recipiente tenga la capacidad requerida. 

**Solución:** 

Un esquema del problema es como el que se muestra en la figura a continuación: 

<p align="center">
  <img src="Esquema_punto2.png">
</p>

El volumen de la caja se puede obtener mediante la siguiente expresión:

<a href="https://www.codecogs.com/eqnedit.php?latex=V(x)=x(0.24-x)(0.32-x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?V(x)=x(0.24-x)(0.32-x)" title="V(x)=x(0.24-x)(0.32-x)" /></a>

Luego, basta con resolver la siguiente ecuación: 

<a href="https://www.codecogs.com/eqnedit.php?latex=V(x)=x(0.24-x)(0.32-x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x(0.24-x)(0.32-x)-0.001=0" title="x(0.24-x)(0.32-x)-0.001=0" /></a>

Para resolver el problema, se debe tener en cuenta que el volumen solamente puede aproximarse por la izquierda al valor equivalente a un litro, para eso se le restará un valor de épsilon que permita aproximarse a la solución por la izquierda, resolvimos el problema mediante el método de Bisecciones y Newton Raphson. 

**Resultados método Bisecciones:** 

```
Intervalo: [0,0.05]

 x  = 0.016962500000000012
Vol = 0.0009999886616640628

Intervalo: [0.05,0.1]

 x  = 0.0809325
Vol = 0.0009999921144448125

Intervalo: [0.1,0.15]

 x  = 0.18210500000000004
Vol = 0.0009999975752305029

```

**Resultados método Newton-Raphson:** 
```
 x  = 0.0.01696064362425921
Vol = 0.0009999102141617382

 x  = 0.08093306077072439
Vol = 0.0009999775971849495

 x  = 0.18210497416831156
Vol = 0.0009999958488588572

```

Graficamente: 

<p align="center">
  <img src="Punto2.png" width="320" heigth="240">
</p>

**Preguntas Adicionales:**

1. ¿Cuál etapa del proceso de resolución de un problema numérico requiere más atención? 

Para solucionar un problema matemático es necesario que todas las etapas del proceso se lleven acabo de manera correcta, sin embargo la formulación matemática inicial es lo más importante. Si la ecuación planteada no es correcta, ningún método numérico por bueno que sea, puede corregir los problemas en el modelo analítico del problema. 

2. ¿Qué conocimientos son necesarios para formular un modelo matemático? 

Depende mucho del problema en cuestión, sin embargo, de manera muy general se necesitan conocimientos de cálculo multivariado, álgebra lineal y ecuaciones diferenciales.  

3. En el ejemplo anterior. ¿Cuál sería la desventaja de intentar obtener experimentalmente la solución mediante prueba y error en lugar de analizar el modelo matemático? 

En caso de que solo se cuente con una lámina, si se falla no hay forma de corregir. En este caso sería un método de acierto o error. 

4. ¿Qué es más crítico: el error de truncamiento o el error de redondeo?

Cuando se redondea, se tienen en cuenta algunas de las cifras que se dejan de lado, sin embargo, cuando se trunca el valor no se consieran las cifras dejadas de lado. Desde esa perspectiva, es más crítico el error de truncamiento. 

5. ¿Cuál es la ventaja de instrumentar computacionalmente un método numérico?
Por que los computadores permiten realizar los procesos iterativos con mucha facilidad, además, como los algoritmos son generales, basta con programarlos una sola vez para aplicarlos en diferentes contextos. 

6. ¿Por qué es importante validar los resultados obtenidos? 

Por que, aun cuando la formulación matemática del problema haya sido correcta, es posible que los métodos numéricos converjan a una solución que no sea correcta.  

## Punto 3 o 4 o 5.  

## Punto 6. 
Eficiencia de un algoritmo esta denotada por T(n)
 
 Al momento de recorrer el algoritmo con n = 73, se realizaron 7 operaciones aritméticas de división.
 
 Ya con <a href="https://www.codecogs.com/eqnedit.php?latex=T(n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T(n)" title="T(n)" /></a> encontrado que es igual a 7, se expresa a O( ) como <a href="https://www.codecogs.com/eqnedit.php?latex=O(2^{-n})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(2^{-n})" title="O(2^{-n})" /></a>
 
## Punto 7.  
Una partícula se mueve en el espacio con el siguiente vector posición: 

<a href="https://www.codecogs.com/eqnedit.php?latex=R(t)=(2\cos&space;(t),2\sin(t),0)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R(t)=(2\cos&space;(t),2\sin(t),0)" title="R(t)=(2\cos (t),2\sin(t),0)" /></a>

Se quiere conocer utilizando métodos numéricos, el tiempo en el que el objeto se encuentre más cercano del punto <a href="https://www.codecogs.com/eqnedit.php?latex=P(2,1,0)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(2,1,0)" title="P(2,1,0)" /></a> . Se utilizará el método de Newton Rapson, usando 4 decimales de precisión. 

**Solución:** 

En primer lugar es necesario plantear la solución analítica del problema, lo que permitirá obtener la expresión que deberá ser resuelta usando métodos numéricos. Para esto, usando los conocimientos de cálculo de una variable, definimos la distancia de la partícula al punto P, como función del tiempo: 

<a href="https://www.codecogs.com/eqnedit.php?latex=d(t)=((2\cos(t)-2)^{2}&plus;(2\sin(t)-1)^{2})^{1/2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?d(t)=((2\cos(t)-2)^{2}&plus;(2\sin(t)-1)^{2})^{1/2}" title="d(t)=((2\cos(t)-2)^{2}+(2\sin(t)-1)^{2})^{1/2}" /></a>

Lo que buscamos es minimizar esta función, pero basta con minimizar su cuadrado. Para esto, derivamos su cuadrado e igualamos la derivada a cero, obtieniendo la ecuación que deberá ser resuelta utilizando el método de Newton.

<a href="https://www.codecogs.com/eqnedit.php?latex=D'(t)=-4(2\cos(t)-2)\sin(t)&plus;2(\sin(t)-1)\cost(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D'(t)=-4(2\cos(t)-2)\sin(t)&plus;2(\sin(t)-1)\cost(t)=0" title="D'(t)=-4(2\cos(t)-2)\sin(t)+2(\sin(t)-1)\cost(t)=0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=D'(t)=-6\sin(2t)&plus;2\sin(t)&plus;8\cost(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D'(t)=-6\sin(2t)&plus;2\sin(t)&plus;8\cost(t)=0" title="D'(t)=-6\sin(2t)+2\sin(t)+8\cost(t)=0" /></a>

Utilizando el método de Newton: 


Resultados: 

```
 t = 0.587219776635034
 d^2 = 0.3111186586832909
 
```

Gráficamente, podemos verificar tanto la validez como la convergencia del método. 

<p align="center">
  <img src="Derivate.png" width="320" heigth="240">
</p>

<p align="center">
  <img src="Distancia.png" width="320" heigth="240">
</p>


## Punto 10.

Se utilizará el método de Newton para encontrar una intersección de las siguientes ecuaciones en coordenadas polares. 

<a href="https://www.codecogs.com/eqnedit.php?latex=r=2&plus;\cos&space;(3t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r=2&plus;\cos&space;(3t)"/></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=r=2-e^{t}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r=2-e^{t}" title="r=2-e^{t}" /></a>

**Solución:** 
                                                                                              
Se igualan las dos ecuaciones y se obtiene la siguiente expresión. 

<a href="https://www.codecogs.com/eqnedit.php?latex=r=2-e^{t}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\cos&space;(3t)+e^{t}=0"/></a>

**Resultados método de Newton:**

```
Solucion en Radianes:  -0.6973291224219446
Solucion en Grados:  -39.954015646338924  
R = 1.5020866070676133
```

No obstante, una de las funciones es periódica, con periodo <a href="https://www.codecogs.com/eqnedit.php?latex=T=\frac{2\pi}{3}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T=\frac{2\pi}{3}" title="T=\frac{2\pi}{3}" /></a> , por lo tanto la respuesta general al problema es: 

<a href="https://www.codecogs.com/eqnedit.php?latex=t=&space;-0.6973&plus;&space;\frac{2k&space;\pi}{3}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t=&space;-0.6973&plus;&space;\frac{2k&space;\pi}{3}" title="t= -0.6973+ \frac{2k \pi}{3}" /></a>

Gráficamente, podemos verificar la validez de la solución. 

<p align="center">
  <img src="Polar plot.png">
</p>

## Punto 14. 

## Punto 15. 

Se propone resolver la integral <a href="https://www.codecogs.com/eqnedit.php?latex=\int_{0}^{x}&space;\left&space;(&space;5&space;-&space;e^{u}&space;\right&space;)&space;du" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int_{0}^{x}&space;\left&space;(&space;5&space;-&space;e^{u}&space;\right&space;)&space;du" title="\int_{0}^{x} \left ( 5 - e^{u} \right ) du" /></a> con el método del punto fijo. 

Al resolver la integral, la expresión puede reescribirse como:

<a href="https://www.codecogs.com/eqnedit.php?latex=f(x)=5x-e^{x}-1=0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)=5x-e^{x}-1=0" title="f(x)=5x-e^{x}-1=0" /></a>

Gráficamente, el posible dar un estimado de la raiz real de la expresión:

<p align="center">
  <img src="Punto_15.png">
</p>


Nuevamenta, la expresión puede reescribirse como: 

<a href="https://www.codecogs.com/eqnedit.php?latex=x=\frac{1&plus;e^{x}}{5}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x=\frac{1&plus;e^{x}}{5}" title="x=\frac{1+e^{x}}{5}" /></a>

Utilizaremos el método del punto fijo para solucionar la expresión, encontreremos una solución en el intervalo

**Resultados:**

Al cabo de 5 iteraciones se obtivieron los siguientes resultados: 

```
 x    = 0.5430355169274723
f(x)  = 1.9939538406139703

```

Se verifica la condición del método del punto fijo, se muestra el valor de la derivada de la función auxiliar y en cada iteración se observa que siempre es menor que 1 en valor absoluto. 

```
Primera iteración: 0.29836493952825405
Segunda iteración: 0.3292055428770587
Tercera iteración: 0.33951662315069553
Cuarta  iteración: 0.34303551692747236
Quinta iteracióon: 0.3442447488046782

```











