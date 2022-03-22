# Entrega_por_Parejas_UML_Codigo

Pinche [aqui](https://github.com/rnoguer22/Entrega_por_Parejas_UML_Codigo.git) para acceder al link de este repositorio

Pelayo Huerta Mijares y Ruben Nogueras Gonzalez hemos resuelto de manera conjunta los ejercicios propuestos en la tarea "Ejercicios de Clases de POO", asi como sus UML correspondientes. Los ejercicios con sus UML asignados son los siguientes:

## Ejercicio 3
### Puzzle

```Python3
class A: 
    def z(self): 
        return self
 
    def y(self, t): 
        return len(t) 

#Funcion que abriremos desde el archivo main.py
def main_puzzle():
    a = A 
    y = a.z
    print(y(a)) #Muestra por pantalla <class '__main__.A'> ya que la funcion z devuelve self
    aa = a() 
    print(aa is a())  #Imprime False ya que esta condicion no es cierta
    z = aa.y 
    print(z(()))  #Devuelve 0 ya que no hemos introducido valores dentro de len ---> len()
    print(a().y((a,)))   #Devuelve len(a,), es decir, 1
    print(A.y(aa, (a,z)))   #Devuelve len(a,z), que es igual a 2 ya que (a,z) tiene 2 elementos
    print(aa.y((z,1,'z')))  #Devuelve len(z,1,'z'), que es 3 ya que tiene 3 elementos
```

![Puzzle drawio](https://user-images.githubusercontent.com/91721762/159479846-257521b5-f254-4ad3-906a-45ddd7dba8b9.png)

### Ejercicio 4
### Logger

```Python3
class Test:
    #metodo llamada
    def llamada(self, string, file):
        #Escribe en file el argumento del metodo
        file.write("{}".format(string))

#Funcion que llamaremos desde el archivo mian.py
def main_logger():
    #Abrimos el archivo y escribimos el mensaje inicial
    file = open("cat log.txt", "w")
    file.write("--Start log--\n")

    #Declaramos la instancia de clase
    test = Test()
    #Bucle para escribir en el archivo .txt
    for i in range(1,6): 
        if i == 1: 
            test.llamada("Primera llamada\n", file) 
        else:
                test.llamada("{}ª llamada\n".format(i), file) 
                if i == 5:
                    #Escribimos el mensaje final y cerramos el archivo
                    file.write("--End log: {} log(s)--".format(i))
                    file.close()
```

![Logger drawio](https://user-images.githubusercontent.com/91721762/159480012-44e427b0-9eea-42ff-b6dc-71590b9a45dc.png)
