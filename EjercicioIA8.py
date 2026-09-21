#EJERCICIO 8:
# Desarrolle una clase llamada Cursos que permita crear cursos y registrar estudiantes dentro de cada curso.

# La clase deberá:

# Tener un método crear_curso(nombre_curso) que cree un curso con una lista vacía de estudiantes dentro de un diccionario.
# Tener un método agregar_estudiante(curso, estudiante) que agregue un estudiante al curso indicado.
# Tener un método curso_mayor_estudiantes() que retorne el nombre del curso que tenga la mayor cantidad de estudiantes.


#BOSQUEJO:
# INICIO

#     Crear clase Cursos

#         Crear diccionario cursos


#         Método crear_curso(nombre_curso)

#             Crear lista vacía

#             Guardar curso en el diccionario
#             junto con la lista vacía


#         Método agregar_estudiante(curso, estudiante)

#             Buscar el curso en el diccionario

#             Agregar estudiante
#             a la lista del curso


#         Método curso_mayor_estudiantes()

#             Crear variable para guardar
#             el curso con mayor cantidad

#             Crear variable para guardar
#             la cantidad máxima

#             Recorrer los cursos

#                 Obtener cantidad de estudiantes

#                 Comparar con la cantidad máxima

#                 Si es mayor

#                     Actualizar cantidad máxima

#                     Guardar nombre del curso


#             Retornar nombre del curso


#     Crear objeto Cursos

#     Crear cursos

#     Agregar estudiantes

#     Mostrar curso con más estudiantes

# FIN


class Cursos:
    def __init__(self):
        self.cursos={}
    
    def crear_curso(self,nombre_curso):
        self.cursos[nombre_curso]=[]
    
    def agregar_estudiante(self,curso, estudiante):
        self.cursos[curso].append(estudiante)
    
    def curso_mayor_estudiantes(self):
        curso_mayor=""
        cant_max=0
        
        for i,c in self.cursos.items():
            if len(c)>= cant_max:
                cant_max= len(c)
                curso_mayor=i
        return curso_mayor
cr= Cursos()
cr.crear_curso("Matemáticas")
cr.crear_curso("Física")
cr.crear_curso("Programación")

cr.agregar_estudiante("Matemáticas", "Juan")
cr.agregar_estudiante("Matemáticas", "Pedro")

cr.agregar_estudiante("Física", "Ana")

cr.agregar_estudiante("Programación", "Carlos")
cr.agregar_estudiante("Programación", "Luis")
cr.agregar_estudiante("Programación", "María")

print(f"El equipo mayor es: {cr.curso_mayor_estudiantes()}")