import os
import time
import random


class nodo:
	def __init__(self, dato):
		self.__dato = dato
		self.__next = None

	@property
	def dato(self):
		return self.__dato

	@property
	def next(self):
		return self.__next

	@next.setter
	def next(self, next):
		self.__next = next


class nodoDoble:
	def __init__(self, dato):
		self.__dato = dato
		self.__next = None
		self.__anterior = None

	@property
	def dato(self):
		return self.__dato

	@property
	def next(self):
		return self.__next

	@next.setter
	def next(self, next):
		self.__next = next

	@property
	def anterior(self):
		return self.__anterior

	@anterior.setter
	def anterior(self, anterior):
		self.__anterior = anterior


class ListaADN:
	def __init__(self):
		self.__head = None

	@property
	def head(self):
		return self.__head

	def cargar(self, nombre):
		archivo = open(nombre, "r")
		lineas = archivo.readlines()
		archivo.close()
		cola = None
		i = 1
		while i < len(lineas):
			secuencia = lineas[i].split("\t")[0]
			j = 0
			while j < len(secuencia):
				nuevo = nodo(secuencia[j])
				if self.__head == None:
					self.__head = nuevo
				else:
					cola.next = nuevo
				cola = nuevo
				j = j + 1
			i = i + 1


class TablaPrefijos:
	def __init__(self):
		self.__primero = None
		self.__ultimo = None
		self.__largo = 0
		self.__mostrar = False
		self.__movimiento = 0

	@property
	def primero(self):
		return self.__primero

	def construir(self, patron, mostrar):
		self.__primero = nodoDoble(0)
		self.__ultimo = self.__primero
		self.__largo = 1
		self.__mostrar = mostrar
		self.__movimiento = 0
		self.ver_inicio(patron)
		k = 0
		i = 1
		while i < len(patron):
			while k > 0 and patron[i] != patron[k]:
				self.ver_devuelve(patron, i, k)
				k = self.obtener(k - 1).dato
			self.ver_compara(patron, i, k)
			if patron[i] == patron[k]:
				k = k + 1
			nuevo = nodoDoble(k)
			self.__ultimo.next = nuevo
			nuevo.anterior = self.__ultimo
			self.__ultimo = nuevo
			self.__largo = self.__largo + 1
			self.ver_anota(patron, k)
			i = i + 1

	def obtener(self, pos):
		if pos < self.__largo / 2:
			actual = self.__primero
			i = 0
			while i < pos:
				actual = actual.next
				i = i + 1
		else:
			actual = self.__ultimo
			i = 0
			while i < self.__largo - 1 - pos:
				actual = actual.anterior
				i = i + 1
		return actual

















