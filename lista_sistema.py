from nodo_sistema import nodo_sistema

class lista_doble_sistema:

    def __init__(self):
        # Referencia al primer nodo
        self.cabeza = None  
        # Referencia al último nodo
        self.cola = None  

    def insertar_sistema(self, sistema):
        # Creamos un nuevo nodo con el objeto proporcionado
        nuevo_nodo = nodo_sistema(sistema=sistema) 
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

    def mostrar_sistema(self):
        # Comenzamos desde la cabeza
        actual = self.cabeza  
        print("----------------")
        while actual:
            # Imprimimos el objeto del nodo actual
            print("Nombre Sistema:", actual.sistema.nombre_sistema, "Altura Máxima Sistema:", actual.sistema.altura_sistema, "Cantidad Drones:", actual.sistema.cantidad_drones)
            actual.sistema.lista_contenido.mostrar_contenido()
            # Avanzamos al siguiente nodo  
            actual = actual.siguiente 
            # Imprimimos "None" al final para indicar el final de la lista
        print("----------------")
