import pygame
import random

pygame.init()

# Ventana
ANCHO = 900
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Muñeco Interactivo")

clock = pygame.time.Clock()

# Colores fondo dinámico
r = 50
g = 100
b = 150

# Jugador
x = 100
y = 450

ancho = 50
alto = 70

velocidad = 5

saltando = False
fuerza_salto = 15

# Moneda
moneda_x = random.randint(50, 850)
moneda_y = random.randint(50, 500)

puntos = 0

fuente = pygame.font.SysFont("arial", 30)

ejecutando = True

while ejecutando:

    clock.tick(60)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()

    # Movimiento
    if teclas[pygame.K_LEFT]:
        x -= velocidad

    if teclas[pygame.K_RIGHT]:
        x += velocidad

    # Salto
    if not saltando:
        if teclas[pygame.K_SPACE]:
            saltando = True

    else:
        y -= fuerza_salto
        fuerza_salto -= 1

        if fuerza_salto < -15:
            saltando = False
            fuerza_salto = 15

    # Límites
    if x < 0:
        x = 0

    if x > ANCHO - ancho:
        x = ANCHO - ancho

    # Fondo dinámico
    r = (r + 1) % 255
    g = (g + 2) % 255
    b = (b + 3) % 255

    pantalla.fill((r, g, b))

    # Piso
    pygame.draw.rect(
        pantalla,
        (40, 140, 40),
        (0, 520, ANCHO, 80)
    )

    # ===== MUÑECO =====

    # Cabeza
    pygame.draw.circle(
        pantalla,
        (255, 220, 180),
        (x + 25, y + 15),
        15
    )

    # Cuerpo
    pygame.draw.line(
        pantalla,
        (0, 0, 0),
        (x + 25, y + 30),
        (x + 25, y + 60),
        4
    )

    # Brazos
    pygame.draw.line(
        pantalla,
        (0, 0, 0),
        (x + 10, y + 40),
        (x + 40, y + 40),
        4
    )

    # Piernas
    pygame.draw.line(
        pantalla,
        (0, 0, 0),
        (x + 25, y + 60),
        (x + 10, y + 80),
        4
    )

    pygame.draw.line(
        pantalla,
        (0, 0, 0),
        (x + 25, y + 60),
        (x + 40, y + 80),
        4
    )

    # Moneda
    pygame.draw.circle(
        pantalla,
        (255, 215, 0),
        (moneda_x, moneda_y),
        15
    )

    # Colisión jugador-moneda
    jugador_rect = pygame.Rect(x, y, 50, 80)
    moneda_rect = pygame.Rect(
        moneda_x - 15,
        moneda_y - 15,
        30,
        30
    )

    if jugador_rect.colliderect(moneda_rect):

        puntos += 1

        moneda_x = random.randint(50, 850)
        moneda_y = random.randint(50, 500)

    # Marcador
    texto = fuente.render(
        f"Puntos: {puntos}",
        True,
        (255, 255, 255)
    )

    pantalla.blit(texto, (20, 20))

    # Instrucciones
    ayuda = fuente.render(
        "← → mover | ESPACIO saltar",
        True,
        (255, 255, 255)
    )

    pantalla.blit(ayuda, (20, 60))

    pygame.display.update()

pygame.quit()