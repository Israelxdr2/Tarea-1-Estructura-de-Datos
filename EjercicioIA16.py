#EJERCICIO 16:

# Crea una clase llamada TransformadorCaracteres que:

# Tenga un método convertir_caracter(caracter) que reciba una letra y retorne el carácter siguiente en el alfabeto utilizando ord() y chr().
# Tenga un método convertir_palabra(palabra) que reciba una palabra y convierta cada letra utilizando el método convertir_caracter().
# El resultado debe ser una nueva palabra con los caracteres transformados.


#BOSQUEJO: 

# INICIO

#  Crear clase TransformadorCaracteres

#     Método convertir_caracter(caracter)

#         Obtener código del carácter usando ord()

#         Sumar 1 al código

#         Convertir el nuevo código a carácter usando chr()

#         Retornar carácter


#     Método convertir_palabra(palabra)

#         Crear variable palabra_nueva vacía

#         Recorrer cada letra de la palabra

#             Utilizar convertir_caracter()

#             Agregar el resultado a palabra_nueva

#         Retornar palabra_nueva


#  Crear objeto TransformadorCaracteres

#  Probar convertir_caracter()

#  Probar convertir_palabra()

#  Mostrar resultados

# FIN

class TransformadorCaracteres:
    def __init__(self):
        self.caracter={}
    def convertir_caracter(self,caracter):
        codigo=ord(caracter)
        
        resultado= codigo + 1 
        
        return chr(resultado)
    def convertir_palabra(self,palabra):
        letra= ""
        
        for i in palabra:
            letra += self.convertir_caracter(i)
            
        self.caracter[palabra]=letra
        
        return letra 
tc = TransformadorCaracteres()

print(tc.convertir_caracter("a"))
print(tc.convertir_palabra("abc"))