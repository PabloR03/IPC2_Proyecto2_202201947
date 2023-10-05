# Importa el nodo
from ndrones import nodo_dron
# Importa tkinter
import tkinter as tk  

class lista_drones:
    def __init__(self):
        # Inicializa la cabeza de la lista como None
        self.cabeza = None  
        # Referencia al último nodo
        self.cola = None  

    def insertar_dron(self, nuevo_dron):
        # Crea un nuevo nodo de tipo 'nodo_dron' con el dron proporcionado
        nuevo_nodo = nodo_dron(nuevo_dron)

        if not self.cabeza:
            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
            self.cabeza = nuevo_nodo
        elif nuevo_nodo.dron.nombre <= self.cabeza.dron.nombre:
            # Comprueba si el nuevo dron debe ser insertado antes de la cabeza actual
            # Inserta el nuevo nodo antes de la cabeza
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            # Si el nuevo dron debe insertarse en medio o al final de la lista, busca la posición adecuada
            actual = self.cabeza
            while actual.siguiente and nuevo_nodo.dron.nombre > actual.siguiente.dron.nombre:
                actual = actual.siguiente
            if actual.siguiente:
                # Inserta el nuevo nodo entre dos nodos existentes
                nuevo_nodo.siguiente = actual.siguiente
                actual.siguiente.anterior = nuevo_nodo
            # Actualiza los punteros 'anterior' y 'siguiente' para insertar el nuevo nodo
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def mostrar_drones_pantalla(self, scrolled_text):
        #Borra El Contenido Actual
        scrolled_text.delete(1.0, tk.END)  
        actual = self.cabeza
        while actual:
            #Agrega el nombre del dron
            scrolled_text.insert(tk.END, actual.dron.nombre + '\n')  
            actual = actual.siguiente

    def mostrar_drones(self):
        actual = self.cabeza
        while actual:
            print(actual.dron.nombre)
            actual = actual.siguiente
        
    def inicializar_lista_drones(self):
        # Comenzamos desde la cabeza
        actual = self.cabeza
        while actual:
            # Guarda una referencia al siguiente nodo
            siguiente = actual.siguiente
            # Elimina el nodo actual  
            del actual 
            # Avanza al siguiente nodo 
            actual = siguiente
        # Después de eliminar todos los nodos, la lista está vacía  
        self.cabeza = None
        self.cola = None  
    