#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def ver_inicio(self, patron):
		if self.__mostrar:
			os.system("cls")
			print("------------------ inicio ------------------")
			self.mostrar_tabla(patron, True)

	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def ver_devuelve(self, patron, i, k):
		if self.__mostrar:
			self.__movimiento = self.__movimiento + 1
			self.dibujar(patron, i, k, "movimiento " + str(self.__movimiento), self.__movimiento)
			print("         No coinciden y k es", k, ", asi que k se devuelve a tabla[", k - 1, "] =", self.obtener(k - 1).dato)
			self.mostrar_tabla(patron, False)

	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def ver_compara(self, patron, i, k):
		if self.__mostrar:
			self.__movimiento = self.__movimiento + 1
			if i == len(patron) - 1:
				self.dibujar(patron, i, k, "tabla final", self.__movimiento)
			else:
				self.dibujar(patron, i, k, "movimiento " + str(self.__movimiento), self.__movimiento)

	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def ver_anota(self, patron, k):
		if self.__mostrar:
			if k > 0:
				print("         Coinciden, asi que k sube a", k, "y se anota", ROJO + str(k) + NORMAL)
			else:
				print("         No coinciden y k ya es 0, asi que se anota", ROJO + "0" + NORMAL)
			self.mostrar_tabla(patron, True)

	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def dibujar(self, patron, i, k, titulo, movimiento):
		segundos = 0
		if movimiento == 2:
			segundos = 11
		elif movimiento == 3:
			segundos = 9
		elif movimiento == 4:
			segundos = 5
		elif movimiento > 4:
			segundos = 3
		esperar(segundos)
		print(raya(titulo, movimiento))
		print("patron: ", pintar(patron, i, VERDE))
		print("copia:  ", "  " * (i - k) + pintar(patron, k, AZUL))
		print("        ", "  " * i + "^", VERDE + patron[i] + NORMAL, "vs", AZUL + patron[k] + NORMAL, "(k =", k, ")")
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def mostrar_tabla(self, patron, nuevo):
		texto = ""
		actual = self.__primero
		while actual != None:
			if nuevo and actual.next == None:
				texto = texto + ROJO + str(actual.dato) + NORMAL + " "
			else:
				texto = texto + str(actual.dato) + " "
			actual = actual.next
		faltan = len(patron) - self.__largo
		print("tabla:  ", texto + "_ " * faltan)
		print()
	#-------------------------------------fin funcion colorear pantalla ---------------------------------------------------
	#-------------------------------------fin funcion colorear pantalla ---------------------------------------------------
    #-------------------------------------fin funcion colorear pantalla ---------------------------------------------------
    #-------------------------------------fin funcion colorear pantalla ---------------------------------------------------
    #-------------------------------------fin funcion colorear pantalla ---------------------------------------------------
    #-------------------------------------fin funcion colorear pantalla ---------------------------------------------------
    #-------------------------------------fin funcion colorear pantalla ---------------------------------------------------
    #-------------------------------------fin funcion colorear pantalla ---------------------------------------------------





























class Buscador:
	def __init__(self, lista, texto):
		self.__lista = lista
		self.__texto = texto
		self.__primeros = []
		self.__ultimos = []
		self.__total = 0
		self.__grabar = True

	def ingenua(self, patron):
		self.reiniciar()
		m = len(patron)
		encontrados = 0
		comparaciones = 0
		inicio = self.__lista.head
		pos = 0
		while inicio != None:
			aux = inicio
			j = 0
			while j < m and aux != None:
				comparaciones = comparaciones + 1
				self.ver_ingenua(patron, pos, j, aux.dato == patron[j])
				if aux.dato != patron[j]:
					break
				j = j + 1
				aux = aux.next
			if j == m:
				encontrados = encontrados + 1
				self.encontrado(pos)
			inicio = inicio.next
			pos = pos + 1
		self.mostrar_movimientos()
		return encontrados, comparaciones

	def kmp(self, patron):
		self.reiniciar()
		m = len(patron)
		tabla = TablaPrefijos()
		tabla.construir(patron, False)
		encontrados = 0
		comparaciones = 0
		j = 0
		actual = self.__lista.head
		pos = 0
		while actual != None:
			while j > 0 and actual.dato != patron[j]:
				comparaciones = comparaciones + 1
				self.ver_kmp_devuelve(patron, pos, j, tabla)
				j = tabla.obtener(j - 1).dato
			comparaciones = comparaciones + 1
			self.ver_kmp(patron, pos, j, tabla, actual.dato == patron[j])
			if actual.dato == patron[j]:
				j = j + 1
			if j == m:
				encontrados = encontrados + 1
				self.encontrado(pos - m + 1)
				j = tabla.obtener(j - 1).dato
			actual = actual.next
			pos = pos + 1
		self.mostrar_movimientos()
		return encontrados, comparaciones

	def rabin_karp(self, patron):
		self.reiniciar()
		m = len(patron)
		base = 256
		primo = 101
		encontrados = 0
		comparaciones = 0

		# formula: h = base^(m - 1) % primo
		h = 1
		i = 0
		while i < m - 1:
			h = (h * base) % primo
			i = i + 1

		# formula: hash = (hash * base + letra) % primo
		hash_patron = 0
		hash_texto = 0
		entra = self.__lista.head
		i = 0
		while i < m:
			hash_patron = (hash_patron * base + ord(patron[i])) % primo
			hash_texto = (hash_texto * base + ord(entra.dato)) % primo
			entra = entra.next
			i = i + 1

		sale = self.__lista.head
		pos = 0
		while sale != None:
			self.ver_hash(patron, pos, hash_texto, hash_patron)
			if hash_patron == hash_texto:
				aux = sale
				j = 0
				while j < m:
					comparaciones = comparaciones + 1
					self.ver_rabin(patron, pos, j, aux.dato == patron[j])
					if aux.dato != patron[j]:
						break
					aux = aux.next
					j = j + 1
				if j == m:
					encontrados = encontrados + 1
					self.encontrado(pos)
			if entra == None:
				break
			# formula: hash_nuevo = (base * (hash_viejo - letra_que_sale * h) + letra_que_entra) % primo
			hash_texto = (base * (hash_texto - ord(sale.dato) * h) + ord(entra.dato)) % primo
			sale = sale.next
			entra = entra.next
			pos = pos + 1
		self.mostrar_movimientos()
		return encontrados, comparaciones



















