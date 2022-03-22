#Creamos la clase palindromo
class Palindormo():

    #Definimos el constructor 
    def __init__(self):
        pass

    def pedir_texto(self):
        texto = str(input("Introduce un texto: "))
        return texto

    #Creamos el método que comprueba si es palindromo
    def esPalindromo(self, texto):
        if len(texto) < 1:
            return True
        
        else:
            #Creamos un bucle recursivo para que compare la primera letra con la última
            if texto[0] == texto[-1]:
                return self.esPalindromo(texto[1:-1])
            else:
                return False

    #Creamos un método para que también funcione con mayusculas, minusculas, acentos y espacios
    def especiales(self, texto):
        texto = texto.lower()
        texto = texto.replace(" ", "")
        texto = texto.replace("á", "a")
        texto = texto.replace("é", "e")
        texto = texto.replace("í", "i")
        texto = texto.replace("ó", "o")
        texto = texto.replace("ú", "u")
        return texto

p = Palindormo()
texto = p.pedir_texto()
p.especiales(texto)
print(p.esPalindromo(texto))



