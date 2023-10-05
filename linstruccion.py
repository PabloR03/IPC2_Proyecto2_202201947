# Importa tkinter
import tkinter as tk

from ninstruccion import n_Indicaciones

class listaInstrucciones:

    def __init__(self):
        self.cabeza = None  
        self.cola = None  
    
    def insertar_instruccion(self, instruccion):
        nuevo_nodo = n_Indicaciones(instruccion=instruccion) 
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo  
        else:
            nuevo_nodo.anterior = self.cola  
            self.cola.siguiente = nuevo_nodo  
            self.cola = nuevo_nodo 

    def mostrar_instruccion(self):
        actual = self.cabeza  
        print("*************************************************")
        while actual:
            print("Nombre:", actual.instruccion.nombre_dron, "Altura:", actual.instruccion.altura_dron)
            actual = actual.siguiente 
        print("*************************************************")

    def mostrar_instruccion_pantalla(self,scrolled_text):        
        actual = self.cabeza
        scrolled_text.insert(tk.END, "Instrucciones Del Mensaje:"+'\n'+'\n')  
        while actual:
            scrolled_text.insert(tk.END, "Nombre Dron: "+ actual.instruccion.nombre_dron +" -- "+"Altura: "+ actual.instruccion.altura_dron+ '\n')
            actual = actual.siguiente
        scrolled_text.insert(tk.END,'\n')  