# ENTRADA:
# - Pares de números (inicio, fin).

# PROCESO:
# 1. Crear la clase SelectorRango.
# 2. Crear crear_rango(inicio, fin).
# 3. Recorrer los números desde inicio hasta fin.
# 4. Guardarlos en una tupla.
# 5. Recibir varios rangos mediante *args.
# 6. Utilizar un conjunto para evitar números repetidos.
# 7. Convertir el conjunto en una lista.

# SALIDA:
# - Lista de números sin duplicados.



#BOSQUEJO:
# INICIO

#     Crear clase SelectorRange


#         Método crear_rango(inicio, fin)

#             Crear lista vacía


#             Recorrer los números
#             desde inicio hasta fin


#                 Agregar cada número
#                 a la lista


#             Convertir la lista
#             en una tupla


#             Retornar la tupla


#         Método elementos_en_multiples_rangos(*rango)

#             Crear conjunto vacío
#             para guardar los resultados
#             sin elementos repetidos


#             Recibir varios rangos


#             Recorrer cada rango


#                 Obtener el inicio del rango

#                 Obtener el final del rango


#                 Crear el rango
#                 utilizando crear_rango()


#                 Recorrer los números
#                 del rango creado


#                     Agregar cada número
#                     al conjunto


#             Convertir el conjunto
#             en una lista


#             Retornar la lista


#     Crear objeto SelectorRange


#     Crear un rango

#         Inicio → 1

#         Fin → 5


#     Mostrar el rango


#     Crear varios rangos

#         (1, 3)

#         (2, 4)


#     Combinar los elementos
#     de los rangos


#     Eliminar elementos repetidos


#     Mostrar los elementos combinados

# FIN

class SelectorRange:
      
    def crear_rango(self,inicio,fin):
        resultado=[]
        
        for i in (range(inicio,fin +1)):
            resultado.append(i)
        
        return tuple(resultado)
        
        
    def elementos_en_multiples_rangos(self,*rango):
        resultado_rangos= set()
        
        for c in rango:
            inicio=c[0]
            fin=c[1]
            
            num_rangos=self.crear_rango(inicio, fin)
            
            for numero in num_rangos:
                resultado_rangos.add(numero)
                
        return list(resultado_rangos)
                
sr= SelectorRange()

print(f"el rango es: {sr.crear_rango(1,5)}")

print(f"Elementos combinados sin duplicacion:{sr.elementos_en_multiples_rangos((1,3),(2,4))}")           