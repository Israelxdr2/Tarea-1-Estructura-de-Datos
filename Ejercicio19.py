# ENTRADA:
# - Nombre del producto.
# - Cantidad.

# PROCESO:
# 1. Crear la clase Inventario.
# 2. Crear un diccionario producto → cantidad.
# 3. Crear agregar_stock().
# 4. Si el producto existe, aumentar su cantidad.
# 5. Si no existe, crearlo.
# 6. Crear restar_stock().
# 7. Verificar si hay suficiente stock.
# 8. Restar la cantidad si existe suficiente.
# 9. Crear productos_bajo_stock().
# 10. Buscar productos con cantidad menor al mínimo.

# SALIDA:
# - True o False al restar.
# - Lista de productos con bajo stock.

#BOSQUEJO:
# INICIO

#     Crear clase Inventario

#         Crear diccionario stock

#         Método agregar_stock(producto, cantidad)

#             Si el producto ya existe

#                 Sumar la cantidad al stock existente

#             Si no existe

#                 Crear el producto en el diccionario

#                 Guardar la cantidad

#         Método restar_stock(producto, cantidad)

#             Verificar que el producto exista

#             Verificar que haya suficiente cantidad

#             Si se cumplen las condiciones

#                 Restar la cantidad del stock

#                 Retornar Verdadero

#             Si no

#                 Retornar Falso

#         Método productos_bajo_stock(minimo)

#             Crear lista vacía

#             Recorrer los productos y sus cantidades

#                 Si la cantidad es menor que el mínimo

#                     Agregar el producto a la lista

#             Retornar la lista

#     Crear objeto Inventario

#     Agregar producto y cantidad

#     Restar una cantidad del producto

#     Mostrar si la operación fue exitosa

#     Buscar productos con stock menor al mínimo

#     Mostrar los productos encontrados

# FIN

class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        else:
            return False

    def productos_bajo_stock(self, minimo):
        resultado = []

        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)

        return resultado


inv = Inventario()

inv.agregar_stock("pan", 50)

print(inv.restar_stock("pan", 30))

print(inv.productos_bajo_stock(25))