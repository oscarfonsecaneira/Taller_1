# N-Seccions
Code for finding the root of a function using a generalization of Bisections Method.

You need to specify the Interval that might contain the root of the function, the number of sub-intervals you want to consider in each iteration and the desired tolerance of the answer. 

```
a := Lower Limit 
b := Upper Limit. 
n := Number of Divisions. 
tol := Desired Tolerance of the Answer. 
```

These are some of the results that can be obtained with the algorithm for different combiantions of functions and parameters:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(x)=(x-3)(x+6)"/>

```
a = -8; b =5 ; n=5  tol=1e-8
```
Results: 
```
 x   = -6.000000000983039
f(x) =  8.847354849706364e-09 
```

<p align="center">
  <img src="f1.png">
</p>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;f(c)=\frac{gm}{c}"/>

```
a = 1; b =20 ; n=2  tol=1e-8
```
Results: 
```
x    = 14.78020382951945
f(x) = 4.175156220753706e-09
```

<p align="center">
  <img src="f2.png">
</p>


