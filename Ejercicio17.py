# ENTRADA:
# - Varias edades.

# PROCESO:
# 1. Crear la clase AgrupadorEdades.
# 2. Crear clasificar_edad().
# 3. Utilizar if/elif para determinar la categoría.
# 4. Crear agrupar_por_categoria().
# 5. Recorrer todas las edades.
# 6. Clasificar cada edad.
# 7. Guardar cada edad en su categoría.
# 8. Crear edad_promedio_categoria().
# 9. Buscar las edades de la categoría.
# 10. Calcular su promedio.

# SALIDA:
# - Diccionario con categorías y edades.
# - Promedio de una categoría.



#BOSQUEJO:
# INICIO

#     Crear clase AgrupadorEdades

#         Crear diccionario grupos

#         Método clasificar_edad(edad)

#             Si la edad es menor que 12

#                 Retornar "niño"

#             Si no, si la edad es menor que 18

#                 Retornar "adolescente"

#             Si no, si la edad es menor que 60

#                 Retornar "adulto"

#             Si no

#                 Retornar "mayor"

#         Método agrupar_por_categoria(*edades)

#             Crear diccionario vacío

#             Recorrer todas las edades

#                 Clasificar la edad

#                 Obtener su categoría

#                 Si la categoría no existe en el diccionario

#                     Crear una lista vacía para esa categoría

#                 Agregar la edad a la lista de su categoría

#             Retornar el diccionario

#         Método edad_promedio_categoria(categoria)

#             Buscar las edades de la categoría

#             Crear variable suma en 0

#             Recorrer las edades

#                 Sumar cada edad

#             Dividir la suma para la cantidad de edades

#             Retornar el promedio

#     Crear objeto AgrupadorEdades

#     Agrupar varias edades

#     Mostrar los grupos creados

#     Calcular el promedio de una categoría

#     Mostrar el promedio

# FIN

class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}
        
    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 60:
            return "adulto"
        else:
            return "mayor"
    def agrupar_por_categoria(self, *edades):
        self.grupos={}
        
        for i in edades:
            categoria = self.clasificar_edad(i)

            if categoria not in self.grupos:
                self.grupos[categoria] = []

            self.grupos[categoria].append(i)

        return self.grupos
    
    def edad_promedio_categoria(self, categoria):
        edades = self.grupos[categoria]
        suma = 0

        for i in edades:
            suma += i

        return suma / len(edades)


ae = AgrupadorEdades()

print(ae.agrupar_por_categoria(5, 15, 30, 70))
print(ae.edad_promedio_categoria("adulto"))
            