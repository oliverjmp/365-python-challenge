"""
Proyecto: 365 Python Challenge
Día 59: Grid Layout Manager
Objetivo: Crear un formulario de registro estructurado y estético.
"""

import tkinter as tk
from tkinter import messagebox

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("CRM Lite - Registro de Usuario")
        self.root.geometry("350x250")
        
        # Configuramos un padding general para el contenedor principal
        self.main_frame = tk.Frame(root, padx=20, pady=20)
        self.main_frame.pack()

        # --- DISEÑO DE GRID ---
        
        # Fila 0: Título (Ocupa 2 columnas)
        tk.Label(self.main_frame, text="NUEVO CONTACTO", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # Fila 1: Nombre
        tk.Label(self.main_frame, text="Nombre:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_name = tk.Entry(self.main_frame)
        self.entry_name.grid(row=1, column=1, pady=5)

        # Fila 2: Email
        tk.Label(self.main_frame, text="Email:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_email = tk.Entry(self.main_frame)
        self.entry_email.grid(row=2, column=1, pady=5)

        # Fila 3: Categoría (Uso de Sticky para alinear)
        tk.Label(self.main_frame, text="Categoría:").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_cat = tk.Entry(self.main_frame)
        self.entry_cat.grid(row=3, column=1, pady=5)

        # Fila 4: Botón de Guardar (Ocupa 2 columnas)
        self.btn_save = tk.Button(
            self.main_frame, 
            text="Guardar en Base de Datos", 
            command=self.save_data,
            bg="#27ae60", 
            fg="white",
            width=25
        )
        self.btn_save.grid(row=4, column=0, columnspan=2, pady=20)

    def save_data(self):
        nombre = self.entry_name.get()
        email = self.entry_email.get()
        
        if nombre and email:
            # Aquí podrías conectar con la lógica del Día 48 para guardar en CSV
            messagebox.showinfo("Éxito", f"Usuario {nombre} registrado correctamente.")
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def clear_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_cat.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()