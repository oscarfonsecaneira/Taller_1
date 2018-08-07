print("Ingrese el valor de n:", end="")
n = int(input())
T = 0;
while n > 0:
  d = n % 2
  n = n // 2
  T = T + 1
  print("d =",d)
print("T(n)=",T)
