class Producto:
	def __init__ (self, nombre , cantidad , precio):
		self.nombre = nombre
		self.cantidad = cantidad
		self.precio = precio 
		
		
	def agregar_stock(self , cantidad , inventario):
		self.cantidad += cantidad
		
		return f"Producto {self.nombre} modificado con exito!"
		
	def reducir_stock(self,cantidad , inventario):
			if self.cantidad >cantidad:
				self.cantidad -= cantidad
				return f"Se ha eliminado {cantidad} unidad/es del producto {self.nombre}"
			else:
				inventario.eliminar_producto(self)
				return "Se elimino el producto al eliminar todas las existencias en el stock"
		
		
	def mostrar_informacion(self, producto):
		return f"""
		Nombre: {producto.nombre}
		Cantidad: {producto.cantidad}
		Precio: {producto.precio}
		"""
		
		
		
class Inventario:
		def __init__ (self , lista_productos = None):
			if lista_productos is None:
				lista_productos = []
				self.lista_productos = lista_productos
				
				
		def agregar_producto(self, producto):
			self.lista_productos.append(producto)
			return f"""
			Se ha agregado el siguiente producto 
			Nombre: {producto.nombre}
			Cantidad: {producto.cantidad}
			Precio: {producto.precio}
			"""
			
		def eliminar_producto(self,producto):
			self.lista_productos.remove(producto)
			return "Producto eliminado con exito"
			
			
		def listar_productos(self):
			salida = [f"Nombre: {x.nombre} Cantidad: {x.cantidad} Precio: {x.precio}" for x in self.lista_productos]
			return "\n".join(salida)
			
			
			
def validar_nombre(nombre):
			nombre = input("Ingresa el nombre: ")
			while not nombre.replace(" " , "").isalpha():
				nombre = input("Ingresa un nombre valido:  ")
			return nombre
			
					
def validar_precio(precio):
	while True:
		try:
			precio = float(input("Ingresa el precio en decimal: "))
			if precio > 0.0:
				return precio
			else:
				print("Precio invalido")			
		except ValueError:
			print("Formato de precio incorrecto")
			
			
def validar_cantidad(cantidad):
			while not isinstance(cantidad , int ) or cantidad < 0:
				try:
					cantidad = int(input("Ingresa la cantidad: "))
					if cantidad > 0:
						return cantidad
					else:
						print("Cantidad invalida")
				except ValueError:
					print("Formato de Cantidad incorrecto (Numero entero)")
					
					
def existencia_producto(producto , inventario ):
					for x in inventario.lista_productos:
						if x.nombre == producto:
							return x
					return False
							

def validar_opcion(opcion):
					while not isinstance( opcion , int) or opcion < 0 and opcion > 5:
							try:
								opcion = int(input("Ingresa una de las opciones: "))
								if opcion > 0 and opcion < 6:
									return opcion
								else:
									print("Ingresa una opcion valida")	
							except ValueError:
								print("Ingresa una opcion valida")
											
	
def opcion_dos(decision):
			 	while True:
					 	    decision = input("Agregar o Reducir Stock?: ").lower()
					 	    if decision == "agregar":
					 	    	return decision
					 	    
					 	    elif decision == "reducir":
					 	    	return decision
					 	    else:
					 	    	print("Opcion invalida")
				
																																																												
																		
def mostrar_menu():
			print("""
			1.Agregar Producto
			2.Modificar Stock de un Producto
			3.Mostrar Todos los Producto
			4.Salir
			""")
			
def menu_interactivo(inventario):
			mostrar_menu()
			while True:
				opcion = validar_opcion(None)
				if opcion == 1:
					nombre = validar_nombre(None)
					estado = existencia_producto(nombre ,inventario)
					if not estado:
						precio = validar_precio(None)
						cantidad = validar_cantidad(None)
						producto = Producto(nombre , cantidad , precio)
						print(inventario.agregar_producto(producto))
					else:
						print("El producto ya existe")
				elif opcion == 2:
					nombre = validar_nombre(None)
					existencia = existencia_producto(nombre , inventario)
					if not existencia:
					  	print("El producto no existe")
					  	
					else:
					 	decision = opcion_dos(None)
					 	if decision == "agregar":
					 		cantidad = validar_cantidad(None)
					 		print(existencia.agregar_stock(cantidad , inventario))
					 	else:
					 	  		cantidad = validar_cantidad(None)
					 	  		print(existencia.reducir_stock(cantidad , inventario))
				
				elif opcion == 3:
					if inventario.lista_productos:
						estado = inventario.listar_productos()
						print(estado)
					else:
						print("Inventario vacio")
						
						
				elif opcion == 4:
					break
			

inventario = Inventario()	
menu_interactivo(inventario)
