#EJERCICIO 14:
# Crea una clase llamada RegistroPrecios que:

# Tenga un método registrar(producto, precio) que guarde cada producto y su precio en un diccionario.
# Tenga un método productos_economicos(precio_maximo) que retorne una lista con los nombres de los productos cuyo precio sea menor o igual al precio máximo indicado.
# Tenga un método producto_mas_caro() que retorne el nombre y precio del producto que tenga el precio más alto.



#BOSQUEJO:
# INICIO

#  Crear clase RegistroPrecios

#     Crear diccionario precios

#     Método registrar(producto, precio)
#         Guardar producto y precio en el diccionario


#     Método productos_economicos(precio_maximo)

#         Crear lista vacía

#         Recorrer diccionario usando items()

#             Obtener producto y precio

#             Si precio <= precio_maximo
#                 Agregar producto a la lista

#         Retornar lista


#     Método producto_mas_caro()

#         Crear variable para producto más caro
#         Crear variable para precio máximo

#         Recorrer diccionario usando items()

#             Obtener producto y precio

#             Si precio es mayor al precio máximo
#                 Actualizar producto más caro
#                 Actualizar precio máximo

#         Retornar una tupla con producto y precio


#  Crear objeto RegistroPrecios

#  Registrar varios productos

#  Mostrar productos económicos

#  Mostrar producto más caro

# FIN

class RegistroPrecios:
    def __init__(self):
        self.registrar={}
    def registrador(self, producto, precio):
        self.registrar[producto]= precio
    def productos_economicos(self,precio_maximo):
        lista=[]
        for i,c in self.registrar.items():
            if  c <= precio_maximo:
                lista.append(i)
        return lista
    def producto_mas_caro(self):
        mas_caro=0
        nombre=""
        
        for i,c in self.registrar.items():
            if c > mas_caro:
                mas_caro=c 
                nombre=i
                
        return (nombre, mas_caro)
        
rp = RegistroPrecios()

rp.registrador("Pan", 2.50)
rp.registrador("Leche", 3.00)
rp.registrador("Carne", 8.00)

print(rp.productos_economicos(3))
print(rp.producto_mas_caro())