cantCasos= int(input("Ingrese la cantidad de casos a resolver: ")) # pedimos la cantidad de casos al usuario
lista =[]         
bandera = False
bandera2 = False

for x in range(cantCasos):     # iteramos de acuerdo a la cantidad de casos 
    print("Ingrese el caso: ",x+1)    # en cada iteracion pide que ingrese el caso, ese dato lo casteamos a entero
    numeroIngreso = int(input("Intruducir un numero que sea de 4 dígitos y que tenga al menos 2 digitos diferentes: "))
    if numeroIngreso == 6174:   #aca si el usuario ingresa la constante, la bandera pasará a ser True para poder asignar el valor de salida 8
        bandera = True
    if numeroIngreso == 1111 or numeroIngreso == 2222 or numeroIngreso == 3333 or numeroIngreso ==4444 or numeroIngreso ==5555 or numeroIngreso == 6666 or numeroIngreso ==7777 or numeroIngreso == 8888 or numeroIngreso ==9999 or numeroIngreso == 0000:
        bandera2 =True   # en este caso hacemos lo mismo que en el if anterior
    numeroResta =0    #asignamos 0 a numero resta para poder hacer la resta de cada numero (en cada vuelta numeroResta se hace 0 para que borre el resultado de la iteracion anterior)
	for i in range(10): #hacemos otro bucle for para poder encontrar la constante (sabiendo que mas de 11 iteraciones no van a ser)
        numeroIngreso="{:04d}".format(numeroIngreso) #con esta funcion le damos 4 digitos al numero que ingreso el usuario (por si mete un 12, quedaría: 0012)
        numGrande = "".join(sorted(numeroIngreso,reverse=True))#con esta funcion ordenamos los digitos del numero de mayor a menor
        numChico = "".join(sorted(numeroIngreso))# aca lo dejamos de menor a mayor

        numeroIngreso = int(numGrande) - int(numChico) #restamos ambos numeros


















    