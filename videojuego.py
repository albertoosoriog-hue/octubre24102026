import tkinter as tk
from tkinter import ttk, messagebox

# Base de datos de jugadores
jugadores = {}

# -------------------------
# Ventana principal
# -------------------------
root = tk.Tk()
root.title("Videojuego RPG")
root.geometry("700x500")
root.config(bg="#1e1e1e")

# -------------------------
# Limpiar pantalla
# -------------------------
def limpiar():
    for widget in root.winfo_children():
        widget.destroy()

# -------------------------
# Menú Principal
# -------------------------
def menu_principal():

    limpiar()

    titulo = tk.Label(
        root,
        text="🎮 VIDEOJUEGO RPG",
        font=("Arial", 24, "bold"),
        bg="#1e1e1e",
        fg="gold"
    )
    titulo.pack(pady=20)

    tk.Button(
        root,
        text="📝 Registrar Jugador",
        width=25,
        height=2,
        command=registrar_jugador
    ).pack(pady=5)

    tk.Button(
        root,
        text="✏️ Actualizar Jugador",
        width=25,
        height=2,
        command=actualizar_jugador
    ).pack(pady=5)

    tk.Button(
        root,
        text="🗑️ Eliminar Jugador",
        width=25,
        height=2,
        command=eliminar_jugador
    ).pack(pady=5)

    tk.Button(
        root,
        text="📋 Mostrar Jugadores",
        width=25,
        height=2,
        command=mostrar_jugadores
    ).pack(pady=5)

    tk.Button(
        root,
        text="🚪 Salir",
        width=25,
        height=2,
        bg="red",
        fg="white",
        command=root.quit
    ).pack(pady=20)

# -------------------------
# Registrar Jugador
# -------------------------
def registrar_jugador():

    limpiar()

    tk.Label(
        root,
        text="Registrar Jugador",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    tk.Label(root, text="ID").pack()
    txt_id = tk.Entry(root)
    txt_id.pack()

    tk.Label(root, text="Nombre").pack()
    txt_nombre = tk.Entry(root)
    txt_nombre.pack()

    tk.Label(root, text="Nivel").pack()
    txt_nivel = tk.Entry(root)
    txt_nivel.pack()

    def guardar():
        id_jugador = txt_id.get()

        if id_jugador == "":
            messagebox.showerror("Error", "Ingrese un ID")
            return

        jugadores[id_jugador] = {
            "nombre": txt_nombre.get(),
            "nivel": txt_nivel.get()
        }

        messagebox.showinfo(
            "Correcto",
            "Jugador registrado"
        )

    tk.Button(
        root,
        text="Guardar",
        bg="green",
        fg="white",
        command=guardar
    ).pack(pady=10)

    tk.Button(
        root,
        text="Volver al Menú",
        command=menu_principal
    ).pack()

# -------------------------
# Actualizar Jugador
# -------------------------
def actualizar_jugador():

    limpiar()

    tk.Label(
        root,
        text="Actualizar Jugador",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    tk.Label(root, text="ID Jugador").pack()
    txt_id = tk.Entry(root)
    txt_id.pack()

    tk.Label(root, text="Nuevo Nombre").pack()
    txt_nombre = tk.Entry(root)
    txt_nombre.pack()

    tk.Label(root, text="Nuevo Nivel").pack()
    txt_nivel = tk.Entry(root)
    txt_nivel.pack()

    def actualizar():

        id_jugador = txt_id.get()

        if id_jugador in jugadores:

            jugadores[id_jugador]["nombre"] = txt_nombre.get()
            jugadores[id_jugador]["nivel"] = txt_nivel.get()

            messagebox.showinfo(
                "Actualizado",
                "Jugador actualizado"
            )

        else:
            messagebox.showerror(
                "Error",
                "Jugador no encontrado"
            )

    tk.Button(
        root,
        text="Actualizar",
        bg="orange",
        command=actualizar
    ).pack(pady=10)

    tk.Button(
        root,
        text="Volver al Menú",
        command=menu_principal
    ).pack()

# -------------------------
# Eliminar Jugador
# -------------------------
def eliminar_jugador():

    limpiar()

    tk.Label(
        root,
        text="Eliminar Jugador",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    tk.Label(root, text="ID Jugador").pack()

    txt_id = tk.Entry(root)
    txt_id.pack()

    def eliminar():

        id_jugador = txt_id.get()

        if id_jugador in jugadores:

            del jugadores[id_jugador]

            messagebox.showinfo(
                "Eliminado",
                "Jugador eliminado"
            )

        else:
            messagebox.showerror(
                "Error",
                "Jugador no existe"
            )

    tk.Button(
        root,
        text="Eliminar",
        bg="red",
        fg="white",
        command=eliminar
    ).pack(pady=10)

    tk.Button(
        root,
        text="Volver al Menú",
        command=menu_principal
    ).pack()

# -------------------------
# Tabla de jugadores
# -------------------------
def mostrar_jugadores():

    limpiar()

    tk.Label(
        root,
        text="Listado de Jugadores",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    columnas = ("ID", "Nombre", "Nivel")

    tabla = ttk.Treeview(
        root,
        columns=columnas,
        show="headings"
    )

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=180)

    for id_jugador, datos in jugadores.items():

        tabla.insert(
            "",
            "end",
            values=(
                id_jugador,
                datos["nombre"],
                datos["nivel"]
            )
        )

    tabla.pack(pady=20)

    tk.Button(
        root,
        text="Volver al Menú",
        command=menu_principal
    ).pack()

# -------------------------
# Iniciar aplicación
# -------------------------
menu_principal()
root.mainloop()