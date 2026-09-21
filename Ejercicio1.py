
# EJERCICIO 1: VALIDADOR DE NOTAS CON PROMEDIO


# ENTRADA:
# - Varias notas.
#
# PROCESO:
# 1. Crear una clase llamada Calificador.
# 2. Crear una lista para almacenar las notas válidas.
# 3. Crear un método validar_nota(nota).
# 4. Comprobar que la nota esté entre 0 y 100.
# 5. Crear un método cargar_notas(*args).
# 6. Recorrer todas las notas recibidas.
# 7. Utilizar validar_nota() para comprobar cada nota.
# 8. Guardar únicamente las notas válidas en la lista.
# 9. Crear un método promedio().
# 10. Sumar las notas almacenadas.
# 11. Dividir la suma para la cantidad de notas.
#
# SALIDA:
# - Lista de notas válidas.
# - Promedio de las notas válidas.

#BOSQUEJO:
# INICIO

#     Crear clase Calificador

#         Crear constructor __init__()

#             Crear lista vacía para guardar las notas


#         Método validar_nota(nota)

#             Recibir una nota

#             Si la nota es mayor o igual a 0
#             y menor o igual a 100

#                 Retornar verdadero

#             Si no

#                 Retornar falso


#         Método cargar_notas(*args)

#             Recibir varias notas

#             Recorrer cada nota

#                 Validar la nota

#                 Si la nota es válida

#                     Agregar la nota a la lista


#             Retornar la lista de notas


#         Método promedio()

#             Crear variable suma = 0

#             Recorrer las notas

#                 Sumar cada nota


#             Dividir la suma
#             para la cantidad de notas

#             Retornar el promedio


#     Crear objeto Calificador

#     Cargar varias notas

#     Validar las notas

#     Guardar solamente las notas válidas

#     Mostrar las notas guardadas

#     Calcular y mostrar el promedio

# FIN

class Calificador:
    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if nota >= 0 and nota <= 100:
            return True
        else:
            return False

   
    def cargar_notas(self, *args):

        for nota in args:

            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

   
    def promedio(self):

        suma = 0

        for nota in self.notas:
            suma += nota

        return suma / len(self.notas)


c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, -5, 88))
print(c.promedio())
 
