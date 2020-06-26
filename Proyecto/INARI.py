from Tkinter import *
import tkMessageBox
import sqlite3


#metodo para insertar valores en la base de datos
def Insertar_en_DB(Nombre,Email,telefono,tipoPedido):
        lista=[telefono,Nombre,Email,telefono,tipoPedido]#se crea una lista con los valores recibidos por parametro
        conn=sqlite3.connect('INARI_DB.db')#se hace la coneccion a la base de datos
        c=conn.cursor()#se crea el cursor
        c.execute('INSERT INTO Panel VALUES(?,?,?,?,?)',lista)#se inserta en la base de datos la lista con los datos
        conn.commit()#commit de la base de datos
        conn.close()#cerrar la base de datos

        #mensaje de el id de la orden(telefono)
        tkMessageBox.showinfo("","ID de la Orden :"+str(telefono))
        #print (c.execute('select * from INARI_DB'))
        #print (row)

#metodo para borrar datos d ela base de datos
def Borrar_en_DB(pid):
        conn=sqlite3.connect('INARI_DB.db')#se hace la coneccion
        c=conn.cursor()#se crea el cursor
        lpid=[pid]#se pasa el id que viene por parametro
        c.execute('select * from Panel  where ID=(?)',lpid)#se selecciona la fila donde coincide el id
        list1=c.fetchmany()#obtiene la fila en la posicion del id indicado
        print (list1)#mostrar la lista(de los datos a borrar de esa fila) en consola
        c.execute('insert into Cancelado values (?,?,?,?,?)',list1[0])#se inserta los datos en una tabla de datos borrados(pedidos cancelados)
        c.execute('delete from Panel where ID=(?)',lpid)#borra los datos finalmente de la fila donde se indica el id

        #mostrar mensaje de que la orden ha sido cancelada
        tkMessageBox.showinfo("","ID de la orden:  "+str(pid)+" ha sido candelada!")
        conn.commit()#commit final de la base de datos
        conn.close()#cerrar base de datos


def cancelar_pedido():

        root=Tk()
        root.title("Cancelar Pedido")

        #variable comando para borrar pedido en base de datos
        command=lambda :Borrar_en_DB(Entry_1.get())

        #elementos
        label_1=Label(root,text="ID del pedido")
        Entry_1=Entry(root,width=50)
        Button_1=Button(root,text="Cancelar pedido",command=command)

        #posicion de lementos
        label_1.grid(row=2,column=2,padx=10,pady=10)
        Entry_1.grid(row=2,column=3,padx=10,pady=10,columnspan=3)
        Button_1.grid(row=4,column=2,padx=10,pady=10)

        root.mainloop()

#esta funcion destruye ventanas,se pasa la ventana por parametro
def destruir_ventana(root):
        root.destroy()


def vendedor():
        #configuraciones basicas de la ventana
        root=Toplevel()
        root.configure(background="Orange red")
        RTitle=root.title("Vendedor")
        RWidth=900
        RHeight=500
        root.geometry(("%dx%d")%(RWidth,RHeight))

        #Label titulo
        LabelTitulo = Label(root,text="INARI ADMIN",font=("AndaleMono",35,"bold"))
        LabelTitulo.grid(row=0,column=2)

        #variables comando para ejecutar ventanas
        command=lambda :Ordenar_pedido()
        command1=lambda :cancelar_pedido()
        command2=lambda :pedidos_realizados()
        command3=lambda :ordenes_canceladas()
        command4=lambda :destruir_ventana(root)

        #activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",14,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5,
        #crear botones
        Button_1=Button(root,text="Nuevo pedido",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5,command=command)
        Button_2=Button(root,text="Cancelar pedido",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5, command=command1)
        Button_3=Button(root,text="Pedidos\n realizados",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5,command=command2)
        Button_4=Button(root,text=" Pedidos\n Cancelados",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5,command=command3)

        #botones nuevos,hay que agregarles las variales commando
        Button_5=Button(root,text="Mostrar Caja",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5)
        Button_6=Button(root,text="  Despachar \npedidos",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5)


        Button_7=Button(root,text="Salir",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=5,height=2,command=command4)

        #posicionar botones
        Button_1.grid(row=1,column=1,padx=60,pady=70)
        Button_2.grid(row=1,column=2,padx=60,pady=70)
        Button_3.grid(row=1,column=3,padx=60,pady=70)
        Button_4.grid(row=2,column=1,padx=60,pady=5)
        Button_5.grid(row=2,column=2,padx=60,pady=5)
        Button_6.grid(row=2,column=3,padx=60,pady=5)

        #boton salir
        Button_7.grid(row=0,column=3,padx=60,pady=10)
        root.mainloop()

