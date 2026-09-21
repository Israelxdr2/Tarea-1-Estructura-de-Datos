#EJERCICIO 15:
# Crea una clase llamada AnalizadorMultiplos que:

# Tenga un método encontrar_multiplos(numero, limite) que retorne una tupla con todos los números que son múltiplos de numero hasta llegar al límite indicado.
# Tenga un método es_multiplo(numero, valor) que retorne True si valor es múltiplo de numero, y False en caso contrario.
# Tenga un método encontrar_multiples_numeros(*numeros) que reciba varios números y retorne un diccionario con el número y sus múltiplos.

#BOSQUEJO:

# INICIO

#  Crear clase AnalizadorMultiplos

#     Método encontrar_multiplos(numero, limite)

#         Crear lista vacía

#         Recorrer números desde 1 hasta el límite

#             Si el número actual es múltiplo de numero
#                 Agregarlo a la lista

#         Convertir la lista en tupla

#         Retornar tupla


#     Método es_multiplo(numero, valor)

#         Si valor % numero == 0
#             Retornar True
#         Si no
#             Retornar False


#     Método encontrar_multiples_numeros(*numeros)

#         Crear diccionario vacío

#         Recorrer los números recibidos

#             Obtener los múltiplos utilizando
#             encontrar_multiplos()

#             Guardar:
#                 número → tupla de múltiplos

#         Retornar diccionario


#  Crear objeto AnalizadorMultiplos

#  Probar encontrar_multiplos()

#  Probar es_multiplo()

#  Probar encontrar_multiples_numeros()

#  Mostrar resultados

# FIN


class AnalizadorMultiplos:
    def encontrar_multiplos(self,numero, limite):
       lista=[]
       for i in range(1, limite +1):
           resultado = numero * i
           lista.append(resultado)
       return lista

    
    def es_multiplo(self, numero, valor):
        
        if valor % numero==0:
            return True
        else:
            return False
    def encontrar_multiples_numeros(self, *numeros):
        resultado={}
        for i in numeros:
            resultado[i]= self.encontrar_multiplos(i,limite=10)
        return resultado
        
am = AnalizadorMultiplos()

print(am.encontrar_multiplos(3, 10))

print(am.es_multiplo(3, 9))

print(am.encontrar_multiples_numeros(2, 3, 5))