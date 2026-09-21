#EJERCICIO 20:
# Clase AnalizadorPalabras que:

# Tenga un método buscar_palabras(texto, inicio) que busque las palabras que empiecen con el texto indicado y retorne una lista.
# Tenga un método agrupar_por_longitud(texto) que agrupe las palabras según su longitud y retorne un diccionario.
# Tenga un método palabras_unicas(texto) que retorne un conjunto con las palabras sin repetir.

#BOSQUEJO:
# INICIO

#     Crear clase AnalizadorPalabras

#         Método buscar_palabras(texto, inicio)
#             Separar texto en palabras
#             Crear lista vacía
#             Recorrer las palabras
#                 Si la palabra empieza con inicio
#                     Agregar palabra a la lista
#             Retornar lista

#         Método agrupar_por_longitud(texto)
#             Separar texto en palabras
#             Crear diccionario vacío
#             Recorrer las palabras
#                 Obtener longitud de la palabra
#                 Si la longitud no está en el diccionario
#                     Crear una lista para esa longitud
#                 Agregar palabra
#             Retornar diccionario

#         Método palabras_unicas(texto)
#             Separar texto en palabras
#             Convertir palabras en conjunto
#             Retornar conjunto

#     Crear objeto AnalizadorPalabras

#     Probar los tres métodos

# FIN

class AnalizadorPalabras:
    def __init__(self):
        self.palabras = []

    def buscar_palabras(self, texto, inicio):
        palabras = texto.split()
        resultado = []

        for palabra in palabras:
            if palabra.startswith(inicio):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        resultado = {}

        for palabra in palabras:
            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        return resultado

    def palabras_unicas(self, texto):
        palabras = texto.split()
        return set(palabras)


ap = AnalizadorPalabras()

print(ap.buscar_palabras("casa carro camino perro", "ca"))
print(ap.agrupar_por_longitud("sol casa perro"))
print(ap.palabras_unicas("sol casa sol perro casa"))