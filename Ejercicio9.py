# ENTRADA:
# - Un texto.

# PROCESO:
# 1. Crear la clase AnalizadorString.
# 2. Crear un atributo para guardar el texto más largo.
# 3. Crear solo_vocales(letra).
# 4. Recorrer el texto carácter por carácter.
# 5. Identificar vocales, consonantes y dígitos.
# 6. Contar cada tipo.
# 7. Guardar el texto más largo analizado.

# SALIDA:
# - Diccionario con cantidad de vocales.
# - Cantidad de consonantes.
# - Cantidad de dígitos.

#BOSQUEJO:
# INICIO

#     Crear clase AnalizadorString

#         Crear variable para guardar
#         el texto más largo


#         Método solo_vocales(letra)

#             Crear conjunto o cadena
#             con las vocales


#             Recibir una letra

#             Comprobar si la letra
#             pertenece a las vocales


#             Si pertenece

#                 Retornar verdadero

#             Si no

#                 Retornar falso


#         Método contar_por_tipo(texto)

#             Crear diccionario resultado

#                 Vocales = 0

#                 Consonantes = 0

#                 Dígitos = 0


#             Recorrer cada carácter del texto


#                 Comprobar si el carácter es una vocal


#                 Si es vocal

#                     Aumentar contador de vocales


#                 Si no

#                     Comprobar si el carácter es un dígito


#                     Si es dígito

#                         Aumentar contador de dígitos


#                     Si no

#                         Aumentar contador de consonantes


#             Comprobar si el texto actual
#             es más largo que el texto guardado


#                 Si es más largo

#                     Guardar el texto actual
#                     como texto más largo


#             Retornar el diccionario resultado


#     Crear objeto AnalizadorString

#     Analizar el texto

#         "Holaa12346"


#     Contar vocales

#     Contar consonantes

#     Contar dígitos


#     Guardar el texto más largo

#     Mostrar los resultados

#     Mostrar el texto más largo

# FIN


class AnalizadorString:
    def __init__(self):
        self.texto=""
        
    def  solo_vocales(self,letra):
        
        vocales="aeiouAEIOU"
        
        if letra in vocales:
            return True
        else:
            return False
    
    def contar_por_tipo(self, texto):
        resultado = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

        for i in texto:
            if self.solo_vocales(i):
                resultado["vocales"] += 1
            elif i.isdigit():
                resultado["digitos"] += 1
            else:
                resultado["consonantes"] += 1

        if len(texto) > len(self.texto_largo):
            self.texto_largo = texto

        return resultado


astr = AnalizadorString()

print(astr.contar_por_tipo("Holaa12346"))
print(f"Texto más largo: {astr.texto_largo}")