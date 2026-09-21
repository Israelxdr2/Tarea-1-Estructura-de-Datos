# ENTRADA:
# - Elementos individuales.

# PROCESO:
# 1. Crear la clase ContadorFrecuencia.
# 2. Crear un diccionario para guardar los elementos.
# 3. Agregar cada elemento al diccionario.
# 4. Si el elemento ya existe, aumentar su contador.
# 5. Si no existe, comenzar su contador en 1.
# 6. Buscar el elemento que tenga mayor frecuencia.
# 7. Consultar cuántas veces aparece un elemento.

# SALIDA:
# - Elemento más frecuente.
# - Frecuencia de un elemento.


#BOSQUEJO:
# INICIO

#     Crear clase ContadorFrecuencia

#         Crear diccionario vacío
#         para guardar los elementos
#         y sus frecuencias


#         Método agregar_elemento(elemento)

#             Recibir un elemento

#             Comprobar si el elemento
#             ya existe en el diccionario


#             Si existe

#                 Aumentar su frecuencia
#                 en 1


#             Si no existe

#                 Agregar el elemento
#                 al diccionario

#                 Establecer su frecuencia en 1


#         Método elemento_mas_frecuente()

#             Crear variable para guardar
#             el elemento con mayor frecuencia

#             Crear variable para guardar
#             la frecuencia mayor


#             Recorrer los elementos
#             y sus frecuencias


#                 Comparar la frecuencia actual
#                 con la frecuencia mayor


#                 Si es mayor

#                     Actualizar la frecuencia mayor

#                     Guardar el elemento


#             Retornar el elemento
#             más frecuente


#         Método frecuencia_elemento(elemento)

#             Recibir un elemento

#             Comprobar si existe
#             en el diccionario


#             Si existe

#                 Retornar su frecuencia


#             Si no existe

#                 Retornar 0


#     Crear objeto ContadorFrecuencia

#     Agregar elementos

#         "a"

#         "b"

#         "c"


#     Buscar el elemento
#     más frecuente


#     Mostrar el elemento más frecuente


#     Buscar la frecuencia
#     del elemento "a"


#     Mostrar la frecuencia

# FIN

class ContadorFrecuencia:
    def __init__(self):
        self.diccionario={}
    
    def  agregar_elemento(self, elemento):
        
        if elemento in self.diccionario:
            self.diccionario[elemento] += 1
        else:
            self.diccionario[elemento] = 1
    def elemento_mas_frecuente(self):
        
        elemento_mayor=""
        frecuencia_mayor=0
        
        for elementoM, frecuenciaM in  self.diccionario.items():
            if frecuenciaM > frecuencia_mayor:
                frecuencia_mayor= frecuenciaM
                elemento_mayor= elementoM
        
        return elemento_mayor
    def frecuencia_elemento(self, elemento):
        if elemento in self.diccionario:
            return self.diccionario[elemento]
        else:
            return 0
        
cf= ContadorFrecuencia()

cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("c")

print(f"El elemento mas frecuente es {cf.elemento_mas_frecuente()}")
print(f"la frecuencia es: {cf.frecuencia_elemento("a")}")