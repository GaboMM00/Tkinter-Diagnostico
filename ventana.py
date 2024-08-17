import tkinter as tk
import time
class GeneradorPiramidesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Pirámides")
        
        # Configuración de la interfaz gráfica
        self.setup_gui()
        
    def setup_gui(self):
        # Campos de entrada
        tk.Label(self.root, text="Introduce un carácter:").pack()
        self.entry_caracter = tk.Entry(self.root)
        self.entry_caracter.pack()

        tk.Label(self.root, text="Introduce un número:").pack()
        self.entry_numero = tk.Entry(self.root)
        self.entry_numero.pack()

        # Vincula la actualización de la pirámide cuando cambia el valor en el entry de número
        self.entry_numero.bind("<KeyRelease>", self.generar_piramide)

        # Área de texto para mostrar la pirámide
        self.text_area = tk.Text(self.root, height=10, width=30)
        self.text_area.pack()

        # Botón para limpiar
        btn_limpiar = tk.Button(self.root, text="Limpiar", command=self.limpiar_texto)
        btn_limpiar.pack()
    def generar_piramide(self, *args):
        return 0
    def limpiar_texto(self):
        return 0
    