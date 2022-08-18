#los modulos se llaman como el archivo
from suma import suma_funcion

#paquetes
from package import say #say es un modulo

from package.say import say #say es una funcion



#archivo principal
if __name__ == '__main__' :

    r = suma_funcion(1,1)
    say.say('hello')
    say('world')

    print(r)
    print('main')




