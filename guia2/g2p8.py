"""Ventas por sucursal. Ingresar una serie de números por teclado que 
representan la cantidad de ventas realizadas en las diferentes sucursales 
de un país de una determinada empresa. Los requerimientos del 
programa son: Informar la cantidad de ventas ingresadas. Total de ventas.
 Cantidad de ventas cuyo valores estén comprendidos entre 100 y 300 
 unidades. Cantidad de ventas con 400,500 y 600 unidades. Indicar si 
 hubo una cantidad de ventas inferior a 50 unidades. Usted deberá 
 ingresar cantidades de ventas hasta que se ingrese un valor negativo."""

#Declaro variables
cantventas=0 #contador +1 x venta ingresada
totalventas=0 #acumulador total ventas
ventas=0    #venta a ingresar
ventascomprendidas=0
cantventas1=0  #400 u
cantventas2=0  #500 u
cantventas3=0  #600 u 
v_menor=0 #menor a 50

#><
#Inicializo gprograma
while ventas >= 0:
    ventas=float(input("Ingrese cantidad de ventas y digite número negativo para finalizar:"))
    totalventas = totalventas + ventas #acumulador total
    cantventas += 1 #contador de ventas

    if ventas >= 100 and ventas <= 300: #entre 100 y 300
        ventascomprendidas += 1
    if ventas == 400:
        cantventas1 += 1
    if ventas == 500:
        cantventas2 += 1
    if ventas == 600:
        cantventas3 += 1
    if ventas < 50:
        v_menor += 1

print(f"La cantidad de ventas ingresadas son de: {cantventas} ")
print(f"El total de ventas ingresadas: {totalventas} ")
print(f"Entre 100 y 300 unidades hay {ventascomprendidas} ventas ")
print(f"La cantidad de ventas con 400 unidades es de {cantventas1}, con 500 unidades es de {cantventas2} y con 600 hay {cantventas3} ")
print(f"La cantidad de ventas inferiores a 50 unidades es de {v_menor} ")