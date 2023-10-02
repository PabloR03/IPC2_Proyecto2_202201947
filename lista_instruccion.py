from nodo_instruccion import nodo_instruccion

class lista_doble_instruccion:

    def __init__(self):
        # Referencia al primer nodo
        self.cabeza = None  
        # Referencia al último nodo
        self.cola = None  
    
    def insertar_instruccion(self, instruccion):
        # Creamos un nuevo nodo con el objeto proporcionado
        nuevo_nodo = nodo_instruccion(instruccion=instruccion) 
        # Si la lista está vacía
        if self.cabeza is None:
            # El nuevo nodo se convierte en la cabeza 
            self.cabeza = nuevo_nodo
            # El nuevo nodo también se convierte en la cola  
            self.cola = nuevo_nodo  
        else:
            # El nuevo nodo apunta al nodo anterior
            nuevo_nodo.anterior = self.cola  
            # El nodo anterior apunta al nuevo nodo
            self.cola.siguiente = nuevo_nodo  
            # El nuevo nodo se convierte en la cola de la lista
            self.cola = nuevo_nodo 

    def mostrar_instruccion(self):
        # Comenzamos desde la cabeza
        actual = self.cabeza  
        print("----------------")
        while actual:
            # Imprimimos el objeto del nodo actual
            print("Nombre:", actual.instruccion.nombre_dron, "Altura:", actual.instruccion.altura_dron)
            # Avanzamos al siguiente nodo  
            actual = actual.siguiente 
            
            # Imprimimos "None" al final para indicar el final de la lista
        print("----------------")