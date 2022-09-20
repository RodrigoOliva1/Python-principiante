"""Secuencia de impares. Cargar por teclado dos números, 
e imprimir los números impares que se encuentran comprendidos
 entre ellos, en forma ascendente y descendente."""

#Declaro avariables
n1=0
n2=0
i=0

#Inicializo programa
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

#reviso menor/mayor para ordenar
if n1 < n2:    
    menor, mayor = n1, n2
else:    
    menor, mayor = n2, n1
#eb caso de ser par +1 o -1 (impar)
if menor % 2 == 0:
    menor += 1
if mayor % 2 == 0:
    mayor -= 1

print("Nros comprendidos en forma ascendente: ")
for i in range(menor, mayor+1, 2):
    print(i, end=" ")

print(" ")

print("Nros comprendidos en forma descendiente: ",)
for i in range(mayor, menor-1, -2):
    print(i, end=" ")




#
#if ---
#    for i in range(mayor, menor, -2):
#       print(n2)

