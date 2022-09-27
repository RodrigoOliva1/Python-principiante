"""Números pares e impares Se pide desarrollar un programa que permita
 leer una serie de números. La nalización de carga de datos se presenta 
 cuando el usuario ingrese un número negativo. Los requerimientos 
 funcionales del programa son: La sumatoria de solo los números que 
 estén comprendidos entre 50 y 100. Cantidad de valores pares ingresados.
  Cantidad de valores impares ingresados. Informar si en 
  la carga de números se ingreso al menos un número 0. Informar
   si la serie contiene solo números pares e impares alternados."""

#Declaro variables
n=0
sumatoria=0
acumulador=0
contadorpar=0
contadorimpar=0
contadorcero=0

#Inicializo programa

while n >=0:
    n= int(input("Ingrese un número e ingrese número negativo para terminar:"))

    if n >= 50 and n <= 100:
        acumulador += n #acumulo nros entre 50 y 100
    
    if n % 2 == 0:
        contadorpar += 1
    if n % 2 != 0:
        contadorimpar += 1
    if n == 0:
        contadorcero += 1

print(f"La suma de  los numeros entre 50 y 100 es: {acumulador} ")
print(f"La cantidad de valores pares es: {contadorpar} ")
print(f"La cantidad de valores impares es: {contadorimpar} ")
print(f"La cantidad de 0 es: {contadorcero} ")
    
