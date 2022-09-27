"""Mostrar por pantalla el promedio de los números ingresados 
por teclado. Se deja de pedir que el usuario agregue números una vez 
ingrese 0 (cero).
"""
#Declaro variables
n=1
acumulador=0
promedio=0
#INicializo programa
while n != 0:
    n=int(input("Ingrese un número y presione 0 para terminar: "))
    acumulador = acumulador + n  #suma de numeros 
    promedio += 1  #acumulador de numeros(cantidad)

print(f"El promedio de los números ingresados es: {acumulador/promedio}")