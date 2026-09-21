#EJERCICIO 18:

# Crea una clase llamada CalculadorTiempo que:

# Tenga un método calcular_tiempo(distancia, velocidad) que reciba la distancia y la velocidad, y calcule el tiempo de viaje usando la fórmula:
# tiempo = distancia / velocidad
# Tenga un método viaje_mas_corto(referencia, *viajes) que reciba varios viajes representados como tuplas (distancia, velocidad) y retorne el viaje que tenga menor tiempo.
# Tenga un atributo tiempos que sea una lista donde se guarden todos los tiempos calculados.

#BOSQUEJO:
# INICIO

#  Crear clase CalculadorTiempo

#     Crear lista tiempos


#     Método calcular_tiempo(distancia, velocidad)

#         Calcular tiempo
#         tiempo = distancia / velocidad

#         Guardar tiempo en la lista

#         Retornar tiempo


#     Método viaje_mas_corto(referencia, *viajes)

#         Crear variable para guardar
#         el viaje con menor tiempo

#         Crear variable para guardar
#         el menor tiempo

#         Recorrer los viajes

#             Obtener distancia y velocidad

#             Calcular tiempo utilizando
#             calcular_tiempo()

#             Comparar con el menor tiempo

#             Si es menor
#                 Actualizar viaje
#                 Actualizar menor tiempo

#         Retornar viaje más corto


#  Crear objeto CalculadorTiempo

#  Calcular el tiempo de un viaje

#  Crear varios viajes

#  Buscar el viaje más corto

#  Mostrar resultados

#  Mostrar lista de tiempos

# FIN

class CalculadorTiempo:

    def __init__(self):
        self.tiempos = []

 
    def calcular_tiempo(self, distancia, velocidad):
        tiempo = distancia / velocidad
        self.tiempos.append(tiempo)
        return tiempo


    def viaje_mas_corto(self, referencia, *viajes):
        menor_tiempo = None
        viaje_corto = None

        for viaje in viajes:
            distancia, velocidad = viaje

            tiempo = self.calcular_tiempo(distancia, velocidad)

            if menor_tiempo is None or tiempo < menor_tiempo:
                menor_tiempo = tiempo
                viaje_corto = viaje

        return viaje_corto


ct = CalculadorTiempo()

print(ct.calcular_tiempo(100, 50))

print(ct.viaje_mas_corto( None, (100, 50), (120, 60),(200, 80)))

print(ct.tiempos)