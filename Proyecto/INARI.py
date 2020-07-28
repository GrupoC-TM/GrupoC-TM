#La sintaxis del import varia segun la version de Tkinter/Python
"""Tener en cuenta!!!,el programa no da errores pero si se produce error de coneccion
    de base de datos o de imagen no encontrada, puede ser la version de linux,
    en este caso debe colocar el archivo .db y la imagen en la carpeta Documentos de su pc.
    para evitar otro tipo de errores como el de 'modulo tkinter no encontrado' puede que no
    tenga instalado este modulo o su version sea vieja,depende de la version cambia el import
    de las siguientes 2 lineas comentadas, sino seguir las instrucciones del informe para instalarlo """
#from tkinter import *
#import tkinter as tk
from Tkinter import *
import Tkinter as tk
import tkMessageBox
import sqlite3
from Bandeja import *
from Pedidos import *


#metodo para insertar valores en la base de datos
def Insertar_en_DB(Nombre,Email,Telefono,Pedido,Costo,pagoCon,Estado,Direccion):

        #se crea una lista con los valores recibidos por parametro
        #en este caso el ID(posicion 1) es el mismo que el telefono para
        #que el usuario no se olvide de su id al momento de ver el estado de su pedido
        lista=[Telefono,Nombre,Email,Telefono,Pedido,Costo,pagoCon,Estado,Direccion]

        #se hace la coneccion a la base de datos
        conn=sqlite3.connect('INARI_DB.db')

        #se crea el cursor
        c=conn.cursor()#se crea el cursor

        #se inserta en la base de datos la lista con los datos
        c.execute('INSERT INTO Panel VALUES(?,?,?,?,?,?,?,?,?)',lista)

        #se crea el commit para guardar los cambios
        conn.commit()

        #cerrar la base de datos
        conn.close()

        #mensaje de que se ha realizado la orden con exito!
        """tkMessageBox.showinfo(
            "", "Orden realizada! \nID de la Orden: "+str(Telefono))"""
        #print (c.execute('select * from INARI_DB'))
        #CONSOLA_MOSTRAR



#funcion para insertar en la tabla estado del id y estado de un pedido cuando es despachado
def insertar_en_Estado(ID,Estado,total):

    #se pasan las variables a una lista porque sino el INSERT a la db da error
    lista=[ID,Estado,total]

    #se crea la variable coneccion
    conn=sqlite3.connect('INARI_DB.db')

    #se crea el cursor
    c=conn.cursor()

    #se ejecuta el ingreso(INSERT) a la base de datos,pasandole la lista con close
    #datos en el orden en que deben ser ingresados
    c.execute('INSERT INTO Estado VALUES(?,?,?)',lista)

    #commit de la base de datos
    conn.commit()

    #cerrar la base de datos
    conn.close()
    #CONSOLA_MOSTRAR

#metodo para borrar datos de la base de datos
def Borrar_en_DB(pid):

        #se crea la variable coneccion
        conn=sqlite3.connect('INARI_DB.db')

        #se crea el cursor
        c=conn.cursor()

        #se pasa el id( pid ) que viene por parametro en la funcion a la lista
        lpid=[pid]

        #se intenta borrar en la db, tabla Panel
        try:

            #obtener en panel
            #se selecciona la fila donde coincide el id ( lpid )
            c.execute('select * from Panel  where ID=(?)',lpid)

            #fetchmany obtiene la fila  en la posicion que indicamos arriba con el cursor
            list1=c.fetchmany()

            #CONSOLA_MOSTRAR
            print (list1)#mostrar la lista(de los datos a borrar de esa fila) en consola

            #se inserta los datos en una tabla de datos borrados(pedidos cancelados)
            #tabla Cancelado para despues mostrar una lista de pedidos cancelados
            c.execute('insert into Cancelado values (?,?,?,?,?,?,?,?,?)',list1[0])

            #borra los datos finalmente de la fila donde se indica el id ( lpid )
            #tabla Panel (principal)
            c.execute('delete from Panel where ID=(?)',lpid)

            #y de Estado tambien
            c.execute('delete from Estado where ID=(?)',lpid)

            #mostrar mensaje de que la orden ha sido cancelada
            tkMessageBox.showinfo(
                "", "ID de la orden:  "+str(lpid)+" ha sido cancelada!")
            #print("ID de la orden:  "+str(lpid)+" ha sido cancelada!")

            #commit final de la base de datos
            conn.commit()

            #cerrar base de datos
            conn.close()

        #en caso de que no exista el ID en la tabla principal puede que el pedido1
        #ya haya sido despachado,al despachar se envia el id y estado modificado
        #a otra tabla (Estado) para que el usuario vea el estado del pedido.
        #entonces borramos de esta tabla tambien el pedido
        except IndexError as e:

            try:


                #se crea la variable coneccion
                conn=sqlite3.connect('INARI_DB.db')

                #se crea el cursor
                c=conn.cursor()

                #-------------------------------------------------------------------------------------------------------
                #validar que existe el num en la tabla estado

                #obtener en Estado
                #se selecciona la fila donde coincide el id ( lpid )
                c.execute('select * from Estado where ID=(?)',lpid)

                #fetchmany obtiene la fila  en la posicion que indicamos arriba con el cursor
                list3=c.fetchmany()

                #CONSOLA_MOSTRAR
                print (list3[0][0])#mostrar la lista(de los datos a borrar de esa fila) en consola
                print(lpid)

                if(list3[0][0] == int(lpid[0])):



                    #falta agregar el total
                    #-------------------------------------------------------------------------------------------------------

                    listCanceladoCamino=[(pid),("-"),("-"),(pid),("cancelado en el\ncamino"),(0),(0),(0),(0)]
                    #listCanceladoCamino=[[pid],["Cancelado"],["en"],["el"],["camino"],["-"],["-"],["-"],["-"]]

                    #enviar a lista cancelado si se cancela en el camino
                    c.execute('insert into Cancelado values (?,?,?,?,?,?,?,?,?)',listCanceladoCamino)

                    #borrar en estado, en la posicion del id ( pid )
                    c.execute('delete from Estado where ID=(?)',lpid)

                    #refuerzo para que borre bien
                    #c.execute('delete from Estado where ID=(?)',lpid)

                    #commit final de la base de datos
                    conn.commit()

                    #cerrar base de datos
                    conn.close()

                    tkMessageBox.showinfo("","ID de la orden:  "+str(lpid)+" ha sido cancelada!")
                    print("ID de la orden:  "+str(lpid)+" ha sido cancelada!")
                else:
                    tkMessageBox.showinfo("","ID de la orden:  "+str(lpid)+" \n no existe o ya ha sido cancelado")
                    print("ID de la orden:  "+str(lpid)+" \n no existe o ya ha sido cancelado")
            #en caso de que no exista en ninguna de las tablas entonces el id ingresado
            #es incorrecto,por lo tanto no existe pedido con ese id
            except Exception as e:
                print("ID de la orden:  "+str(lpid)+" \n no existe o ya ha sido cancelado")
                tkMessageBox.showinfo(
                    "", "ID de la orden:  "+str(lpid)+" \n no existe o ya ha sido cancelado")


