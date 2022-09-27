"""Promedio de números aleatorios: Realice un programa que permita 
calcular el promedio de 1000 números aleatorios generados en el rango 
de[0,100000]."""

import random
#declaracion devariables
n=0
promedio=0.0
nrosaleatorios=0

for i in range(0, 1000):
    n = random.randint(0, 100000)
    nrosaleatorios = nrosaleatorios + n
    
promedio = nrosaleatorios / 1000

print(f"El promedio de 1000 numeros aleatorios es: {promedio}")
