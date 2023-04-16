#tkinter
'''
esta libreria esta integrada a python sirve para generar interfaces graficas

relief= FLAT  #se puede igualar a las siguientes opciones para darles un efecto tridimencional al panel
                #FLAT,RAISED,SUNKEN,GROOVE,RIDGE
'''
from tkinter import *
from tkinter import filedialog, messagebox   #filedialog es dialogo de archivo y messagebox es caja de mensaje
import random
import datetime

operador = ''#se van a guardar los numero que se presionen en calculadora
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]#lista con los precios de los productos
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):#esta funcion se llama cada que se precione un boton de calculadora
    global operador#se hace una variable global por que la variable esta fuera de la funcion
    operador = operador + numero#se le agrega el numero a operador
    visor_calculadora.delete(0, END)#para que borre los botones anterior presionados y no los muestre nuevamente
    visor_calculadora.insert(END, operador)#Visor insertara todos los numero que se vayan precionando desde el fin
def borrar():
    global operador#se llama a la variable que esta fuera de la funcion
    operador =''#se vuelve a inicializar operador para evitar que se guarde cache
    visor_calculadora.delete(0, END)#borra la info de la pantalla
def obtener_resultado():
    global operador
    resultado = str(eval(operador))#eval sirve para evaluar/identificar al operador ingresado (division,multiplicacion,resta,suma)y lo convierte a str
    visor_calculadora.delete(0, END)  # para que borre los botones anterior presionados y no los muestre nuevamente
    visor_calculadora.insert(END, resultado)#Visor insertara todos los numero que se vayan precionando desde el fin
    operador = ''#pedimos que restablezca para evitar guardar cache en la variable operador
def revisar_check():
    x = 0
    for c in cuadros_comida:#para cuando se active la casilla del check se pueda escribir la cantidad
        if variables_comida[x].get()==1:#si se selecciona la casilla
            cuadros_comida[x].config(state=NORMAL)#para permitir la escritura
            if cuadros_comida[x].get() == '0':#para evitar que borre todas las demas casillas cuando se desactive una casilla
                cuadros_comida[x].delete(0,END)#para eliminar el 0 cuando se active la casilla de escriturda de la comida
            cuadros_comida[x].focus()#se muestra el cursor en la casilla activa.
        else:#para regresar a la normalidad la casilla blanca cuando se desactive. y se muestre el cero
            cuadros_comida[x].config(state=DISABLED)#si se desactiva la casilla
            texto_comida[x].set("0")#colocar en cero el cuadro de texto. de comidas
        x += 1
    x = 0
    for c in cuadros_bebida:#para cuando se active la casilla del check se pueda escribir la cantidad
        if variables_bebida[x].get()==1:#si se selecciona la casilla
            cuadros_bebida[x].config(state=NORMAL)#para permitir la escritura
            if cuadros_bebida[x].get() == '0':#para evitar que borre todas las demas casillas cuando se desactive una casilla
                cuadros_bebida[x].delete(0,END)#para eliminar el 0 cuando se active la casilla de escriturda de las bebidas
            cuadros_bebida[x].focus()#se muestra el cursor en la casilla activa.
        else:#para regresar a la normalidad la casilla blanca cuando se desactive. y se muestre el cero
            cuadros_bebida[x].config(state=DISABLED)#si se desactiva la casilla
            texto_bebida[x].set("0")#colocar en cero el cuadro de texto. de bebidas
        x += 1
    x = 0
    for c in cuadros_postre:#para cuando se active la casilla del check se pueda escribir la cantidad
        if variables_postre[x].get()==1:#si se selecciona la casilla
            cuadros_postre[x].config(state=NORMAL)#para permitir la escritura
            if cuadros_postre[x].get() == '0':#para evitar que borre todas las demas casillas cuando se desactive una casilla
                cuadros_postre[x].delete(0,END)#para eliminar el 0 cuando se active la casilla de escriturda de los postres
            cuadros_postre[x].focus()#se muestra el cursor en la casilla activa.
        else:#para regresar a la normalidad la casilla blanca cuando se desactive. y se muestre el cero
            cuadros_postre[x].config(state=DISABLED)#si se desactiva la casilla
            texto_postre[x].set("0")#colocar en cero el cuadro de texto. de postres
        x += 1
