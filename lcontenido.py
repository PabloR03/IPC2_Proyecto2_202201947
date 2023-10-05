from ncontenido import n_caracteres

class listaCaracteresDrones:

    def __init__(self):
        self.cabeza = None  
        self.cola = None  

    def insertar_contenido(self, contenido):
        nuevo_nodo = n_caracteres(contenido=contenido) 
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo  
        else:
            nuevo_nodo.anterior = self.cola  
            self.cola.siguiente = nuevo_nodo  
            self.cola = nuevo_nodo 

    def mostrar_contenido(self):
        actual = self.cabeza  
        print("---------")
        while actual:
            print("Altura:", actual.contenido.altura_dron, "Simbolo:", actual.contenido.simbolo_altura)
            actual = actual.siguiente 
        print("----------")