class nodo_instruccion:
    def __init__(self, instruccion=None, siguiente=None, anterior=None):
        self.instruccion = instruccion
        self.siguiente = siguiente
        self.anterior = anterior