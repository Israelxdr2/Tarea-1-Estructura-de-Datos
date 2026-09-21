# ENTRADA:
# - Temperaturas individuales o varias temperaturas.

# PROCESO:
# 1. Crear la clase GestorTemperatura.
# 2. Crear una lista para guardar las temperaturas.
# 3. Crear registrar_temperatura(temp) para guardar una temperatura.
# 4. Crear minima() para obtener la temperatura menor.
# 5. Crear maxima() para obtener la temperatura mayor.
# 6. Crear promedio() para calcular el promedio.
# 7. Crear registrar_multiples(*temps) para registrar varias temperaturas.

# SALIDA:
# - Temperatura mínima.
# - Temperatura máxima.
# - Promedio.

#BOSQUEJO:
# INICIO

#     Crear clase GestorTemperatura

#         Crear constructor __init__()

#             Crear lista vacía para guardar
#             las temperaturas


#         Método registrar_temperatura(temp)

#             Recibir una temperatura

#             Agregar la temperatura
#             a la lista


#         Método minimo()

#             Buscar la temperatura más pequeña
#             de la lista

#             Retornar la temperatura mínima


#         Método maximo()

#             Buscar la temperatura más grande
#             de la lista

#             Retornar la temperatura máxima


#         Método promedio()

#             Crear variable suma = 0

#             Recorrer las temperaturas

#                 Sumar cada temperatura


#             Dividir la suma
#             para la cantidad de temperaturas

#             Retornar el promedio


#         Método registrar_multiples(*temps)

#             Recibir varias temperaturas

#             Recorrer cada temperatura

#                 Llamar al método
#                 registrar_temperatura()


#                 Agregar la temperatura
#                 a la lista


#     Crear objeto GestorTemperatura

#     Registrar varias temperaturas

#         10, 34, 54, 67


#     Buscar temperatura mínima

#     Buscar temperatura máxima

#     Calcular promedio


#     Mostrar temperatura mínima

#     Mostrar temperatura máxima

#     Mostrar promedio

# FIN

class  GestorTemperatura:
    def __init__(self):
        self.temperaturas = []
        
    def registrar_temperatura(self, temp):
        
        self.temperaturas.append(temp)
        
    def minimo(self):
        return min(self.temperaturas)
    
    def maximo (self):
        return max(self.temperaturas)
    
    def promedio(self):
        suma=0
        for i in self.temperaturas:
            suma+= i
        return suma/len(self.temperaturas)
    def registrar_multiples(self, *temps):
        for c in temps:
            self.registrar_temperatura(c)

gt= GestorTemperatura()

gt.registrar_multiples(10, 34, 54, 67)

print(f"El minimo es: {gt.minimo()}")
print(f"El maximo es: {gt.maximo()}")
print(f"El promedio es: {gt.promedio()}")
             