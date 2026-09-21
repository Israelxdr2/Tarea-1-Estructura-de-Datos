#EJERCICIO 13:
# Crea una clase llamada CombinadorNombres que:

# Tenga un método intercalar(lista1, lista2) que reciba dos listas de nombres y retorne una nueva lista alternando los elementos de ambas listas.
# Tenga un método intercalar_multiples(*listas) que permita combinar varias listas reutilizando el método intercalar().

#BOSQUEJO:

# INICIO

#  Crear clase CombinadorNombres

#     Método intercalar(lista1, lista2)

#         Crear lista resultado vacía

#         Recorrer los elementos usando índices

#             Agregar elemento de lista1
#             Agregar elemento de lista2

#         Retornar lista resultado


#     Método intercalar_multiples(*listas)

#         Tomar la primera lista como resultado

#         Recorrer las demás listas

#             Utilizar el método intercalar()
#             Actualizar resultado

#         Retornar resultado


#  Crear objeto CombinadorNombres

#  Crear dos listas de nombres

#  Utilizar intercalar()

#  Mostrar resultado

# FIN

class CombinadorNombres:
    def intercalar(self,lista1, lista2):
        lista=[]
        
        for i in range(len(lista1)):
            lista.append(lista1[i])
            lista.append(lista2[i])
        return lista
    def intercalar_multiples(self,*listas):
        
        resultado=[]
        
        for i in range(len(listas[0])):
            for c in listas:
                resultado.append(c[i])
            
        return resultado
cn = CombinadorNombres()

lista1 = ["Ana", "Luis"]
lista2 = ["Pedro", "Sofia"]

print(cn.intercalar(lista1, lista2))

print(cn.intercalar_multiples(["Ana", "Luis"],["Pedro", "Sofia"],["Carlos", "Maria"]))




