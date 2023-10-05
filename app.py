import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox, filedialog, scrolledtext, Label, Entry
import os, subprocess
#Impotar Listas y Clases

from ldron import lista_doble_dron
from odron import dron

from ldrones import lista_drones
from odrones import drones

from lsistema import lista_doble_sistema
from osistema import sistema

from lcontenido import lista_doble_contenido
from ocontenido import contenido

from lmensaje import lista_doble_mensaje
from omensaje import mensaje

from lmensaje_recibido import lista_doble_mensaje_recibido
from omensaje_recibido import mensaje_recibido

from ldron_recibido import lista_doble_dron_recibido
from odron_recibido import dron_recibido

from linstruccion_dron import lista_doble_instruccion_dron
from oinstruccion_dron import instruccion_dron

from linstruccion import lista_doble_instruccion
from oinstruccion import instruccion

#Lista Global Par XML Entrada
listaDronesparaTodo = lista_drones()
listaSistemaparaTodo= lista_doble_sistema()
listaMensajeparaTodo = lista_doble_mensaje()
#Lista Global Par XML Salida
listaMensajeResivido = lista_doble_mensaje_recibido()


class ventana_principal:
    def __init__(self, root):
        #ruta de archivo a analizar_Archivo
        self.archivo_analizado=True

        #datos de ventana principal
        self.root = root
        self.root.title("P2 Sistemas de Drones de encriptamiento - 202201947")
        self.root.geometry("1280x720")
        self.root.resizable(0,0)
        #cuadro que contiene a los botones
        barra_de_opciones = tk.Frame(root, bg="forestgreen")
        barra_de_opciones.pack(pady=5)
        barra_de_opciones.pack_propagate()
        barra_de_opciones.configure(width=1280, height=100)
        
        #cuadro que contiene a los botones secundarios
        self.barra_de_opcionessec = tk.Frame(root, bg="limegreen")
        self.barra_de_opcionessec.pack(pady=5)
        self.barra_de_opcionessec.pack_propagate()
        self.barra_de_opcionessec.configure(width=1280, height=50)

        #cuadro que contiene al text box
        #cuadro De Texto
        cuadrotexto_frame=tk.Frame(root,bg="mediumseagreen")
        self.cuadroTexto = scrolledtext.ScrolledText(cuadrotexto_frame, bg="White", width=152, height=31)
        self.cuadroTexto.place(x=10, y=10)
        #area de texto para el nombre del dron
        self.text_area = tk.Text(self.barra_de_opcionessec)
        self.text_area.place(x=500, y=11, width=150, height=30)
        cuadrotexto_frame.pack(pady=3)
        cuadrotexto_frame.pack_propagate()
        cuadrotexto_frame.configure(width=1260, height=520)

        #boton de cargar Archivo XML
        boton_inicializar=tk.Button(barra_de_opciones, text="CARGAR ARCHIVO XML", command=self.cargar_archivo)
        boton_inicializar.place(x=28.75, y=20, width=150, height=60)

        #boton de inicializar
        boton_cargar=tk.Button(barra_de_opciones, text="INICIALIZAR", command=self.inicializar)
        boton_cargar.place(x=207.5, y=20, width=150, height=60)

        #boton salida de Archivo XML
        boton_salida=tk.Button(barra_de_opciones, text="SALIDA ARCHIVO XML", command=self.generar_xml)
        boton_salida.place(x=386.25, y=20, width=150, height=60)

        #boton tipo menu gestion de gestion de drones (ver listado, agregar al listado)
        boton_Gdrones=tk.Menubutton(barra_de_opciones, text="GESTION DE DRONES")        
        boton_Gdrones.place(x=564.5, y=20, width=150, height=60)
            #op del menu
        op=Menu(boton_Gdrones,tearoff=0)
        boton_Gdrones["menu"]=op
        op.add_command(label="VER LISTADO", command=self.mostrar_drones)
        #op.add_command(label="AGREGAR DRON")

        # Definir el botón y asignar la función graficar_drones como su comando
        boton_grafica = tk.Button(barra_de_opciones, text="GRAFICA DE SISTEMA DE DRONES", command=self.graficar_drones, wraplength=150)
        boton_grafica.place(x=743.25, y=20, width=150, height=60)


        #boton tipo menu para la gestion de mensajes
        boton_Gmensajes=tk.Menubutton(barra_de_opciones, text="GESTION DE MENSAJES")
        boton_Gmensajes.place(x=922, y=20, width=150, height=60)
            #op del menu
        op=Menu(boton_Gmensajes,tearoff=0)
        boton_Gmensajes["menu"]=op
        op.add_command(label="VER LISTADO DE MENSAJES E INSTRUCCIONES", command=self.mostrar_lista_mensaje)
        #op.add_command(label="GENERAR SISTEMA DE DRONES CON MENSAJE Y TIEMPO")
        op.add_command(label="CREAR GRAFICA DE INSTRUCCIONES")
        
        #boton para ayuda
        boton_ayuda=tk.Button(barra_de_opciones, text="AYUDA", command=self.ayuda)
        boton_ayuda.place(x=1100.75, y=20, width=150, height=60)

    #Funcion para el boton CARGAR ARCHIVO XML
    def cargar_archivo(self):
        ruta = tk.Tk()
        ruta.withdraw()
        ruta.attributes('-topmost', True)
        try:
            ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos XML", f"*.xml")])
            with open(ruta_archivo, "r") as archivo:
                tree = ET.parse(ruta_archivo)
                root = tree.getroot()
                #Lista Dron
                nivel_drones = root.find('.//listaDrones')
                for nivel_drones in nivel_drones.findall('.//dron'):
                    nombre_dron=nivel_drones.text
                    nuevo_dron=drones(nombre_dron)
                    listaDronesparaTodo.insertar_dron(nuevo_dron)
                #Lista Sistema Drones
                nivel_sistemas_drones = root.find('.//listaSistemasDrones')
                for sistema_drones in nivel_sistemas_drones.findall('.//sistemaDrones'):
                    nombre_sistema = sistema_drones.get('nombre')
                    altura_maxima = sistema_drones.find('alturaMaxima').text 
                    cantidad_drones = sistema_drones.find('cantidadDrones').text
                    #Lista Contenido Según El Dron
                    lista_dron=lista_doble_dron()
                    for nivel_contenido in sistema_drones.findall('.//contenido'):
                        nombre_dron_contenido = nivel_contenido.find('dron').text
                        #Se Busca en Lista Dron
                        alturas = nivel_contenido.find('alturas')
                        #Lista Contenido Alturas
                        lista_contenido=lista_doble_contenido()
                        for altura in alturas.findall('altura'):
                            altura_contenido = altura.get('valor') 
                            simbolo_altura = altura.text
                            nuevo_contenido=contenido(altura_contenido, simbolo_altura)
                            lista_contenido.insertar_contenido(nuevo_contenido)
                        nuevo_dron=dron(nombre_dron_contenido, lista_contenido)
                        lista_dron.insertar_dron(nuevo_dron)
                    nuevo_sistema=sistema(nombre_sistema, altura_maxima, cantidad_drones, lista_dron)
                    listaSistemaparaTodo.insertar_sistema(nuevo_sistema)
                #Lista Mensajes
                lista_mensajes = root.find('.//listaMensajes')
                for nivel_mensaje in lista_mensajes.findall('.//Mensaje'):
                    nombre_mensaje = nivel_mensaje.get('nombre') 
                    sistema_drones_mensaje = nivel_mensaje.find('sistemaDrones').text
                    #Contenido Instrucciones
                    nivel_instrucciones = nivel_mensaje.find('instrucciones')
                    #Lista_Intruccion
                    lista_instruccion_temporal=lista_doble_instruccion()
                    for nivel_instruccion in nivel_instrucciones.findall('instruccion'):
                        dron_instruccion = nivel_instruccion.get('dron')
                        altura_dron = nivel_instruccion.text
                        nueva_instruccion=instruccion(dron_instruccion, altura_dron)
                        lista_instruccion_temporal.insertar_instruccion(nueva_instruccion)
                    nuevo_mensaje=mensaje(nombre_mensaje, sistema_drones_mensaje, lista_instruccion_temporal)
                    listaMensajeparaTodo.insertar_mensaje(nuevo_mensaje)
                self.desencriptar_lista_mensaje()
            messagebox.showinfo("Abrir", "Archivo Cargado")
        except Exception as e:
            messagebox.showerror("Error", f"No se ha seleccionado ningún archivo: {str(e)}")
            return