def total():
    #cuando se presione el boton total, tiene que sacar el precio por los productos consumidos, luego hacer un subtotal de comidas postres y bebidas, impuestos y un total general
    sub_total_comida = 0
    p = 0 # para recorrer por los precios de las comidas
    for cantidad in texto_comida:#obtener las cantidades de cada comida (pollo,cordero y salmon)
        #cantidad es un tipo de stringvar por eso se ocupa get() para obtener lo que tiene, pero obtiene un integer por lo que lo convertimos a float
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1
    sub_total_bebida = 0
    p = 0 # para recorrer por los precios de las bebidas
    for cantidad in texto_bebida:#obtener las cantidades de cada bebida
        #cantidad es un tipo de stringvar por eso se ocupa get() para obtener lo que tiene, pero obtiene un integer por lo que lo convertimos a float
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1
    sub_total_postre = 0
    p = 0 # para recorrer por los precios de los postres
    for cantidad in texto_postre:#obtener las cantidades de cada postre
        #cantidad es un tipo de stringvar por eso se ocupa get() para obtener lo que tiene, pero obtiene un integer por lo que lo convertimos a float
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.07
    total = sub_total + impuestos
    #set para colocar,se coloca en var costo comida el valor de subtotal comida con dos decimales.,
    var_costo_comida.set(f"$ {round(sub_total_comida,2)}")#round es la funcion redondear y el 2 son dos decimales
    var_costo_bebida.set(f"$ {round(sub_total_bebida, 2)}")
    var_costo_postre.set(f"$ {round(sub_total_postre, 2)}")
    var_subtotal.set(f"${round(sub_total, 2)}")
    var_impuesto.set(f"$ {round(impuestos, 2)}")
    var_total.set(f"$ {round(total, 2)}")
def recibo():
    texto_recibo.delete(1.0,END)#para borrar lo anterior en el texto comience desde 1.0
    num_recibo = f"N# - {random.randint(1000, 9999)}"#para generar numeros de ticket aleatorio, e imprimirlos
    fecha = datetime.datetime.now()#para obtener la fecha del dia de hoy
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'#para mostrar la fecha
    texto_recibo.insert(END, f"Datos: \t{num_recibo}\t\t{fecha_recibo}\n")#para mostrar los datos desde end hasta fecha recibo
    texto_recibo.insert(END, f'*' * 58 + '\n')#mostrar una linea de asteriscos para separar
    texto_recibo.insert(END, 'Items\t\tCant. \tCosto Items\n')#mostrar algunas categorias
    texto_recibo.insert(END, f'-' * 70 + '\n')#comienza desde el END el final donde se quedo
    #BUSCAR LAS CADA UNO DE LOS ITEMS CONSUMIDOS
    x = 0
    for comida in texto_comida:#buscar la comida en el texto ingresado
        if comida.get() != '0':#solo buscar la comida que tienen numeros ingresados en las casillas
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'${int(comida.get()) * precios_comida[x]}\n')#si se quita int(comida.get()) *   se mostrara el precio unitario por item
        x += 1
    x = 0
    for bebida in texto_bebida:#buscar la comida en el texto ingresado
        if bebida.get() != '0':#solo buscar la comida que tienen numeros ingresados en las casillas
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'${int(bebida.get()) * precios_bebida[x]}\n')
        x += 1
    x = 0
    for postre in texto_postre:#buscar la comida en el texto ingresado
        if postre.get() != '0':#solo buscar la comida que tienen numeros ingresados en las casillas
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t'
                                     f'${int(postre.get()) * precios_postres[x]}\n')
        x += 1
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo del postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Sub Total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Los esperamos, vuelvan pronto\n')
def guardar():
    #guardara la info de recibo
    info_recibo = texto_recibo.get(1.0,END)#vamos a obtener todo lo que se tenga desde el comienzo 1.0 hasta el final
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')#Pedir al usuario que guarde un archivo, en modo escritura w y con la extension .txt
    archivo.write(info_recibo)#se guarda toda la info de recibo en el bloc de notas, el cual el usuario debe elegir el nombre y carpeta
    archivo.close()#se cierra el archivo al finalizar el guardado
    messagebox.showinfo("Informacion", 'Su recibo ha sido Guardado y timbrado')#se muestra un mensaje en pantalla con el siguiente texto
