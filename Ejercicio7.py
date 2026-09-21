# ENTRADA:
# - Nombres y edades.

# PROCESO:
# 1. Crear la clase GestorPersonas.
# 2. Crear un diccionario para guardar nombre y edad.
# 3. Crear agregar_persona(nombre, edad).
# 4. Crear personas_mayores(edad_minima).
# 5. Recorrer el diccionario para buscar las personas mayores.
# 6. Crear edad_promedio() para calcular el promedio.

# SALIDA:
# - Lista de personas que cumplen la edad mínima.
# - Promedio de edades.

#BOSQUEJO:
# INICIO

#     Crear clase GestorPersonas

#         Crear diccionario personas


#         Método agregar_persona(nombre, edad)

#             Recibir nombre y edad de la persona

#             Guardar nombre y edad
#             en el diccionario


#         Método personas_mayores(edad_minima)

#             Crear lista vacía para guardar
#             las personas que cumplen la edad mínima


#             Recorrer las personas del diccionario

#                 Obtener nombre y edad


#                 Comparar la edad con la edad mínima


#                 Si la edad es mayor o igual
#                 a la edad mínima

#                     Agregar nombre
#                     a la lista resultado


#             Retornar la lista de personas


#         Método edad_promedio()

#             Crear variable suma = 0

#             Recorrer las edades de las personas

#                 Sumar cada edad


#             Dividir la suma
#             para la cantidad de personas

#             Retornar el promedio


#     Crear objeto GestorPersonas

#     Agregar personas

#         Ismael → 77

#         Israel → 20

#         Samuel → 45


#     Buscar personas con edad
#     mayor o igual a 25


#     Mostrar las personas encontradas


#     Calcular la edad promedio

#     Mostrar la edad promedio

# FIN


class GestorPersonas:
    def __init__(self):
        self.personas = {}
    
    def agregar_persona(self,nombre, edad):
        self.personas[nombre]=edad
    
    def personas_mayores(self, edad_minima):
        resultado=[]
        
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        
        return resultado

    def edad_promedio(self):
        suma=0
        for i in self.personas.values():
            suma += i
        return suma/len(self.personas)
    
gp= GestorPersonas()

gp.agregar_persona("ismael",77)
gp.agregar_persona("israel",20)
gp.agregar_persona("Samuel",45)

print(f"personas mayores {gp.personas_mayores(25)}")

print(f"la edad promedio es{gp.edad_promedio()}")