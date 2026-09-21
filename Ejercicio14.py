# ENTRADA:
# - Nombre del estudiante.
# - Nota.

# PROCESO:
# 1. Crear la clase RegistroNotas.
# 2. Crear un diccionario estudiante → nota.
# 3. Registrar estudiantes y sus notas.
# 4. Recorrer el diccionario para encontrar aprobados.
# 5. Comparar las notas para encontrar la mayor.
# 6. Guardar el nombre y la nota del mejor estudiante.

# SALIDA:
# - Lista de estudiantes aprobados.
# - Tupla con nombre y nota del mejor estudiante.


#BOSQUEJO:
# INICIO

#     Crear clase RegistroNotas

#         Crear diccionario registro


#         Método registrar(estudiante, nota)

#             Recibir nombre del estudiante
#             y su nota


#             Guardar estudiante y nota
#             en el diccionario


#         Método estudiantes_aprobados(nota_minima)

#             Crear lista vacía para guardar
#             estudiantes aprobados


#             Recorrer estudiantes y notas


#                 Comparar la nota
#                 con la nota mínima


#                 Si la nota es mayor o igual
#                 a la nota mínima

#                     Agregar estudiante
#                     a la lista


#             Retornar lista de aprobados


#         Método mejor_estudiante()

#             Crear variable para guardar
#             el mejor estudiante

#             Crear variable para guardar
#             la mejor nota


#             Recorrer estudiantes y notas


#                 Comparar la nota actual
#                 con la mejor nota


#                 Si la nota es mayor

#                     Actualizar la mejor nota

#                     Guardar el nombre
#                     del estudiante


#             Retornar estudiante
#             y su nota


#     Crear objeto RegistroNotas


#     Registrar estudiantes

#         Ana → 95

#         Bob → 70

#         Carlos → 85


#     Buscar estudiantes aprobados

#         Nota mínima → 70


#     Mostrar estudiantes aprobados


#     Buscar estudiante
#     con mejor nota


#     Mostrar mejor estudiante
#     y su nota

# FIN
class  RegistroNotas:
    def __init__(self):
        self.registro={}
        
    def registrar(self,estudiante, nota):
        self.registro[estudiante]=nota
        
    def  estudiantes_aprobados(self, nota_minima):
        lista=[]
        for i, c in  self.registro.items():
            
            if c >= nota_minima:
                lista.append(i)
        return lista
            
            
    def mejor_estudiante(self):
       
        mejor_est= ""
        mejor_nota=0
        
        for est, mayor in self.registro.items():
            
            if mejor_nota > mayor:
                mejor_nota= mayor
                mejor_est= est
        
        return (mejor_est,mejor_nota)
    

rn = RegistroNotas()

rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Carlos", 85)

print(f"los estudiantes aprobados son: {rn.estudiantes_aprobados(70)}")
print(f"El mejor estudiantes es: {rn.mejor_estudiante()}")


    