# Importa el nodo
from ndrones import n_dron
# Importa tkinter
import tkinter as tk  

class listaDrones:
    def __init__(self):
        # Inicializa la cabeza de la lista como None
        self.cabeza = None  
        # Referencia al último nodo
        self.cola = None  

    def insertar_dron(self, nuevo_dron):
        nuevo_nodo = n_dron(nuevo_dron)

        if not self.cabeza:
            self.cabeza = nuevo_nodo
        elif nuevo_nodo.dron.nombre <= self.cabeza.dron.nombre:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente and nuevo_nodo.dron.nombre > actual.siguiente.dron.nombre:
                actual = actual.siguiente
            if actual.siguiente:
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente.anterior = nuevo_nodo
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def mostrar_drones_pantalla(self, scrolled_text):
        scrolled_text.delete(1.0, tk.END)  
        actual = self.cabeza
        while actual:
            scrolled_text.insert(tk.END, actual.dron.nombre + '\n')  
            actual = actual.siguiente

    def mostrar_drones(self):
        actual = self.cabeza
        while actual:
            print(actual.dron.nombre)
            actual = actual.siguiente
        
    def inicializar_lista_drones(self):
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            del actual 
            actual = siguiente
        self.cabeza = None
        self.cola = None  
    