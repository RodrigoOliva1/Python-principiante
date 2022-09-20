"""Ciclistas: La final de una carrera de ciclistas tiene n competidores 
(n se ingresa por teclado). Desarrollar un programa que permita cargar, 
por cada competidor, nombre y tiempo de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera. 
Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas."""

#declaro variables
competidores=0
nombre=""
t_carrera=0.0
t_record=0.0
ganador=""
menor=999.0
promedio=0.0


#inicializo programa
while competidores <= 0:
    competidores = int(input("Ingrese la cantidad de competidores: "))
    t_record = float(input("Ingrese el tiempo record registrado: "))

    if competidores <= 0:
        print("Error -- ")
     
#for para recorrer los competidores
for competidores in range (1, competidores+1, 1):
    nombre = str(input("Ingrese su nombre: "))
    t_carrera = float(input("En cuánto tiempo finalizó la carrera? "))
    print(f"El competidor nro {competidores} {nombre.title()} completó la carrera en {t_carrera}")

    ###############################
    promedio = promedio + t_carrera
    #guardo el menor tiempo
    if t_carrera < menor:
        menor = t_carrera
        ganador = nombre
promedio = promedio / competidores


print(f"El ganador de la carrera es: {ganador.title()}")
print(f"Completó la carrera en: {menor} ")
print(f"El promedio entre los cilistas es: {promedio}")



#inicializo programa

