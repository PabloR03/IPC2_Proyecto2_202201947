import xml.etree.ElementTree as ET
# Importa tkinter
import tkinter as tk
from tkinter import messagebox
from nmensaje_recibido import n_MensajeIntercambiado
import os

class listaMensajeIntercambiado:

    def __init__(self):
        self.cabeza = None  
        self.cola = None  

    def insertar_mensaje_recibido(self, mensaje_recibido):
        nuevo_nodo = n_MensajeIntercambiado(mensaje_recibido=mensaje_recibido) 
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo  
        else:
            nuevo_nodo.anterior = self.cola  
            self.cola.siguiente = nuevo_nodo  
            self.cola = nuevo_nodo 

    def mostrar_mensaje_recibido(self):
        actual = self.cabeza  
        print("*******************************************")
        while actual:
            print("Nombre Mensaje:", actual.mensaje_recibido.nombre_mensaje, "Sistema Dron:", actual.mensaje_recibido.nombre_sistema_dron, "Tiempo Optimo:", actual.mensaje_recibido.tiempo_optimo, "Mensaje Recibido:", actual.mensaje_recibido.mensaje_recibido)
            print(" ")
            actual.mensaje_recibido.lista_dron_recibido.mostrar_dron_recibido()
            actual = actual.siguiente 
        print("*******************************************")

    def mostrar_mensajes_recibido_pantalla(self,nombre_mensaje,scrolled_text):
        scrolled_text.delete(1.0, tk.END)
        actual = self.cabeza  
        while actual:
            if actual.mensaje_recibido.nombre_mensaje==nombre_mensaje:
                scrolled_text.insert(tk.END, "Nombre: "+ actual.mensaje_recibido.nombre_mensaje +'\n')
                scrolled_text.insert(tk.END, "Sistema a utilizar: "+ actual.mensaje_recibido.nombre_sistema_dron +'\n')
                scrolled_text.insert(tk.END, "Mensaje antes de enviar: "+actual.mensaje_recibido.mensaje_recibido+'\n')
                scrolled_text.insert(tk.END, "Posible Tiempo en encriptar: "+str(actual.mensaje_recibido.tiempo_optimo)+'\n')
                break
            else:
                actual = actual.siguiente

    def escribir_archivo_salida(self):
        actual=self.cabeza
        respuesta = ET.Element("respuesta")
        lista_mensajes = ET.SubElement(respuesta, "listaMensajes") 
    
        while actual is not None:
            mensaje = ET.SubElement(lista_mensajes, "mensaje")
            mensaje.set("nombre", actual.mensaje_recibido.nombre_mensaje)

            sistema_drones = ET.SubElement(mensaje, "sistemaDrones")
            sistema_drones.text = actual.mensaje_recibido.nombre_sistema_dron
            
            tiempo_optimo = ET.SubElement(mensaje, "tiempoOptimo")
            tiempo_optimo.text = str(actual.mensaje_recibido.tiempo_optimo)
            
            mensaje_recibido = ET.SubElement(mensaje, "mensajeRecibido")
            mensaje_recibido.text = actual.mensaje_recibido.mensaje_recibido

            instrucciones = ET.SubElement(mensaje, "instrucciones")
            tiempo_optimo_mensaje=actual.mensaje_recibido.tiempo_optimo

            contador_tiempo=1
            while int(tiempo_optimo_mensaje)>=contador_tiempo:
                tiempo= ET.SubElement(instrucciones, "tiempo")
                tiempo.set("valor", str(contador_tiempo))
                acciones=ET.SubElement(tiempo, "acciones")
                n_dron=actual.mensaje_recibido.lista_dron_recibido.cabeza
                while n_dron is not None:
                    n_Indicaciones=n_dron.dron_recibido.lista_instruccion_dron.cabeza
                    while n_Indicaciones is not None:
                        if n_Indicaciones.instruccion_dron.tiempo==contador_tiempo:
                            dron=ET.SubElement(acciones, "Dron")
                            dron.set("nombre",  n_dron.dron_recibido.nombre_dron)
                            dron.text=n_Indicaciones.instruccion_dron.accion
                            break
                        else:
                            n_Indicaciones=n_Indicaciones.siguiente
                    n_dron=n_dron.siguiente
                contador_tiempo+=1
            actual = actual.siguiente

        datos=ET.tostring(respuesta)
        datos=str(datos)
        self.xml_identado(respuesta)
        arbol_xml=ET.ElementTree(respuesta)
        arbol_xml.write("SALIDA_XML.xml",encoding="UTF-8",xml_declaration=True)

    def xml_identado(self, element, indent='  '):
        queue = [(0, element)]
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level + 1)
            if queue:
                element.tail = '\n' + indent * queue[0][0]
            else:
                element.tail = '\n' + indent * (level - 1)
            queue[0:0] = children