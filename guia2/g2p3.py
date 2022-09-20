"""Sueldos y aguinaldo. Ingresar por teclado los sueldos de un vendedor, 
correspondientes al primer semestre del año y luego:
a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más 
alto del período.
b) Determinar en qué mes recibió el sueldo más bajo del período.
c) Informar el sueldo promedio del semestre."""

#declaro variables
sueldo=0.0
aguinaldo=0.0
s_alto=0.0
s_bajo=0.0
promedio=0.0
min=9999999
x=0

#inicializo programa
for x in range(1, 7):
    sueldo=float(input(f"Ingrese el sueldo recibido en el mes {x}:"))

    #acumulador
    promedio = promedio + sueldo
    ##
    if sueldo > s_alto: 
        s_alto = sueldo #calculo aguinaldo a partir del sueldo mas alto
        aguinaldo = s_alto / 2
    ##
    if sueldo < min:
        s_bajo = x #guardo el mes con sueldo mas bajo
        min = sueldo

promedio = promedio / x

print(f"El aguinaldo es de: ${aguinaldo}")
print(f"El mes número {s_bajo} tuvo el sueldo más bajo con ${min}")
print(f"El sueldo promedio del semestre es de: ${promedio}")
#