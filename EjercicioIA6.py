#EJERCICIO 6:
#Desarrolle una clase llamada GestorCalificaciones que permita registrar calificaciones de estudiantes y obtener diferentes estadísticas.
# La clase deberá:
# Tener un método registrar_calificacion(nota) que guarde la calificación en una lista.
# Tener un método minima() que retorne la calificación más baja registrada.
# Tener un método maxima() que retorne la calificación más alta registrada.
# Tener un método promedio() que calcule y retorne el promedio de las calificaciones.
# Tener un método registrar_multiples(*notas) que permita registrar varias calificaciones y reutilice el método registrar_calificacion().

#BOSQUEJO:

#INICIO

#    Crear clase GestorCalificaciones

#        Crear lista calificaciones


#        Método registrar_calificacion(nota)

#           Guardar nota en la lista


#        Método minima()
#            Buscar la calificación mínima
#            Retornar mínima


#        Método maxima()
#            Buscar la calificación máxima
#            Retornar máxima

#        Método promedio()
#            Crear variable suma = 0
#            Recorrer las calificaciones
#              Sumar cada calificación

#            Calcular promedio
#            Retornar promedio
#        Método registrar_multiples(*notas)
#            Recorrer las notas recibidas
#                Utilizar registrar_calificacion()
#               para guardar cada nota

#    Crear objeto GestorCalificaciones

#    Registrar varias calificaciones

#    Mostrar calificación mínima

#    Mostrar calificación máxima

#    Mostrar promedio

#FIN

class GestorCalificaciones:

    def __init__(self):

        self.calificaciones= []

        

    def registrar_calificacion(self, nota):
        self.calificaciones.append(nota)

    def minima(self):
        return min(self.calificaciones)

    def maxima(self):
        return max(self.calificaciones)

    def promedio(self):
        suma=0
        for i in self.calificaciones:
            suma+= i
        return suma/len(self.calificaciones)

            

    def registrar_multiples(self, *notas):
        for c in notas:
            self.registrar_calificacion(c)



gc= GestorCalificaciones()

gc.registrar_multiples(10, 34, 54, 67)



print(f"El minimo es: {gc.minima()}")

print(f"El maximo es: {gc.maxima()}")

print(f"El promedio es: {gc.promedio()}")    