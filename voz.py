import tkinter as tk
from tkinter import ttk, messagebox
import pyttsx3
import pygame
import vlc

# -------------------------
# CONFIGURACIÓN DE VOZ
# -------------------------

voz = pyttsx3.init()

def hablar(texto):
    voz.say(texto)
    voz.runAndWait()

# -------------------------
# CONFIGURACIÓN DE AUDIO
# -------------------------

pygame.mixer.init()

# Cambiar por tu archivo mp3
# ejemplo: musica.mp3

def reproducir_audio():
    pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(-1)

def detener_audio():
    pygame.mixer.music.stop()

# -------------------------
# REPRODUCIR VIDEO
# -------------------------

def reproducir_video():

    reproductor = vlc.MediaPlayer("intro.mp4")
    reproductor.play()

    hablar("Bienvenido al videojuego RPG")

# -------------------------
# BASE DE DATOS
# -------------------------

jugadores = {}

# -------------------------
# VENTANA
# -------------------------

root = tk.Tk()
root.title("RPG GAME")
root.geometry("800x550")
root.configure(bg="#202020")

# -------------------------
# LIMPIAR
# -------------------------

def limpiar():
    for widget in root.winfo_children():
        widget.destroy()

# -------------------------
# MENÚ PRINCIPAL
# -------------------------

def menu():

    limpiar()

    tk.Label(
        root,
        text="🎮 VIDEOJUEGO RPG",
        font=("Arial", 25, "bold"),
        bg="#202020",
        fg="gold"
    ).pack(pady=20)

    tk.Button(
        root,
        text="📝 Registrar Jugador",
        width=25,
        command=registrar
    ).pack(pady=5)

    tk.Button(
        root,
        text="✏️ Actualizar Jugador",
        width=25,
        command=actualizar
    ).pack(pady=5)

    tk.Button(
        root,
        text="🗑️ Eliminar Jugador",
        width=25,
        command=eliminar
    ).pack(pady=5)

    tk.Button(
        root,
        text="📋 Mostrar Jugadores",
        width=25,
        command=mostrar
    ).pack(pady=5)

    tk.Button(
        root,
        text="🎥 Ver Video",
        width=25,
        command=reproducir_video
    ).pack(pady=5)

    tk.Button(
        root,
        text="🔊 Música ON",
        width=25,
        command=reproducir_audio
    ).pack(pady=5)

    tk.Button(
        root,
        text="🔇 Música OFF",
        width=25,
        command=detener_audio
    ).pack(pady=5)

    tk.Button(
        root,
        text="🚪 Salir",
        width=25,
        bg="red",
        fg="white",
        command=root.quit
    ).pack(pady=15)

# -------------------------
# REGISTRAR
# -------------------------

def registrar():

    limpiar()

    hablar("Registrar jugador")

    tk.Label(
        root,
        text="Registrar Jugador",
        font=("Arial",18,"bold")
    ).pack()

    tk.Label(root,text="ID").pack()
    txt_id = tk.Entry(root)
    txt_id.pack()

    tk.Label(root,text="Nombre").pack()
    txt_nombre = tk.Entry(root)
    txt_nombre.pack()

    tk.Label(root,text="Nivel").pack()
    txt_nivel = tk.Entry(root)
    txt_nivel.pack()

    def guardar():

        jugadores[txt_id.get()] = {
            "nombre": txt_nombre.get(),
            "nivel": txt_nivel.get()
        }

        messagebox.showinfo(
            "OK",
            "Jugador Guardado"
        )

        hablar("Jugador registrado correctamente")

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
        command=menu
    ).pack()

# -------------------------
# ACTUALIZAR
# -------------------------

def actualizar():

    limpiar()

    hablar("Actualizar jugador")

    tk.Label(
        root,
        text="Actualizar Jugador",
        font=("Arial",18,"bold")
    ).pack()

    tk.Label(root,text="ID").pack()
    txt_id = tk.Entry(root)
    txt_id.pack()

    tk.Label(root,text="Nuevo Nivel").pack()
    txt_nivel = tk.Entry(root)
    txt_nivel.pack()

    def modificar():

        if txt_id.get() in jugadores:

            jugadores[txt_id.get()]["nivel"] = txt_nivel.get()

            hablar("Jugador actualizado")

            messagebox.showinfo(
                "OK",
                "Datos actualizados"
            )

    tk.Button(
        root,
        text="Actualizar",
        bg="orange",
        command=modificar
    ).pack(pady=10)

    tk.Button(
        root,
        text="Volver al Menú",
        command=menu
    ).pack()

# -------------------------
# ELIMINAR
# -------------------------

def eliminar():

    limpiar()

    hablar("Eliminar jugador")

    tk.Label(
        root,
        text="Eliminar Jugador",
        font=("Arial",18,"bold")
    ).pack()

    tk.Label(root,text="ID").pack()

    txt_id = tk.Entry(root)
    txt_id.pack()

    def borrar():

        if txt_id.get() in jugadores:

            del jugadores[txt_id.get()]

            hablar("Jugador eliminado")

            messagebox.showinfo(
                "OK",
                "Registro eliminado"
            )

    tk.Button(
        root,
        text="Eliminar",
        bg="red",
        fg="white",
        command=borrar
    ).pack(pady=10)

    tk.Button(
        root,
        text="Volver al Menú",
        command=menu
    ).pack()

# -------------------------
# MOSTRAR TABLA
# -------------------------

def mostrar():

    limpiar()

    columnas = ("ID","Nombre","Nivel")

    tabla = ttk.Treeview(
        root,
        columns=columnas,
        show="headings"
    )

    for c in columnas:
        tabla.heading(c,text=c)

    for idj, datos in jugadores.items():

        tabla.insert(
            "",
            "end",
            values=(
                idj,
                datos["nombre"],
                datos["nivel"]
            )
        )

    tabla.pack(fill="both", expand=True, pady=20)

    tk.Button(
        root,
        text="Volver al Menú",
        command=menu
    ).pack()

# -------------------------
# INICIO DEL JUEGO
# -------------------------

hablar("Bienvenido al Videojuego RPG")

menu()

root.mainloop()