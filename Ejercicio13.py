# ENTRADA:
# - Dos o más listas.

# PROCESO:
# 1. Crear la clase CombinadorListas.
# 2. Crear intercalar(lista1, lista2).
# 3. Recorrer las posiciones de las listas.
# 4. Agregar un elemento de la primera lista.
# 5. Agregar un elemento de la segunda lista.
# 6. Crear intercalar_multiples(*listas).
# 7. Reutilizar intercalar() para combinar varias listas.

# SALIDA:
# - Lista con los elementos intercalados.


#BOSQUEJO:
# INICIO

#     Crear clase CombinadorListas


#         Método intercalar(lista1, lista2)

#             Crear lista vacía para guardar
#             el resultado


#             Recorrer las posiciones
#             de la primera lista


#                 Agregar elemento de lista1
#                 a la lista resultado


#                 Agregar elemento de lista2
#                 a la lista resultado


#             Retornar la lista resultado


#         Método intercalar_multiples(*listas)

#             Crear lista vacía para guardar
#             el resultado


#             Recibir varias listas


#             Recorrer las posiciones
#             de las listas


#                 Recorrer cada lista


#                     Obtener el elemento
#                     de la posición actual


#                     Agregar el elemento
#                     a la lista resultado


#             Retornar la lista resultado


#     Crear objeto CombinadorListas


#     Intercalar dos listas

#         [1, 2]

#         [3, 4]


#     Combinar varias listas

#         [1, 2]

#         [3, 4]

#         [5, 6]


#     Recorrer primero la posición 0
#     de todas las listas


#         1 → 3 → 5


#     Recorrer después la posición 1
#     de todas las listas


#         2 → 4 → 6


#     Mostrar la lista intercalada

# FIN

class CombinadorListas:
    def  intercalar(self,lista1, lista2):
        lista=[]
        
        for i in range(len(lista1)):
            lista.append(lista1[i])
            lista.append(lista2[i])
        
        return lista
    
    def intercalar_multiples(self, *listas):
        resultado=[]
        
        for c in range(len(listas[0])):
            for num in listas:
                resultado.append(num[c])
        
        return resultado
    
cl= CombinadorListas()

cl.intercalar([1, 2], [3, 4])

print(f"El intercalado queda asi: {cl.intercalar_multiples([1, 2],[3, 4],[5, 6])}")