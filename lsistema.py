from nsistema import n_sistemaDrones
import os
class listaSistemaDrones:

    def __init__(self):
        # Referencia al primer nodo
        self.cabeza = None  
        # Referencia al último nodo
        self.cola = None  

    def insertar_sistema(self, sistema):
        # Creamos un nuevo nodo con el objeto proporcionado
        nuevo_nodo = n_sistemaDrones(sistema=sistema) 
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
        while actual:
            # Imprimimos el objeto del nodo actual
            print("Nombre Sistema:", actual.sistema.nombre_sistema, "Altura Máxima Sistema:", actual.sistema.altura_sistema, "Cantidad Drones:", actual.sistema.cantidad_drones)
            actual.sistema.lista_dron.mostrar_drones()
            # Avanzamos al siguiente nodo  
            actual = actual.siguiente 

    def graficar_sistema_drones(self):
        actual = self.cabeza
        while actual is not None:
            nombre=actual.sistema.nombre_sistema
            altura=actual.sistema.altura_sistema
            cantidad=actual.sistema.cantidad_drones
            f = open(nombre+'.dot','w')
            texto="""
                digraph G {
                subgraph cluster_0 {fillcolor="limegreen" style="filled" gradientangle="200"
                    node [ style=filled,shape="square",fillcolor="palegreen" ]"Altura: """+altura+"""";
                    node [ style=filled,shape="square",fillcolor="palegreen" ]"Cantidad: """+cantidad+"""";
                    label=" """+nombre+""""
                    }
                a0 [shape=none label=<
                <TABLE border="0" cellspacing="10" cellpadding="10">\n
                <TR><TD bgcolor="steelblue" gradientangle="315">Altura (metros)</TD>\n"""
            contador_altura=1
            while int(altura)>=contador_altura:
                texto+="""<TD style="radial" bgcolor="skyblue" gradientangle="60">"""+str(contador_altura)+"""</TD>\n"""
                contador_altura+=1
            texto+="""</TR>"""

            n_dron=actual.sistema.lista_dron.cabeza
            while n_dron is not None:
                texto+="""<TR>"""
                texto+="""<TD style="radial" bgcolor="steelblue"  gradientangle="60">"""+n_dron.dron.nombre_dron+"""</TD>\n"""
                n_caracteres = n_dron.dron.lista_contenido.cabeza
                while n_caracteres is not None:
                    texto+="""<TD style="radial" bgcolor="skyblue" gradientangle="60">"""+n_caracteres.contenido.simbolo_altura+"""</TD>\n"""
                    n_caracteres=n_caracteres.siguiente
                n_dron=n_dron.siguiente
                texto+="""</TR>"""

            texto+="""</TABLE>>];\n}"""
            f.write(texto)
            f.close()
            os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
            os.system(f'dot -Tpng {nombre}.dot -o Grafica_{nombre}.png')
            actual=actual.siguiente

    def inicializar_lista_sistema(self):
        # Comenzamos desde la cabeza
        actual = self.cabeza
        while actual:
            # Guarda una referencia al siguiente nodo
            siguiente = actual.siguiente
            # Elimina el nodo actual  
            del actual 
            # Avanza al siguiente nodo 
            actual = siguiente
        # Después de eliminar todos los nodos, la lista está vacía  
        self.cabeza = None
        self.cola = None  