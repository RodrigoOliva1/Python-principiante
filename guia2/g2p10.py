"""Búsqueda de mayor Realizar un programa que permita buscar el mayor 
de 10.000 números aleatorios generados en el rango de[0,100.000]."""
from ast import Num
import random
#declaro variables
n=0
mayor=0

#
for i in range(10000):
    n = random.randint(0, 100000)

    if n > mayor:  #numero mayor, maximos minimos
        mayor = n 

print(f"El numero mas alto entre los 10000 es: {mayor}")