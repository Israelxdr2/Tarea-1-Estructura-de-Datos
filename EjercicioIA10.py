#EJERCICIO 10:

# Desarrolle una clase llamada Peliculas que permita registrar películas junto con su género y administrarlas.

# La clase deberá:

# Tener un método agregar_pelicula(titulo, genero) que guarde cada película en una lista de tuplas con la estructura (titulo, genero).
# Tener un método peliculas_accion() que retorne únicamente las películas cuyo género sea "accion".
# Tener un método eliminar_pelicula(titulo) que elimine de la lista la película cuyo título coincida con el indicado.

#BOSQUEJO:

# INICIO

#     Crear clase Peliculas

#         Crear lista peliculas


#         Método agregar_pelicula(titulo, genero)

#             Crear tupla con:
#                 titulo
#                 genero

#             Agregar tupla a la lista


#         Método peliculas_accion()

#             Crear lista vacía

#             Recorrer las películas

#                 Si el género es "accion"

#                     Agregar película
#                     a la lista

#             Retornar lista


#         Método eliminar_pelicula(titulo)

#             Recorrer las películas

#                 Si el título coincide

#                     Eliminar película
#                     de la lista


#     Crear objeto Peliculas

#     Agregar varias películas

#     Mostrar películas de acción

#     Eliminar una película

#     Mostrar lista actualizada

# FIN


class Peliculas:
    def __init__(self):
        self.peliculas=[]
    def agregar_pelicula(self,titulo, genero):
        tuplas=(titulo, genero)
        self.peliculas.append(tuplas)
    
    def peliculas_accion(self):
        resultado=[]
        for i in self.peliculas:
            if i[1]=="Accion":
                resultado.append(i)
        return resultado
    def eliminar_pelicula(self,titulo):
        
        for i in self.peliculas:
            if i[0]==titulo:
                self.peliculas.remove(i)
                break
pl= Peliculas()

pl.agregar_pelicula("It", "Terror")
pl.agregar_pelicula("Fast and fury", "Accion")
pl.agregar_pelicula("Pokemon", "Aventura")

print(pl.peliculas_accion())
pl.eliminar_pelicula("It")
print(f"Películas restantes: {pl.peliculas}")