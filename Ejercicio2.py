
# EJERCICIO 2: ANALIZADOR DE TEXTO

# ENTRADA:
# - Varias palabras.
#
# PROCESO:
# 1. Crear una clase llamada AnalizadorTexto.
# 2. Crear una lista para almacenar las palabras.
# 3. Crear un conjunto para almacenar palabras únicas.
# 4. Crear un método agregar_palabra().
# 5. Agregar la palabra a la lista.
# 6. Agregar la palabra al conjunto.
# 7. Crear un método contar_palabras().
# 8. Contar las palabras almacenadas.
# 9. Crear un método agregar_multiples(*args).
# 10. Recorrer las palabras recibidas.
# 11. Utilizar agregar_palabra() para agregar cada palabra.
#
# SALIDA:
# - Cantidad de palabras.
# - Palabras únicas.


#BOSQUEJO:
# INICIO

#     Crear clase Analizadortexto

#         Crear constructor __init__()

#             Crear lista vacía para guardar palabras

#             Crear conjunto vacío para guardar
#             solamente palabras únicas


#         Método agregar_palabra(palabra)

#             Recibir una palabra

#             Agregar la palabra a la lista

#             Agregar la palabra al conjunto


#         Método contar_pal()

#             Contar las palabras que existen
#             en el conjunto

#             Retornar la cantidad


#         Método agregar_multiples(*args)

#             Recibir varias palabras

#             Recorrer cada palabra

#                 Llamar al método agregar_palabra()

#                 Agregar la palabra a la lista

#                 Agregar la palabra al conjunto


#     Crear objeto Analizadortexto

#     Agregar varias palabras

#         "Hola"

#         "Estudiar"

#         "jugar"

#         "Hola"


#     Contar las palabras únicas

#     Mostrar cantidad de palabras únicas

#     Mostrar las palabras únicas

# FIN



class Analizadortexto:
    
    def __init__(self):
        self.palabra= []
        self.unico= set()
    
  
       
    def agregar_palabra(self, conjunto):
        
            self.palabra.append(conjunto)
            self.unico.add(conjunto)
    
    def contar_pal(self):
       return len(self.unico)
    
    def agregar_multiples(self, *args):
       
        for pal in args:
            self.agregar_palabra(pal)

at= Analizadortexto()

at.agregar_multiples("Hola", "Estudiar", "jugar","Hola")

print(at.contar_pal())
print(f"Las palabras unicas son: {at.unico}")
  
