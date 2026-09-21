#EJERICICIO 1:
#Desarrolle una clase llamada ControlEdades que permita registrar y validar varias edades.

#La clase deberá:

#Crear una lista para almacenar las edades válidas.
#Tener un método validar_edad(edad) que compruebe si la edad está dentro del rango permitido de 0 a 120 años.
#Tener un método cargar_edades(*args) que reciba varias edades.
#Validar cada edad utilizando el método validar_edad().
#Guardar únicamente las edades válidas en la lista.
#Tener un método promedio() que calcule el promedio de las edades válidas.

#BOSQUEJO
#INICIO

   # Crear clase ControlEdades

      #  Crear lista edades

       # Método validar_edad(edad)
       #     Si edad está entre 0 y 120
        #        Retornar verdadero
        #    Si no
         #       Retornar falso
       # Método cargar_edades(*args)
        #    Recorrer las edades recibidas
        #        Validar cada edad
        #        Si es válida
         #           Guardarla en la lista
          #  Retornar lista de edades válidas
      #  Método promedio()
       #     Crear variable suma = 0
         #   Recorrer las edades
         #       Sumar cada edad
         #   Calcular promedio
         #   Retornar promedio

   # Crear objeto ControlEdades
   # Cargar varias edades
    #Mostrar edades válidas
    #Mostrar promedio
#FIN

#CODIGO

class ControlEdades:
    def __init__(self):
        self.edades=[]
    def validar_edad(self, edad):
        if edad > 0 and edad < 120:
            return True
        else:
            return False
    def cargar_Edades(self,*args):
        for i in args:
            if self.validar_edad(i):
                self.edades.append(i)
           
        return self.edades
    
    def promedio(self):
        suma=0 
        for c in self.edades:
            suma += c 
        
        return suma/len(self.edades)
ce= ControlEdades()
print(f"{ce.cargar_Edades(1,45,32,52,22,18,150,-3)}")
print(f"{ce.promedio()}")