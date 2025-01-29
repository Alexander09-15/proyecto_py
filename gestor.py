import re

class Estudiante:
  def __init__(self, nombre, edad, calificaciones):
    self.nombre = nombre
    self.edad = edad
    self.calificaciones = []


  def agregar_calificacion(self, nota):
    if nota < 0.0 or nota > 100.0:
      return "La nota que intentas ingresar no es valida"
    else:
      self.calificaciones.append(nota)
      return f"Se ha agregado la siguiente nota: {nota} exitosamente"

  def calcular_promedio(self):
    if not self.calificaciones:
      return 0.0
    else:
      promedio = 0.0
      for x in self.calificaciones:
        promedio += x
      promedio/=len(self.calificaciones)
      return round(promedio , 2)

  def __str__(self):
    return self.nombre

  
class GestorEstudiante:
  def __init__ (self , estudiantes = None):
    if estudiantes is None:
        estudiantes = []
        self.estudiantes = estudiantes

  def agregar_estudiante(self , estudiante):
    if not isinstance(estudiante, Estudiante):
      return "El estudiante que intentas ingresar no es valido"
    else:
      
      self.estudiantes.append(estudiante)
      return f"Estudiante {estudiante.nombre} de edad {estudiante.edad} años, ha sido agregado con exito"

  def mostrar_estudiante(self):
    if not self.estudiantes:
      return "La lista de estudiantes esta vacia"
    else:
      std_str = ''
      for estudiante in self.estudiantes:
        std_str += f"Nombre {estudiante.nombre} Edad: {estudiante.edad} Promedio: {estudiante.calcular_promedio()} "
      return std_str 
      
  def buscar_estudiante(self , nombre):
    for n in self.estudiantes:
      if n.nombre == nombre:
        return f"Nombre: {n.nombre} Edad: {n.edad} Promedio: {n.calcular_promedio()}"

    return "El estudiante que ingresaste no existe"

  def eliminar_estudiante(self, nombre):
    for n in self.estudiantes:
      if n.nombre == nombre:
        self.estudiantes.remove(n)
        return "El estudiante ha sido eliminado"

    return "El estudiante que intentas eliminar no existe"




def validar_nombre(entrada):
  while True:
    entrada = input("Ingresa un nombre valido (Letras-Espacios): ")
    if re.match("^[A-Za-z\s]+$" , entrada):
      return entrada.lower()
      
    else:
      print("El nombre que ingresaste no es valido, debe ser como se indica.")
  

      
def validar_edad(entrada):
  while True:
    try:
        entrada = int(input("Ingresa una edad (0-50)>... : "))
        if entrada > 0 and entrada <= 50:
          return entrada
        else:
          print("Debes ingresar un rango de edad valida")
          continue
    except ValueError:
      print("Por favor ingresa un numero entero valido")
  

    
def validar_nota(entrada):
  while True:
    try:
        entrada = int(input("Ingresa una nota (0-100)>... : "))
        if entrada > 0 and entrada <= 100:
          return entrada
        else:
          print("Debes ingresar un rango de nota valida")
          continue
    except ValueError:
      print("Por favor ingresa un numero entero valido")
  
def busqueda_estudiante(nombre , gestor):
  for x in gestor.estudiantes:
    if nombre.lower() == x.nombre.lower():
      return x
    
    return None

def mostrar_menu():
  print("""GESTOR DE ESTUDIANTES
  
  1. Registrar estudiantes
  2. Agregar calificaciones a un estudiante
  3.Mostrar todos los estudiantes
  4.Buscar un estudiante por su nombre
  5. Eliminar un estudiante
  6.Salir del programa""")

def validar_opcion(opcion):
  while True:
    
      try:
        opcion = int(input("Ingresa la opcion que deseas elegir (1-6): "))
        if opcion > 0 and opcion < 7:
          return opcion
        else:
          print("Opcion no valida")
      except ValueError:
        print("Opcion no valida")
        continue

    
          
def menu_interactivo( gestor):
  mostrar_menu()


  while True:
    opcion = validar_opcion(None)
    if opcion == 1:
      nombre = validar_nombre(None)
      edad = validar_edad(None)
      estudiante = Estudiante(nombre,edad,None)
    
      print(gestor.agregar_estudiante(estudiante))
    
  
    elif opcion == 2:
       nombre = validar_nombre(None)
       estudiante = busqueda_estudiante(nombre , gestor)
       if estudiante:
         nota = validar_nota(None)
         print(estudiante.agregar_calificacion(nota))
       else:
          print("Estudiante no encontrado")
          
    elif opcion == 3:
      print(gestor.mostrar_estudiante())
      
    elif opcion == 4:
      nombre = validar_nombre(None)
      estudiante = busqueda_estudiante(nombre , gestor)
      if estudiante:
         print(f"Nombre: {estudiante.nombre} Edad: {estudiante.edad} Promedio: {estudiante.calcular_promedio()}")
         
      else:
          print("Estudiante no encontrado")
          

    elif opcion == 5:
      nombre = validar_nombre(None)
      estudiante = busqueda_estudiante(nombre , gestor)
      if estudiante:
          print(gestor.eliminar_estudiante(estudiante.nombre))
      else:
          print("Estudiante no encontrado")
          
    elif opcion == 6:
      break

gestor = GestorEstudiante()
menu_interactivo(gestor)
