"""Complejo de cines Desarrollar un programa que permita 
procesar funciones de un complejo de cines. Por cada función 
se conoce:cantidad de espectadores y descuento(S/N).La carga termina
 cuando la cantidad de espectadores sea igual a 0(cero).El programa 
 deberá:Calcular la recaudación total del complejo,considerando que 
 el valor de la entrada es de $50en los días con descuento y $75 en 
 los días sin descuento. Determinar cuántas funciones con descuentos 
 efectuaron y qué porcentaje representan sobre el total de funciones"""

#declaro variables
espectadores=1
recaudacion_t=0
#descuento=""
precio=0
funciondto=0
funciones=0
 
espectadores=int(input("Ingrese la cantidad de espectadores que ingresaron y 0 para terminar: "))
while espectadores != 0:
    descuento = str(input("Descuento S/N:"))

    if descuento == 'S':
        precio = 50
    else:
        precio = 75
    recaudacion_t = recaudacion_t + (espectadores * precio) #recaudacion total

    if descuento == 'S':
        funciondto +=1 #funciones con descuento
    funciones += 1 #cantidad de funciones
    espectadores = int(input("Ingrese la cantidad de espectadores que ingresaron y 0 para terminar: "))
print(f"La recaudacion total es: {recaudacion_t} ")
print(f"El porcentaje de funciones con descuento es: {(funciondto *100)/funciones} ")

