#EJERCICIO 7:

#Desarrolle una clase llamada GestorInventario que permita registrar productos junto con sus precios y obtener información sobre ellos.
# La clase deberá:
# 
# Tener un método agregar_producto(nombre, precio) que guarde el nombre y precio del producto en un diccionario.
# Tener un método productos_economicos(precio_maximo) que retorne una lista con los nombres de los productos cuyo precio sea menor o igual al precio máximo indicado.
# Tener un método precio_promedio() que retorne el promedio de los precios registrados.

#BOSQUEJO:

# INICIO

#     Crear clase GestorInventario

#         Crear diccionario productos
#         Método agregar_producto(nombre, precio)

#             Guardar nombre y precio
#             en el diccionario
#         Método productos_economicos(precio_maximo)

#             Crear lista vacía

#             Recorrer productos utilizando items()

#                 Si el precio es menor o igual
#                 al precio máximo

#                     Agregar nombre a la lista

#             Retornar lista
#         Método precio_promedio()

#             Crear variable suma = 0

#             Recorrer los precios

#                 Sumar cada precio

#             Calcular promedio

#             Retornar promedio


#     Crear objeto GestorInventario

#     Registrar productos

#     Mostrar productos económicos

#     Mostrar precio promedio

# FIN


class GestorInventario:
    def __init__(self):
        self.producto={}
    
    def agregar_producto(self,nombre, precio):
        self.producto[nombre]= precio
    
    def productos_economicos(self,precio_maximo):
        lista=[]
        
        for i, c in self.producto.items():
            if c <= precio_maximo:
                lista.append(i)
                
        return lista
    def precio_promedio(self):
        suma=0
        for c in self.producto.values():
            suma += c 
        
        return suma/len(self.producto)
gi= GestorInventario()

gi.agregar_producto("Pan", 2.50)
gi.agregar_producto("Leche", 3.00)
gi.agregar_producto("Arroz", 5.00)
gi.agregar_producto("Carne", 8.00)

print(f"productos economicos {gi.productos_economicos(6)}")

print(f"el promedio es {gi.precio_promedio()}")