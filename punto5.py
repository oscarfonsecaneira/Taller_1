v = 4
Ev = 0.1
t = 5
Et = 0.1
d = v*t
Eda = ((Ev/v)+(Et/t))*d
print("Distancia:",d)
print("Error abosoluto:",Eda)
Edr = Eda/d
print("Error relativo:",Edr)
