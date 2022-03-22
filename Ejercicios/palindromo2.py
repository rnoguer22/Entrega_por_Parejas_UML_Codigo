#Creamos la clase
from readline import get_history_length


class Palindromo2():

    #Definimos el constructor
    def __init__(self, palabra):
        self.palabra = palabra

    #Definimos el método test
    def test(self):

        while len(self.palabra) >= 1:
            #Si la primera y ultima letra son las mismas las "elimina" de la palabra y vuelve a iniciar el método test
            if self.palabra[0] == self.palabra[-1]:
                self.palabra = self.palabra[1:-1]
                return self.test()

            else:
                return False

        if len(self.palabra) < 1:
            return True

    #Definimos el destructor
    def borrar(self):
        del self.palabra
    
       
       
    

            
    

p = Palindromo2("radar")
print(p.test())
p.borrar()

p = Palindromo2("sonar")
print(p.test())