#Funcion para el INICIALIZAR EL SISTEMA
    def inicializar(self):
        if listaDronesparaTodo.cabeza is not None and (listaSistemaparaTodo.cabeza is not None or listaMensajeparaTodo is not None):
            listaDronesparaTodo.inicializar_lista_drones()
            listaSistemaparaTodo.inicializar_lista_sistema()
            listaMensajeparaTodo.inicializar_lista_mensaje()
            messagebox.showinfo("Inicializar", "Sistema Limpio")
        else:
            listaDronesparaTodo.mostrar_drones()
            messagebox.showinfo("Sistema", "Limpiando Drones")
            listaSistemaparaTodo.mostrar_sistema()
            messagebox.showinfo("Sistema", "Limpiando Sistema de drones")
            listaMensajeparaTodo.mostrar_mensaje()
            messagebox.showinfo("Sistema", "Limpiando Mensajes")
            messagebox.showwarning("Error", "No hay archivo cargado")
        
    #Función Ver Listado Drones De Gestión De Drones
    def mostrar_drones(self):

        #boton que tiene el cuadro de texto para agregar dron
        self.boton_agregar_dron=tk.Button(self.barra_de_opcionessec, text="AGREGAR DRON", command=self.agregar_dron)
        self.boton_agregar_dron.place(x=700, y=11, width=150, height=30)

        #poner el boton de agregar dron visible
        if listaDronesparaTodo.cabeza is not None:
            listaDronesparaTodo.mostrar_drones_pantalla(self.cuadroTexto)
            messagebox.showinfo("Gestión ", "Lista Drones Mostrada")
        else:
            messagebox.showwarning("Error", "No hay archivo cargado")      

    #Función Agregar Dron De Gestión De Drones
    def agregar_dron(self):
        #Obtiene el nombre del dron desde la caja_texto
        nombre_dron = self.text_area.get("1.0", "end-1c")
        #Obtiene la cabeza de la lista de drones
        nodo_dron = listaDronesparaTodo.cabeza
        # Verifica si el nombre del dron es una cadena vacía
        if nombre_dron == "":
            messagebox.showwarning("Error", "Llena el cuadro de texto")
        else:
            # Itera a través de la lista de drones para verificar si el nombre del dron ya existe
            while nodo_dron:
                if nodo_dron.dron.nombre == nombre_dron:
                    # Si encuentra un dron con el mismo nombre, muestra un mensaje de advertencia y sale de la función
                    messagebox.showwarning("Error", "El Dron ya existe en la lista.")
                    return
                # Avanza al siguiente nodo en la lista
                nodo_dron = nodo_dron.siguiente
            # Si el nombre del dron no existe en la lista, crea un nuevo dron y lo inserta en la lista
            listaDronesparaTodo.insertar_dron(drones(nombre_dron))
            # Llama a la función para mostrar la lista actualizada
            listaDronesparaTodo.mostrar_drones_pantalla(self.cuadroTexto)
            # Muestra un mensaje informativo
            messagebox.showinfo("Gestión", "Dron Agregado")