def reset():
    texto_recibo.delete(0.1,END)#se borra desde el comienzo hasta el final END los datos guardados en la variable y lo que se muestra en pantalla
    for texto in texto_comida:
        texto.set('0')#colocar en cero los cuadros de ingreso de valores
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postre:
        texto.set('0')
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)#Para desactivar los cuadros de ingreso de texto
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)
    for v in variables_comida:
        v.set(0)#Para desactivar las casillas de los checkbutton
    for v in variables_bebida:
        v.set(0)
    for v in variables_postre:
        v.set(0)
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


#Iniciar tkinter
aplicacion = Tk()#asi se inicia tkinter
#Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')#se coloca el tamaño de la pantalla y en que posicicion x y aparecera en el escritorio que es en la (0,0)
#Evitar maximizar
aplicacion.resizable(0,0)#desactivar maximizar la ventana
#Titulo de la ventana
aplicacion.title("Mi restaurante -  Sistema de facturacion")
#Color de fonde de la ventana
aplicacion.config(bg='burlywood')#bg=background para el color de la pantalla, se puede poner el nombre del color como 'blue' o en RGB



#------CREACION DE PANELES DE ITEMS se puede ver en la imagen DISEÑO_PANELES.jpeg--------
#Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)#se ubica en aplicacion con un bd=1 es el borde y relievef es un efecto tridimencional del tipo FLAT
panel_superior.pack(side=TOP)#para colocar la poscicion del panel en la pantalla, side =TOP
#Etiqueta titulo, es parte de panel superior
#label es etiqueta, ira en panel superior, con el texto sistema facturacion, con color de letras fg=azure4
etiqueta_titulo = Label(panel_superior, text= 'Sistema de Facturacion', fg='azure4',
                        font=('Dosis', 58), bg='burlywood', width=22)#tipo de letra dosis con tamaño 58, color de fondo burly y con el ancho del label 22
etiqueta_titulo.grid(row=0, column=0)#grid es la cuadricula, se coloca row=0 y column=0 por que es el unico elemento

#---PANEL IZQUIERDO--- PARA LOS PANEL COMIDA,BEBIDA,POSTRE
panel_izquierdo = Frame(aplicacion,bd=1, relief=FLAT,padx=27)
panel_izquierdo.pack(side=LEFT)#LEFT se ubicara a la izquierda de la pantalla

#---PANEL INFERIOR COSTOS--- SE ENCUENTRA ABAJO DE TODO
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4',padx=24)#se cambia el background y se agrega padx para que combine y se vea mejor los curados de textode costos, donde comida y subtotal
panel_costos.pack(side=BOTTOM)#BOTTOM se ubicara abajo de todo                #se agrego un padx=25 para evitar que se pegue a la calculadora y cuadros de total,recibo, guardar, resetear

#Panel_comidas  **LabelFrame es un cuadro que viene con la etique incorporada en este caso panel_izquierdo
panel_comidas = LabelFrame(panel_izquierdo,text='Comida', font=('Dosis',19,'bold'),#dosis el tipo de letra tamaño 19 y bold=negritas
                           bd=1,relief=FLAT,fg='azure4')
panel_comidas.pack(side=LEFT)

#Panel_bebidas
panel_bebidas = LabelFrame(panel_izquierdo,text='Bebida', font=('Dosis',19,'bold'),
                           bd=1,relief=FLAT,fg='azure4')
panel_bebidas.pack(side=LEFT)

#Panel_postres
panel_postres = LabelFrame(panel_izquierdo,text='Postres', font=('Dosis',19,'bold'),
                           bd=1,relief=FLAT,fg='azure4')
panel_postres.pack(side=LEFT)

