"""
Proyecto: 365 Python Challenge
Día 58: GUI Foundations
Objetivo: Crear una ventana interactiva que salude al usuario.
"""

import tkinter as tk
from tkinter import messagebox

class FirstApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Oliver's Python Challenge - Day 58")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        # 1. Crear un Label (Etiqueta de texto)
        self.label_titulo = tk.Label(
            root, 
            text="Bienvenido a la Fase 6", 
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            pady=20
        )
        self.label_titulo.pack()

        # 2. Crear un Entry (Caja de texto para el usuario)
        self.label_instruccion = tk.Label(root, text="Introduce tu nombre:", bg="#f0f0f0")
        self.label_instruccion.pack()
        
        self.entrada_nombre = tk.Entry(root, font=("Arial", 12))
        self.entrada_nombre.pack(pady=10)

        # 3. Crear un Button (El disparador de eventos)
        self.boton_saludo = tk.Button(
            root, 
            text="¡Salúdame!", 
            command=self.saludar_usuario, # Callback: qué función ejecutar al hacer clic
            bg="#3498db", 
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        )
        self.boton_saludo.pack(pady=20)

    def saludar_usuario(self):
        nombre = self.entrada_nombre.get()
        if nombre:
            # Mostramos un cuadro de diálogo emergente
            messagebox.showinfo("Saludo Pro", f"Hola {nombre}, bienvenido al desarrollo GUI.")
        else:
            messagebox.showwarning("Atención", "Por favor, escribe un nombre primero.")

if __name__ == "__main__":
    # Inicializar la ventana principal
    root = tk.Tk()
    
    # Instanciar nuestra clase
    app = FirstApp(root)
    
    # 4. EL EVENT LOOP: Mantiene la ventana abierta y escuchando
    print("🖥️ Aplicación GUI iniciada. Esperando interacción del usuario...")
    root.mainloop()
    print("👋 Aplicación cerrada.")