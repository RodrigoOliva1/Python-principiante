"""Crear un conversor de dólares a pesos y pesos a dólares, 
donde se ingrese por teclado el valor del peso actual."""

#declaro variables
dolar=140.16
moneda=0.0
opcion=0

#menu
print("---Menu---")
print("1. Peso Argentino a dolar")
print("2. Dolar a peso Argentino")
#inicializo programa
opcion=int(input("Seleccione una opcion: "))

#si el numero seleccionado es menor o igual a 0, o mayor/igual a 3
if (opcion<=0)or(opcion>=3): 
    print("Error")

if opcion==1:
    moneda=float(input("Ingrese la cantidad de pesos Argentinos a convertir:"))
    print("Usted ingresó", moneda, "pesos Argentinos y son", moneda/dolar, "dolares")

else:
    moneda=float(input("Ingrese la cantidad de dolares a convertir:"))
    print("Usted ingresó", moneda, "dolares y son", moneda*dolar, "pesos Argentinos.")
