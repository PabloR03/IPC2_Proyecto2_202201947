from ninstruccion_dron import n_instruccionDron

class listaInstruccionDrones:

    def __init__(self):
        self.cabeza = None  
        self.cola = None  

    def insertar_instruccion_dron(self, instruccion_dron):
        nuevo_nodo = n_instruccionDron(instruccion_dron=instruccion_dron) 
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo  
        else:
            nuevo_nodo.anterior = self.cola  
            self.cola.siguiente = nuevo_nodo  
            self.cola = nuevo_nodo 
    
    def mostrar_instruccion_dron(self):
        actual = self.cabeza  
        print("*************************************************")
        while actual:
            print("Tiempo:", actual.instruccion_dron.tiempo, "Acción:", actual.instruccion_dron.accion)
            actual = actual.siguiente 
        print("*************************************************")