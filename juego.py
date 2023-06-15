import random
class Juego():
    def __init__(self):
        self.jugadores = ["Yeison", "Manuel", "Mariana", "Camila", "Karoll", "Juan", "Macalister", "Sebastian", "Nicol", "Natalia", "Felicia", "Carlos"]
        self.categorias = ["calculo", "fisica", "algebra", "circuitos", "programacion"]
        self.aleatorio1 = random.choice(self.jugadores)
        print(self.aleatorio1)
        self.aleatorio2 = random.choice(self.categorias)
        print(self.aleatorio2)
        self.entrada=str(input('ingrece la categoria que le toco '))
        if self.entrada=="calculo":
            self.calculo()
        elif self.entrada=="fisica":
            self.fisica()
        elif self.entrada=="algebra":
            self.algebra()
        elif self.entrada=="circuitos":
            self.circuitos()
        elif self.entrada=="programacion":
            self.programacion()
        else:
            print("Esrciba una categoria valida")
            a=Juego()
            
        
    def calculo(self):
        self.r=int(input('1. ¿Cual es la derivada de 3x?  '))
        if self.r==3:
            self.b=str(input('''2. ¿Que se halla derivando la velocidad
                                    a)aceleracion
                                    b)posicion  '''))
            if self.b=='a':
                self.e=int(input('3. ¿Cuanto es 2x10+10?  '))
                if self.e==30:
                    self.g=input('4.¿Cuánto da la integral de 2dx?  ')
                    if self.g=="2x+c":
                        self.i=input('''5. ¿Cuádo se integra la velocidad que se obtiene?
                                           a)aceleracion
                                           b)posicion  ''')
                        if self.i=="b":
                            print('ganaste')
                            
                            
                        else:
                            a=Juego()
                    else:
                        a=Juego()
                        
                else:
                    a=Juego()
            else:
                a=Juego()
        else:
            a=Juego()
                

    def fisica(self):
        self.r=input('''1. ¿cual es la gravedad de la tierra?
                             a)9,81
                             b)19,81  ''')
        if self.r=="a":
            self.b=str(input('''2. ¿Cómo se expresa nano
                                    a)10 a la 9
                                    b)10 a la -9  '''))
            if self.b=='b':
                self.e=input('''3. ¿La energia es la capacidad de realizar un trabajo?
                                        a)verdadero
                                        b)falso  ''')
                if self.e=="a":
                    self.g=input('4.¿Donde nacio Isaac Newton?  ')
                    if self.g=="inglaterra" or self.g=="Inglaterra":
                        self.i=int(input('5. ¿Cuántos milímetros hay en un litro?  '))
                        if self.i==1000:
                            print('ganaste')
                            
                            
                        else:
                            a=Juego()
                    else:
                        a=Juego()
                        
                else:
                    a=Juego()
            else:
                a=Juego()
        else:
            a=Juego()
            




    def algebra(self):
        self.r=input('1. ¿En algebra se usan solos numeros? ')
        if self.r=="si" or self.r=="Si":
            self.b=str(input('2. ¿Cuanto es (a+a) '))
            if self.b=='2a':
                self.e=input('''3. ¿En algebra existen las cuatro operaciones?
                                        a)verdadero
                                        b)falso ''')
                if self.e=="a":
                    self.g=input('''4. ¿la derivada es un tema de algebra?
                                          a)verdadero
                                          b)falso  ''')
                    if self.g=="a":
                        self.i=input('''5. ¿En algebra no se usan signos positivos y negativos?
                                          a)verdadero
                                          b)falso  ''')
                        if self.i=="b":
                            print('ganaste')
                            
                            
                        else:
                            a=Juego()
                    else:
                        a=Juego()
                        
                else:
                    a=Juego()
            else:
                a=Juego()
        else:
            a=Juego()
               
   

    def circuitos(self):
        self.r=int(input('1. ¿Si tenemos 3 resistencias en serie de 2 ohmios cuanto es la resistencia equivalente?  '))
        if self.r==6:
            self.b=str(input('2. ¿Podemos sumar el valor de una resistencia con un capacitor?  '))
            if self.b=='No' or self.b=="no":
                self.e=input('''3. ¿Podemo denominar a un corto circuito como un aumento brusco de la intensidad de una corriente?
                                      a)verdadero
                                      b)falso  ''')
                if self.e=="a":
                    self.g=input('''4.¿Una fuente de corriente ideal es la que nos suministra una intensidad constante independientemente del valor de la tensión?
                                           a)verdadero
                                           b)falso  ''')
                    if self.g=="a":
                        self.i=int(input('5. ¿Si tenemos 2 resistencias en paralelo de 2 ohmios cuanto es la resistencia equivalente?  '))
                        if self.i==1:
                            print('ganaste')
                            
                            
                        else:
                            a=Juego()
                    else:
                        a=Juego()
                        
                else:
                    a=Juego()
            else:
                a=Juego()
        else:
            a=Juego()
                    



    def programacion(self):
        self.r=input('1. ¿c++ es un lenguaje de programacion?  ')
        if self.r=="si":
            self.b=str(input('2. ¿Que tipo de dato numerico puede ser positivos o negativos? (entero/decimal)  '))
            if self.b=='entero':
                self.e=input('3. ¿El algoritmo se transformara en un programa de calculadora?  ')
                if self.e=="si" or self.e=="Si":
                    self.g=input('''4. Menciona dos variables
                                            a)locales y globales
                                            b)faciles y neutras  ''')
                    if self.g=="a":
                        self.i=int(input('5. ¿Cuántas estructuras ciclicas existen?  '))
                        if self.i==3:
                            print('ganaste')
                            
                            
                        else:
                            a=Juego()
                    else:
                        a=Juego()
                        
                else:
                    a=Juego()
            else:
                a=Juego()
        else:
            a=Juego()
            
a=Juego()    












