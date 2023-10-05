from ncontenido import n_caracteres

class listaCaracteresDrones:

    def __init__(self):
        # Referencia al primer nodo
        self.cabeza = None  
        # Referencia al último nodo
        self.cola = None  

    def insertar_contenido(self, contenido):
        # Creamos un nuevo nodo con el objeto proporcionado
        nuevo_nodo = n_caracteres(contenido=contenido) 
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

    def mostrar_contenido(self):
        # Comenzamos desde la cabeza
        actual = self.cabeza  
        print("---------")
        while actual:
            # Imprimimos el objeto del nodo actual
            print("Altura:", actual.contenido.altura_dron, "Simbolo:", actual.contenido.simbolo_altura)
            # Avanzamos al siguiente nodo  
            actual = actual.siguiente 
            # Imprimimos "None" al final para indicar el final de la lista
        print("----------")