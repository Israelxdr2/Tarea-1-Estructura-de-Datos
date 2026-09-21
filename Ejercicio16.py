# ENTRADA:
# - Una letra o palabra.
# - Un desplazamiento entre 1 y 25.

# PROCESO:
# 1. Crear la clase CodificadorCesar.
# 2. Crear un diccionario para guardar el historial.
# 3. Crear codificar_letra().
# 4. Convertir la letra a código ASCII con ord().
# 5. Desplazar la letra utilizando el operador %.
# 6. Convertir nuevamente el código a letra con chr().
# 7. Crear codificar_palabra().
# 8. Recorrer la palabra letra por letra.
# 9. Utilizar codificar_letra() para cada letra.
# 10. Guardar la palabra codificada en el historial.

# SALIDA:
# - Palabra codificada.
# - Historial de codificaciones.

#BOSQUEJO:
# INICIO

#     Crear clase CodificadorCesar

#         Crear diccionario vacío
#         para guardar el historial


#         Método codificar_letra(letra, desplazamiento)

#             Recibir una letra
#             y un desplazamiento


#             Convertir la letra
#             a su código numérico


#             Convertir el código de la letra
#             a una posición dentro del alfabeto


#             Sumar el desplazamiento


#             Utilizar módulo 26
#             para mantener el resultado
#             dentro del alfabeto


#             Convertir nuevamente
#             el código numérico a una letra


#             Retornar la letra codificada


#         Método codificar_palabra(palabra, desplazamiento)

#             Crear cadena vacía
#             para guardar el resultado


#             Recorrer cada letra
#             de la palabra


#                 Codificar la letra
#                 utilizando codificar_letra()


#                 Agregar la letra codificada
#                 al resultado


#             Guardar en el diccionario:

#                 Palabra original → palabra codificada


#             Retornar la palabra codificada


#     Crear objeto CodificadorCesar


#     Codificar la palabra

#         "hola"

#         Desplazamiento → 3


#     Codificar cada letra

#         h → k

#         o → r

#         l → o

#         a → d


#     Formar la palabra codificada

#         "krod"


#     Guardar la palabra original
#     y la codificada en el historial


#     Mostrar palabra codificada

#     Mostrar historial

# FIN

class CodificadorCesar:
    def __init__(self):
        self.codigo= {}

    def codificar_letra(self, letra, desplazamiento):
        codigo = ord(letra)

        nuevo_codigo = (codigo - ord("a") + desplazamiento) % 26 + ord("a")

        return chr(nuevo_codigo)
    
    def codificar_palabra(self,palabra, desplazamiento):
        
        string= ""
        
        for i in palabra:
            string += self.codificar_letra(i, desplazamiento)
        
        self.codigo[palabra]= string
        
        return string 


cc = CodificadorCesar()

print(f"la palabra codificada: {cc.codificar_palabra("hola", 3)}")
print(f"El historial es: {cc.codigo}")