"""
Un objeto es la representación de un objeto de la realidad
este tiene.

- propiedade -> lo que describe mi objeto y puede ser mutables si es necesario
- metodos -> acciones que puede tener mi objeto

"""

#las clases son publicas en python pero con una convención sabremos que es
#privada y por lo tanto no podremos modificarlo desde afuera

class Dino :

    on = False
    _private_propertie = True #solo la puede modificar desde la clase, aunque se 
                              #pueda desde fuera, por buena pract y convenciones
                              #hacerlo solo dentro de la clase

    def light(self) : #self es el objeto en si mismo
        self.on = True


    def get_private_propiertie(self) :
        return self._private_propertie


d = Dino() #instanciar el objeto (crear - crea una ref en memoria)
d.light()


#con una clase statica podremos usar sus propiedades y metodos, son accesibles
#no hay nada privado
class Static :

    static_propertie = "hey you"

    @staticmethod #este decorador nos ayuda a crear este metodo estatico
    def static_method() :
        Static.static_propertie #accedemos haciendo referencia asi misma
                                #ya que no tienen referencia asi mismas
        print('static methdo')


Static.static_method()

#herencia
"""
    es cuando queremos reutilizar caracteristicas de un objeto y reutilizarlo.
"""

class Juguete :
    encendido = False


    def encender(self) :
        self.encendido = True

    def apagar(self) :
        self.encendido = False



class DinoTwo(Juguete) :

    modelo_dino = 'xyz'

#ahora dino tiene los metodos y propiedades de un juguete.

d =  DinoTwo()
#caracteristicas de su padre
d.apagar()
d.encender()
print(d.encendido)
#caracteristicas propias
print(d.modelo_dino)

#contructor
"""
    - Es la primera funcion en ejecutarce cuando se instancia la clase
"""

class X:

    def __init__(self):
        print('primera funcion en ejecutarce')

#pasar parametros
class Y :

    def __init__(self, valor_y):
        self.y = valor_y


x = X()
y = Y(22)

#podemos ejecutar el constructor de la clase padre

class Z(Y) :

    def __init__(self, valor_z, valor_y):
        super().__init__(valor_y)
        self.z = valor_z

#clases abstracta

"""
    - nos sirven para funcionalidad a muchos objetos que hereden de el.
    - obligamos a que ese objeto tenga ese metodo y propiedad y con ello
      lograr polimorfismo (muchas formas de un objeto) el cual puede tener un
      mismo comportamiento con el mismo nombre y actuar de muchas formas según
      que objeto
"""

from abc import ABC, abstractmethod

class Animal(ABC) :

    @abstractmethod
    def sonido(self, s) :
        pass


class Pato(Animal) :
    
    def sonido(self, s):
        print(s)


class Perro(Animal) :

    def sonido(self, s):
        print(s)


#muchas formas para un mismo comportamiento

p = Pato()
p.sonido('cuak!')

pe = Perro()
p.sonido('wof!')