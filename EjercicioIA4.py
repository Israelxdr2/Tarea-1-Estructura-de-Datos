#EJERCICIO 4:
#Desarrolle una clase llamada BuscadorNumeros que permita trabajar con listas de números y buscar aquellos que cumplan una condición determinada.

#La clase deberá:

#Tener un método buscar_mayores(lista, limite) que retorne una lista con los números que sean mayores que el límite indicado.
#Tener un método buscar_multiples(*listas) que reciba varias listas y utilice el método buscar_mayores() para procesarlas.
#El método buscar_multiples() deberá retornar un diccionario, donde cada lista original se relacione con su lista de números mayores.
#Para utilizar las listas como claves del diccionario, deberán convertirse en tuplas.

##INICIO

#    Crear clase BuscadorNumeros
#        Método buscar_mayores(lista, limite)
#            Crear lista vacía

#            Recorrer la lista
 #               Si el número es mayor que el límite
#                    Agregar número a la lista

 #           Retornar lista

 #       Método buscar_multiples(*listas)

#           Crear diccionario vacío

#          Recorrer las listas recibidas

#              Convertir la lista en tupla

 #              Utilizar buscar_mayores()
                
 #               Guardar:
 #                  tupla → resultado

 #           Retornar diccionario

 #   Crear objeto BuscadorNumeros

 #   Probar buscar_mayores()

 #   Probar buscar_multiples()

  #  Mostrar resultados

#FIN

class BuscadorNumeros:

    def buscar_mayores(self, lista, limite):
        resultado=[]
        
        for i in lista:
            if i > limite:
                resultado.append(i)
        return resultado
    
    def buscar_multiples(self,limite, *listas):
        dic={}
        for i in listas:
            buscador= self.buscar_mayores(i,limite)
            dic[tuple(i)]= tuple(buscador)
        return dic

bn = BuscadorNumeros()

print("Mayores a 5:", bn.buscar_mayores([2, 8, 5, 10, 3], 5))


resultado_multiples = bn.buscar_multiples(5, [2, 8, 5, 10, 3], [1, 6, 7, 4])

print(f"Diccionario de múltiples listas:{resultado_multiples}")