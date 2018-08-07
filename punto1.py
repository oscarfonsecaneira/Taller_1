def horner(p, n, x, numero_operaciones):
  y = p[0]
  for i in range (1, n):
    y = x*y + p[i]
    numero_operaciones[0] = numero_operaciones[0] + 2
  return y

p = [7,6,-6,0,3,-4]
n = 6
x0 = 3
print("Valor de x:", x0, "\n")
for i in range (0, n-1): 
  if(i!=0):
    print("Derivada ", i)
  numero_operaciones = [0]
  if (n-1==1):
    print(f"Polinomio: {p[0]}x +{p[1]}", end="")
  else:
    print(f"Polinomio: {p[0]}x^{n-1} ", end="")
    m = n - 2
    for k in range(-1, m):
      if(p[k+2]!=0):
        if(p[k+2]>0):
          print("+", end="")
          if(m!=0):
            if(m==1):
              print(f"{p[k+2]}x ", end="")
            else:  
              print(f"{p[k+2]}x^{m} ", end="")
          else:
            print(f"{p[k+2]}", end="")
        else:
          if(m!=0):
            if(m==1):
              print(f"{p[k+2]}x ", end="")
            else:  
              print(f"{p[k+2]}x^{m} ", end="")
          else:
            print(f"{p[k+2]}", end="")
      m = m-1
  print("\nResultado polinomio:", horner(p, n, x0, numero_operaciones))
  print("Numero de operaciones:", numero_operaciones, "\n")
  p.pop()
  n = n - 1
  k = n
  for j in range(0, k):
    p[j] = p[j]*k
    k = k - 1
    
