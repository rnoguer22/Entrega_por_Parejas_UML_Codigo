if __name__ == "__main__":

    from Ejercicios.Logger import main_logger
    print ("Ejercicio Logger:")
    main_logger()
    print ("\n")

    from Ejercicios.Puzzle import main_puzzle
    print ("Ejercicio Puzzle:")
    main_puzzle()
    print ("\n")

    from Ejercicios.palindromo import *
    print("Ejertcicio palíndromo 1:")
    p = Palindormo()
    texto = p.pedir_texto()
    p.especiales(texto)
    print(p.esPalindromo(texto))
    print("\n")

    from Ejercicios.palindromo2 import *
    print("Ejercicio palindromo 2")
    p = Palindromo2("radar")
    print(p.test())
    p.borrar()
    p = Palindromo2("sonar")
    print(p.test())
    p.borrar()

