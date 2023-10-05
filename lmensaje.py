# Importa tkinter
import tkinter as tk
from nmensaje import n_Mensaje

class listaMensaje:

    def __init__(self):
        self.cabeza = None  
        self.cola = None  

    def insertar_mensaje(self, mensaje):
        nuevo_nodo = n_Mensaje(mensaje=mensaje) 
        if self.cabeza is None or mensaje.nombre_mensaje < self.cabeza.mensaje.nombre_mensaje:
            nuevo_nodo.siguiente = self.cabeza
            if self.cabeza:
                self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            if self.cola is None:
                self.cola = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente and mensaje.nombre_mensaje >= actual.siguiente.mensaje.nombre_mensaje:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            if nuevo_nodo.siguiente is None:
                self.cola = nuevo_nodo

    def mostrar_mensaje(self):
        actual = self.cabeza  
        while actual:
            actual.mensaje.lista_instruccion.mostrar_instruccion()
            actual = actual.siguiente 

    def inicializar_lista_mensaje(self):
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            del actual 
            actual = siguiente
        self.cabeza = None
        self.cola = None  

    def mostrar_mensajes_pantalla(self,scrolled_text):
        scrolled_text.delete(1.0, tk.END)
        actual = self.cabeza  
        while actual:
            scrolled_text.insert(tk.END, actual.mensaje.nombre_mensaje + '\n')
            actual.mensaje.lista_instruccion.mostrar_instruccion_pantalla(scrolled_text)
            actual = actual.siguiente