"""Menores y promedio Realizar un programa que genere 5000 numeros 
aleatorios en el rango de [0,100000] y que permita:Determinar el menor 
de los numeros genera dos en forma aleatoria.Calcular el valor promedio
 de los números menores a 10.000."""
import random
#Declaro variables
n=0
menor=999999
promedio=0.0
contador_m=0
acumulador_m=0

#Inicializo programa 
for i in range(0, 5000):
    n=random.randint(0, 100000)

    if n < menor:
        menor = n
    if n < 10000:
        contador_m += 1 #cantidad menores a 10.000
        acumulador_m += n #acumulador 

promedio = acumulador_m/contador_m

print(f"El menor de los numeros es: {menor} ")
print(f"El promedio de los numeros menores a 10.000 es: {promedio} ")
