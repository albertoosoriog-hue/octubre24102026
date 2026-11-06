import tensorflow as tf

print("VERSION DE TENSORFLOW:", tf.__version__)
# Prueba Simple: Crear una constante

hello = tf.constant ("HOLA TENSORFLOW")
tf.print(hello)