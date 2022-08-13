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