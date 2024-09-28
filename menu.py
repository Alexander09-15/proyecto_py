from func.asistend import desicion, talk


print("""
Elige una opción 
1. Escaneo de puertos
""")

opción = input("Elige una opción: ")

if opción == "1":
    text = talk()
    desicion(text)
