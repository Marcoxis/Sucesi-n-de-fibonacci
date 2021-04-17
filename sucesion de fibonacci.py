#Programa sencillito, bien fresquito, que hace la sucesión de fibonacci#

import time

k = 1
n = int(input("Escribe el número de veces que quieres que se haga la sucesión de fibonacci: "))
a = 0
b = 1

while k<=n:
    time.sleep(0.3)
    c = a+b
    a = b
    b=c
    print(c)
    k= k+1    
