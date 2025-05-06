#tahia teran 
#01/04/2025
import random

numero_aleatorio = random.randint(0, 7)


if numero_aleatorio == 1:
    respuesta = "✅si, definitivamente"
elif numero_aleatorio == 2:
    respuesta = "⭐con toda certeza que sí"
elif numero_aleatorio == 3:
    respuesta = "🫤respuesta confusa, intentalo de nuevo"
elif numero_aleatorio == 4:
    respuesta = "🕛pregúntalo nuevamente más tarde"
elif numero_aleatorio == 5:
    respuesta = "🤫mejor no decirte ahora"
elif numero_aleatorio == 6:
    respuesta = "❌mis fuentes dicen que no"
elif numero_aleatorio == 7:
    respuesta = "🤷‍♀️muy dudoso"
else:
    respuesta = "❓no tengo respuesta para ti"

print(respuesta)


    

