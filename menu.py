from scan_ports import menu_ports

def menu():
    print(f"""
        FUNCIONES
          1.Escaneo de Puertos
""")

    opcion = input("Elige una opcion... > ")
    if opcion == "1":
      menu_ports()

menu()    