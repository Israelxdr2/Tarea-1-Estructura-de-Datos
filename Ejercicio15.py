# ENTRADA:
# - Uno o varios números.

# PROCESO:
# 1. Crear la clase DivisorFinder.
# 2. Crear encontrar_divisores(numero).
# 3. Recorrer números desde 1 hasta el número.
# 4. Comprobar cuáles dividen exactamente al número.
# 5. Guardar los divisores en una lista.
# 6. Convertir la lista en una tupla.
# 7. Crear es_perfecto(numero).
# 8. Sumar los divisores excepto el mismo número.
# 9. Comparar la suma con el número.
# 10. Crear encontrar_multiples_divisores(*numeros).

# SALIDA:
# - Tupla de divisores.
# - True o False.
# - Diccionario de números y sus divisores.

#BOSQUEJO:
# INICIO

#     Crear clase DivisorFinder


#         Método encontrar_divisores(numero)

#             Crear lista vacía para guardar
#             los divisores


#             Recorrer los números
#             desde 1 hasta el número


#                 Comprobar si el número
#                 es divisible por el valor actual


#                 Si el residuo es igual a 0

#                     Agregar el valor
#                     a la lista de divisores


#             Convertir la lista
#             en una tupla


#             Retornar la tupla


#         Método es_perfecto(numero)

#             Encontrar los divisores
#             del número


#             Crear variable suma = 0


#             Recorrer los divisores


#                 Comprobar que el divisor
#                 no sea el número original


#                 Si no es el número original

#                     Sumar el divisor


#             Comparar la suma
#             con el número original


#             Si la suma es igual al número

#                 Retornar verdadero


#             Si no

#                 Retornar falso


#         Método encontrar_multiples_divisores(*numeros)

#             Crear diccionario vacío


#             Recibir varios números


#             Recorrer cada número


#                 Encontrar sus divisores


#                 Guardar el número como clave

#                 Guardar sus divisores como valor


#             Retornar el diccionario


#     Crear objeto DivisorFinder


#     Encontrar divisores de 12

#     Mostrar los divisores


#     Comprobar si 6 es un número perfecto

#     Mostrar el resultado


#     Encontrar divisores de varios números

#         15

#         6

#         10


#     Mostrar el diccionario de resultados

# FIN

class DivisorFinder:
  
    def encontrar_divisores(self,numero):
        lista=[]
        for i in range(1,numero +1):
            if numero %i==0:
                lista.append(i)
        return tuple(lista)
    def  es_perfecto(self, numero):
        div= self.encontrar_divisores(numero)
        suma=0
        
        for c in div:
            if c != numero:
                suma+= c
        
        if suma == numero:
            return True
        else:
            return False
    def  encontrar_multiples_divisores(self,*numeros):
        resultado={}
        
        for i in numeros:
            resultado[i]= self.encontrar_divisores(i)
            
        return resultado
        
Df=DivisorFinder()
print(f"{Df.encontrar_divisores(12)}")
print(f"{Df.es_perfecto(6)}")       
print(f"{Df.encontrar_multiples_divisores(15,6,10)}")        