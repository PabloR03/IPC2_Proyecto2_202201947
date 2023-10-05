class nodo_mensaje_recibido:
    def __init__(self, mensaje_recibido=None, siguiente=None, anterior=None):
        self.mensaje_recibido=mensaje_recibido
        self.siguiente = siguiente
        self.anterior = anterior