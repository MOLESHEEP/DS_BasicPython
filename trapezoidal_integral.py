from math import sin

from numpy import double
# --example--
# print(sin(0))
# >>> 0
# -----------
a = input("Please input lower limit: ")
b = input("Please input higher limit: ")
a = float(a)
b = float(b)
h = (b-a)/100
S = 0
for i in range(1,100):
    S = S + h/2*(sin(a+(i-1)*h)+sin(a+i*h))
print(S)
