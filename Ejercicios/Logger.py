class Test:
    #metodo llamada
    def llamada(self, string):
        #Escribe en file el argumento del metodo
        file.write("{}".format(string))

#Abrimos el archivo y escribimos el mensaje inicial
file = open("cat log.txt", "w")
file.write("--Start log--\n")

#Declaramos la instancia de clase
test = Test()
#Bucle para escribir en el archivo .txt
for i in range(1,6): 
   if i == 1: 
       test.llamada("Primera llamada\n") 
   else:
        test.llamada("{}ª llamada\n".format(i)) 
        if i == 5:
            #Escribimos el mensaje final y cerramos el archivo
            file.write("--End log: {} log(s)--".format(i))
            file.close()