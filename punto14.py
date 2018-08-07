import math

def funcion(x):
  return ((9.8*68.1)/x)*(1-math.exp(-(x/68.1)*10))-40

def verificar(intervalo):
  valor_inf = funcion(intervalo[0])
  valor_sup = funcion(intervalo[1])
  return valor_inf*valor_sup

def operacion(a, b, E, d):
  x = a
  if (d > E):
    if(funcion(x) > 0):
      d = (b-a)/10
      x = x + d
      return operacion(x,b,E,d)
    else:
      x = x - d
      d = d/10
      x = x + d
      return operacion(x,b,E,d)
  else:
    return round(x,8)

intervalo = [10,20]
a = intervalo[0]
b = intervalo[1]
E = 0.000001
d = 10
verificacion = verificar(intervalo)
if (verificacion > 0):
  print("El intervalo no encierra la raiz")
else:
  print("La raiz es:", operacion(a, b, E, d))
