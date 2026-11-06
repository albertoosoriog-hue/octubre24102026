import tkinter as tk
from tkinter import messagebox

# Base de datos temporal
datos = {}

# Ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Datos")
ventana.geometry("500x350")

# Función para limpiar pantalla
def limpiar():
    for widget in ventana.winfo_children():
        widget.destroy()

# Menú principal
def menu_principal():
    limpiar()

    titulo = tk.Label(
        ventana,
        text="MENÚ PRINCIPAL",
        font=("Arial", 18, "bold")
    )
    titulo.pack(pady=20)

    tk.Button(
        ventana,
        text="Registrar Datos",
        width=20,
        command=registrar_datos
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Actualizar Datos",
        width=20,
        command=actualizar_datos
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Eliminar Datos",
        width=20,
        command=eliminar_datos
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Salir",
        width=20,
        bg="red",
        fg="white",
        command=ventana.quit
    ).pack(pady=20)

# Registrar datos
def registrar_datos():
    limpiar()

    tk.Label(ventana, text="REGISTRAR DATOS",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(ventana, text="ID:").pack()
    id_entry = tk.Entry(ventana)
    id_entry.pack()

    tk.Label(ventana, text="Nombre:").pack()
    nombre_entry = tk.Entry(ventana)
    nombre_entry.pack()

    def guardar():
        id_usuario = id_entry.get()
        nombre = nombre_entry.get()

        if id_usuario and nombre:
            datos[id_usuario] = nombre
            messagebox.showinfo("Éxito", "Datos registrados correctamente")
        else:
            messagebox.showwarning("Error", "Complete todos los campos")

    tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)

    tk.Button(
        ventana,
        text="Volver al Menú",
        command=menu_principal
    ).pack()

# Actualizar datos
def actualizar_datos():
    limpiar()

    tk.Label(ventana, text="ACTUALIZAR DATOS",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(ventana, text="ID:").pack()
    id_entry = tk.Entry(ventana)
    id_entry.pack()

    tk.Label(ventana, text="Nuevo Nombre:").pack()
    nombre_entry = tk.Entry(ventana)
    nombre_entry.pack()

    def actualizar():
        id_usuario = id_entry.get()
        nuevo_nombre = nombre_entry.get()

        if id_usuario in datos:
            datos[id_usuario] = nuevo_nombre
            messagebox.showinfo("Éxito", "Datos actualizados")
        else:
            messagebox.showwarning("Error", "ID no encontrado")

    tk.Button(
        ventana,
        text="Actualizar",
        command=actualizar
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Volver al Menú",
        command=menu_principal
    ).pack()

# Eliminar datos
def eliminar_datos():
    limpiar()

    tk.Label(ventana, text="ELIMINAR DATOS",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(ventana, text="ID:").pack()
    id_entry = tk.Entry(ventana)
    id_entry.pack()

    def eliminar():
        id_usuario = id_entry.get()

        if id_usuario in datos:
            del datos[id_usuario]
            messagebox.showinfo("Éxito", "Registro eliminado")
        else:
            messagebox.showwarning("Error", "ID no encontrado")

    tk.Button(
        ventana,
        text="Eliminar",
        command=eliminar
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Volver al Menú",
        command=menu_principal
    ).pack()

# Iniciar programa
menu_principal()
ventana.mainloop()