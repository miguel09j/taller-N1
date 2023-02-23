valor = float(input("ingrese le valor de su producto: "))
 
total_sin_iva = valor - 1.127 * 100

iva = valor-total_sin_iva

print("el precio original es: ",valor)
print("")
print("el total sin iva es: ",total_sin_iva)
print("")
print("el valor del iva se muestra con la mayor aproximacion posible: ")
print("")
print("el iva es de: ", iva)


