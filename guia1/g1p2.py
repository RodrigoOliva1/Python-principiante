"""Escribir un programa que pregunte un nombre de usuario, 
y que después muestre por pantalla si su cantidad de 
letras es par o impar."""

usuario=str(input("Ingrese su nombre de usuario:"))

#print(len(usuario))
if len(usuario)%2 == 0:
    print("Par")
else: 
    print("Impar")
    