#---PANEL DERECHA--PARA LOS PANEL CALCULADORA,RECIBO,BOTONES
panel_derecha = Frame(aplicacion,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

#Panel recibo
panel_recibo= Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

#Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

#-----LISTAS------
#lista de productos
lista_comidas = ["pollo","cordero","salmon","merluza","kebab","pizza1","pizza2","pizza3"]
lista_bebidas = ['agua','soda','jugo','cola','vino1','vino2','cerveza1','cerveza2']
lista_postres = ['helado','fruta','brownies','flan','mousse','pastel1','pastel2','pastel3']

#-----GENERAR CHECKBUTTONS DE ITEMS Y CUADROS DE TEXTO -----
#Comidas
variables_comida = []#se ocuparan variables para cada elemento de la lista, por lo que se inicializa este arreglo
cuadros_comida = []#para los valores a ingresar, en los cuadros de entrada
texto_comida = []#para variar los texto ingresados
contador = 0
for comida in lista_comidas:
    # GENERAR Checkbutton por cada elemento de la lista
    variables_comida.append('')
    variables_comida[contador] = IntVar()#el elemento se debe cambiar a tipo entero , para recorrer los elementos se usa el contador y se acambia a entero con IntVar, que es una varibale tipo entera de
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),#se genera el checkbutton, en panel comida, extrayendo el nombre de la lista con title
                         font=('Dosis',15,'bold'),
                         onvalue=1,#onvalue =1 es on cuando este activado,
                         offvalue=0,#offvalue=cuando este desactivado
                         variable=variables_comida[contador],
                         command=revisar_check)#PARA CUANDO SE ACTIVE LA CASILLA DEL CHECK se pueda escribir o editar
    comida.grid(row=contador,
                column=0,
                sticky=W)#para hacer saltos de linea cambiamos la fila con row=contador, para que el texto se justifique de lado izquierdo se ocupa W
    #CREAR los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')#se agrega el numeor escrito en el cuadro de texto de la comida como pollo, salmon, pizza
    texto_comida[contador] = StringVar()#string var es un tipo de variable de tkinter
    texto_comida[contador].set('0')#set para establecer el valor iniciar dentro del cuatro de texto
    cuadros_comida[contador] = Entry (panel_comidas,
                                      font=('Dosis',16,'bold'),#fuente de letra,tamaño y negritas
                                      bd=1,#borde
                                      width=6,#ancho del cuadro
                                      state=DISABLED,#el cuadro esta desactivado hasta que se coloque el checkbox
                                      textvariable=texto_comida[contador])#para variar los textos de cada tipo de comida
    cuadros_comida[contador].grid(row=contador,
                                  column=1,#es la columna 1 por que es la comunda siguiente a los checkbutton
                                  sticky=W)#justificar texto
    contador += 1
#Bebidas
variables_bebida = []
cuadros_bebida = []
texto_bebida= []
contador = 0
for bebida in lista_bebidas:
    # GENERAR Checkbutton por cada elemento de la lista
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis',15,'bold'),
                         onvalue=1,#onvalue =1 es on cuando este activado,
                         offvalue=0,#offvalue=cuando este desactivado
                         variable=variables_bebida[contador],
                         command=revisar_check)#PARA CUANDO SE ACTIVE LA CASILLA DEL CHECK se pueda escribir o editar)
    bebida.grid(row=contador,
                column=0,
                sticky=W)
    #CREAR los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')#se agrega el numeor escrito en el cuadro de texto de la bebida elegida, como agua
    texto_bebida[contador] = StringVar()  # string var es un tipo de variable de tkinter
    texto_bebida[contador].set('0')  # set para establecer el valor iniciar dentro del cuatro de texto
    cuadros_bebida[contador] = Entry (panel_bebidas,
                                      font=('Dosis',16,'bold'),#fuente de letra,tamaño y negritas
                                      bd=1,#borde
                                      width=6,#ancho del cuadro
                                      state=DISABLED,#el cuadro esta desactivado hasta que se coloque el checkbox
                                      textvariable=texto_bebida[contador])#para variar los textos de cada tipo de comida
    cuadros_bebida[contador].grid(row=contador,
                                  column=1,#es la columna 1 por que es la comunda siguiente a los checkbutton
                                  sticky=W)#justificar texto
    contador += 1
