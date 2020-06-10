from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

"""
todo esta hecho por funciones, la primera funcion en ejecutarse es login,esta en su boton registrar tiene
un command que ejecuta la funcion registrar que abre la interface registrar; en el boton de loguear hay
un command que ejecuta una funcion validador,en la funcion validador si todo esta bien ejecuta la funcion 
de la interfaz del programa final.

Nombres de las interfaces raiz:
ventanap == ventana de login
ventana2 == ventana registrar
ventana3 == ventana del programa

El programa se  basa en funciones por lo que no se termina hasta que no lo cerrar,salta de una funcion
a otra.
tambien las interfaces no las empaqueto porque algunos items se buguean,creo todo en la interfaz raiz,
tampoco creo frames porque tambien da error en algunas cosas por eso hago todo en la interfaz raiz.
tampoco coloco fondos de pantalla,ni iconos, ni nada que tenga que ver con importar imagenes porque da error

la base de datos utilizada es sqlite3 y un programa llamado db browser para hacer la base de datos sin codigo

para pasar de la ventana login,ingresar una "a" en el label user para acceder al programa,la ventana
registro no registra nada porque falta que guarde los datos en la db y demas...., al igual que el resto
de interfaces,les falta la conexion con la base de datos para funcionar bien
"""

class Program:

    def login1(self):

        # en las demas funciones que crean las interfaces,como primer linea lo que hago es
        # cerrar las demas ventanas como lo hago en las siguientes lineas, lo pongo en un try,catch
        #porque si la ventana que queres cerrar no esta abierta,esta da error y con el try cerrar si esta
        # la ventana abierta,sino no esta no pasa nada y el programa sigue
        #en caso de tener abierta la ventana registro cerrala
        try:
            self.cerrarV(self.ventana2)
        except :
            pass

        self.ventanap = Tk()
        self.ventanap.config(width=450, height=270)
        self.ventanap.title("Login user")
        #self.ventanap.iconbitmap("imagenes/icono.ico")
        self.ventanap.resizable(0, 0)

        
        """
        #No colocar porque da bugs y errores,es mejor sin fondo
        #fondo de imagen
        self.img1 = PhotoImage(file="imagenes/interFondo.png")
        self.fondo = Label(self.ventanap, image=self.img1,
                           relief=RAISED)
        self.fondo.place(x=0, y=0)
        """

        

        #label user
        self.user = Label(self.ventanap, text="Usuario: ", bg="black",
                          fg="azure", font=("Comic Sans MS", 13),anchor="center").place(x=50, y=40)

        #campo de texto user
        self.userText = StringVar()                  
        self.userIn = Entry(self.ventanap, textvariable=self.userText,bg="black",
                            fg="azure", font=("Courier", 13),borderwidth=5).place(x=50, y=80)
        #self.userIn =StringVar(Entry(self.self.ventanap,bg="black",fg="white",font=("Arial",13)).place(x=50,y=80))

        # label password y textfield
        self.password = Label(self.ventanap, text="Contraseña: ",
                              bg="black", fg="azure", font=("Comic Sans MS", 13),anchor="center").place(x=50, y=130)
        
        #campo de texto password
        self.passTexto=StringVar()
        self.passIn = Entry(self.ventanap,textvariable=self.passTexto, show="*", bg="black",
                            fg="azure", font=("Arial", 13),borderwidth=5).place(x=50, y=170)

        # crear boton loguear
        self.login = Button(self.ventanap, text="Loguear", bg="black", fg="cyan", font=(
            "Arial", 16),borderwidth=4 ,command=self.validarUser).place(x=50, y=220)
        
        # crear boton registrar
        self.reg = Button(self.ventanap, text="Registrar", bg="black", fg="cyan", font=(
            "Arial", 16),borderwidth=4, command=self.registrar).place(x=200, y=220)

         
        self.ventanap.mainloop() 
    def registrar(self):
        #cerrar ventana principal
        self.cerrarV(self.ventanap)

        self.ventana2 = Tk()
        self.ventana2.config(width=420, height=610)
        self.ventana2.resizable(0, 0)
        self.ventana2.title("Register user")
        #self.ventana2.iconbitmap("imagenes/icono.ico")
        
        """
        #No colocar porque da bugs y errores,es mejor sin fondo
        # fondo de imagen
        self.img = PhotoImage(file="imagenes/fondoRegister.png")
        self.fondo = Label(self.ventana2, image=self.img,
                           relief=RAISED)
        self.fondo.place(x=-3, y=-2)
        """

        

        # label user
        self.user = Label(self.ventana2, text="Usuario: ", bg="black",
                          fg="azure", font=("Comic Sans MS", 13)).place(x=(190-7), y=40)
        
        #campo de texto user
        self.userTextR=StringVar()
        self.userIn = Entry(self.ventana2, textvariable=self.userTextR,bg="black",
                            fg="azure", font=("Courier", 13),borderwidth=3).place(x=(120-7), y=80)
                          

        # label password
        self.password = Label(self.ventana2, text="Contraseña: ", bg="black",
                              fg="azure", font=("Comic Sans MS", 13)).place(x=(175-7), y=140)
        
        # campo de texto password
        self.passTextoR=StringVar()
        self.passIn = Entry(self.ventana2, textvariable= self.passTextoR, show="*", bg="black",
                            fg="azure", font=("Arial", 13),borderwidth=3).place(x=(132-7), y=180)

        # re password label
        self.password2 = Label(self.ventana2 ,text=" Repetir contraseña: ",
                               bg="black", fg="azure", font=("Comic Sans MS", 13)).place(x=(140-7), y=230)
        
        # campo de texto RePassword
        self.passTextoR2=StringVar()
        self.passIn2 = Entry(self.ventana2, textvariable= self.passTextoR2, show="*",  bg="black",
                             fg="azure", font=("Arial", 13),borderwidth=3).place(x=(132-7), y=270)

        #boton registro
        self.regist = Button(self.ventana2, text="Registrar", bg="black",
                             fg="cyan", font=("Comic Sans MS", 40), borderwidth=7,command=self.validarRegistro)
        self.regist.place(x=70, y=350)

        self.ventana2.mainloop() 
    def Programa(self):

        #cerrar las posibles ventanas abiertas
        try:
            self.cerrarV(self.ventana2)
        except:
            self.cerrarV(self.ventanap)
 
        self.ventana3 = Tk()
        self.ventana3.geometry("800x600")
        self.ventana3.resizable(False, False)

        interfaz3 = Frame(self.ventana3)
        interfaz3.config(width=800, height=600)

        interfaz3.config(cursor="hand2")
        self.ventana3.title("programa")
        #self.ventana3.iconbitmap("imagenes/icono.ico")

        """
        #No colocar porque da bugs y errores,es mejor sin fondo
        # fondo de imagen
        img = PhotoImage(file="imagenes/fondo.png")
        fondo = Label(self.ventana3, image=img,
                      relief=RAISED)#.place(x=-3, y=-2)
        """             
        


        # codigo botones

        def codigoBotonMostrar():
            self.texto.delete(1.0, END)
            self.texto.insert("insert", "boton mostrar-anda")

        def codigoBotonGuardar():
            self.texto.delete(1.0, END)
            self.texto.insert("insert", "boton guardar-anda")


        # botones
        mostrar = Button(self.ventana3, text="Mostrar", bg="black", fg="cyan", font=("Comic Sans MS",
            12),borderwidth=3, command=codigoBotonMostrar).place(x=590, y=250)
        guardar = Button(self.ventana3, text="Guardar", bg="black", fg="cyan", font=("Comic Sans MS",
            12),borderwidth=3, command=codigoBotonGuardar).place(x=680, y=250)

        
        #self.textoT=StringVar()
        self.texto = Text(self.ventana3, width=33, height=5, bg="white", fg="black", font=("Consolas",30))
        #texto.place(x=38,y=300)#correcto pos
        #le saque el textvariable=slef.textoT

        #insertar texto al final, tambien se puede usar 0.0 para el principio
        #self.texto.insert(tk.END,"aaaa")
        #self.texto.insert(tk.END,"eeeeeee")
        #self.texto.insert(tk.END,"\npppppppp")
        


        # correcto posicion de scroll/texto
        self.texto.grid(row=3, column=2, pady=300, padx=38)
        

        scrollYComentarios = Scrollbar(self.ventana3, command=self.texto.yview)

        scrollYComentarios.grid(row=3, column=2, pady=300, padx=38, sticky="nse")
        #scrollYComentarios.grid(row=4, column=1,sticky="nse")


        self.texto.config(yscrollcommand=scrollYComentarios.set)

        interfaz3.mainloop()