def cancelar_pedido():

        root=Tk()
        root.title("Cancelar Pedido")

        #variable comando que ejecuta la funcion para borrar en db y le pasa el id por
        #parametro
        command=lambda :Borrar_en_DB(Entry_1.get())

        #elementos de la interfaz
        label_1=Label(root,text="ID del pedido")
        Entry_1=Entry(root,width=50)

        #ejecuta el command anterior
        Button_1=Button(root,text="Cancelar pedido",command=command)

        #posicion de elementos
        label_1.grid(row=2,column=2,padx=10,pady=10)
        Entry_1.grid(row=2,column=3,padx=10,pady=10,columnspan=3)
        Button_1.grid(row=4,column=2,padx=10,pady=10)


        root.mainloop()


#funcion que muestra la interfaz de pedidos realizados
def pedidos_realizados():
        #configuracion basica de la ventana
        root1=Tk()
        root1.configure(background="orange red")
        RTitle=root1.title("Pedidos realizados")
        RWidth=1350
        RHeight=900
        root1.geometry(("%dx%d")%(RWidth,RHeight))


        #etiqueta del titulo
        label_1=Label(root1,text="Descripcion de pedidos realizados:",fg="white",bg="black")
        label_1.place(x=20,y=15)

        #variable de coneccion a la base de datos
        conn=sqlite3.connect('INARI_DB.db')

        #variable cursor
        c=conn.cursor()

        #variable contador,se usara mas adelante para mostrar las etiquetas
        #una posicion mas abajo x c/u
        n=6

        #etiquetas y sus posicionamientos
        label_2=Label(root1,text="ID:")
        label_2.grid(row=4,column=0,padx=30,pady=10)

        label_3=Label(root1,text="Nombre:")
        label_3.grid(row=4,column=1,padx=30,pady=10)

        label_4=Label(root1,text="EMAIL:")
        label_4.grid(row=4,column=2,padx=10,pady=10)

        label_5=Label(root1,text="Telefono:")
        label_5.grid(row=4,column=3,padx=20,pady=10)

        label_6=Label(root1,text="Pedido:")
        label_6.grid(row=4,column=4,padx=5,pady=10)

        label_7 = Label(root1,text="Total:")
        label_7.grid(row=4,column=5,padx=90,pady=10)

        label_8 = Label(root1,text="Direccion:")
        label_8.grid(row=4,column=6,padx=10,pady=10)

        label_9 = Label(root1,text="Estado:")
        label_9.grid(row=4,column=7,padx=10,pady=10)

        # For each que muestra los pedidos realizados hasta el final.
        # Obtiene el panel completo y la variable row1 es una fila del Panel
        # Que baja por cada vuelta del for y obtiene sus datos
        print("\nPedidos realizados:")
        for row1 in c.execute('select * from Panel'):
                n+=1

                # ID
                label_10=Label(root1,text=str(row1[0]),justify="left")
                label_10.grid(row=n,column=0,padx=0,pady=10)
                print("--------------------------------------------------------------------")
                print("\nID: "+str(row1[0]))

                # Nombre
                label_11=Label(root1,text=str(row1[1]))
                label_11.grid(row=n,column=1,padx=10,pady=10)
                print("Nombre: "+str(row1[1]))

                # EMAIL
                label_12=Label(root1,text=str(row1[2]))
                label_12.grid(row=n,column=2,padx=10,pady=10)
                print("Email: "+str(row1[2]))

                # Telefono
                label_13=Label(root1,text=str(row1[3]))
                label_13.grid(row=n,column=3,padx=10,pady=10)
                print("Telefono: "+str(row1[3]))

                # Pedido + costo
                label_14=Label(root1,text=str(row1[4])+" \nPaga Con:"+str(row1[6]))
                label_14.grid(row=n,column=4,padx=5,pady=10)
                print("Pedido: "+str(row1[4]))
                print("Paga Con:"+str(row1[6]))

                # Total
                label_15=Label(root1,text=str(row1[5]))
                label_15.grid(row=n,column=5,padx=10,pady=10)
                print("Total: "+str(row1[5]))

                # Direccion
                label_16=Label(root1,text=str(row1[8]))
                label_16.grid(row=n,column=6,padx=10,pady=10)
                print("Direccion: "+str(row1[8]))

                # Estado
                label_17=Label(root1,text=str(row1[7]))
                label_17.grid(row=n,column=7,padx=10,pady=10)
                print("Estado: "+str(row1[7]))
                print("--------------------------------------------------------------------")




        # Etiqueta despachar
        label_18=Label(root1,text="Despachar el pedido con el ID:",fg="white",bg="black")
        label_18.grid(row=2,column=6,padx=10,pady=10)

        # Se crea lista de ides
        listaID = []

        # Agarrar todo los ides de los pedidos y alojarlos en la listaID
        # Tabla Panel
        for id in c.execute('select * from Panel'):

        # Los ides estan en la posicion 0 de la tabla Panel

            listaID += [id[0]]


        # Crea una variable string var para alojar los id en forma de string
        variable = StringVar(root1)

        # Guarda el primer id de la lista
        # Valor por defecto el 0 para que el menu desplegable muestra el primer id
        # Cuando no se selecciona ninguna opcion
        try:
            variable.set(listaID[0])

            # Crea el menu deplegable de ID
            # Se pasa la variable de por defecto y  se le agrega una tupla con todos los ID
            w = OptionMenu( *(root1, variable) + tuple(listaID))
            w.grid(row=2,column=7,padx=10,pady=10)# Se posiciona

        except Exception as e:
            tkMessageBox.showinfo(
                "", "no hay ningun pedido realizado! :(")
            print("no hay ningun pedido realizado! :(")





        # Command del boton  para despachar pedidos(funcion estado())
        commanDesp = lambda: estado()

        # Se crea el boton despachar
        BotonDespachar=Button(root1,text="Despachar",activebackground="DeepSkyBlue3",command=commanDesp)
        BotonDespachar.grid(row=2,column=8,padx=10,pady=10)

        # Funcion para modificar el estado y despachar de la lista de pedidos
        def estado():

            #For each que se trae todo de Estado y recorre cada fila con el objeto "id"
            for id in c.execute('select * from Estado'):

                # Si el id actual es igual al id seleccionado
                if(id[0]==int(variable.get())):

                    # Guardo en una lista el estado y el id para el update,ya que solo recibe 2 parametros el execute
                    list3=["En camino",id[0]]#Id actual

                    # Actualizo el estado del pedido y le paso la lista
                    c.execute('UPDATE Estado SET estado = (?) where ID = (?)',list3)

                    # Commit final de la base de datos
                    conn.commit()

            # Eliminar el pedido de la lista de pedidos al apretar el boton despacharPedido
            # For each que se trae todo de panel y recorre cada fila con el objeto id
            for id in c.execute('select * from Panel'):

                # Si el id actual es igual al id seleccionado
                if(id[0]==int(variable.get())):

                    # Siempre tengo que hacer una lista porque sino la base de datos da error
                    # Insertar una lista
                    listNum=[id[0]]

                    # Borro de Panel la fila en la cual tengo el id en la listaNum
                    c.execute('DELETE FROM Panel where ID =  (?)',listNum)

                    # Commit final de la base de datos
                    conn.commit()

                    tkMessageBox.showinfo("", "ID de la Orden :"+str(
                        listNum)+" ha sido despachado!\n vuelva a entrar a 'Pedidos realizados' para actualizar los datos!")
                    print("ID de la Orden :"+str(
                        listNum)+" ha sido despachado!\n vuelva a entrar a 'Pedidos realizados' para actualizar los datos!")

        #cerrar la coneccion,no cerrar sino va a dar error,se cierra mas arriba
        #conn.close()

        root1.mainloop()