#Postres
variables_postre = []
cuadros_postre= []
texto_postre= []
contador = 0
for postre in lista_postres:
    # GENERAR Checkbutton por cada elemento de la lista
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis',15,'bold'),
                         onvalue=1,#onvalue =1 es on cuando este activado
                         offvalue=0,#offvalue=cuando este desactivado
                         variable=variables_postre[contador],
                         command=revisar_check)#PARA CUANDO SE ACTIVE LA CASILLA DEL CHECK se pueda escribir o editar)
    postre.grid(row=contador,
                column=0,
                sticky=W)
    #CREAR los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')#se agrega el numeor escrito en el cuadro de texto del postre elegido
    texto_postre[contador] = StringVar()  # string var es un tipo de variable de tkinter
    texto_postre[contador].set('0')  # set para establecer el valor iniciar dentro del cuatro de texto
    cuadros_postre[contador] = Entry (panel_postres,
                                      font=('Dosis',16,'bold'),#fuente de letra,tamaño y negritas
                                      bd=1,#borde
                                      width=6,#ancho del cuadro
                                      state=DISABLED,#el cuadro esta desactivado hasta que se coloque el checkbox
                                      textvariable=texto_postre[contador])#para variar los textos de cada tipo de comida
    cuadros_postre[contador].grid(row=contador,
                                  column=1,#es la columna 1 por que es la comunda siguiente a los checkbutton
                                  sticky=W)#justificar texto
    contador+=1
#--------PANEL DE ETIQUETAS DE COSTO Y CAMPOS DE ENTRADA----------
#variables
var_costo_comida = StringVar()#para el ingreso de texto de costo comida
var_costo_bebida = StringVar()#para el ingreso de texto de costo bebida
var_costo_postre = StringVar()#para el ingreso de texto de costo postre
var_subtotal = StringVar()#para el ingreso de texto de costo subtotal
var_impuesto = StringVar()#para el ingreso de texto de costo impuesto
var_total = StringVar()#para el ingreso de texto de costo total
#COSTO comida
etiqueta_costo_comida = Label(panel_costos,#para generar la etiqueda del caudro de costo comida
                              text='Costo comida',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0,# 0 para que este arriba de todo
                           column=0,)
texto_costo_comida = Entry(panel_costos,#para generar el texto del costo de la comida
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',#para que no se pueda editar, que sea solo lectura
                           textvariable=var_costo_comida)#inicializamos estas variables, para posteriormente mostrar en pantalla el valor de las operaciones
texto_costo_comida.grid(row=0,
                        column=1,# 1 por que estara alado de la etiqueda costo comida
                        padx=41)#para despegar los cacuadros de texto que tengan mas separacion entre ellos
#COSTO bebida
etiqueta_costo_bebida = Label(panel_costos,#para generar la etiqueda del caudro de costo bebida
                              text='Costo bebida',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1,#se cambia la fila para que se encuentre abajo de comida
                           column=0,)
texto_costo_bebida = Entry(panel_costos,#para generar el texto del costo de la bebida
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',#para que no se pueda editar, que sea solo lectura
                           textvariable=var_costo_bebida)#inicializamos estas variables, para posteriormente mostrar en pantalla el valor de las operaciones
texto_costo_bebida.grid(row=1,#se cambia la fila para que se encuentre abajo de comida
                        column=1,# 1 por que estara alado de la etiqueda costo bebida
                        padx=41)#para despegar los cacuadros de texto que tengan mas separacion entre ellos
#COSTO postre
etiqueta_costo_postre = Label(panel_costos,#para generar la etiqueda del caudro de costo postre
                              text='Costo postre',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2,#se cambia la fila para que se encuentre abajo de bebida
                           column=0,)
texto_costo_postre = Entry(panel_costos,#para generar el texto del costo de la postre
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',#para que no se pueda editar, que sea solo lectura
                           textvariable=var_costo_postre)#inicializamos estas variables, para posteriormente mostrar en pantalla el valor de las operaciones
texto_costo_postre.grid(row=2,#se cambia la fila para que se encuentre abajo de bebida
                        column=1,# 1 por que estara alado de la etiqueda costo postre
                        padx=42)#para despegar los cacuadros de texto que tengan mas separacion entre ellos
#SUBTOTAL
etiqueta_subtotal = Label(panel_costos,#para generar la etiqueda del caudro de subtotal
                              text='Subtotal',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0,#se cambia la fila para que se encuentre alado de comida
                           column=2,)
