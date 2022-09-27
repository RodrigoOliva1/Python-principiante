""" Decimal a Hexadecimal: Generar n números aleatorios entre el rango
 de 5000 y 450000, por cada uno de ellos mostrar y generar el 
 numero hexadecimal."""

import random

#Declaro variables
numero=0
hexadecimal=0

numero= random.randint(5000, 450000) #funcion para generar numeros aleatorios comprendidos entre 5000 y 450000

print(f"El número es: {numero} ") #número generado
hexadecimal=hex(numero) #funcion hex para convertir a hexadecimal

print(f"El numero en hexadecimal es: {hexadecimal}") 
