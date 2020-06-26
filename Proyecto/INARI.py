rom Tkinter import *
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
