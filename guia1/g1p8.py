"""Conversión de medidas. Desarrolle un programa para convertir una 
medida dada en pies a sus equivalentes en: yardas pulgadas cenơmetros
 metros Sabiendo que: 1 pie = 12 pulgadas 1 yarda = 3 pies 
 1 pulgada = 2.54 centímetros 1 metro =1000"""

#declaro variables
pies=0.0

#inicializo programa
pies=float(input("Ingrese la medida en pies:"))

#muestro los equivalentes
print("El equivalente en yardas es: ", pies/3)
print("El equivalente en pulgadas es:", pies*12)
print("El equivalente en centímetros:", pies*30.48)
print("El equivalente en metros es:", pies/3.281)
