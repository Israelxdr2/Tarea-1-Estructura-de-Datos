# ENTRADA:
# - Dos puntos representados como tuplas (x, y).
# - Varios puntos para buscar el más cercano.

# PROCESO:
# 1. Crear la clase CalculadorDistancia.
# 2. Crear una lista para guardar las distancias.
# 3. Crear distancia_euclidiana().
# 4. Obtener x e y de cada punto.
# 5. Aplicar la fórmula de distancia.
# 6. Guardar la distancia calculada.
# 7. Crear punto_mas_cercano().
# 8. Calcular la distancia de cada punto respecto a la referencia.
# 9. Comparar las distancias.
# 10. Retornar el punto con menor distancia.

# SALIDA:
# - Distancia.
# - Punto más cercano.



#BOSQUEJO:
# INICIO

#     Crear clase CalculadorDistancia

#         Crear lista distancias

#         Método distancia_euclidiana(p1, p2)

#             Obtener coordenada x del primer punto

#             Obtener coordenada y del primer punto

#             Obtener coordenada x del segundo punto

#             Obtener coordenada y del segundo punto

#             Calcular diferencia entre las coordenadas x

#             Calcular diferencia entre las coordenadas y

#             Elevar ambas diferencias al cuadrado

#             Sumar los resultados

#             Obtener la raíz cuadrada

#             Guardar la distancia en la lista

#             Retornar la distancia

#         Método punto_mas_cercano(referencia, *puntos)

#             Crear variable para guardar
#             el punto más cercano

#             Crear variable para guardar
#             la distancia menor

#             Recorrer todos los puntos

#                 Calcular la distancia entre
#                 la referencia y el punto actual

#                 Si todavía no existe una distancia menor
#                 o la distancia actual es menor

#                     Guardar la distancia actual

#                     Guardar el punto actual

#             Retornar el punto más cercano

#     Crear objeto CalculadorDistancia

#     Calcular la distancia entre dos puntos

#     Mostrar la distancia

#     Buscar el punto más cercano a una referencia

#     Mostrar el punto más cercano

# FIN

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]

        x2 = p2[0]
        y2 = p2[1]

        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        distancia_menor = None

        for c in puntos:
            distancia = self.distancia_euclidiana(referencia, c)

            if distancia_menor is None or distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = c

        return punto_cercano


cd = CalculadorDistancia()

print(cd.distancia_euclidiana((0, 0), (3, 4)))

print(cd.punto_mas_cercano((0, 0),(3, 4),(1, 1),(5, 5)))