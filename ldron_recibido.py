from ndron_recibido import n_dronCambio

class listaDronIntercambiado:

    def __init__(self):
        self.cabeza = None  
        self.cola = None  

    def insertar_dron_recibido(self, dron_recibido):
        nuevo_nodo = n_dronCambio(dron_recibido=dron_recibido) 
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo  
        else:
            nuevo_nodo.anterior = self.cola  
            self.cola.siguiente = nuevo_nodo  
            self.cola = nuevo_nodo 

    def mostrar_dron_recibido(self):
        actual = self.cabeza  
        print("---------")
        while actual:
            print("Nombre Del Dron:", actual.dron_recibido.nombre_dron)
            actual.dron_recibido.lista_instruccion_dron.mostrar_instruccion_dron()
            actual = actual.siguiente 
        print("----------")