"""
Las funciones son subalgoritmos los cuales podremos reutilizar

- no usar muchos parametros
- nombre semantico
- solo deben hacer una sola cosa


"""

def saludo_a(nombre) :
    print('hola', nombre)


#funciones con valores por default
def suma(a = 1, b = 1) :
    print(a + b)


suma()
suma(2,3)

#name parameters -> podemos mandar los parametros en cualquier orden
#después de que se les de el nombre.

def resta(a, b) :
    print(a-b)

resta(b=2, a=0)

#parametros variables, el cual nos da la posibilidad de tener muuuchos parametros

def n(*args) : #args es una convención
    print(args) #devuelve una tupla

n(1,2,3,4,5,67,8,9)

#con name parameters
def k(**kwargs) :
    print(kwargs) #mostrará un diccionario

k(a=1, b=2, c=3)


#funciones anonimas - lambdas
hola = lambda: print('hola')
hola()

#con parametro
hola_a = lambda nombre: print('hola', nombre)
hola_a('lucas')

