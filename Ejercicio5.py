# EJERCICIO 5: ANALIZADOR DE NÚMEROS 

# ENTRADA: 
# - Varios números. 
# # PROCESO: 
# 1. Crear una clase llamada AnalizadorNumeros.
# 2. Crear un método es_par().
# 3. Comprobar si un número es divisible entre 2.
# 4. Crear un método separar(*numeros). 
# 5. Crear un diccionario con pares e impares.
# 6. Recorrer todos los números recibidos. 
# 7. Utilizar es_par() para clasificarlos. 
# 8. Guardar cada número en su grupo correspondiente.
# 9. Crear un método cantidad_pares_impares(). 
# 10. Contar los elementos de cada grupo.
# 11. Devolver las cantidades como una tupla. 

# # # SALIDA: 
# # - Diccionario con números pares e impares. # - Cantidad de pares e impares.


#BOSQUEJO:
# INICIO

#     Crear clase AnalizadorNumeros

#         Crear constructor __init__()

#             Crear lista vacía para guardar
#             los números pares

#             Crear lista vacía para guardar
#             los números impares


#         Método es_par(numero)

#             Recibir un número

#             Comprobar si el número es divisible
#             entre 2

#             Si el residuo es igual a 0

#                 Retornar verdadero

#             Si no

#                 Retornar falso


#         Método separar(*numeros)

#             Vaciar la lista de pares

#             Vaciar la lista de impares


#             Recibir varios números

#             Recorrer cada número


#                 Comprobar si el número es par


#                 Si es par

#                     Agregar el número
#                     a la lista de pares


#                 Si no

#                     Agregar el número
#                     a la lista de impares


#             Crear un diccionario con:

#                 Pares → lista de pares

#                 Impares → lista de impares


#             Retornar el diccionario


#         Método cantidad_pares_impares()

#             Obtener la cantidad de números pares

#             Obtener la cantidad de números impares

#             Retornar ambas cantidades


#     Crear objeto AnalizadorNumeros

#     Separar los números

#         1, 2, 3, 4, 5


#     Guardar los números pares

#         2, 4


#     Guardar los números impares

#         1, 3, 5


#     Mostrar pares e impares

#     Contar cantidad de pares e impares

#     Mostrar las cantidades

# FIN

class AnalizadorNumeros:
    
    def __init__(self):
        
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        
          if numero %2==0 :
                    return True
                
          else: 
                    return False
        
    def separar(self, *numeros):
      
        self.pares = []
        self.impares = []
        
        for num in numeros:
            
            if self.es_par(num):
                self.pares.append(num)
            else:
                self.impares.append(num)
                
        
        return {'pares': self.pares, 'impares': self.impares}
         
    def cantidad_pares_impares(self):
       
        cant_pares = len(self.pares)
        cant_impares = len(self.impares)
        return (cant_pares, cant_impares)
        

an = AnalizadorNumeros()

print(f"Separar {an.separar(1, 2, 3, 4, 5)}")
print(f"Cantidades (pares, impares): {an.cantidad_pares_impares()}")