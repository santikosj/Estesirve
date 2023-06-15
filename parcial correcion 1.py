import csv
admin=[1234]
doc=[2345,5987,1290]
estu=[3275,4002,0000,9884,5502]
biblioteca=[]
academico=[]
convi=[]
vota=[]

class acceso():
    def __init__(self):
        self.a=input("Escriba su nombre por favor ")
        self.b=input("Escriba su apellido por favor ")
        self.c=int(input("Digite su edad "))
        self.d=int(input('''     Que usuario es usted
                             1)Admin
                             2)Doc
                             3)Estu\n   '''))
        self.e=int(input("Digite su contraseña "))
        
##biblioteca
    def biblioteca(self):
        super().__init__()
        if self.e in admin and self.d==1:
            print("usted ingreso al sistema como administrador")
            self.tipo=input("ingrese si es libro o revista\n")
            if self.tipo=="libro":
                self.nombre=input('ingrese el nombre del libro\n')
                self.autor=input('ingrese el nombre del autor\n')
                self.cantidad=input('ingrese cantidad de libros\n')
                biblioteca.append([self.tipo, self.autor, self.nombre, self.cantidad])
                self.guardar()
            elif self.tipo=="revista":
                self.titulo=input('ingrese el titulo de la revista\n')
                self.año=input('ingrese el año de edicion\n')
                biblioteca.append([self.tipo, self.titulo, self.año])
                self.guardar()
        elif self.e in doc and self.d==2:
            print("usted ingreso al sistema como docente")
            self.mostrar()
        elif self.e in estu and self.d==3:
            print("usted ingreso al sistema como estudiante")
            self.mostrar()
        else:
            print("digite una contraseña correcta ")

    def guardar(self):
        with open('C:/Users/JUAN/Documents/biblioteca.csv', 'w',  newline='') as biblio:
            self.escri=csv.writer(biblio, delimiter=';')
            self.escri.writerows(biblioteca)
            print('ok')
    def mostrar(self):
        print('ingreso a mostrar')
        for i in biblioteca:
            print(i)
            
##votaciones
        

    def votaciones(self):
        super().__init__()
        if self.e in admin and self.d==1:
            print("usted ingreso al sistema como administrador")
            self.academico()
        elif self.e in doc and self.d==2:
            print("usted ingreso al sistema como docente")
            self.academico()

        elif self.e in estu and self.d==3:
            print("usted ingreso al sistema como estudiante")    
            self.jj=int(input('''ingrese el numero del candidato
                              1)Felipe Arroyo
                              2)Marian Buitrago\n'''))
            if self.jj==1 or self.jj==2:
                vota.append([self.jj])
                self.sive()
            elif self.jj==3:
                print("digite un numero de candidato correcto")
            else:
                print("digite un numero de candidato correcto")
        else:
            print("digite una contraseña correcta ") 

    def sive(self):
        with open('C:/Users/JUAN/Documents/vota.csv', 'w',  newline='') as biblio:
            self.escri=csv.writer(biblio, delimiter=';')
            self.escri.writerows(vota)
            print('ok')
    def votii(self):
        print('ingreso a mostrar')
        for i in vota:
            print(i)
            
              

        


##academico
    def academico(self):
        if self.e in admin and self.d==1:
            print("usted ingreso al sistema como administrador")
            self.muestra()
        
        elif self.e in doc and self.d==2:
            print("usted ingreso al sistema como docente")
            self.p=input('ingrese el nombre del estudiante\n')
            self.c=int(input('ingrese la nota del estudiante\n'))
            academico.append([self.p, self.c])
            self.guarda()
            self.muestra()
            
        elif self.e in estu and self.d==3:
            print("usted ingreso al sistema como estudiante")
            self.muestra()
        else:
            print("digite una contraseña correcta ")

    def guarda(self):
        with open('C:/Users/JUAN/Documents/academico.csv', 'w',  newline='') as biblio:
            self.escri=csv.writer(biblio, delimiter=';')
            self.escri.writerows(academico)
            print('ok')

    def muestra(self):
        print('ingreso a mostrar')
        for i in academico:
            print(i)



##convivencia
    def convi(self):
        super().__init__()
        if self.e in admin and self.d==1:
            print("usted ingreso al sistema como administrador")
            self.look()
        elif self.e in doc and self.d==2:
            print("usted ingreso al sistema como docente")
            self.t=input('ingrese el nombre del estudiante\n')
            self.b=str(input('ingrese la fecha\n'))
            self.bb=str(input("ingrese la hora "))
            self.aa=input("ingrese la asignatura ")
            self.ff=input("ingrese la falta ")
            self.fff=input(" ingrese felicitaciones ")
            self.rr=input("ingrese las recomendaciones ")
            convi.append([self.t, self.b, self.bb, self.aa, "observador", self.ff, self.fff, self.rr ])
            self.saver()
            self.look()
        elif self.e in estu and self.d==3:
            print("usted ingreso al sistema como estudiante")
            self.look()
        else:
            print("digite una contraseña correcta ")
            
    def saver(self):
        with open('C:/Users/JUAN/Documents/convi.csv', 'w',  newline='') as biblio:
            self.escri=csv.writer(biblio, delimiter=';')
            self.escri.writerows(convi)
            print('ok')

    def look(self):
        print('ingreso a mostrar')
        for i in convi:
            print(i)