#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def ver_ingenua(self, patron, pos, j, coinciden):
		if self.__grabar:
			dibujo = self.dibujar(patron, pos, pos + j, j)
			if coinciden:
				dibujo = dibujo + "         Coinciden, asi que paso a la siguiente letra (van " + ROJO + str(j + 1) + NORMAL + " iguales)\n"
			else:
				dibujo = dibujo + "         No coinciden, se corre el patron una posicion\n"
			self.guardar(dibujo)
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def ver_kmp_devuelve(self, patron, pos, j, tabla):
		if self.__grabar:
			dibujo = self.dibujar(patron, pos - j, pos, j)
			dibujo = dibujo + "         No coinciden y j es " + str(j) + ", asi que j se devuelve a tabla[" + str(j - 1) + "] = " + ROJO + str(tabla.obtener(j - 1).dato) + NORMAL + "\n"
			dibujo = dibujo + "tabla:   " + self.tabla_texto(tabla, j - 1) + "\n"
			self.guardar(dibujo)
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def ver_kmp(self, patron, pos, j, tabla, coinciden):
		if self.__grabar:
			dibujo = self.dibujar(patron, pos - j, pos, j)
			if coinciden:
				dibujo = dibujo + "         Coinciden, asi que j sube a " + ROJO + str(j + 1) + NORMAL + "\n"
			else:
				dibujo = dibujo + "         No coinciden y j ya es 0, se avanza a la siguiente letra\n"
			dibujo = dibujo + "tabla:   " + self.tabla_texto(tabla, -1) + "\n"
			self.guardar(dibujo)
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def ver_hash(self, patron, pos, hash_texto, hash_patron):
		if self.__grabar:
			dibujo = self.dibujar(patron, pos, pos, 0)
			dibujo = dibujo + "         hash ventana = " + ROJO + str(hash_texto) + NORMAL + "   hash patron = " + str(hash_patron) + "\n"
			if hash_patron == hash_texto:
				dibujo = dibujo + "         Los hash son iguales, asi que reviso letra por letra\n"
			else:
				dibujo = dibujo + "         Los hash son diferentes, se corre la ventana una posicion\n"
			self.guardar(dibujo)
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def ver_rabin(self, patron, pos, j, coinciden):
		if self.__grabar:
			dibujo = self.dibujar(patron, pos, pos + j, j)
			if coinciden:
				dibujo = dibujo + "         Coinciden (van " + ROJO + str(j + 1) + NORMAL + " iguales)\n"
			else:
				dibujo = dibujo + "         No coinciden, el hash era igual por casualidad\n"
			self.guardar(dibujo)
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def reiniciar(self):
		self.__primeros = []
		self.__ultimos = []
		self.__total = 0
		self.__grabar = True
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def guardar(self, dibujo):
		self.__total = self.__total + 1
		if len(self.__primeros) < 10:
			self.__primeros.append(dibujo)
		else:
			self.__ultimos.append(dibujo)
			if len(self.__ultimos) > 20:
				del self.__ultimos[0]
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def encontrado(self, posicion):
		if self.__grabar:
			mensaje = "\n         " + ROJO + "ENCONTRADO en la posicion " + str(posicion) + NORMAL + "\n"
			if len(self.__ultimos) > 0:
				self.__ultimos[len(self.__ultimos) - 1] = self.__ultimos[len(self.__ultimos) - 1] + mensaje
			else:
				self.__primeros[len(self.__primeros) - 1] = self.__primeros[len(self.__primeros) - 1] + mensaje
			self.__grabar = False
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def mostrar_movimientos(self):
		os.system("cls")
		pausa = 0
		mostrados = 0
		i = 0
		while i < len(self.__primeros):
			esperar(pausa)
			print(self.__primeros[i])
			mostrados = mostrados + 1
			pausa = self.siguiente_pausa(mostrados, pausa)
			i = i + 1
		if self.__total > 30:
			esperar(pausa)
			print()
			print("     . . .", self.__total - 30, "movimientos mas tarde . . .  (^_^)")
			esperar(5)
		i = 0
		while i < len(self.__ultimos):
			if i > 0 or self.__total <= 30:
				esperar(pausa)
			print(self.__ultimos[i])
			mostrados = mostrados + 1
			pausa = self.siguiente_pausa(mostrados, pausa)
			i = i + 1
		if self.__grabar:
			print("no se encontro el patron")
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def siguiente_pausa(self, mostrados, pausa):
		if mostrados == 1:
			return 11
		elif mostrados == 2:
			return 9
		elif mostrados == 3:
			return 5
		elif mostrados == 4:
			return 3
		else:
			return pausa * 0.82
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def dibujar(self, patron, inicio, i, j):
		desde = inicio - 5
		if desde < 0:
			desde = 0
		pedazo = self.__texto[desde:desde + len(patron) + 20]
		dibujo = raya("movimiento " + str(self.__total + 1), self.__total + 1) + "\n"
		dibujo = dibujo + "texto desde la posicion " + str(desde) + "\n"
		dibujo = dibujo + "texto:   " + pintar(pedazo, i - desde, VERDE) + "\n"
		dibujo = dibujo + "patron:  " + "  " * (inicio - desde) + pintar(patron, j, AZUL) + "\n"
		dibujo = dibujo + "         " + "  " * (i - desde) + "^ " + VERDE + self.__texto[i] + NORMAL + " vs " + AZUL + patron[j] + NORMAL + "\n"
		return dibujo
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	def tabla_texto(self, tabla, rojo):
		texto = ""
		actual = tabla.primero
		pos = 0
		while actual != None:
			if pos == rojo:
				texto = texto + ROJO + str(actual.dato) + NORMAL + " "
			else:
				texto = texto + str(actual.dato) + " "
			actual = actual.next
			pos = pos + 1
		return texto
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
os.system("")

