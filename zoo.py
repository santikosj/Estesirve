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
