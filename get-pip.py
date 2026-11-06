import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# 1. Datos de entrenamiento
correos = [
    "Gana dinero ahora, reclama tu premio gratis",
    "Haz clic aquí para reclamar tu recompensa",
    "Has ganado un celular, reclama tu premio",
    "Confirma tu contraseña urgentemente",
    "Compra ahora y recibe un descuento increíble",
    "Reunión de equipo mañana a las diez",
    "Adjunto el informe solicitado",
    "Hola, podemos hablar esta tarde",
    "La factura del mes está adjunta",
    "Confirmo la cita para el próximo lunes"
]

categorias = [
    "spam", "spam", "spam", "spam", "spam",
    "legitimo", "legitimo", "legitimo",
    "legitimo", "legitimo"
]

# 2. Entrenar el modelo
modelo = Pipeline([
    ("vectorizador", TfidfVectorizer()),
    ("clasificador", MultinomialNB())
])

modelo.fit(correos, categorias)

# 3. Analizar un correo nuevo
print("=== DETECTOR DE SPAM ===")
mensaje = input("Escribe el texto del correo: ")

if mensaje.strip():
    resultado = modelo.predict([mensaje])[0]

    if resultado == "spam":
        print("ALERTA: POSIBLE CORREO SPAM")
    else:
        print("RESULTADO: POSIBLE CORREO LEGÍTIMO")
else:
    print("Debes escribir el texto de un correo.")