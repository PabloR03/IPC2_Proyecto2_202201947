class nodo_instruccion_dron:
    def __init__(self, instruccion_dron=None, siguiente=None, anterior=None):
        self.instruccion_dron = instruccion_dron
        self.siguiente = siguiente
        self.anterior = anterior