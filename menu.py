from calo import calcular_macros
def menu():
    print(f"""
        FUNCIONES
          1.calcular tus calorias necesarias.
""")

    opcion = input("Elige una opcion... > ")
    if opcion == "1":
        calcular_macros()
menu()    