# EJERCICIO 2: 
# Desarrolle una clase llamada RegistroNumeros que permita almacenar varios números y determinar cuáles son únicos.
# La clase deberá:
# 
# Crear una lista para almacenar todos los números registrados.
# Crear un conjunto (set) para almacenar únicamente los números que no se repiten.
# Tener un método agregar_numero(numero) que agregue el número tanto a la lista como al conjunto.
# Tener un método contar_numeros() que indique la cantidad total de números registrados.
# Tener un método agregar_multiples(*args) que permita registrar varios números.
# Tener un método mostrar_unicos() que devuelva el conjunto de números únicos.


# INICIO
# 
# Crear clase RegistroNumeros

#       Crear lista numeros

#          Crear conjunto unicos

#        Método agregar_numero(numero)
#            Agregar numero a la lista
#            Agregar numero al conjunto
#        Método contar_numeros()
#            Contar elementos de la lista
#            Retornar cantidad
#       Método agregar_multiples(*args)
#        Recorrer los números recibidos
#                Utilizar agregar_numero()
#        Método mostrar_unicos()
#           Retornar conjunto de números únicos
#    Crear objeto RegistroNumeros

#    Agregar varios números

#    Mostrar cantidad total

#    Mostrar números únicos
#FIN

class RegistrarNumeros:
    def __init__(self):
        self.numeros=[]
        self.unicos=set()
        
    def agregar_numero(self, numero):
        self.numeros.append(numero)
        self.unicos.add(numero)
        
    def contar_numeros(self):
    
        return len(self.numeros)
            
            
    def agregar_multiples(self,*args):
        for c in args:
            self.agregar_numero(c)
    def mostrar_unicos(self):
        
        return self.unicos
rn= RegistrarNumeros()

rn.agregar_multiples(1,3,4,5,21,1,3,7,8,8)

print(f"{rn.contar_numeros()}")
print(f"{rn.mostrar_unicos()}")