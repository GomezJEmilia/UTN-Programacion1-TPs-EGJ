# Trabajo práctico N°7 - Programación I 
# DATOS COMPLEJOS
# Estudiante: Emilia Gómez Juárez

# Ejercicio 1: dado el diccionario precios_frutas, añadir las siguientes frutas con sus respectivos precios: naranja = 1200, manzana = 1500,
# pera = 2300.
def agregar_productos_ej1 (diccionario_precios):
    diccionario_precios ['Naranja'] = 1200
    diccionario_precios ['Manzana'] = 1500
    diccionario_precios ['Pera'] = 2300
    
    return diccionario_precios


# Ejercicio 2: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# actualizar los precios de las siguientes frutas:
def modificar_precios_ej2 (diccionario):
    diccionario ['Banana'] = 1300
    diccionario ['Manzana'] = 1700
    diccionario ['Melón'] = 2800
    
    return diccionario


# Ejercicio 3:Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una 
# lista que contenga únicamente las frutas sin los precios.
def lista_frutas(diccicionario_frutas_precios):
    return  list(diccicionario_frutas_precios.keys())


# Ejercicio 4: Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
def guardar_contactos():
    diccionario_contactos = {}
    contador = 1
    
    while contador < 6:
        contacto = input ("Ingresa el nombre y el número de teléfono separado por un espacio\n")
        diccionario_contactos[contacto.split()[0]] = contacto.split()[1]
        contador += 1
    return diccionario_contactos

def buscar_contacto (diccionario, nombre):
    print(nombre in diccionario.keys())
    if nombre in diccionario.keys():
        return (f"Encontramos el contacto! El número de teléfono es el siguiente: {diccionario[nombre]}")
    else:
        return "No existe un contacto asociado a tal nombre"


# Ejercicio 5: Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra
def imprimir_palabras_unicas(set_palabras):    
    print ("Las palabras únicas de la frase son:")
    for palabra in set_palabras:
        print(palabra)

def diccionario_palabras_cantidad (set_palabras, lista_palabras):
    veces_por_palabras = {}
    for palabra in set_palabras:
        contador_palabras = 0
        for i in range ((len(lista_palabras))):
            if lista_palabras[i] == palabra:
                contador_palabras +=1
        veces_por_palabras [palabra] = contador_palabras

    return veces_por_palabras


# Ejercicio 6: Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio
# de cada alumno.
def registro_alumnos_notas():
    lista_alumnos = []

    for i in range(3): 
        nombre = input("Nombre del alumno: ")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
    
        notas = (nota1, nota2, nota3)
        lista_alumnos.append((nombre, notas))
    return lista_alumnos

def calculo_promedio(lista_alumnos):
    for alumno in lista_alumnos:
        nombre, notas = alumno
        print(nombre, notas)
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {nombre} es {promedio}")


# Ejercicio 8: Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
def consultar_stock(diccionario_stock, producto):
    print(f"El stock del producto {producto} es {diccionario_stock[producto]}")

def agregar_unidades(producto, cantidad, diccionario_stock):
    if producto in diccionario_stock:
        diccionario_stock[producto] +=  cantidad
        print (f"Stock actualizado. El producto {producto} ahora tiene {diccionario_stock[producto]} elementos en stock")
        return diccionario_stock
    else: print ("El producto ingresado no existe")

def agregar_producto (producto_nuevo, cantidad, diccionario_stock):
    if producto_nuevo in diccionario_stock:
        print (f"El producto {producto_nuevo} ya existe, hay {diccionario_stock[producto_nuevo]} unidades en stock")
    else:
        diccionario_stock[producto_nuevo] = cantidad
        print (f"Producto agregado. El producto {producto_nuevo} tiene {diccionario_stock[producto_nuevo]} elementos en stock")


# Ejercicio 9: Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Permití consultar
# qué actividad hay en cierto día y hora.
def consultar_evento(dia, hora):
    clave = (dia, hora)
    if clave in agenda:
        print(f"En {dia} a las {hora} tenés: {agenda[clave]}")
    else:
        print(f"No hay eventos programados para {dia} a las {hora}.")


