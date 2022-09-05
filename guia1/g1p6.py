"""Área de un triángulo. Desarrolle un programa para calcular
 el área de un triángulo, cargando por teclado el valor de la base, 
 pero sabiendo que su altura es igual al cuadrado de la base."""

base=float(input("Inngrese el valor de la base del triangulo:"))

altura=base**2  #su altura es igual al cuadrado de la base

print("El área del triángulo es:", (base*altura)/2)