#Función para procesar todos los mensajes del archivo XML de entrada
    def desencriptar_lista_mensaje(self):
        nodo_mensaje = listaMensajeparaTodo.cabeza
        nodo_mensaje_variable = listaMensajeparaTodo.cabeza
        #Variables Globales En La Función
        nombre_mensaje_recibido=""
        nombre_sistema_recibido=""
        mensaje_recibido_des=""
        tiempo_optimo_des=0
        while nodo_mensaje is not None:
            #Se Recorren Todos Los Mensajes
            while nodo_mensaje_variable is not None:
                if nodo_mensaje.mensaje.nombre_mensaje == nodo_mensaje_variable.mensaje.nombre_mensaje:
                    #--Nombre Del Mensaje
                    nombre_mensaje_recibido=nodo_mensaje.mensaje.nombre_mensaje
                    nodo_sistema = listaSistemaparaTodo.cabeza
                    #Se Recorren Los Sistemas Para encontrar Una Coincidencia
                    while nodo_sistema is not None:
                        #Si el nombre_sistema_dron de mensaje es igual al nombre sistema del sistema 
                        if nodo_mensaje.mensaje.nombre_sistema_dron == nodo_sistema.sistema.nombre_sistema:
                            #--Nombre Del Sistema
                            nombre_sistema_recibido=nodo_sistema.sistema.nombre_sistema
                            nodo_instruccion = nodo_mensaje.mensaje.lista_instruccion.cabeza
                            #Se recorren las instrucciones del mensaje actual
                            while nodo_instruccion is not None:
                                nodo_dron = nodo_sistema.sistema.lista_dron.cabeza
                                #Se recorren la lista de dron para buscar el nombre_dron 
                                while nodo_dron is not None:
                                    #Si el nombre_dron de la instruccion es igual al nombre_dron del dron
                                    if nodo_instruccion.instruccion.nombre_dron == nodo_dron.dron.nombre_dron:
                                        nodo_contenido = nodo_dron.dron.lista_contenido.cabeza
                                        #Se Recorre el Contenido del dron actual para buscar su altura
                                        while nodo_contenido is not None:
                                            #Si la altura del Contenido es la misma que la altura de la instruccion
                                            if nodo_instruccion.instruccion.altura_dron == nodo_contenido.contenido.altura_dron:
                                                #--Mensaje Recibido
                                                mensaje_recibido_des+=nodo_contenido.contenido.simbolo_altura
                                            nodo_contenido=nodo_contenido.siguiente
                                        break #Se rompe la iteracion del dron
                                    #Si el nombre no es igual, se pasa el siguientre dron
                                    else:
                                        nodo_dron = nodo_dron.siguiente
                                #Se pasa la siguiente instrucción
                                nodo_instruccion = nodo_instruccion.siguiente
                            #Se crea un nodo dron para recorrer todos los drones del sistema
                            nodo_dron_tiempo=nodo_sistema.sistema.lista_dron.cabeza
                            #Se crea una lista temporal dron recibido
                            lista_dron_recibido_temporal=lista_doble_dron_recibido()
                            #Se recorre cada dron del sistema
                            while nodo_dron_tiempo is not None:
                                #--Nombre Dron Recibido
                                nombre_dron=nodo_dron_tiempo.dron.nombre_dron
                                #Contador para saber el segundo
                                tiempo_optimo=1
                                #Se crea un nodo instrucción para recorrer todas las instrucciones
                                nodo_instruccion_mensaje=nodo_mensaje.mensaje.lista_instruccion.cabeza
                                #Se crea una lista instrucción dron temporal
                                lista_instruccion_dron_temporal=lista_doble_instruccion_dron()
                                #Se recorre cada instrucción del sistema
                                while nodo_instruccion_mensaje is not None:
                                    #Si el nombre del dron de la instrucción es igual al nombre dron del dron actual
                                    if nodo_instruccion_mensaje.instruccion.nombre_dron == nodo_dron_tiempo.dron.nombre_dron:
                                        #Se inserta una nueva instrucción en el segundo actual
                                        accion="Emitir Luz"
                                        #Se crea una nueva instrucción dron y se inserta en la lista temporal
                                        nueva_instruccion_dron=instruccion_dron(tiempo_optimo, accion)
                                        lista_instruccion_dron_temporal.insertar_instruccion_dron(nueva_instruccion_dron)
                                    #Si el nombre del dron de la instrucción no es igual al nombre dron del dron actual
                                    elif nodo_instruccion_mensaje.instruccion.nombre_dron != nodo_dron_tiempo.dron.nombre_dron:
                                        #Se inserta una nueva instrucción en el segundo actual
                                        accion="Esperar"
                                        #Se crea una nueva instrucción dron y se inserta en la lista temporal
                                        nueva_instruccion_dron=instruccion_dron(tiempo_optimo, accion)
                                        lista_instruccion_dron_temporal.insertar_instruccion_dron(nueva_instruccion_dron)
                                    #Se aumenta el contador del segundo
                                    tiempo_optimo+=1
                                    #Se Pasa a la siguiente instrucción
                                    nodo_instruccion_mensaje=nodo_instruccion_mensaje.siguiente
                                #Se crea un nuevo dron recibido y se inserta en la lista
                                nuevo_don_recibido=dron_recibido(nombre_dron,lista_instruccion_dron_temporal)
                                lista_dron_recibido_temporal.insertar_dron_recibido(nuevo_don_recibido)
                                #Se reinicia el contador del segundo actual
                                tiempo_optimo=1
                                #Se pasa al siguiente dron
                                nodo_dron_tiempo=nodo_dron_tiempo.siguiente
                            #Se recorre cada instrucción del sistema
                            nodo_instruccion_tiempo=nodo_mensaje.mensaje.lista_instruccion.cabeza
                            #Se recore la lista de instrucciones
                            while nodo_instruccion_tiempo is not None:
                                #Se aumenta en 1 el tiempo por cada instruccón
                                tiempo_optimo_des+=1
                                #Se pasa a la siguiente instrucción
                                nodo_instruccion_tiempo=nodo_instruccion_tiempo.siguiente
                            #Se crea un nuevo mensaje recibido y se inserta en la lista
                            nuevo_mensaje_recibido=mensaje_recibido(nombre_mensaje_recibido, nombre_sistema_recibido, tiempo_optimo_des, mensaje_recibido_des, lista_dron_recibido_temporal)
                            listaMensajeResivido.insertar_mensaje_recibido(nuevo_mensaje_recibido) 
                            #Se reinicia la cadena y los contadores
                            mensaje_recibido_des=""
                            tiempo_optimo_des=0
                            break #Se Rompre La Iteracion Del Sistema
                        else:
                            #Se pasa al siguiente sistema
                            nodo_sistema=nodo_sistema.siguiente
                    break #Se Rompre La Iteración Del Mensaje
                else:
                    #Se pasa al siguiente mensaje
                    nodo_mensaje_variable=nodo_mensaje_variable.siguiente
            #Se pasa al siguiente mensaje
            nodo_mensaje=nodo_mensaje.siguiente

