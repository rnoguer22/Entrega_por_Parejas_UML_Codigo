try:
    from Ejercicios.Logger import (
        Test,
        main_logger
    )

    from Ejercicios.Puzzle import (
        A,
        main_puzzle
    )
except ModuleNotFoundError:
    #Hacemos uso de excepciones para que el codigo compile, no encuentro el error
    print ("Error de importacion")
    pass