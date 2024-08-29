puntuacion = int(input("Ingresa el número de tu calificación (0-100): "))

if puntuacion > 100 or puntuacion < 0:
    print("Por favor ingresa un número entre 0-100.")
elif puntuacion >= 90:
    print(f"Tu puntuación de {puntuacion} es sobresaliente, ¡felicitaciones!")
elif puntuacion >= 80:
    print(f"Tu puntuación de {puntuacion} es notable, ¡felicitaciones!")
elif puntuacion >= 70:
    print(f"Tu puntuación de {puntuacion} te permite aprobar, ¡felicitaciones!")
else:
    print(f"Tu puntuación de {puntuacion} no alcanza para aprobar, ¡esfuérzate más!")