#Función General: Generar archivo XML de salida
    def generar_xml(self):
        if listaMensajeResivido.cabeza is None:
            messagebox.showwarning("Error", "No hay archivo cargado")
            return
        listaMensajeResivido.escribir_archivo_salida()
        messagebox.showinfo("Generar ", "Archivo Xml Generado")

    #Funcion para el boton AYUDA
    def ayuda(self):
        messagebox.showinfo("AYUDA", "Programa Realizado por: Pablo Andres Rodriguez Lima \n Curso: IPC2 Seccion D \n USAC \n Segundo Semestre 2023 \n \n La ayuda se encuentra en el archivo Documentacion_IPC2_Proyecto2_202201947.pdf \n (Se abrira automaticamente al cerrar esta ventana)")
        archivo = "C:\\Users\\rodri\\Documentos\\U\\SEMESTRE 4\\LABORATORIO IPC2\\PRACTICA 2\\Entregable\\IPC2_Proyecto2_202201947\\20220147_Documentacion.pdf"
        try:
            # Abre el archivo PDF con el visor de PDF predeterminado en Windows
            subprocess.Popen(["start", "", archivo], shell=True)
        except FileNotFoundError:
            print("El archivo PDF no se encontró.")
        except Exception as e:
            print(f"Se produjo un error: {str(e)}")

    def graficar_drones(self):
        nodo_sistema = listaSistemaparaTodo.cabeza
        if nodo_sistema is not None:
            listaSistemaparaTodo.graficar_sistema_drones()
            messagebox.showinfo("Gestión", "Sistema Drones Graficados")
        else:
            messagebox.showwarning("Error", "No hay archivo cargado")

    def mostrar_lista_mensaje(self):
        #boton que tiene el cuadro de texto para agregar dron
        self.boton_agregar_dron=tk.Button(self.barra_de_opcionessec,wraplength=130, text="BUSCAR MENSJAES por nombre", command=self.mostrar_informacion_mensaje)
        self.boton_agregar_dron.place(x=700, y=11, width=150, height=30)
        if listaMensajeparaTodo.cabeza is not None:
            listaMensajeparaTodo.mostrar_mensajes_pantalla(self.cuadroTexto)
            messagebox.showinfo("Gestión", "Lista Mensajes Mostrada")
        else:
            messagebox.showwarning("Error", "No hay archivo cargado")

    def mostrar_informacion_mensaje(self):
        #self.cuadroTexto.delete()
        #Se verifica que la lista esté llena
        if listaMensajeResivido.cabeza is None:
            messagebox.showwarning("Error ", "No hay archivo cargado")
            return
        #Obtiene el nombre del mensaje desde la caja_texto
        nombre_mensaje=self.text_area.get("1.0", "end-1c")
        #Variable Para Saber si el mensaje Existe
        mensaje_existe=False
        #Verifica si el nombre del mensaje es una cadena vacía
        if nombre_mensaje == "":
            messagebox.showwarning("Error", "Llene el cuadro de texto")
        else:
            # Itera a través de la lista mensaje para verificar si el mensaje existe
            nodo_mensaje=listaMensajeResivido.cabeza
            while nodo_mensaje is not None:
                if nodo_mensaje.mensaje_recibido.nombre_mensaje == nombre_mensaje:
                    mensaje_existe=True
                    break
                else:
                    # Avanza al siguiente nodo en la lista
                    nodo_mensaje = nodo_mensaje.siguiente
            if mensaje_existe is True:
                listaMensajeResivido.mostrar_mensajes_recibido_pantalla(nombre_mensaje,self.cuadroTexto)
                messagebox.showinfo("Gestión", "Mensaje Mostrado ")
            else:
                messagebox.showwarning("Error", "El Mensaje no existe en la lista.")
                
if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = ventana_principal(root)
    root.mainloop()