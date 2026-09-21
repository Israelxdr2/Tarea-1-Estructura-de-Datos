# ENTRADA:
# - Nombres de equipos.
# - Nombres de jugadores.

# PROCESO:
# 1. Crear la clase Equipos.
# 2. Crear un diccionario para guardar los equipos.
# 3. Crear cada equipo con una lista vacía.
# 4. Agregar jugadores a la lista correspondiente.
# 5. Contar los jugadores de cada equipo.
# 6. Comparar las cantidades.
# 7. Retornar el equipo con más jugadores.

# SALIDA:
# - Nombre del equipo con mayor cantidad de jugadores.

#BOSQUEJO:
# INICIO

#     Crear clase Equipos

#         Crear diccionario equipos


#         Método crear_equipo(nombre_equipo)

#             Recibir nombre del equipo

#             Crear una lista vacía

#             Guardar el equipo en el diccionario
#             junto con la lista vacía


#         Método agregar_jugador(equipo, jugador)

#             Recibir nombre del equipo
#             y nombre del jugador

#             Buscar el equipo en el diccionario

#             Agregar jugador
#             a la lista del equipo


#         Método equipo_mayor_integrantes()

#             Crear variable mayor = 0

#             Crear variable equipo_Mayor = ""
#             para guardar el nombre del equipo


#             Recorrer los equipos

#                 Obtener la cantidad
#                 de jugadores


#                 Comparar la cantidad de jugadores
#                 con la cantidad mayor


#                 Si la cantidad es mayor

#                     Actualizar la cantidad mayor

#                     Guardar el nombre del equipo


#             Retornar el nombre del equipo
#             con más integrantes


#     Crear objeto Equipos

#     Crear equipos

#         Rojo

#         Azul


#     Agregar jugadores

#         Rojo → Karla

#         Rojo → Sam

#         Azul → Alex


#     Buscar el equipo
#     con mayor cantidad de integrantes


#     Mostrar el equipo con más integrantes

# FIN

class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []
    
    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)
        
    def equipo_mayor_integrantes(self):
        mayor=0
        equipo_Mayor=""
        
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor:
                mayor= len(jugadores)
                equipo_Mayor= equipo
            
        return equipo_Mayor
    
Eq= Equipos()

Eq.crear_equipo("Rojo")
Eq.crear_equipo("Azul")

Eq.agregar_jugador("Rojo", "Karla")
Eq.agregar_jugador("Rojo", "Sam")
Eq.agregar_jugador("Azul", "Alex")

print(f"El equipo mayor es: {Eq.equipo_mayor_integrantes()}")


            
        