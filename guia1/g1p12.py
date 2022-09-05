"""Escribir un programa que pida dos números y muestre como 
resultado su división, cociente y resto."""

#declaro variables
a=0.0
b=0.0

#Inicializo programa
a=float(input("Ingrese número A:"))
b=float(input("Ingrese número B:"))

#muestro los resultados
print("El resultado es:", a/b)
print("El cociente: ", a//b)
print("El resto es:", a%b)

