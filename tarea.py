
import tkinter as tk
from tkinter import messagebox
import random

# ==========================================
# CONFIGURACION GENERAL
# ==========================================

VENTANA_ANCHO = 1000
VENTANA_ALTO = 700

FONDO = "#070B1E"
AZUL = "#00D9FF"
MORADO = "#A855F7"
VERDE = "#00FF99"
BLANCO = "#FFFFFF"
GRIS = "#AAB8D0"

OPCIONES = ["PIEDRA", "PAPEL", "TIJERA"]

class NeonArena:

    def __init__(self, root):
        self.root = root
        self.root.title("ALBERTO OSORIO - Juego Python")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.configure(bg=FONDO)

        self.modo = None
        self.puntos1 = 0
        self.puntos2 = 0
        self.turno = 1
        self.jugada_usuario1 = None
        self.jugador_actual = None

        # Fondo futurista generado con codigo
        self.fondo = tk.Canvas(
            root,
            width=1000,
            height=700,
            bg=FONDO,
            highlightthickness=0
        )
        self.fondo.place(x=0, y=0)

        self.dibujar_fondo()
        self.panel = tk.Frame(root, bg=FONDO)
        self.panel.place(relx=0.5, rely=0.5, anchor="center")

        self.menu_principal()

    # ==========================================
    # FONDO FUTURISTA
    # ==========================================

    def dibujar_fondo(self):
        self.fondo.delete("all")

        # Estrellas
        random.seed(15)
        for i in range(100):
            x = random.randint(0, 1000)
            y = random.randint(0, 700)
            self.fondo.create_oval(
                x, y, x+2, y+2,
                fill=AZUL,
                outline=""
            )

        # Cuadricula futurista
        for x in range(0, 1000, 50):
            self.fondo.create_line(
                x, 0, x, 700,
                fill="#10233D"
            )

        for y in range(0, 700, 50):
            self.fondo.create_line(
                0, y, 1000, y,
                fill="#10233D"
            )

        # Lineas decorativas
        self.fondo.create_line(
            0, 150, 1000, 150,
            fill="#123D62", width=2
        )
        self.fondo.create_line(
            0, 550, 1000, 550,
            fill="#123D62", width=2
        )

    # ==========================================
    # FUNCIONES DE INTERFAZ
    # ==========================================

    def limpiar(self):
        for widget in self.panel.winfo_children():
            widget.destroy()

    def titulo(self, texto):
        tk.Label(
            self.panel,
            text=texto,
            font=("Arial", 30, "bold"),
            fg=AZUL,
            bg=FONDO
        ).pack(pady=15)

    def boton(self, texto, comando, color=AZUL):
        return tk.Button(
            self.panel,
            text=texto,
            command=comando,
            font=("Arial", 13, "bold"),
            fg=FONDO,
            bg=color,
            activebackground=BLANCO,
            activeforeground=FONDO,
            width=35,
            height=2,
            cursor="hand2",
            relief="flat",
            bd=0
        )

    # ==========================================
    # MENU PRINCIPAL
    # ==========================================

    def menu_principal(self):
        self.limpiar()
        self.modo = None

        self.titulo("NEON ARENA")

        tk.Label(
            self.panel,
            text="PIEDRA  -  PAPEL  -  TIJERA",
            font=("Arial", 15, "bold"),
            fg=BLANCO,
            bg=FONDO
        ).pack(pady=10)

        tk.Label(
            self.panel,
            text="SELECCIONA TU MODALIDAD DE JUEGO",
            font=("Arial", 12),
            fg=GRIS,
            bg=FONDO
        ).pack(pady=15)

        self.boton(
            "1. PC CONTRA USUARIO",
            lambda: self.iniciar_juego(1)
        ).pack(pady=10)

        self.boton(
            "2. PC ELIGE USUARIO 1 O USUARIO 2",
            lambda: self.iniciar_juego(2),
            MORADO
        ).pack(pady=10)

        self.boton(
            "3. USUARIO 1 CONTRA USUARIO 2",
            lambda: self.iniciar_juego(3),
            VERDE
        ).pack(pady=10)

        tk.Label(
            self.panel,
            text="SISTEMA DE JUEGO PYTHON V1.0",
            font=("Arial", 10),
            fg=GRIS,
            bg=FONDO
        ).pack(pady=25)

        self.boton(
            "SALIR DEL JUEGO",
            self.salir,
            "#FF5555"
        ).pack(pady=10)

    # ==========================================
    # INICIAR MODALIDAD
    # ==========================================

    def iniciar_juego(self, modo):
        self.modo = modo
        self.puntos1 = 0
        self.puntos2 = 0
        self.turno = 1
        self.jugada_usuario1 = None
        self.jugador_actual = None

        self.pantalla_juego()

    # ==========================================
    # PANTALLA DEL JUEGO
    # ==========================================

    def pantalla_juego(self):
        self.limpiar()

        if self.modo == 1:
            nombre = "PC CONTRA USUARIO"
        elif self.modo == 2:
            nombre = "PC ELIGE SU OPONENTE"
        else:
            nombre = "USUARIO 1 CONTRA USUARIO 2"

        self.titulo(nombre)

        self.marcador = tk.Label(
            self.panel,
            text="PC: 0     |     USUARIOS: 0",
            font=("Arial", 18, "bold"),
            fg=VERDE,
            bg=FONDO
        )
        self.marcador.pack(pady=15)

        self.instruccion = tk.Label(
            self.panel,
            text="Selecciona tu jugada",
            font=("Arial", 14, "bold"),
            fg=BLANCO,
            bg=FONDO,
            wraplength=650
        )
        self.instruccion.pack(pady=15)

        self.resultado = tk.Label(
            self.panel,
            text="¡PREPARADO PARA JUGAR!",
            font=("Arial", 15, "bold"),
            fg=AZUL,
            bg=FONDO,
            wraplength=650
        )
        self.resultado.pack(pady=15)

        self.botones_jugada = tk.Frame(
            self.panel,
            bg=FONDO
        )
        self.botones_jugada.pack(pady=10)

        for opcion in OPCIONES:
            tk.Button(
                self.botones_jugada,
                text=opcion,
                command=lambda o=opcion: self.jugar(o),
                font=("Arial", 12, "bold"),
                fg=FONDO,
                bg=AZUL,
                width=12,
                height=2,
                cursor="hand2",
                relief="flat"
            ).pack(side="left", padx=8)

        self.actualizar_marcador()

        tk.Label(
            self.panel,
            text="",
            bg=FONDO
        ).pack(pady=8)

        self.boton(
            "REINICIAR PARTIDA",
            self.reiniciar,
            MORADO
        ).pack(pady=6)

        self.boton(
            "VOLVER AL MENU",
            self.menu_principal,
            "#F5C542"
        ).pack(pady=6)

        self.boton(
            "SALIR",
            self.salir,
            "#FF5555"
        ).pack(pady=6)

    # ==========================================
    # LOGICA DEL JUEGO
    # ==========================================

    def ganador(self, jugador, computadora):

        if jugador == computadora:
            return "EMPATE"

        reglas = {
            "PIEDRA": "TIJERA",
            "PAPEL": "PIEDRA",
            "TIJERA": "PAPEL"
        }

        if reglas[jugador] == computadora:
            return "JUGADOR"

        return "PC"

    def jugar(self, jugada):

        if self.modo == 1:
            self.jugar_pc_usuario(jugada)

        elif self.modo == 2:
            self.jugar_pc_dos_usuarios(jugada)

        elif self.modo == 3:
            self.jugar_dos_usuarios(jugada)

    # ==========================================
    # MODO 1: PC CONTRA USUARIO
    # ==========================================

    def jugar_pc_usuario(self, jugada):

        pc = random.choice(OPCIONES)
        ganador = self.ganador(jugada, pc)

        if ganador == "JUGADOR":
            self.puntos2 += 1
            mensaje = "¡GANASTE! USUARIO VENCE AL PC"

        elif ganador == "PC":
            self.puntos1 += 1
            mensaje = "¡GANA LA COMPUTADORA!"

        else:
            mensaje = "¡EMPATE!"

        self.resultado.config(
            text=f"USUARIO: {jugada}  |  PC: {pc}\n{mensaje}",
            fg=VERDE if ganador == "JUGADOR" else AZUL
        )

        self.actualizar_marcador()

    # ==========================================
    # MODO 2: PC ELIGE USUARIO 1 O USUARIO 2
    # ==========================================

    def jugar_pc_dos_usuarios(self, jugada):

        if self.jugador_actual is None:

            self.jugador_actual = random.choice(
                ["USUARIO 1", "USUARIO 2"]
            )

            self.instruccion.config(
                text=f"PC HA ELEGIDO A {self.jugador_actual}. "
                     "Ese usuario debe seleccionar su jugada."
            )

            self.resultado.config(
                text="TURNO DEL JUGADOR SELECCIONADO",
                fg=MORADO
            )

            return

        pc = random.choice(OPCIONES)
        ganador = self.ganador(jugada, pc)

        if ganador == "JUGADOR":
            self.puntos2 += 1
            mensaje = f"¡GANA {self.jugador_actual}!"

        elif ganador == "PC":
            self.puntos1 += 1
            mensaje = "¡GANA EL PC!"

        else:
            mensaje = "¡EMPATE!"

        self.resultado.config(
            text=f"{self.jugador_actual}: {jugada}\n"
                 f"PC: {pc}\n{mensaje}",
            fg=VERDE
        )

        self.jugador_actual = None
        self.instruccion.config(
            text="PC seleccionará aleatoriamente a Usuario 1 o Usuario 2."
        )

        self.actualizar_marcador()

    # ==========================================
    # MODO 3: USUARIO 1 CONTRA USUARIO 2
    # ==========================================

    def jugar_dos_usuarios(self, jugada):

        if self.turno == 1:

            self.jugada_usuario1 = jugada
            self.turno = 2

            self.instruccion.config(
                text="Turno de Usuario 2. Pase el dispositivo."
            )

            self.resultado.config(
                text="JUGADA DE USUARIO 1 REGISTRADA.\n"
                     "USUARIO 2: SELECCIONE SU JUGADA.",
                fg=MORADO
            )

        else:

            jugada_usuario2 = jugada

            ganador = self.ganador(
                self.jugada_usuario1,
                jugada_usuario2
            )

            if ganador == "JUGADOR":
                self.puntos1 += 1
                mensaje = "¡GANA USUARIO 1!"

            elif ganador == "PC":
                self.puntos2 += 1
                mensaje = "¡GANA USUARIO 2!"

            else:
                mensaje = "¡EMPATE!"

            self.resultado.config(
                text=f"USUARIO 1: {self.jugada_usuario1}\n"
                     f"USUARIO 2: {jugada_usuario2}\n"
                     f"{mensaje}",
                fg=VERDE
            )

            self.turno = 1
            self.jugada_usuario1 = None

            self.instruccion.config(
                text="Nueva ronda: Usuario 1 comienza."
            )

            self.actualizar_marcador()

    # ==========================================
    # MARCADOR
    # ==========================================

    def actualizar_marcador(self):

        if self.modo == 1:
            texto = (
                f"PC: {self.puntos1}   |   "
                f"USUARIO: {self.puntos2}"
            )

        elif self.modo == 2:
            texto = (
                f"PC: {self.puntos1}   |   "
                f"USUARIOS: {self.puntos2}"
            )

        else:
            texto = (
                f"USUARIO 1: {self.puntos1}   |   "
                f"USUARIO 2: {self.puntos2}"
            )

        self.marcador.config(text=texto)

    # ==========================================
    # REINICIAR
    # ==========================================

    def reiniciar(self):

        self.puntos1 = 0
        self.puntos2 = 0
        self.turno = 1
        self.jugada_usuario1 = None
        self.jugador_actual = None

        self.actualizar_marcador()

        self.instruccion.config(
            text="Selecciona tu jugada"
            if self.modo == 1
            else (
                "PC seleccionará aleatoriamente a Usuario 1 o Usuario 2."
                if self.modo == 2
                else "Nueva ronda: Usuario 1 comienza."
            )
        )

        self.resultado.config(
            text="PARTIDA REINICIADA",
            fg=AZUL
        )

    # ==========================================
    # SALIR
    # ==========================================

    def salir(self):

        respuesta = messagebox.askyesno(
            "NEON ARENA",
            "¿Deseas salir del videojuego?"
        )

        if respuesta:
            self.root.destroy()


# ==========================================
# EJECUTAR VIDEOJUEGO
# ==========================================

if __name__ == "__main__":

    ventana = tk.Tk()

    juego = NeonArena(ventana)

    ventana.mainloop()
