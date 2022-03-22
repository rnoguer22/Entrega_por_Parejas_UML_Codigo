#Creamos la clase
from readline import get_history_length


class Palindromo2():

    #Definimos el constructor
    def __init__(self, palabra):
        self.palabra = palabra

    #Definimos el método test
    def test(self):

        while len(self.palabra) >= 1:
            
            if self.palabra[0] == self.palabra[-1]:
                self.palabra = self.palabra[1:-1]
                return self.test()

            else:
                return False

        if len(self.palabra) < 1:
            return True

            
    

p = Palindromo2("radar")
print(p.test())


