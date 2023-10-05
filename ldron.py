from ndron import n_dron

class listaDron:

    def __init__(self):
        self.cabeza = None  
        self.cola = None  

    def insertar_dron(self, dron):
        nuevo_nodo = n_dron(dron=dron) 
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo  
        else:
            nuevo_nodo.anterior = self.cola  
            self.cola.siguiente = nuevo_nodo  
            self.cola = nuevo_nodo 

    def mostrar_drones(self):
        actual = self.cabeza  
        print("---------------Datos De Los Drones----------------")
        while actual:
            print(actual.dron.nombre_dron)
            actual.dron.lista_contenido.mostrar_contenido()
            actual = actual.siguiente 
        print("**************************************************")
        print("")
