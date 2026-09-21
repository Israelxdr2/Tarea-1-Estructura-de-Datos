#EJERCICIO 12:
# Crea una clase llamada SelectorEdades que:

# Tenga un método crear_rango(inicio, fin) que retorne una tupla con los números de edad comprendidos entre inicio y fin.
# Tenga un método edades_en_multiples_rangos(*rangos) que reciba varios rangos como tuplas (inicio, fin) y retorne una lista con todas las edades de los rangos sin repetir.
# Para eliminar las edades repetidas, utiliza un conjunto (set).

#BOSQUEJO:
# INICIO

#  Crear clase SelectorEdades

#     Método crear_rango(inicio, fin)
#         Crear una tupla con las edades desde inicio hasta fin
#         Retornar la tupla

#     Método edades_en_multiples_rangos(*rangos)

#         Crear un conjunto vacío

#         Recorrer cada rango recibido
#             Obtener inicio y fin
#             Crear el rango utilizando crear_rango()
#             Recorrer las edades del rango
#                 Agregar cada edad al conjunto

#         Convertir el conjunto a lista

#         Retornar la lista

#  Crear objeto SelectorEdades

#  Llamar al método con varios rangos

#  Mostrar resultado

# FIN

class SelectorEdades:
    
    def crear_rango(self, inicio, fin):
        lista=[]
        for i in range(inicio, fin +1):
            lista.append(i)
        return tuple(lista)
    def edades_en_multiples_rangos(self,*rangos):
        conjunto=set()
        
        for i in rangos:
            inicio=i[0]
            fin=i[1]
            
            num_rangos=self.crear_rango(inicio,fin)
            
            for c in num_rangos:
                conjunto.add(c)
        return list(conjunto)

se = SelectorEdades()

print(se.crear_rango(10,20))
print(f"{se.edades_en_multiples_rangos((10, 13), (12, 15))}")