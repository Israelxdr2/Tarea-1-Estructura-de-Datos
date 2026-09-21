# EJERCICIO 3: CARRO DE COMPRAS

#
# ENTRADA:
# - Nombre del artículo.
# - Precio del artículo.
#
# PROCESO:
# 1. Crear una clase llamada CarroCompras.
# 2. Crear un diccionario para almacenar los artículos.
# 3. Crear un método agregar_articulo().
# 4. Guardar el nombre y precio en el diccionario.
# 5. Crear un método total_carrito().
# 6. Recorrer los precios de los artículos.
# 7. Sumar todos los precios.
# 8. Crear un método articulos_por_rango().
# 9. Recorrer los artículos.
# 10. Comparar sus precios con el rango indicado.
# 11. Guardar los artículos que estén dentro del rango.
#
# SALIDA:
# - Total del carrito.
# - Artículos que pertenecen al rango indicado.

#BOSQUEJO:
# INICIO

#     Crear clase CarroCompras

#         Crear diccionario articulos


#         Método agregar_articulo(nombre, precio)

#             Recibir nombre y precio del artículo

#             Guardar el artículo en el diccionario

#                 Nombre como clave

#                 Precio como valor


#         Método total_carrito()

#             Crear variable total = 0

#             Recorrer los precios de los artículos

#                 Sumar cada precio al total


#             Retornar el total


#         Método articulos_por_rango(minimo, maximo)

#             Crear diccionario vacío para guardar
#             los artículos que cumplen el rango


#             Recorrer los artículos

#                 Obtener nombre y precio


#                 Comparar si el precio está entre
#                 el mínimo y el máximo


#                 Si cumple el rango

#                     Guardar nombre y precio
#                     en el diccionario resultado


#             Retornar el diccionario resultado


#     Crear objeto CarroCompras

#     Agregar artículos al carrito

#         Mouse → 15

#         Teclado → 30

#         Monitor → 200

#         Audífonos → 25


#     Calcular y mostrar el total del carrito

#     Buscar artículos entre $20 y $50

#     Mostrar los artículos encontrados

# FIN

class CarroCompras:
    def __init__(self):
        self.articulos = {}
     
    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio
    
    def total_carrito(self):
        total = 0
        for precio in self.articulos.values():
            total += precio
        return total

    def articulos_por_rango(self, minimo, maximo):
        resultado = {}
        
       
        for nombre, precio in self.articulos.items(): 
            
           
            if minimo <= precio <= maximo:
                resultado[nombre] = precio   
        
        return resultado
        

carrito = CarroCompras()

carrito.agregar_articulo("Mouse", 15)
carrito.agregar_articulo("Teclado", 30) 
carrito.agregar_articulo("Monitor", 200)
carrito.agregar_articulo("Audífonos", 25)

print("Total del carrito:", carrito.total_carrito()) 
print("Artículos entre $20 y $50:") 
print(carrito.articulos_por_rango(20, 50))

    
    
    
    