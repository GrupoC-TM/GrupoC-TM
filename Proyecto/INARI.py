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
