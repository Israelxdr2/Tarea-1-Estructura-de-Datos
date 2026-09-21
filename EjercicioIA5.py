#EJERCICIO 5:
#Desarrolle una clase llamada ClasificadorNumeros que permita identificar y separar números positivos y negativos.


#La clase deberá:

#Tener un método es_positivo(numero) que retorne True si el número es positivo y False en caso contrario.
#Tener un método separar(*numeros) que reciba varios números y retorne un diccionario con dos categorías:
#"positivos" → lista de números positivos.
#"negativos" → lista de números negativos.
#El método separar() deberá reutilizar el método es_positivo().
#Tener un método cantidad_positivos_negativos() que retorne una tupla con la cantidad de números positivos y negativos.

#BOSQUEJO:
#INICIO

#    Crear clase ClasificadorNumeros

#        Método es_positivo(numero)

#            Si numero > 0
#                Retornar True
#            Si no
 #               Retornar False


 #       Método separar(*numeros)
#
#            Crear lista positivos
#            Crear lista negativos

#            Recorrer los números recibidos

#                Utilizar es_positivo()
#
#                Si es positivo
#                    Agregar a positivos

#                Si no
#                    Agregar a negativos

#               Crear diccionario

 #               "positivos" → lista positivos
 #               "negativos" → lista negativos

 #           Retornar diccionario


 #       Método cantidad_positivos_negativos()
#
 #           Contar números positivos
#            Contar números negativos

#            Crear tupla con las cantidades

#            Retornar tupla


#    Crear objeto ClasificadorNumeros

#    Agregar varios números

#    Mostrar números positivos y negativos

#    Mostrar cantidades
#
#FIN

class ClasificadorNumeros:
    def __init__(self):
        self.positivos=[]
        self.negativos=[]
        
    def es_positivo(self, numero):
            if numero >=0:
                return True
            else:
                return False
    def separar(self,*numeros):
        self.positivos=[]
        self.negativos=[]
        
        for i in numeros:
            if self.es_positivo(i):
                self.positivos.append(i)
            else:
                self.negativos.append(i)
        return {"positivos": self.positivos, "negativos": self.negativos}
    
    def cantidad_positivos_negativos(self):
        
        cantidad_positivos=len(self.positivos)
        cantidad_negativos=len(self.negativos)
        return(cantidad_positivos,cantidad_negativos)

cn = ClasificadorNumeros()

print(f"{cn.separar(5, -2, 8, -7, 3, -1)}")
print(f"{cn.cantidad_positivos_negativos()}")
print(f"{cn.es_positivo(5)}")