ROJO = "\033[91m"
NORMAL = "\033[0m"
VERDE = "\033[92m"
AZUL = "\033[94m"
COLORES = ["\033[93m", "\033[95m", "\033[96m", "\033[97m", "\033[90m", "\033[33m", "\033[35m", "\033[36m"]
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
def raya(titulo, movimiento):
	color = COLORES[movimiento % len(COLORES)]
	return "\n------------------ " + titulo + " --------" + color + "----" + NORMAL + "------"
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
def esperar(segundos):
	if segundos <= 0:
		return
	if segundos >= 10:
		paso = 1
	else:
		paso = segundos / 10
	cantidad = round(segundos / paso)
	i = 0
	while i < cantidad:
		print(".", end=" ", flush=True)
		time.sleep(paso)
		i = i + 1
	print()
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
def pintar(cadena, pos, color):
	resultado = ""
	i = 0
	while i < len(cadena):
		if i == pos:
			resultado = resultado + color + cadena[i] + NORMAL + " "
		else:
			resultado = resultado + cadena[i] + " "
		i = i + 1
	return resultado
def elegir_patron(texto):
	os.system("cls")
	inicio = random.randint(0, len(texto) - 1300)
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	print(COLORES[1] + "fragmento aleatorio del ADN" + NORMAL)
	print()
	parrafo = 0
	while parrafo < 13:
		print(texto[inicio + parrafo * 100:inicio + parrafo * 100 + 100])
		print()
		parrafo = parrafo + 1
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	print(ROJO + "selecciona el patron con el mouse" + AZUL + " y presiona Enter" + NORMAL)
	antes = os.popen("powershell -command Get-Clipboard").read().strip()
	ahora = antes
	while ahora == antes:
		time.sleep(0.5)
		ahora = os.popen("powershell -command Get-Clipboard").read().strip()
	return ahora


