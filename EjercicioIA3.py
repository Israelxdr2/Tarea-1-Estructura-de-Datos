#EJERCICIO 3:
# Desarrolle una clase llamada GestorProductos que permita registrar productos con sus respectivos precios y realizar algunas operaciones sobre ellos.
# La clase deberá:
# Tener un método agregar_producto(nombre, precio) que guarde cada producto y su precio en un diccionario.
# Tener un método productos_caros(precio_minimo) que retorne una lista con los nombres de los productos cuyo precio sea mayor o igual al precio indicado.
# Tener un método precio_promedio() que calcule y retorne el promedio de los precios registrados.
# Tener un método agregar_multiples(*productos) que permita registrar varios productos reutilizando el método agregar_producto().

#BOSQUEJO:
#INICIO

#    Crear clase GestorProductos

#        Crear diccionario productos

#        Método agregar_producto(nombre, precio)
#            Guardar nombre y precio en el diccionario

#        Método productos_caros(precio_minimo)
#            Crear lista vacía
#            Recorrer los productos
#                Si el precio es mayor o igual al precio mínimo
#                    Agregar nombre a la lista

#           Retornar lista

#        Método precio_promedio()
#            Crear variable suma = 0
#            Recorrer los productos
#                Sumar los precios

#            Calcular promedio
#            Retornar promedio

#        Método agregar_multiples(*productos)
#            Recorrer los productos recibidos
#                Utilizar agregar_producto()

#   Crear objeto GestorProductos

#    Registrar productos

#    Mostrar productos que cumplen el precio mínimo

#    Mostrar precio promedio

#FIN

class GestorProductos:
    def __init__(self):
        self.productos={}
    def agregar_producto(self,nombre, precio):
        self.productos[nombre]= precio
    def productos_caros(self,precio_minimo):
        lista=[]
        for i, c in self.productos.items():
            
            if c >= precio_minimo:
                lista.append(i)
            
        return lista
    def precio_promedio(self):
        suma=0
        
        for c in self.productos.values():
            suma += c 
        
        return suma/len(self.productos)
    def agregar_multiples(self, *productos):
        
        for i in productos:
            self.agregar_producto(*i)
gp = GestorProductos()

gp.agregar_producto("Pan", 2.50)
gp.agregar_producto("Leche", 3.00)
gp.agregar_producto("Carne", 8.00)

print(f"los productos con mayor precio son: {gp.productos_caros(3)}")
print(f"El promedio de los productos son: {gp.precio_promedio()}")