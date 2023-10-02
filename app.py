import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox, filedialog, scrolledtext
import os, subprocess
#Impotar Listas y Clases

from lista_sistema import lista_doble_sistema
from osistema import sistema

from lista_contenido import lista_doble_contenido
from ocontenido import contenido

from lista_mensaje import lista_doble_mensaje
from omensaje import mensaje

from lista_instruccion import lista_doble_instruccion
from oinstruccion import instruccion

#Listas Globales 
lista_sistema_temporal = lista_doble_sistema()
lista_mensaje_temporal = lista_doble_mensaje()

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
        barra_de_opciones = tk.Frame(root, bg="dodgerblue4")
        barra_de_opciones.pack(pady=5)
        barra_de_opciones.pack_propagate()
        barra_de_opciones.configure(width=1280, height=100)
        
        #boton de inicializar
        boton_inicializar=tk.Button(barra_de_opciones, text="CARGAR ARCHIVO XML", command=self.cargar_archivo)
        boton_inicializar.place(x=28.75, y=20, width=150, height=60)

        #boton de cargar Archivo XML
        boton_cargar=tk.Button(barra_de_opciones, text="INICIALIZAR")
        boton_cargar.place(x=207.5, y=20, width=150, height=60)

        #boton salida de Archivo XML
        boton_salida=tk.Button(barra_de_opciones, text="SALIDA ARCHIVO XML")
        boton_salida.place(x=386.25, y=20, width=150, height=60)

        #boton tipo menu gestion de gestion de drones (ver listado, agregar al listado)
        boton_Gdrones=tk.Menubutton(barra_de_opciones, text="GESTION DE DRONES")        
        boton_Gdrones.place(x=564.5, y=20, width=150, height=60)
            #op del menu
        op=Menu(boton_Gdrones,tearoff=0)
        boton_Gdrones["menu"]=op
        op.add_command(label="VER LISTADO")
        op.add_command(label="AGREGAR DRON")

        # Texto largo que quieres mostrar en el botón
        boton_grafica=tk.Button(barra_de_opciones, text="GRAFICA DE SISTEMA DE DRONES",wraplength=150)
        boton_grafica.place(x=743.25, y=20, width=150, height=60)

        #boton tipo menu para la gestion de mensajes
        boton_Gmensajes=tk.Menubutton(barra_de_opciones, text="GESTION DE MENSAJES")
        boton_Gmensajes.place(x=922, y=20, width=150, height=60)
            #op del menu
        op=Menu(boton_Gmensajes,tearoff=0)
        boton_Gmensajes["menu"]=op
        op.add_command(label="VER LISTADO DE MENSAJES E INSTRUCCIONES")
        op.add_command(label="GENERAR SISTEMA DE DRONES CON MENSAJE Y TIEMPO")
        op.add_command(label="CREAR GRAFICA DE INSTRUCCIONES")
        
        #boton para ayuda
        boton_ayuda=tk.Button(barra_de_opciones, text="AYUDA", command=self.ayuda)
        boton_ayuda.place(x=1100.75, y=20, width=150, height=60)

    #Funcion para el boton CARGAR ARCHIVO XML
    def cargar_archivo(self):
        ruta = tk.Tk()
        ruta.withdraw()
        ruta.attributes('-topmost', True)
    #try:
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos XML", f"*.xml")])
        with open(ruta_archivo, "r") as archivo:
            tree = ET.parse(ruta_archivo)
            root = tree.getroot()
            #Lista Drones
            
        messagebox.showinfo("Abrir", "Archivo Cargado Correctamente.")


    #Funcion para el boton AYUDA
    def ayuda(self):
        messagebox.showinfo("AYUDA", "Programa Realizado por: Pablo Andres Rodriguez Lima \n Curso: IPC2 Seccion D \n USAC \n Segundo Semestre 2023 \n \n La ayuda se encuentra en el archivo Documentacion_IPC2_Proyecto2_202201947.pdf \n (Se abrira automaticamente al cerrar esta ventana)")
        archivo = "C:\\Users\\rodri\\Documentos\\U\\SEMESTRE 4\\LABORATORIO IPC2\\PRACTICA 2\\Entregable\\IPC2_Proyecto2_202201947\\[IPC2]Proyecto_2_2S2023-v2.pdf"
        try:
            # Abre el archivo PDF con el visor de PDF predeterminado en Windows
            subprocess.Popen(["start", "", archivo], shell=True)
        except FileNotFoundError:
            print("El archivo PDF no se encontró.")
        except Exception as e:
            print(f"Se produjo un error: {str(e)}")



if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = ventana_principal(root)
    root.mainloop()