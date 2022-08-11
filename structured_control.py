#las condiciones son tomas de desiciones que nos permiten ejecutar cierta
#reglas que nosotros mismos demos.
#todo lo que se coloca en una condicion se ejecuta si solo si se cumple

"""
OPERADORES CONDICIONALES
> MAYOR, < MENOR, >= MAYOR O IGUAL, <= MENOR O IGUAL

if condicion:
    acciones


and -> para que se cumpla ambas condiciones deben ser verdad V and V = V
or -> solos es falso cuanda ambas condiciones son falsas, mientras
      ambas condiciones son verdad.
not -> niega una condicion

"""

a = 5
b = 6

if a >= 5 and b <= 6 :
    print('yass')
elif a >= 6 :
    print('yass 2')
else:
    print('no cumpli ninguna condición')



"""
sirve para recorrer cualquier valor iterable

- strings
- listas
- tuplas
- diccionarios
- sets ( conjuntos )

"""

lista = [1,2,3,34,5]

for valor in lista :
    print(lista)