texto_subtotal = Entry(panel_costos,#para generar el texto del subtotal
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',#para que no se pueda editar, que sea solo lectura
                           textvariable=var_subtotal)#inicializamos estas variables, para posteriormente mostrar en pantalla el valor de las operaciones
texto_subtotal.grid(row=0,#para que sea la primera fila
                    column=3,#  en la tercera columna despues de cuadro texto comida
                    padx=42)#para despegar los cacuadros de texto que tengan mas separacion entre ellos
#IMPUESTOS
etiqueta_impuestos = Label(panel_costos,#para generar la etiqueda del caudro de impuestos
                              text='Impuestos',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuestos.grid(row=1,#se cambia la fila
                           column=2,)
texto_impuestos = Entry(panel_costos,#para generar el texto del impuestos
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',#para que no se pueda editar, que sea solo lectura
                           textvariable=var_impuesto)#inicializamos estas variables, para posteriormente mostrar en pantalla el valor de las operaciones
texto_impuestos.grid(row=1,#se cambia la fila
                     column=3,#  en la tercera columna despues de cuadro texto bebida
                     padx=42)#para despegar los cacuadros de texto que tengan mas separacion entre ellos
#TOTAL
etiqueta_total = Label(panel_costos,#para generar la etiqueda del caudro de total
                              text='Total',
                              font=('Dosis',12,'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2,#se cambia la fila
                           column=2,)
texto_total = Entry(panel_costos,#para generar el texto del total
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',#para que no se pueda editar, que sea solo lectura
                           textvariable=var_total)#inicializamos estas variables, para posteriormente mostrar en pantalla el valor de las operaciones
texto_total.grid(row=2,#se cambia la fila
                 column=3,#  en la tercera columna despues de cuadro texto postre
                 padx=42)#para despegar los cacuadros de texto que tengan mas separacion entre ellos
#BOTONES
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',12,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    botones_creados.append(boton)#crear una lista con los  4 botones
    boton.grid(row=0,
           column=columnas)
    columnas += 1

#BOTONES DE TOTAL,RECIBO,GUARDAR,RESET
botones_creados[0].config(command=total)#boton de total, se llama la funcion total
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=reset)


#AREA DEL RECIBO
texto_recibo = Text(panel_recibo,#se pone la etiqueta text por que sera un espacio de texto
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=40,#el ancho del cuadro
                    height=9)#se agrega tamaño para el espacio del texto
texto_recibo.grid(row=0,
                  column=0)
#CALCULADORA
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis',16,'bold'),
                          width=30,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)#con este comando ocupara todo el espacio de la columna
#Botones CALCULADORA
botones_calculadora = ['7','8','9','+','4','5','6','-',
                       '1','2','3','x','CE','DEL','0','/']
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora:#va recorriendo por la lista botones_calculadora
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis',10,'bold'),
                   fg='white',
                   bg='azure4',
                   bd='1',
                   width=10)
    botones_guardados.append(boton)#se agregan los botones que se tienen en calculadora
    boton.grid(row=fila,#toma el valor de fila que va incrementando dependiendo del condicional
               column=columna)
    if columna == 3:#hacemos el recorrido por las filas, para que se muestres 3 botones por fila
        fila += 1
    columna += 1
    if columna ==4 :#evitar que cree mas columnas
        columna = 0

#command llamamos a una funcion y con lambda mandamos el argumento, se coloca click_boton que es la funcion que se genero para mostar los numeros
#se coloca el numero [0] segun su poscicion en la lista botones_guardados.
botones_guardados[0].config(command=lambda: click_boton('7'))#se colocan los botones de manera ordenanda, visor_calculadora mostrara de manera ordenada
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)#llamamos a la funcion que se declaro al inicio para mostrar el resultado de la operacion con CE
botones_guardados[13].config(command=borrar)#se llama a la funcion que se declaro al inicio para el boton delete DEL
botones_guardados[14].config(command=lambda: click_boton('0'))#
botones_guardados[15].config(command=lambda: click_boton('/'))


#Evitar que se cierre ventana
aplicacion.mainloop()#mainloop sirve para que el codigo se mantenga ejecutandose



