#EJERCICIO 4: INVERSOR DE SECUENCIA 

# ENTRADA: # - Una lista de elementos. 
# # PROCESO: # 1. Crear una clase llamada InversorSecuencia.
# # 2. Crear un método invertir(). 
# # 3. Crear una lista vacía para guardar el resultado.
# # 4. Recorrer la lista desde el último elemento hasta el primero. 
# # 5. Agregar cada elemento a la nueva lista. 
# # 6. Devolver la lista invertida. 
# # 7. Crear un método invertir_multiples(*listas). 
# 8. Recorrer las listas recibidas.
# # 9. Utilizar el método invertir() para cada lista.
# # 10. Guardar los resultados. # 

# # SALIDA: 
# # - Lista invertida.
# # - Varias listas invertidas.


#BOSQUEJO:
# INICIO

#     Crear clase InversorSecuencia


#         Método invertir_lista(lista)

#             Crear lista vacía llamada resultado


#             Recorrer la lista desde el último elemento
#             hasta el primer elemento


#                 Obtener el elemento de la posición actual


#                 Agregar el elemento a resultado


#             Retornar la lista resultado


#         Método invertir_multiples(*listas)

#             Crear diccionario vacío


#             Recibir varias listas

#             Recorrer cada lista


#                 Invertir la lista
#                 utilizando invertir_lista()


#                 Convertir la lista original
#                 en una tupla


#                 Convertir la lista invertida
#                 en una tupla


#                 Guardar en el diccionario

#                     Tupla original → tupla invertida


#             Retornar el diccionario


#     Crear objeto InversorSecuencia


#     Invertir una lista

#         [1, 2, 3, 4]

#         Resultado:

#         [4, 3, 2, 1]


#     Invertir varias listas

#         [1, 2, 3, 4]

#         [2, 3, 4]


#     Guardar las listas originales e invertidas
#     como claves y valores del diccionario


#     Mostrar el resultado

# FIN


class InversorSecuencia:
   
        
    def  invertir_lista(self, lista):
        resultado=[]
        
        for i in range(len(lista) -1, -1, -1):
            resultado.append(lista[i])
        
        return resultado
    
    def invertir_multiples(self, *listas):
        
        dic={}
        
        for c in listas:
            
            Invertido = self.invertir_lista(c)
            dic[tuple(c)]= tuple(Invertido)
        
        return dic
            
Is= InversorSecuencia()


print(f"lista invertida: {Is.invertir_lista([1,2,3,4])}")
print(f"Diccionario Multiple: {Is.invertir_multiples([1, 2, 3, 4], [2, 3, 4])}")