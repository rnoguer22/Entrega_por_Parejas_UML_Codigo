class A: 
    def z(self): 
        return self
 
    def y(self, t): 
        return len(t) 

#Funcion que abriremos desde el archivo main.py
def main():
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