import socket
def escanear_puerto(ip, puerto):
    """Escanea un puerto en una IP específica."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        resultado = s.connect_ex((ip, puerto))
        return resultado == 0  # Retorna True si el puerto está abierto
    except Exception as e:
        print(f"Error al escanear el puerto {puerto}: {e}")
        return False
    finally:
        s.close()

def escanear_rango(ip, rango_inferior, rango_superior):
    """Escanea un rango de puertos en una IP específica."""
    resultados = {}
    for puerto in range(rango_inferior, rango_superior + 1):
        abierto = escanear_puerto(ip, puerto)
        resultados[puerto] = abierto
    return resultados

def menu_ports():
    """Muestra un menú para interactuar con el escáner de puertos."""
    while True:
        print("\nMenú de Escaneo de Puertos")
        print("1. Escanear un rango de puertos")
        print("2. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            ip = input("Introduce la IP a escanear: ")
            rango_inferior = int(input("Introduce el puerto inferior: "))
            rango_superior = int(input("Introduce el puerto superior: "))
            
            resultados = escanear_rango(ip, rango_inferior, rango_superior)

            for puerto, abierto in resultados.items():
                estado = "abierto" if abierto else "cerrado"
                print(f"Puerto {puerto} está {estado}")
        
        elif opcion == '2':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "_main_":
    menu_ports()