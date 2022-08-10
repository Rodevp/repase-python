#en python todo es un objeto
#python cuando creamos una variable y tiene su espacio en memoria al cambiarle
#el valor python reserva otro espacio de memoria cambia y la anterior se dehecha
#o lo deja en el limbo hasta que vuelva hacerse referencia a ese espacio de memoria

#datos mutables en python
"""
    - numerico
    - texto
    - tuplas
"""
n = 2
saludo = "hola"
tupla = (1,2,3,4,5)

#mutables
"""
    - listas
    - diccionarios
"""

lista = [1,2,3,4]
lista.append(2) #agregar a una lista
lista.remove(4) #elimina pasado un elemento

#funciona clave - valor
diccionario = {
    "potato": "papa",
    "apple": "manzana",
}

#conjuntos
a = {0,1,2,3,4,5}
b = {2,4,6,8}
union = a | b # - diferencia, & intersecion 