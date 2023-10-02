from nodo_mensaje import nodo_mensaje

class lista_doble_mensaje:

    def __init__(self):
        # Referencia al primer nodo
        self.cabeza = None  
        # Referencia al último nodo
        self.cola = None  

    def insertar_mensaje(self, mensaje):
        # Creamos un nuevo nodo con el objeto proporcionado
        nuevo_nodo = nodo_mensaje(mensaje=mensaje) 
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

    def mostrar_mensaje(self):
        # Comenzamos desde la cabeza
        actual = self.cabeza  
        print("----------------")
        while actual:
            # Imprimimos el objeto del nodo actual
            print("Nombre Sistema:", actual.mensaje.nombre_mensaje, "Sistema Dron:", actual.mensaje.nombre_sistema_dron)
            print(" ")
            actual.mensaje.lista_instruccion.mostrar_instruccion()
            # Avanzamos al siguiente nodo  
            actual = actual.siguiente 
            # Imprimimos "None" al final para indicar el final de la lista
        print("----------------")


    def comparar(self, lista_sistema):
            nodo_mensaje = self.cabeza
            nodo_sistema = lista_sistema.cabeza

            nodo_instruccion = nodo_mensaje.mensaje.lista_instruccion.cabeza
            nodo_contenido = nodo_sistema.sistema.lista_contenido.cabeza

            while nodo_mensaje is not None:
                #El Mensaje que se está Procesando
                print(nodo_mensaje.mensaje.nombre_mensaje)
                nodo_sistema = lista_sistema.cabeza

                while nodo_sistema is not None:
                    #Si el nombre_sistema_dron de mensaje es igual al nombre sistema del sistema 
                    if nodo_mensaje.mensaje.nombre_sistema_dron == nodo_sistema.sistema.nombre_sistema:
                        #Se recorren las instrucciones del mensaje actual
                        print("----------")
                        nodo_instruccion = nodo_mensaje.mensaje.lista_instruccion.cabeza
                        nodo_contenido = nodo_sistema.sistema.lista_contenido.cabeza
                        
                        while nodo_instruccion is not None:
                            print(nodo_instruccion.instruccion.altura_dron)
                            nodo_instruccion = nodo_instruccion.siguiente

                        print("Los Sistemas Son Iguales")
                        break
                    else:
                        print("Los Sistemas No Son Iguales")
                        nodo_sistema=nodo_sistema.siguiente

                nodo_mensaje=nodo_mensaje.siguiente
            return True


