# ENTRADA:
# - Un texto.
# - Un patrón.

# PROCESO:
# 1. Crear la clase AnalizadorPatrones.
# 2. Crear encontrar_palabras().
# 3. Separar el texto en palabras usando split().
# 4. Revisar qué palabras comienzan con el patrón.
# 5. Crear agrupar_por_longitud().
# 6. Separar el texto en palabras.
# 7. Obtener la longitud de cada palabra.
# 8. Guardar las palabras en un diccionario según su longitud.
# 9. Crear palabras_unicas().
# 10. Utilizar un conjunto para eliminar palabras repetidas.

# SALIDA:
# - Lista de palabras que coinciden.
# - Diccionario agrupado por longitud.
# - Conjunto de palabras únicas.

#BOSQUEJO:
# INICIO

#     Crear clase AnalizadorPatrones

#         Crear lista palabras

#         Método encontrar_palabras(texto, patron)

#             Crear lista vacía

#             Separar el texto en palabras

#             Recorrer todas las palabras

#                 Verificar si la palabra comienza
#                 con el patrón

#                 Si comienza con el patrón

#                     Agregar la palabra a la lista

#             Retornar la lista

#         Método agrupar_por_longitud(texto)

#             Crear diccionario vacío

#             Separar el texto en palabras

#             Recorrer todas las palabras

#                 Obtener la longitud de la palabra

#                 Si la longitud no existe en el diccionario

#                     Crear una lista vacía para esa longitud

#                 Agregar la palabra a la lista correspondiente

#             Guardar las palabras en el atributo palabras

#             Retornar el diccionario

#         Método palabras_unicas()

#             Convertir las palabras almacenadas
#             en un conjunto

#             Retornar el conjunto

#     Crear objeto AnalizadorPatrones

#     Buscar palabras que comiencen con un patrón

#     Mostrar las palabras encontradas

#     Agrupar las palabras según su longitud

#     Mostrar los grupos

#     Obtener las palabras únicas

#     Mostrar las palabras únicas

# FIN

class AnalizadorPatrones:
    def __init__(self):
        self.palabras = []

    def encontrar_palabras(self, texto, patron):
        resultado = []

        palabras = texto.split()

        for c in palabras:
            if c.startswith(patron):
                resultado.append(c)

        return resultado

    def agrupar_por_longitud(self, texto):
        resultado = {}

        palabras = texto.split()

        for palabra in palabras:
            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        self.palabras = palabras

        return resultado

    def palabras_unicas(self):
        return set(self.palabras)


ap = AnalizadorPatrones()

print(ap.encontrar_palabras("el gato está aquí", "ga"))

print(ap.agrupar_por_longitud("el gato está aquí"))

print(ap.palabras_unicas())