'''
#funcion que dejo para mostrar como agregar una imagen
def img():
        #si queres se crea una ventana
        root=Toplevel()
        root.configure(background="orange")
        RTitle=root.title("probar")
        RWidth=900
        RHeight=500
        root.geometry(("%dx%d")%(RWidth,RHeight))

        #y aca le pegas la imagen
        #las siguiente lineas son para colocar una imagen!!!
        im = Image.open(file="inari.gif")
        tkimage = ImageTk.PhotoImage(im)
        myvar=tkinter.Label(root,image = tkimage)
        myvar.place(x=0, y=0, relwidth=1, relheight=1)


        root.mainloop()
'''




# ver el estado del pedido
def track_pedido():

        # crea la ventana
        root=Tk()
        RTitle=root.title("Estado del pedido")

        # etiqueta
        label_1=Label(root,text="ID del pedido")
        label_1.grid(row=2,column=2,padx=10,pady=10)

        # campo de texto
        Entry_1=Entry(root,width=50)
        Entry_1.grid(row=2,column=3,padx=10,pady=10,columnspan=3)

        # variable comando para el boton,la siguiente funcion verifica que exista el id del pedido
        # y se le pasa por parametro el id que se ingresa en el campo de texto
        command2=lambda :traerEstado(Entry_1.get())

        # boton de trackeo de orden
        Button_1=Button(root,text="Verificar",command=command2)
        Button_1.grid(row=4,column=2,padx=10,pady=10)

        # conectar con la base de datos
        conn=sqlite3.connect('INARI_DB.db')#variable de coneccion a la base de datos

        # variable cursor
        c=conn.cursor()

        print("\nEstado del pedido:")

        #mostrar estado del pedido
        def traerEstado(id):

            #si el pedido esta, cambia a true
            validador = FALSE

            #buscar en db la columna del id en la tabla Estado
            for columna in c.execute('select * from Estado'):

                #busca en cada fila si en la columna 0 existe el id ingresado
                if (columna[0] == int(id)):
                    print(columna[0])#se muestra en consola para verificar

                    tkMessageBox.showinfo("","Su pedido esta :"+str(columna[1])+" :D")
                    print("Su pedido esta :"+str(columna[1])+" :D")

                    #el validador cambia a true para que no se ejecute el if siguiente
                    validador=TRUE

            #si no existe ningna orden con el id ingresado, se ejecuta el siguiente mensaje
            if(validador==FALSE):
                tkMessageBox.showinfo(
                    "", "No existe ningun pedido con el id :  "+str(id))
                print("No existe ningun pedido con el id :  "+str(id))


        #cerrar la coneccion,no cerrar sino da error
        #conn.close()

        root.mainloop()



