class Test:
    def llamada(self, string):
        file.write("{}".format(string))

file = open("cat log.txt", "w")
file.write("--Start log--\n")

test = Test()
for i in range(1,6): 
   if i == 1: 
       test.llamada("Primera llamada\n") 
   else:
       test.llamada("{}ª llamada\n".format(i)) 