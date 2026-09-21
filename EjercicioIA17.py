#EJERCICIO 17:
# Crea una clase llamada AgrupadorTemperaturas que:

# Tenga un método clasificar_temperatura(temp) que retorne una categoría según la temperatura:
# Menor de 15 → "fria"
# De 15 a 24 → "templada"
# De 25 a 34 → "calida"
# 35 o más → "caliente"
# Tenga un método agrupar_por_categoria(*temperaturas) que reciba varias temperaturas y retorne un diccionario donde cada categoría tenga una lista con las temperaturas correspondientes.
# # Tenga un método temperatura_promedio_categoria(categoria) que calcule el promedio de las temperaturas pertenecientes a una categoría.

#BOSQUEJO:

# INICIO

#  Crear clase AgrupadorTemperaturas

#     Crear diccionario para almacenar las categorías

#     Método clasificar_temperatura(temp)

#         Si temp < 15
#             Retornar "fria"

#         Si temp está entre 15 y 24
#             Retornar "templada"

#         Si temp está entre 25 y 34
#             Retornar "calida"

#         Si temp >= 35
#             Retornar "caliente"


#     Método agrupar_por_categoria(*temperaturas)

#         Crear diccionario con las categorías
#         Crear una lista vacía para cada categoría

#         Recorrer las temperaturas

#             Utilizar clasificar_temperatura()

#             Obtener categoría

#             Agregar temperatura a la lista
#             de esa categoría

#         Retornar diccionario


#     Método temperatura_promedio_categoria(categoria)

#         Obtener lista de temperaturas
#         de la categoría

#         Sumar las temperaturas

#         Dividir para la cantidad de temperaturas

#         Retornar promedio


#  Crear objeto AgrupadorTemperaturas

#  Agrupar varias temperaturas

#  Mostrar diccionario agrupado

#  Calcular promedio de una categoría

#  Mostrar promedio

# FIN

class AgrupadorTemperaturas:
    def __init__(self):
        self.agrupar={}
    def clasificar_temperatura(self,temp):
        
        if temp < 15:
            return "fria"
        elif temp <= 24:
            return "templada"
        elif temp <35:
            return "calida"
        else:
            return "caliente"
            
            
    def agrupar_por_categoria(self, *temperaturas):
        self.agrupar={}
        
        for i in temperaturas:
            categoria=self.clasificar_temperatura(i)
            
            if categoria not in self.agrupar:
               self.agrupar[categoria]=[]
               
            self.agrupar[categoria].append(i)
    
        return self.agrupar 
        
    def temperatura_promedio_categoria(self,categoria):
        promedio=self.agrupar[categoria]
        suma=0
        
        for i in promedio:
            suma += i
            
        return suma/len(promedio)
        
at = AgrupadorTemperaturas()

print(at.agrupar_por_categoria(10, 20, 28, 38))
print(at.temperatura_promedio_categoria("calida"))