#funcion que muestra las ordenes canceladas
def ordenes_canceladas():
        #Configuracion basica de la ventana
        root1=Tk()
        root1.configure(background="orange red")
        RTitle=root1.title("Ordenes Canceladas")
        RWidth=750
        RHeight=700
        root1.geometry(("%dx%d")%(RWidth,RHeight))

        #Etiqueta del titulo
        label_1=Label(root1,text="Ordenes Canceladas:")
        label_1.grid(row=2,column=2,padx=10,pady=10)


        #crea la variable que conecta con la base de datos
        conn=sqlite3.connect('INARI_DB.db')

        #crea la variable con la coneccion y el cursor
        c=conn.cursor()

        n=6#variable contador para mostrar etiquetas en cada fila despues

        #labels base y sus posicionamientos
        label_2=Label(root1,text="ID")
        label_2.grid(row=4,column=0,padx=10,pady=10)

        label_3=Label(root1,text="Nombre")
        label_3.grid(row=4,column=1,padx=10,pady=10)

        label_4=Label(root1,text="Email")
        label_4.grid(row=4,column=2,padx=10,pady=10)

        label_5=Label(root1,text="Telefono")
        label_5.grid(row=4,column=3,padx=10,pady=10)

        label_6=Label(root1,text="Pedido")
        label_6.grid(row=4,column=4,padx=10,pady=10)

        label_7=Label(root1,text="Total")
        label_7.grid(row=4,column=6,padx=10,pady=10)



        #muestra todas las ordenes canceladas hasta el final, agregando labels automatico
        print("\nOrdenes Canceladas:")
        for row1 in c.execute('select * from Cancelado'):
                n+=1

                #ID
                label_7=Label(root1,text=str(row1[0]),justify="left")
                label_7.grid(row=n,column=0,padx=0,pady=10)
                print("-----------------------------------------")
                print("\nID: "+str(row1[0]))

                #Nombre
                label_8=Label(root1,text=str(row1[1]))
                label_8.grid(row=n,column=1,padx=10,pady=10)
                print("Nombre: "+str(row1[1]))

                #Email
                label_9=Label(root1,text=str(row1[2]))
                label_9.grid(row=n,column=2,padx=10,pady=10)
                print("Email: "+str(row1[2]))

                #Telefono
                label_10=Label(root1,text=str(row1[3]))
                label_10.grid(row=n,column=3,padx=10,pady=10)
                print("Telefono: "+str(row1[3]))

                #Bandeja
                label_11=Label(root1,text=str(row1[4]))
                label_11.grid(row=n,column=4,padx=10,pady=10)
                print("Bandeja: "+str(row1[4]))

                #Total
                label_12=Label(root1,text=str(row1[5]))
                label_12.grid(row=n,column=6,padx=10,pady=10)
                print("Total: "+str(row1[5]))
                print("-----------------------------------------")


        #cerrar la coneccion
        conn.close()

        root1.mainloop()

# Ventana mostrar Caja
def Caja():
        # Configuracion base de la ventana
        rootCaja=Tk()
        rootCaja.configure(background="orange red")
        RTitle=rootCaja.title("Caja")
        RWidth=600
        RHeight=900
        rootCaja.geometry(("%dx%d")%(RWidth,RHeight))

        # Label titulo
        LabelTitulo = Label(rootCaja,text="INARI SUSHI\nCAJA",font=("AndaleMono",20,"bold"))

        # LabelTitulo.grid(row=0,column=2,padx=3,pady=10)
        LabelTitulo.grid(row=0,column=3,padx=10,pady=10)

        # Etiquetas fijas
        # ID
        label_1=Label(rootCaja,text="ID:")
        label_1.grid(row=4,column=3,padx=10,pady=10)

        # total
        label_2=Label(rootCaja,text="Total de cada pedido:")
        label_2.grid(row=4,column=5,padx=10,pady=10)

        n = 6
        cierre = 0

        # se crea la variable coneccion
        conn=sqlite3.connect('INARI_DB.db')

        # se crea el cursor
        c=conn.cursor()

        print("Caja:")
        for row2 in c.execute('select * from Estado'):

                n+=1

                if(row2[1] == "En camino"):

                    #ID
                    label_3=Label(rootCaja,text=str(row2[0]),justify="left")
                    label_3.grid(row=n,column=3,padx=0,pady=10)
                    print("ID:"+str(row2[0]))

                    #total
                    label_4=Label(rootCaja,text=str(row2[2]),justify="left")
                    label_4.grid(row=n,column=5,padx=0,pady=10)
                    print("Total del pedido:"+str(row2[2]))

                    cierre+=int(row2[2])

        #total
        label_4=Label(rootCaja,text="cierre de caja del dia con:",justify="left")
        label_4.grid(row=0,column=6,padx=10,pady=10)


        #mostrar cierre
        print("Cierre de la caja: "+str(cierre))


        #total 2
        label_4=Label(rootCaja,text="$"+str(cierre),justify="left")
        label_4.grid(row=0,column=7,padx=10,pady=10)


        #cerrar la coneccion
        conn.close()

        rootCaja.mainloop()


