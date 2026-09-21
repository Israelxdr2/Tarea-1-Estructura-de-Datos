#EJERCICI 9:
# Desarrolle una clase llamada AnalizadorTexto que permita analizar diferentes textos y contar la cantidad de letras mayúsculas, letras minúsculas y dígitos que contiene cada texto.

# La clase deberá:

# Tener un método es_mayuscula(caracter) que retorne True si el carácter es una letra mayúscula y False en caso contrario.
# Tener un método contar_por_tipo(texto) que recorra el texto carácter por carácter y retorne un diccionario con la cantidad de:
# "mayusculas"
# "minusculas"
# "digitos"
# El método contar_por_tipo() deberá utilizar es_mayuscula() para identificar las letras mayúsculas.
# Tener un atributo que almacene el texto más largo que haya sido analizado.



#BOSQUEJ0:

# INICIO

#     Crear clase AnalizadorTexto

#         Crear atributo texto_mas_largo


#         Método es_mayuscula(caracter)

#             Si el carácter es mayúscula
#                 Retornar True
#             Si no
#                 Retornar False


#         Método contar_por_tipo(texto)

#             Crear contador de mayúsculas = 0
#             Crear contador de minúsculas = 0
#             Crear contador de dígitos = 0

#             Recorrer el texto carácter por carácter

#                 Si es mayúscula
#                     Aumentar contador de mayúsculas

#                 Si es minúscula
#                     Aumentar contador de minúsculas

#                 Si es dígito
#                     Aumentar contador de dígitos


#             Comparar longitud del texto
#             con el texto más largo

#             Si el texto actual es más largo
#                 Actualizar texto_mas_largo


#             Crear diccionario con los contadores

#             Retornar diccionario


#     Crear objeto AnalizadorTexto

#     Analizar textos

#     Mostrar resultados

#     Mostrar texto más largo

# FIN



class AnalizadorTexto:
    def __init__(self):
        self.texto= ""
        self.texto_mas_largo=""
        
    def es_mayuscula(self,caracter):
        
        mayus= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if caracter in mayus:
            return True
        else:
             return False
        
    def contar_por_tipo(self,texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        
        
        resultado = {
            "mayusculas": 0,
            "minusculas": 0,
            "digitos": 0
            
        }
        
        for i in texto:
            if self.es_mayuscula(i):
                resultado["mayusculas"]+=1
            elif i.isdigit:
                resultado["digitos"] +=1
            else:
                resultado["minusculas"]+=1
        
        return resultado
                
        
at=AnalizadorTexto()

print(f"Es 'H' mayúscula?: {at.es_mayuscula("H")}")

print("Conteo:", at.contar_por_tipo( "Hola Mundo 2026!"))
print("El texto más largo analizado fue:", at.texto_mas_largo)