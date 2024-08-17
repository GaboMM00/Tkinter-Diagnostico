
import tkinter as tk
import time

class GeneradorPiramidesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Pirámides")
        
        # Inicializar el tiempo del reloj
        self.tiempo_inicial = 0

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
        caracter = self.entry_caracter.get()
        numero_str = self.entry_numero.get()
        
        if not numero_str.isdigit():
            return
        
        numero = int(numero_str)

        piramide = ""
        for i in range(1, numero + 1):
            piramide += " " * (numero - i) + caracter * (2 * i - 1) + "\n"
        
        self.text_area.delete("1.0", tk.END)  # Limpia el área de texto antes de imprimir la nueva pirámide
        self.text_area.insert(tk.END, piramide)
        self.iniciar_reloj()

    def limpiar_texto(self):
        self.text_area.delete("1.0", tk.END)
        self.detener_reloj()

    def iniciar_reloj(self):
        self.tiempo_inicial = time.time()

    def detener_reloj(self):
        tiempo_final = time.time()
        tiempo_total = tiempo_final - self.tiempo_inicial
        self.text_area.insert(tk.END, f"\nTiempo en pantalla: {tiempo_total:.2f} segundos\n")