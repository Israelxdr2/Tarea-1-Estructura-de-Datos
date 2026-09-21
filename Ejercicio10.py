# ENTRADA:
# - Descripción de la tarea.
# - Prioridad.

# PROCESO:
# 1. Crear la clase Tareas.
# 2. Crear una lista para guardar las tareas.
# 3. Cada tarea será una tupla (descripción, prioridad).
# 4. Crear agregar_tarea().
# 5. Crear tareas_prioritarias() para buscar las tareas de prioridad alta.
# 6. Crear eliminar_completada() para eliminar una tarea.

# SALIDA:
# - Lista de tareas prioritarias.



#BOSQUEJO:
# INICIO

#     Crear clase Tareas

#         Crear lista vacía
#         para guardar las tareas


#         Método agregar_tarea(descripcion, prioridad)

#             Recibir descripción y prioridad


#             Crear una tupla con:

#                 Descripción

#                 Prioridad


#             Agregar la tupla
#             a la lista de tareas


#         Método tareas_prioritarias()

#             Crear lista vacía
#             para guardar las tareas prioritarias


#             Recorrer las tareas


#                 Obtener descripción y prioridad


#                 Comprobar si la prioridad es "Alta"


#                 Si es "Alta"

#                     Agregar la tarea
#                     a la lista resultado


#             Retornar las tareas prioritarias


#         Método eliminar_completada(descripcion)

#             Recibir la descripción
#             de la tarea a eliminar


#             Recorrer las tareas


#                 Comprobar si la descripción
#                 coincide con la descripción recibida


#                 Si coincide

#                     Eliminar la tarea de la lista

#                     Detener el recorrido


#     Crear objeto Tareas


#     Agregar tareas

#         Estudiar → Alta

#         Practicar → Alta

#         Repasar → Baja


#     Buscar tareas prioritarias


#     Mostrar tareas prioritarias


#     Eliminar la tarea "Estudiar"


#     Mostrar la lista de tareas actualizada

# FIN

class Tareas:
    def __init__(self):
        self.prioridades=[]
    
    def  agregar_tarea(self, descripcion, prioridad):
        
        tarea=(descripcion, prioridad)
        self.prioridades.append(tarea)
    
    def  tareas_prioritarias(self):
        resultado=[]
        
        for i in self.prioridades:
            if i[1]== "Alta":
                resultado.append(i)
        return resultado
    
    def  eliminar_completada(self,descripcion):
        
        for c in self.prioridades:
            if c[0] == descripcion:
                self.prioridades.remove(c)
                break

tr= Tareas()

tr.agregar_tarea("Estudiar", "Alta")
tr.agregar_tarea("Practicar", "Alta")
tr.agregar_tarea("Repasar", "Baja")

print(f"las tareas prioritarias son: {tr.tareas_prioritarias()}")

tr.eliminar_completada("Estudiar")

print(f"Tareas actualizadas: {tr.prioridades}")