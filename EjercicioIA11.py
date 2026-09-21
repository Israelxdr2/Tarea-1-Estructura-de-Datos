
#EJERCICIO 11:
# Crea una clase llamada ContadorProductos que:

# Tenga un método agregar_producto(producto) que guarde en un diccionario cuántas veces se registra cada producto.
# Tenga un método producto_mas_registrado() que retorne el producto que aparece más veces.
# Tenga un método cantidad_producto(producto) que retorne cuántas veces se ha registrado ese producto.



#BOSQUEJO:
# INICIO

#  Crear clase ContadorProductos

#     Crear diccionario productos

#     Método agregar_producto(producto)
#         Si el producto ya existe en el diccionario
#             Aumentar su contador
#         Si no existe
#             Guardarlo con cantidad 1

#     Método producto_mas_registrado()
#         Crear variable para guardar producto con mayor cantidad
#         Crear variable para guardar cantidad máxima

#         Recorrer el diccionario
#             Comparar cantidades
#             Si la cantidad actual es mayor
#                 Actualizar producto
#                 Actualizar cantidad máxima

#         Retornar producto más registrado

#     Método cantidad_producto(producto)
#         Buscar producto en el diccionario
#         Retornar su cantidad

#  Crear objeto ContadorProductos

#  Agregar varios productos

#  Mostrar producto más registrado

#  Mostrar cantidad del producto consultado

# FIN


class ContadorProductos:
    def __init__(self):
        self.contador={}
    
    def agregar_producto(self, producto):
        
        if producto in self.contador:
            self.contador[producto] +=1
        else:
            self.contador[producto] =1
            
    def producto_mas_registrado(self):
        name=""
        prod_mayor=0
        
        for i, c in self.contador.items():
            if c > prod_mayor:
                prod_mayor=c
                name=i
        return name
    
    def cantidad_producto(self, producto):
       
        if producto  in self.contador :
            return self.contador[producto]
        else:
            return 0
        
      
        
cp= ContadorProductos()

cp.agregar_producto("pan")
cp.agregar_producto("leche")
cp.agregar_producto("pan")
cp.agregar_producto("arroz")
cp.agregar_producto("pan")
cp.agregar_producto("leche")

print(cp.producto_mas_registrado())
print(cp.cantidad_producto("pan"))