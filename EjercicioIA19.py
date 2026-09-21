#EJERCICIO 19:

# Crea una clase llamada AlmacenMateriales que:

# Tenga un método agregar_material(material, cantidad) que guarde en un diccionario la cantidad disponible de cada material.
# Si el material ya existe, debe sumar la nueva cantidad a la cantidad que ya tenía.
# Tenga un método retirar_material(material, cantidad) que disminuya la cantidad disponible y retorne:
# True si existe suficiente material.
# False si no existe o no hay suficiente cantidad.
# Tenga un método materiales_bajo_cantidad(minimo) que retorne una lista con los materiales cuya cantidad sea menor al mínimo indicado.

#BOSQUEJO:

# INICIO

#  Crear clase AlmacenMateriales

#     Crear diccionario materiales


#     Método agregar_material(material, cantidad)

#         Si el material ya existe
#             Sumar cantidad a la cantidad actual

#         Si no existe
#             Guardar material con su cantidad


#     Método retirar_material(material, cantidad)

#         Si material existe Y tiene suficiente cantidad

#             Restar cantidad

#             Retornar True

#         Si no

#             Retornar False


#     Método materiales_bajo_cantidad(minimo)

#         Crear lista vacía

#         Recorrer diccionario

#             Obtener material y cantidad

#             Si cantidad < minimo
#                 Agregar material a la lista

#         Retornar lista


#  Crear objeto AlmacenMateriales

#  Agregar materiales

#  Retirar un material

#  Mostrar resultado de la retirada

#  Buscar materiales con poca cantidad

#  Mostrar lista

# FIN

class AlmacenMateriales:

    def __init__(self):
        self.materiales = {}


    def agregar_material(self, material, cantidad):
        if material in self.materiales:
            self.materiales[material] += cantidad
        else:
            self.materiales[material] = cantidad

    
    def retirar_material(self, material, cantidad):
        if material in self.materiales and self.materiales[material] >= cantidad:
            self.materiales[material] -= cantidad
            return True
        else:
            return False

    def materiales_bajo_cantidad(self, minimo):
        lista = []

        for material, cantidad in self.materiales.items():
            if cantidad < minimo:
                lista.append(material)

        return lista


am = AlmacenMateriales()


am.agregar_material("cuadernos", 20)
am.agregar_material("lapices", 50)
am.agregar_material("borradores", 10)


print(am.retirar_material("cuadernos", 15))
print(am.materiales_bajo_cantidad(10))