# Ejercicio 10: Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario 
# donde: las capitales sean las claves y los países sean los valores.
def invertir_claves_valores(diccionario):
    diccionario_invertido = {}
    for clave in diccionario:
        diccionario_invertido[diccionario[clave]] = clave
    return diccionario_invertido

# Programa principal: pruebas de cada ejercicio
# Ejercicios 1, 2 y 3
print("__________ Ejercicios 1, 2 y 3 __________")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas_actualizado = modificar_precios_ej2 (agregar_productos_ej1(precios_frutas))

print(precios_frutas_actualizado)
print(lista_frutas(precios_frutas_actualizado))

# Ejercicio 4
print("\n__________ Ejercicio 4 __________")
print("A continuación, recibirá indicaciones para agendar 5 contactos con nombre y numero celular")
contactos = guardar_contactos()

nombre_a_buscar = input("Ingrese el nombre del contacto a buscar\n")
print (buscar_contacto(contactos, nombre_a_buscar))

# Ejercicio 5
print("\n__________ Ejercicio 5 __________")
frase = input("Ingresa una frase por favor\n")
lista_palabras = frase.split()
palabras_unicas = set(lista_palabras)

imprimir_palabras_unicas(palabras_unicas)
print (f"El diccionario con la cantidad de veces que aparece cada palabra es:\n{diccionario_palabras_cantidad(palabras_unicas, lista_palabras)}")

# Ejercicio 6
print("\n__________ Ejercicio 6 __________")
calculo_promedio(registro_alumnos_notas())

# Ejercicio  7: Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2. 
# Mostrá los alumnos que aprobaron los dos parciales
# Mostrá los alumnos que aprobaron al menos un parcial
# Mostrá la lista total de los alumnos que aprobaron un parcial sin repetir.
print("\n__________ Ejercicio 7 __________")
parcial1 = set(input("Ingrese las matrículas de los estudiantes aprobados del Parcial 1 separados por comas: ").split(","))
parcial2 = set(input("Ingrese las matrículas de los estudiantes aprobados del Parcial 2 separados por comas: ").split(","))

parcial1 = {x.strip() for x in parcial1}
parcial2 = {x.strip() for x in parcial2}

aprobados_ambos = parcial1.intersection(parcial2)
aprobados_solo_uno = parcial1.difference(parcial2).union(parcial2.difference(parcial1))
aprobados_al_menos_uno = parcial1.union(parcial2)

print("Aprobaron ambos parciales:", aprobados_ambos)
print("Aprobaron solo un parcial:", aprobados_solo_uno)
print("Aprobaron al menos un parcial:", aprobados_al_menos_uno)

# Ejercicio 8
print("\n__________ Ejercicio 8 __________")
stock_productos = {
    "Lápices de colores": 48,
    "Cuadernos A4": 32,
    "Cartulinas blancas": 15,
    "Plasticola grande": 20,
    "Tijeras escolares": 27
}
producto_buscado = input("Ingrese el producto del cuál desea consultar el stock:\n")
consultar_stock( stock_productos, producto_buscado)

producta_agregar_unidades = input("Ingrese el producto al cuál desea agregar unidades:\n")
unidades_agregar = input("Cuántas unidades desea agregar?\n")
agregar_unidades(producta_agregar_unidades,unidades_agregar, stock_productos)

nuevo_producto = input("Qué producto desea agregar al inventario?\n")
cantidad_nuevo_producto = input("Cuántas unidades del producto nuevo se agregan?\n")
agregar_producto(nuevo_producto, cantidad_nuevo_producto, stock_productos)
agregar_producto("Tijeras escolares", 5, stock_productos)

# Ejercicio 9
print("\n__________ Ejercicio 9 __________")
agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "14:30"): "Clase de yoga",
    ("Miércoles", "09:00"): "Turno médico",
    ("Jueves", "16:00"): "Estudio personal",
    ("Viernes", "18:00"): "Encuentro con amigas"
}

consultar_evento("Martes", "14:30")
consultar_evento("Lunes", "15:00")     

# Ejercicio 10
print("\n__________ Ejercicio 10 __________")
capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Perú": "Lima",
    "Colombia": "Bogotá",
    "México": "Ciudad de México",
    "España": "Madrid",
    "Italia": "Roma"
}

print(invertir_claves_valores(capitales))