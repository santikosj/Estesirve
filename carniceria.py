##class carniceria():
##
##    def __init__(self):
##        self.tipo=input("ingrese el tipo de animal ")
##        self.edad=int(input("ingrese la edad del animal en meses "))
##
##    def imprimir(self):
##        print (self.tipo, " ", "edad ", self.edad, "meses")
##
##class precio(carniceria):
##    def __init__(self):
##        super().__init__()
##        self.peso=int(input("ingrese el peso del animal "))
##
##class imprim(precio):
##    def __init__(self):
##        super().__init__()
##        if self.tipo=="pollo":
##            precio2=self.peso*12000
##            print(self.tipo, " ", "edad ", self.edad," " "meses"," ", "precio  $", precio2)
##        elif self.tipo=="res":
##            precio2=self.peso*20000
##            print(self.tipo, " ", "edad ", self.edad," " "meses"," ", "precio  $", precio2)
##        else:
##            precio2=self.peso*15000
##            print(self.tipo, " ", "edad ", self.edad," " "meses"," ", "precio  $", precio2)
##
##    

##class cliente():
##    def __init__(self):
##        self.nombre=input("escriba su nombre ")
##        self.tipocuenta=input("escriba el tipo de cuenta ")
##        self.__codigo=1234
##
##    def __cuenta(self):
##        print("cuenta de procesamiento")
##
##    def getcodigo(self):
##        return self.__codigo
##
##cli=cliente()
##print(cli._cliente__codigo)
##cli._cliente__cuenta()


class z():
    def __init__(self):
        self.tia=int(input('''que tipo de animal es:
                       1.acuatico
                       2.terrestre
                       3.aereo\n'''))
        self.teo=int(input('''escriba el tipo del animal que va alimentar
                          1.herbivoro
                          2.carnivoro
                          3.omnivoro\n'''))
        self.peso=int(input("digite el peso del animal "))
class alimento(z):
    def __init__(self):
        super().__init__()
        if self.tia==1:
            if self.teo==1:
                if self.peso>=20:
                    print("animal acuatico y herbivoro suministrar purina gruesa")
                else:
                    print("animal acuatico y herbivoro suministrar purina delgada")
            elif self.teo==2:
                if self.peso>=20:
                    print("animal acuatico y carnivoro suministrar 10kg de carne")
                else:
                    print("animal acuatico y carnivoro suministrar 5kg de carne")
            elif self.teo==3:
                if self.peso>=20:
                    print("animal acuatico y omnivoro suministrar 5kg de carne y 2kg de purina gruesa")
                else:
                    print("animal acuatico y omnivoro suministrar 2kg de carne y 1kg de purina gruesa")

        elif self.tia==2:
            if self.teo==1:
                if self.peso>=20:
                    print("animal terrestre y herbivoro frutas selecionadas min 8kg o alimento del zoo")
                else:
                    print("animal terrestre y herbivoro frutas selecionadas max 5kg o alimento del zoo")
            elif self.teo==2:
                if self.peso>=20:
                    print("animal terrestre y carnivoro suministrar 10kg de carne")
                else:
                    print("animal terrestre y carnivoro suministrar 5kg de carne")
            elif self.teo==3:
                if self.peso>=20:
                    print("animal terrestre y omnivoro suministrar 5kg de almiento zoo y 2kg de carne molida ")
                else:
                    print("animal terrestre y omnivoro suministrar 2kg de alimento zoo y 1kg de carne molida")

        elif self.tia==3:
            if self.teo==1:
                if self.peso>=20:
                    print("animal aereo y herbivoro suministrar purina gruesa")
                else:
                    print("animal aereo y herbivoro suministrar purina delgada")
            elif self.teo==2:
                if self.peso>=20:
                    print("animal aereo y carnivoro suministrar 3kg de carne")
                else:
                    print("animal aereo y carnivoro suministrar 1kg de carne")
            elif self.teo==3:
                if self.peso>=20:
                    print("animal aereo y omnivoro suministrar 1kg de carne molida y 2kg de purina gruesa")
                else:
                    print("animal aereo y omnivoro suministrar 2kg de carne molida y 1kg de purina gruesa")
