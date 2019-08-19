# REPL: Read Evaluate Print Loop = Python Terminal
import math
from math import factorial

print('Hello, Python')

# For example with math functions
for i in range(5):
    print('El cuadrado de {} es: {}'.format(i, math.pow(i, 2)))
    if factorial(i) > 1:
        print('El facorial de {} es: {}'.format(i, factorial(i)))
    else:
        print('Tu factorial es 1!!!')

# Hoy many groups of k fruits can do on a set of n fruits?
# factorial(y) / factorial(k) * factorial(n-k)

n = 5
k = 3
# // nos devuelve un integer, / devuelve float
print('En un grupo de 5 elementos, podemos hacer {} grupos de 3 elementos'
      .format(factorial(n) // factorial(k) * factorial(n - k)))

# While loop
c = 5
while c != 0:
    print(c)
    c -= 1

# break statement
c = 5
while c != 0:
    if c == 2:
        break
    print(c)
    c -= 1
