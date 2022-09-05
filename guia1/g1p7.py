"""Últimos dígitos ¿Cómo usaría el operador resto (%) para obtener 
el valor del último dígito de un número entero? ¿Y cómo obtendría los 
dos últimos dígitos? Desarrolle un programa que cargue un número entero
 por teclado, y muestre el último dígito del mismo (por un lado) y los 
 dos últimos dígitos (por otro lado)."""

#variables
numero=0

#inicializo programa
numero=int(input("Ingrese un número(entero):"))

#muestro el resto para ver ultimos digitos
print("El último digito es:", numero%10)
print("Los ultimos dos dígitos son:", numero%100)
