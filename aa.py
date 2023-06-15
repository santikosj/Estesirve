from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
#messagebox: ventanas emergentes

root=Tk()
root.title("PROGRAMA JUANITO")
root.config(bg="green")

miframe=Frame(root, width=1200, height=600)
miframe.pack()
#------------------AÑADIR IMAGENES---------------------------------------------

img=PhotoImage(file="TITI.png")
lblimg=Label(miframe, image=img).place(x=0,y=0)


#------------------CREAR OTRA VENTANA----------------------------------

def crear_ventana():
    ventana=Toplevel(root) #Toplevel(raiz) crea una ventana nueva para interactuar
    texto1=Label(ventana, text="BIENVENIDOS AL PROGRAMA DEL JUANITO")
    texto1.grid(row=0, column=0)
    varoption=IntVar()
    botoncircular=Radiobutton(ventana, text="masculino", variable=varoption, value=1)
    botoncircular.grid(row=4, column=1, pady=4, padx=4)
    botoncircular2=Radiobutton(ventana, text="femenino ", variable=varoption, value=2)
    botoncircular2.grid(row=5, column=1, pady=4, padx=4)
    
#------------------VENTANAS EMERGENTES------------------------------------



#--------------------------ABRIR O GUARDAR FICHEROS------------------------


def guardarfichero():
    fichero=filedialog.asksaveasfile(title="Guardar")#conectado al menu archivo/guardar

def imprim():
    text1=cuadrotexto.get()
    print(text1)
    text2=cuadrotexto2.get()
    print(text2)

#-------------------------MENÚS DE ARRIBA---------------------------------------------


#-------------------------CUADROS DE TEXTO---------------------------------

cuadrotexto=Entry(miframe)
cuadrotexto.grid(row=0, column=1, pady=5)
cuadrotexto.config(fg="blue", justify="center")

cuadrotexto2=Entry(miframe)
cuadrotexto2.grid(row=1, column=1, pady=5)
cuadrotexto2.config(fg="black", justify="center", font="Helvetica 10")

#--------------------------CUADROS DE COMENTARIOS----------------------------



#----------------------TEXTOS-----------------------------------------------------------

usuario=Label(miframe, text="nombre: ")
usuario.grid(row=0, column=0, pady=5)

contrasena=Label(miframe, text="edad: ")
contrasena.grid(row=1,column=0, pady=5)


#-------------------------BOTONES UNICA OPCION-------------------------------



#-------------------BOTONES--------------------------------------------------------

boton1=Button(miframe, text="entrar", command =crear_ventana)
boton1.grid(row=4, column=0)

boton=Button(miframe, text="guardar", command=guardarfichero)   #COMMAND redirige a una funcion para realizar una accion
boton.grid(row=4,column=1)

boton2=Button(miframe, text="imprimir", command=imprim) 
boton2.grid(row=4,column=2)


root.mainloop()