lista = ListaADN()
lista.cargar("human.txt")
#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
letras = []
actual = lista.head
while actual != None:
	letras.append(actual.dato)
	actual = actual.next
texto = "".join(letras)
buscador = Buscador(lista, texto)

patron = elegir_patron(texto)
resultado_ingenua = ""
resultado_kmp = ""
resultado_rabin = ""

while True:
	os.system("cls")
	#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
	print(VERDE + "patron: " + patron + NORMAL)
	if resultado_ingenua != "":
		print(COLORES[0] + resultado_ingenua + NORMAL)
	if resultado_kmp != "":
		print(COLORES[1] + resultado_kmp + NORMAL)
	if resultado_rabin != "":
		print(COLORES[2] + resultado_rabin + NORMAL)
	print()
	print("======= BUSQUEDA DE PATRONES EN " + COLORES[0] + "A" + AZUL + "D" + ROJO + "N" + NORMAL + " =======")
    
    
    #-------------------------------------fin funcion solo para colorear pantalla ---------------------------------------------------
    #-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
    #-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
    #-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
    #-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
    #-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
    #-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
    #-------------------------------------fin funcion solo para colorear pantalla ---------------------------------------------------
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
	print("1. Ver tabla de prefijos")
	print("2. Busqueda ingenua")
	print("3. KMP")
	print("4. Rabin-Karp")
	print("5. Cambiar patron")
	opcion = input("opcion: ")

	if opcion == "1":
		tabla = TablaPrefijos()
		tabla.construir(patron, True)

	elif opcion == "2":
		encontrados, comparaciones = buscador.ingenua(patron)
		resultado_ingenua = "ingenua: " + str(encontrados) + " veces, " + str(comparaciones) + " comparaciones"
		#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
		print(COLORES[0] + resultado_ingenua + NORMAL)
	elif opcion == "3":
		encontrados, comparaciones = buscador.kmp(patron)
		resultado_kmp = "kmp: " + str(encontrados) + " veces, " + str(comparaciones) + " comparaciones"
		#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
		print(COLORES[1] + resultado_kmp + NORMAL)
	elif opcion == "4":
		encontrados, comparaciones = buscador.rabin_karp(patron)
		resultado_rabin = "rabin karp: " + str(encontrados) + " veces, " + str(comparaciones) + " comparaciones"
		#-------------------------------------funcion solo para colorear pantalla ---------------------------------------------------
		print(COLORES[2] + resultado_rabin + NORMAL)
	elif opcion == "5":
		patron = input("ingrese patron: ")
		resultado_ingenua = ""
		resultado_kmp = ""
		resultado_rabin = ""

	else:
		print("opcion no valida")

	if opcion != "5":
		input("presiona Enter para continuar")