#funcion para ordenar pedidos
def Ordenar_pedido():
        #configuracion basica de la ventana
        root2=Tk()
        root2.configure(background="Orange red")
        RTitle=root2.title("Nueva Orden")
        RWidth=1000
        RHeight=500
        root2.geometry(("%dx%d")%(RWidth,RHeight))
        var1=IntVar() #en caso de error descomentar

        Label_titulo=Label(root2,text="INARI PEDIDOS",font=("AndaleMono",20,"bold"),fg="white",bg="black")
        Label_titulo.place(x=320,y=20)

        #crean los objetos de las bandejas
        bandeja1 = Bandeja(1, " URAKAMI (roll - 8 piezas) ", 380)
        bandeja2 = Bandeja(2, "  GEISHAS (bocado - 4 piezas) ", 250)
        bandeja3 = Bandeja(3, "  TEMAKIS (cono - 1 pieza) ", 200)
        bandeja4 = Bandeja(4, "  HOSOMAKI (roll - 6 piezas)", 210)
        bandeja5 = Bandeja(5, "  SASHIMI (bocado - 5 piezas) ", 280)
        bandeja6 = Bandeja(6, " GUNKAN (bolitas - 5 piezas)", 210)
        bandeja7 = Bandeja(7, " NIGURI (bolitas - 5 piezas)", 240)

        #crear objeto Pedidos para el pedido actual
        pedido1 = Pedidos()

        #se limpia el objeto
        try:
            pedido1.total = 0
            pedido1.direccion=""
            con=0
            for i in pedido1.listaDePedidos:
                del pedido1.listaDePedidos[con]
                con+=1
        except Exception as e:
            pass


        #Etiquetas
        label_1=Label(root2,text="Nombre:")
        label_2=Label(root2,text="Pedido:")
        label_3=Label(root2,text="E-Mail:")
        label_4=Label(root2,text="Telefono:")
        label_5=Label(root2,text="Direccion:")
        label_6=Label(root2,text="Cantidad:")
        label_7=Label(root2,text="Pago con:")
        label_AG=Label(root2,text="Carrito:")



        # (lista) de opciones

        Opciones = [
            [bandeja1.posBandeja, bandeja1.tipoBandeja , bandeja1.precio],
            [bandeja2.posBandeja, bandeja2.tipoBandeja , bandeja2.precio],
            [bandeja3.posBandeja, bandeja3.tipoBandeja , bandeja3.precio],
            [bandeja4.posBandeja, bandeja4.tipoBandeja , bandeja4.precio],
            [bandeja5.posBandeja, bandeja5.tipoBandeja , bandeja5.precio],
            [bandeja6.posBandeja, bandeja6.tipoBandeja , bandeja6.precio],
            [bandeja7.posBandeja, bandeja7.tipoBandeja , bandeja7.precio]
        ]

        # lista de cantidad
        Cantidad = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
        ]



        # Menu para las opciones-------------------------------------------------------------------------------
        # Crea una variable para alojar la primer tabla
        variable = StringVar(root2)


        # valor defecto 0 para mostrar la primera opcion si es que no se selecciona ninguna
        variable.set(Opciones[0])

        #crea el menu deplegable
        w = OptionMenu( *(root2, variable) + tuple(Opciones))
        w.grid(row=3,column=3,padx=10,pady=10)#se posiciona

        # Menu para la cantidad----------------------------------------------------------------------------------
        # Crea una variable para alojar la primer tabla
        variableCantidad = StringVar(root2)

        # valor defecto 0 para mostrar la primera opcion si es que no se selecciona ninguna
        variableCantidad.set(Cantidad[0])

        #Crea el menu deplegable
        w2 = OptionMenu( *(root2, variableCantidad) + tuple(Cantidad))
        w2.grid(row=3,column=9,padx=10,pady=10)#se posiciona


        # Crea los campos de texto
        # Nombre
        Entry_1=Entry(root2,width=50)

        # Email
        Entry_2=Entry(root2,width=50)

        # Telefono
        Entry_3=Entry(root2,width=50)

        # Direccion
        Entry_4=Entry(root2,width=50)

        # PagoCon
        Entry_5=Entry(root2,width=20)


        #------------------------------------------------------------------------------------------------------------------------------------------
        # Agregar labels al carrito:

        # Listas para el total y el carrito
        total=[]
        carrito=[]

        # Creo variable comando
        commandAG2= lambda:mostrar()


        # Funcion para pintar los labels del carrito
        def mostrar():

            # Obtiene la opcion seleccionada + la cantidad y la agrega a la lista carrito
            carrito.append([variable.get(),variableCantidad.get()])

            # Hasta el largo del carrito
            for i in range(len(carrito)):

                # Mostrar el pedido del carrito en posicion i
                label_00=Label(root2,text=str(carrito[i]))

                # Ubicarlo en columna 5+i ,( 5 porque en la etiqueta, carrito esta en la fila 5)
                # Y se muestra un label por fila
                label_00.grid(row=i+5,column=10,padx=10,pady=10)

        # Sacar el total

            listaPedidos = []

            # a la lista pedidos agrego las tablas seleccionadas
            listaPedidos.append(variable.get())

            # print(int(listaPedidos[0][2]))#obtener el numero de la orden
            total = 0

            # devuelve el precio de la bandeja seleccionada por la cantidad
            # se ejecuta la funcion tomarSeleccion que toma un int que es el primer numero
            # que identifica la tabla de la listaPedidos por eso su posicion [0][1] por
            # la cantidad seleccionada en el menu cantidad pero casteado a int.
            # la funcion toma ese valor y nos devuelve el valor de la bandeja.
            # depende el valor ingresado,son los valores que devuelve y los multiplica
            # por la seleccion que hay en el menu de cantidad.todo se suma en total
            total += tomarSeleccion(int(listaPedidos[0][1]))*int(variableCantidad.get())

            # el total se va guardando en el objeto ya que por cada vez que agregamos al Carrito
            # este cambia, y se acumula en el atributo total del objeto pedido1
            pedido1.total+=total



            #label total

            label_01=Label(root2,text=("Total: ",sacarTotal(total)))
            label_01.grid(row=7,column=4,padx=5,pady=10)

            #mostrar en consola resultados

            print("\nPedido")
            for er in pedido1.listaDePedidos:
                print(er)

            #print(pedido1.listaDePedidos)

            print("Total:",pedido1.total)

        #-------------------------------------------------------------------------------------------------------------------------------------

        # este es un backUp por las dudas
        # el boton ordenar ejecuta la variable comando y esta ingresa datos en la base de datos
        # Button_1=Button(root2,text="Ordenar",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",14,"bold"),bg="white",fg="black",borderwidth=4,width=7,height=3,command=command)

        #boton_AG "agregar al carrito"
        Button_AG=Button(root2,text="Agregar al carrito",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",10,"bold"),bg="white",fg="black",borderwidth=4,width=17,height=2,command=commandAG2)


        #Labels para identificar los campos de texto y el OptionMenu
        #nombre
        label_1.grid(row=2,column=2,padx=10,pady=10)

        #pedido:
        label_2.grid(row=3,column=2,padx=10,pady=10)

        #EMail:
        label_3.grid(row=4,column=2,padx=10,pady=10)

        #telefono:
        label_4.grid(row=5,column=2,padx=10,pady=10)

        #Direccion:
        label_5.grid(row=6,column=2,padx=10,pady=10)

        #Cantidad:
        label_6.grid(row=3,column=6,padx=10,pady=10)

        #PagoCon:
        label_7.grid(row=7,column=2,padx=10,pady=10)

        #Carrito:
        label_AG.grid(row=4,column=10,padx=10,pady=10)


        #posicionamiento de entradas(campo de texto) y boton

        #Nombre
        Entry_1.grid(row=2,column=3,padx=10,pady=10,columnspan=3)

        #Email
        Entry_2.grid(row=4,column=3,padx=10,pady=10,columnspan=3)

        #Telefono
        Entry_3.grid(row=5,column=3,padx=10,pady=10,columnspan=3)

        #direccion
        Entry_4.grid(row=6,column=3,padx=10,pady=10,columnspan=3)

        #pagoCon
        Entry_5.grid(row=7,column=2,padx=0,pady=10,columnspan=3)

        #Button_1.grid(row=8,column=2,padx=10,pady=10)#Ordenar

        #agregar al carrito
        Button_AG.grid(row=3,column=10,padx=10,pady=10)



        #funcion para validar la bandeja y retornar su valor,tambien agrega al objeto pedidos_realizados
        #los pedidos realizados
        def tomarSeleccion(seleccion):

            #tabla 1
            if(seleccion == 1):

                #guarda la cantidad seleccionada
                bandeja1.cantidad=variableCantidad.get()

                #guarda el carito o lista de comprar en una lista actual de este nuevo pedido
                pedido1.listaDePedidos.append([bandeja1.posBandeja,bandeja1.tipoBandeja,bandeja1.precio,bandeja1.cantidad])

                #retorna el precio depende de la opcion elegida para sacar el total
                return int(380)

            #tabla 2
            if(seleccion == 2):

                #guarda la cantidad seleccionada
                bandeja2.cantidad=variableCantidad.get()

                #guarda el carito o lista de comprar en una lista actual de este nuevo pedido
                pedido1.listaDePedidos.append([bandeja2.posBandeja,bandeja2.tipoBandeja,bandeja2.precio,bandeja2.cantidad])

                #retorna el precio depende de la opcion elegida para sacar el total
                return int(250)

            #tabla 3
            if(seleccion == 3):

                # guarda la cantidad seleccionada
                bandeja3.cantidad=variableCantidad.get()

                # guarda el carito o lista de comprar en una lista actual de este nuevo pedido
                pedido1.listaDePedidos.append([bandeja3.posBandeja,bandeja3.tipoBandeja,bandeja3.precio,bandeja3.cantidad])

                # retorna el precio depende de la opcion elegida para sacar el total
                return int(200)
            #tabla 4
            if(seleccion == 4):

                # guarda la cantidad seleccionada
                bandeja4.cantidad = variableCantidad.get()

                # guarda el carrito o lista de comprar en una lista actual de este nuevo pedido
                pedido1.listaDePedidos.append(
                    [bandeja4.posBandeja, bandeja4.tipoBandeja, bandeja4.precio, bandeja4.cantidad])

                #retorna el precio depende de la opcion elegida para sacar el total
                return int(210)

            #tabla 5
            if(seleccion == 5):

                #guarda la cantidad seleccionada
                bandeja5.cantidad = variableCantidad.get()

                #guarda el carrito o lista de comprar en una lista actual de este nuevo pedido
                pedido1.listaDePedidos.append(
                    [bandeja5.posBandeja, bandeja5.tipoBandeja, bandeja5.precio, bandeja5.cantidad])

                #retorna el precio depende de la opcion elegida para sacar el total
                return int(280)

            #tabla 6
            if(seleccion == 6):

                #guarda la cantidad seleccionada
                bandeja6.cantidad = variableCantidad.get()

                #guarda el carrito o lista de comprar en una lista actual de este nuevo pedido
                pedido1.listaDePedidos.append(
                    [bandeja6.posBandeja, bandeja6.tipoBandeja, bandeja4.precio, bandeja6.cantidad])

                #retorna el precio depende de la opcion elegida para sacar el total
                return int(210)

            #tabla 7
            if(seleccion == 7):

                #guarda la cantidad seleccionada
                bandeja7.cantidad = variableCantidad.get()

                #guarda el carrito o lista de comprar en una lista actual de este nuevo pedido
                pedido1.listaDePedidos.append(
                    [bandeja7.posBandeja, bandeja7.tipoBandeja, bandeja7.precio, bandeja7.cantidad])

                #retorna el precio depende de la opcion elegida para sacar el total
                return int(240)

        #funcion para sacar total
        def sacarTotal(numero):
            total.append(numero)
            aux = 0
            for n in total:
                aux+=n
            return aux


        #command que inserta en la base de datos todos los datos al dar click en Ordenar
        commandAux =lambda: botonOrdenar(Entry_1.get(),Entry_2.get(),Entry_3.get(),pedido1.listaDePedidos,pedido1.total,Entry_5.get(),"En cocina",Entry_4.get())

        #comando que destruye la ventana al apretar Salir
        commandSalir = lambda:destruir_ventana(root2)

        #boton ordenar
        Button_1=Button(root2,text="Ordenar",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",14,"bold"),bg="white",fg="black",borderwidth=4,width=7,height=3,command=commandAux)
        #posiccion
        Button_1.grid(row=8,column=2,padx=10,pady=10)

        #boton salir de la ventana
        Button_Salir =Button(root2,text="Salir",activebackground="khaki1",relief=SUNKEN,font=("AndaleMono",14,"bold"),borderwidth=4,bg="white",fg="black",width=5,height=2,command=commandSalir)

        #posicionamiento del boton salir
        Button_Salir.grid(row=1,column=10,padx=30,pady=10)

        con=0
        for i in pedido1.listaDePedidos:
            del pedido1.listaDePedidos[con]
            con+=1





        #funcion que inserta los datos en la base de datos
        def botonOrdenar(Nombre,Email,Telefono,pedido,costo,pagoCon,Estado,direccion):

            #cramos cadena y count
            cadena=" "

            count=0

            #guardan en la cadena el pedido y cantidad hasta que de error de exceder el index
            for item in pedido:
                try:#                   pedido                                  cantidad
                    cadena += str(pedido[count][1])+" x"+str(pedido[count][3])+" | \n"
                    #toma de la lista pedido,[count] es para recorrer cada sublista y el segundo corchete
                    #es para obtener el string de la tabla seleccionada[1], el de [3] es para obtener
                    #la cantidad
                    #se obtiene el "tabla elegida  x2" (x2=cantidad)
                    count+=1
                except Exception as e:
                    #si falla que termine
                    break

            #finalmente insertar en la base de datos todo!
            """ Se agregan tres variables de validacion que empiezan con valor FALSE
            y se agrega la validacion individual de cada campo, si cumplen cambian su
            valor a TRUE.Finalmente hay una validacion que compara que todas las validaciones
            sean verdaderas y se envian los datos a la base de datos """

            valTelefono=False
            valPagocon=False
            valCorreo=False

            #validador de telefono

            if  (len(Telefono)>=7) and (len(Telefono)<=10)and (type(int(Telefono))== int):

                valTelefono=True

            else:

                tkMessageBox.showinfo(
                    "", "Ingrese un numero de telefono valido")
                #print("Ingrese un numero de telefono valido")

            #validador de PagoCon
            try:

                if  (int(pagoCon)>=costo):

                    valPagocon=True

                else:

                    tkMessageBox.showinfo(
                        "", "Pago insuficiente \nFaltan: $"+str(int(costo)-int(pagoCon)))
            except Exception as e:
                tkMessageBox.showinfo(
                    "", "El Pago ingresado es invalido ")
                #print("El Pago ingresado es invalido ")


            #validador de correo
            #aca el len devuelve el largo del String
            for l in range(len(Email)):

            #y con el range lo que hace es un array con la cantidad de elmentos que contenga el email ingresado
            	if Email [l] == "@":

            		valCorreo = True

            if(valCorreo==False):

            	tkMessageBox.showinfo(
                "", "Correo ingresado no valido")
                #print("Correo ingresado no valido")

            #Validacion de telefono ,pago con y correo

            if (valTelefono)and(valPagocon)and(valCorreo):

                Insertar_en_DB(Nombre,Email,Telefono,cadena,costo,pagoCon,Estado,direccion)
                print("""Pedido Realizado!:
                \nNombre: """+str(Nombre)+"""
                \nEmail: """+str(Email)+""")
                \nID-Telefono: """+str(Telefono)+""")
                \nPedido: """+str(cadena)+""")
                \nCosto: """+str(costo)+""")
                \nPago con: """+str(pagoCon)+""")
                \nEstado: """+str(Estado)+""")
                \nDireccion: """+str(direccion)+""")
                \nVuelto: """+str(int(pagoCon)-int(costo)))

                #insertar en tabla estado el id, el estado y costo
                insertar_en_Estado(Telefono,Estado,costo)

                destruir_ventana(root2)

                tkMessageBox.showinfo(
                    "", "Orden realizada! \nID de la Orden: "+str(Telefono)+"\nVuelto:"+str(int(pagoCon)-int(costo)))
                print("Orden realizada! \nID de la Orden: "+str(Telefono)+"\nVuelto:"+str(int(pagoCon)-int(costo)))

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

        """image = tk.PhotoImage(file="inari.gif")
        image = image.subsample(1, 1)
        label = tk.Label(image=image)
        label.place(x=0, y=0, relwidth=1.0, relheight=1.0)"""


        #Label titulo
        LabelTitulo = Label(root,text="INARI SUSHI\nBienvenido!!!",font=("AndaleMono",50,"bold"))
        #LabelTitulo.grid(row=0,column=2,padx=3,pady=10)
        LabelTitulo.place(x= 140,y =30)


        #variables comando para abrir ventanas
        command=lambda :Ordenar_pedido()
        command1=lambda :cancelar_pedido()
        command2=lambda :track_pedido()
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

#esta funcion destruye ventanas,se pasa la ventana por parametro
def destruir_ventana(root):
        root.destroy()


def acerca_de():
    rootAC=Tk()
    rootAC.configure(background="Orange red")
    RTitle=rootAC.title("Acerca De: ?")
    RWidth=605
    RHeight=500
    rootAC.geometry(("%dx%d")%(RWidth,RHeight))

    texto = Text(rootAC, width=60, height=26, bg="white", fg="black", font=("Consolas",12))
    texto.grid(row=0, column=0, pady=0, padx=0)

    texto.insert("insert", """*********************INARI SUSHI****************************
            \nEste software fue realizado como proyecto para la promocion de la materia 'Metodologiade la investigacion' de la        universidad tecnologica nacional de Mendoza Argentina.
             \n\nEste fue desarrollado por el siguiente grupo de alumnos:
             \nGrilli Luciano
             \nMauriz Sebastian
             \nCandia Mauro
             \nRoza Joaquin
             \n\nEl software consiste en un delivery de sushi para el local  INARI el cual se tiene las funciones necesarias y mayormente requeridas para un delivery""")


    rootAC.mainloop()




#ventana vendedor
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
        command5=lambda :Caja()
        command6=lambda :acerca_de()



        #activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",14,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5,
        #crear botones
        Button_1=Button(root,text="Nuevo pedido",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5,command=command)
        Button_2=Button(root,text="Cancelar pedido",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5, command=command1)
        Button_3=Button(root,text="Pedidos\n realizados",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5,command=command2)
        Button_4=Button(root,text=" Pedidos\n Cancelados",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5,command=command3)
        Button_5=Button(root,text="Mostrar Caja",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5,command=command5)
        Button_6=Button(root,text="  Acerca De",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=15,height=5,command=command6)


        Button_7=Button(root,text="Salir",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",12,"bold"),bg="white",fg="black",borderwidth=4,width=5,height=2,command=command4)

        #posicionar botones
        #Nuevo pedido
        Button_1.grid(row=1,column=1,padx=60,pady=70)

        #Cancelar pedido
        Button_2.grid(row=1,column=2,padx=60,pady=70)

        #pedidos realizados
        Button_3.grid(row=1,column=3,padx=60,pady=70)

        #pedidos cancelados
        Button_4.grid(row=2,column=1,padx=60,pady=5)

        #mostrar caja
        Button_5.grid(row=2,column=2,padx=60,pady=5)

        #despachar pedidos
        Button_6.grid(row=2,column=3,padx=60,pady=5)

        #boton salir
        Button_7.grid(row=0,column=3,padx=60,pady=10)
        root.mainloop()

#Ventana Main
def main():
        root = tk.Tk()
        root.configure(background="orange red")
        RTitle=root.title("Delivery Sushi")

        image = tk.PhotoImage(file="inari.gif")
        image = image.subsample(1, 1)
        label = tk.Label(image=image)
        label.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        #Label titulo
        #LabelTitulo = Label(root,font=("AndaleMono",50,"bold"))
        #LabelTitulo.grid(row=0,column=2,padx=3,pady=10)
        #LabelTitulo.place(x= 140,y =30)

        #asignan variables de ancho y alto y se colocan en geometry
        RWidth=625
        RHeight=600
        root.geometry(("%dx%d")%(RWidth,RHeight))

        #variables comandos que ejecutan ventanas
        command=lambda :vendedor()
        command_1=lambda :cliente()

        #botones
        Button_1=Button(root,text="Vendedor",activebackground="DeepSkyBlue3",relief=SUNKEN,font=("AndaleMono",14,"bold"),bg="white",fg="black",borderwidth=4,width=12,height=5,command=command)
        Button_2=Button(root,text="Cliente",activebackground="khaki1",relief=SUNKEN,font=("AndaleMono",14,"bold"),bg="white",fg="black",borderwidth=4,width=12,height=5,command=command_1)
        #Button_1.grid(row=1,column=1,padx=5,pady=140)
        #Button_2.grid(row=1,column=2,padx=6,pady=140)
        Button_1.place(x= 50, y= 275)
        Button_2.place(x= 415, y= 275)


        root.mainloop()

main()
