import tkinter as tk
from tkinter import messagebox

# Diccionario para almacenar jugadores
jugadores = {}

# ----------------------------
# Funciones
# ----------------------------

def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()

def menu_principal():
    limpiar_ventana()

    titulo = tk.Label(
        ventana,
        text="🎮 VIDEOJUEGO RPG",
        font=("Arial", 20, "bold"),
        fg="blue"
    )
    titulo.pack(pady=20)

    tk.Button(
        ventana,
        text="📝 Registrar Jugador",
        width=25,
        height=2,
        command=registrar_jugador
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="✏️ Actualizar Jugador",
        width=25,
        height=2,
        command=actualizar_jugador
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="🗑️ Eliminar Jugador",
        width=25,
        height=2,
        command=eliminar_jugador
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="🚪 Salir",
        width=25,
        height=2,
        bg="red",
        fg="white",
        command=ventana.quit
    ).pack(pady=15)

# ----------------------------
# Registrar Jugador
# ----------------------------

def registrar_jugador():
    limpiar_ventana()

    tk.Label(
        ventana,
        text="Registrar Nuevo Jugador",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(ventana, text="ID Jugador").pack()
    txt_id = tk.Entry(ventana)
    txt_id.pack()

    tk.Label(ventana, text="Nombre").pack()
    txt_nombre = tk.Entry(ventana)
    txt_nombre.pack()

    tk.Label(ventana, text="Nivel").pack()
    txt_nivel = tk.Entry(ventana)
    txt_nivel.pack()

    def guardar():
        jugador_id = txt_id.get()
        nombre = txt_nombre.get()
        nivel = txt_nivel.get()

        if jugador_id in jugadores:
            messagebox.showwarning(
                "Error",
                "El jugador ya existe."
            )
        else:
            jugadores[jugador_id] = {
                "nombre": nombre,
                "nivel": nivel
            }

            messagebox.showinfo(
                "Éxito",
                "Jugador registrado."
            )

    tk.Button(
        ventana,
        text="Guardar",
        bg="green",
        fg="white",
        command=guardar
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Volver al Menú",
        command=menu_principal
    ).pack()

# ----------------------------
# Actualizar Jugador
# ----------------------------

def actualizar_jugador():
    limpiar_ventana()

    tk.Label(
        ventana,
        text="Actualizar Jugador",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(ventana, text="ID Jugador").pack()
    txt_id = tk.Entry(ventana)
    txt_id.pack()

    tk.Label(ventana, text="Nuevo Nivel").pack()
    txt_nivel = tk.Entry(ventana)
    txt_nivel.pack()

    def actualizar():
        jugador_id = txt_id.get()

        if jugador_id in jugadores:
            jugadores[jugador_id]["nivel"] = txt_nivel.get()

            messagebox.showinfo(
                "Actualizado",
                f"Jugador actualizado al nivel {txt_nivel.get()}"
            )
        else:
            messagebox.showwarning(
                "Error",
                "Jugador no encontrado."
            )

    tk.Button(
        ventana,
        text="Actualizar",
        bg="orange",
        command=actualizar
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Volver al Menú",
        command=menu_principal
    ).pack()

# ----------------------------
# Eliminar Jugador
# ----------------------------

def eliminar_jugador():
    limpiar_ventana()

    tk.Label(
        ventana,
        text="Eliminar Jugador",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(ventana, text="ID Jugador").pack()

    txt_id = tk.Entry(ventana)
    txt_id.pack()

    def eliminar():
        jugador_id = txt_id.get()

        if jugador_id in jugadores:
            del jugadores[jugador_id]

            messagebox.showinfo(
                "Eliminado",
                "Jugador eliminado."
            )
        else:
            messagebox.showwarning(
                "Error",
                "Jugador no existe."
            )

    tk.Button(
        ventana,
        text="Eliminar",
        bg="red",
        fg="white",
        command=eliminar
    ).pack(pady=10)

    tk.Button(
        ventana,
        text="Volver al Menú",
        command=menu_principal
    ).pack()

# ----------------------------
# Ventana principal
# ----------------------------

ventana = tk.Tk()
ventana.title("Videojuego RPG")
ventana.geometry("500x400")
ventana.resizable(False, False)

menu_principal()

ventana.mainloop()