#Ventana Main
def main():
        root=Tk()
        root.configure(background="orange red")
        RTitle=root.title("Delivery Sushi")

        #Label titulo
        LabelTitulo = Label(root,text="INARI SUSHI",font=("AndaleMono",50,"bold"))
        #LabelTitulo.grid(row=0,column=2,padx=3,pady=10)
        LabelTitulo.place(x= 140,y =30)

        #asignan variables de ancho y alto y se colocan en geometry
        RWidth=700
        RHeight=400
        root.geometry(("%dx%d")%(RWidth,RHeight))

        #variables comandos que ejecutan ventanas
        command=lambda :vendedor()
        command_1=lambda :cliente()

        #botones
        Button_1=Button(root,text="Vendedor",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",14,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5,command=command)
        Button_2=Button(root,text="Cliente",activebackground="khaki1",relief=SUNKEN,font=("AndaleMono",14,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5,command=command_1)
        #Button_1.grid(row=1,column=1,padx=5,pady=140)
        #Button_2.grid(row=1,column=2,padx=6,pady=140)
        Button_1.place(x= 50,y =180)
        Button_2.place(x=460,y =180)


        root.mainloop()

main()

def Ordenar_pedido():
        #configuracion basica de la ventana
        root2=Tk()
        root2.configure(background="Orange red")
        RTitle=root2.title("Nueva Orden")
        RWidth=900
        RHeight=400
        root2.geometry(("%dx%d")%(RWidth,RHeight))
        var1=IntVar() #en caso de error descomentar

        #etiquetas
        label_1=Label(root2,text="Nombre")
        label_2=Label(root2,text="Pedido")
        label_3=Label(root2,text="E-Mail")
        label_4=Label(root2,text="Telefono")
        label_5=Label(root2,text="Cantidad:")
        label_AG=Label(root2,text="Carrito:")



        #(lista) de opciones
        Opciones = [
            "Sushi bandeja basica (400 ARs)",
            "Sushi bandeja mediana (900 ARs)",
            "Sushi bandeja completa (900 ARs)"
        ]

        Cantidad = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
        ]



        #para las opciones----------------
        #crea na variable para alojar string
        variable = StringVar(root2)
        #guarda la lista en una variable de tipo string var(como un vector)
        variable.set(Opciones[0]) # valor defecto

        #crea el menu deplegable
        w = OptionMenu( *(root2, variable) + tuple(Opciones))
        w.grid(row=3,column=3,padx=10,pady=10)#se posiciona

        #para la cantidad--------------------
        #crea na variable para alojar string
        variableCantidad = StringVar(root2)
        #guarda la lista en una variableCantidad de tipo string var(como un vector)
        variableCantidad.set(Cantidad[0]) # valor defecto

        #crea el menu deplegable
        w = OptionMenu( *(root2, variableCantidad) + tuple(Cantidad))
        w.grid(row=3,column=9,padx=10,pady=10)#se posiciona


        #crea los campos de texto
        Entry_1=Entry(root2,width=50)
        Entry_2=Entry(root2,width=50)
        Entry_3=Entry(root2,width=50)

        #boton_1 "ordenar"
        #crea una variable comando la cual llama a la funcion Insertar_en_DB y le pasa los campos de texto
        #por parametro y se ejecuta al presionar el boton_1
        command=lambda :Insertar_en_DB(Entry_1.get(),Entry_2.get(),Entry_3.get(),variable.get())

        #el boton ordenar ejecuta la variable comando y esta ingresa datos en la base de datos
        Button_1=Button(root2,text="Ordenar",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",14,"bold"),bg="white",fg="black",borderwidth=4,width=7,height=3,command=command)

        #boton_AG "agregar al carrito", le falta el command
        Button_AG=Button(root2,text="Agregar al carrito",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",10,"bold"),bg="white",fg="black",borderwidth=4,width=17,height=2)


        #Labels para identificar los campos de texto y el OptionMenu
        label_1.grid(row=2,column=2,padx=10,pady=10)
        label_2.grid(row=3,column=2,padx=10,pady=10)
        label_3.grid(row=4,column=2,padx=10,pady=10)
        label_4.grid(row=5,column=2,padx=10,pady=10)
        label_5.grid(row=3,column=6,padx=10,pady=10)
        label_AG.grid(row=4,column=10,padx=10,pady=10)

        #posicionamiento de entradas(campo de texto) y boton
        Entry_1.grid(row=2,column=3,padx=10,pady=10,columnspan=3)
        Entry_2.grid(row=4,column=3,padx=10,pady=10,columnspan=3)
        Entry_3.grid(row=5,column=3,padx=10,pady=10,columnspan=3)
        Button_1.grid(row=6,column=2,padx=10,pady=10)
        Button_AG.grid(row=3,column=10,padx=10,pady=10)

        #agregar codigo para mostrar la lista del carrito,hacer con una lista y mostrarla con un for,
        #en el boton AG,hacer el comand para guardar los valores elegios en una lista y que la agrege la la lista
        # y la muestre, todo en una funcion que la va a ejecutar el command del boton AG

        root2.mainloop()

#ventana cliente
def cliente():
        #configuracion base de la ventana
        root=Toplevel()
        root.configure(background="orange red")
        RTitle=root.title("Cliente")
        RWidth=900
        RHeight=500
        root.geometry(("%dx%d")%(RWidth,RHeight))

        #Label titulo
        LabelTitulo = Label(root,text="INARI SUSHI\nBienvenido!!!",font=("AndaleMono",50,"bold"))
        #LabelTitulo.grid(row=0,column=2,padx=3,pady=10)
        LabelTitulo.place(x= 140,y =30)

        #variables comando para abrir ventanas
        command=lambda :Ordenar_pedido()
        command1=lambda :cancelar_pedido()
        command2=lambda :track_pizza()
        command4=lambda :destruir_ventana(root)


        #activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",14,"bold"),borderwidth=4,
        #crear botones
        Button_1=Button(root,text="Nuevo Pedido",activebackground="khaki1",relief=SUNKEN,font=("AndaleMono",14,"bold"),borderwidth=4,bg="white",fg="black",width=14,height=5,command=command)
        Button_2=Button(root,text="Cancelar Pedido",activebackground="khaki1",relief=SUNKEN,font=("AndaleMono",14,"bold"),borderwidth=4,bg="white",fg="black",width=14,height=5,command=command1)
        Button_3=Button(root,text="Track Pedidos",activebackground="khaki1",relief=SUNKEN,font=("AndaleMono",14,"bold"),borderwidth=4,bg="white",fg="black",width=14,height=5,command=command2)
        Button_4=Button(root,text="Salir",activebackground="khaki1",relief=SUNKEN,font=("AndaleMono",14,"bold"),borderwidth=4,bg="white",fg="black",width=5,height=2,command=command4)

        #posicionamiento de botones
        Button_1.grid(row=2,column=1,padx=55,pady=250)
        Button_2.grid(row=2,column=2,padx=55,pady=250)
        Button_3.grid(row=2,column=3,padx=55,pady=250)

        #boton salir
        Button_4.grid(row=1,column=3,padx=30,pady=10)

        root.mainloop()
