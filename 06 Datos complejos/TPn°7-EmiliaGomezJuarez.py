# Trabajo práctico N°7 - Programación I 
# DATOS COMPLEJOS
# Estudiante: Emilia Gómez Juárez

# Ejercicio 1: dado el diccionario precios_frutas, añadir las siguientes frutas con sus respectivos precios: naranja = 1200, manzana = 1500,
# pera = 2300.
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

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

#print (modificar_precios_ej2 (agregar_productos_ej1(precios_frutas)))

# Ejercicio 3:Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una 
# lista que contenga únicamente las frutas sin los precios.

def lista_frutas(diccicionario_frutas_precios):
    return  list(diccicionario_frutas_precios.keys())

#print(lista_frutas(precios_frutas))

# Ejercicio 4: Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

def guardar_contactos():
    diccionario_contactos = {}
    contador = 1
    
    while contador < 3:
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

#print("A continuación, recibirá indicaciones para agendar 5 contactos con nombre y numero celular")
#contactos = guardar_contactos()

#nombre_a_buscar = input("Ingrese el nombre del contacto a buscar\n")
#print (buscar_contacto(contactos, nombre_a_buscar))

# Ejercicio 5: Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra

frase = input("Ingresa una frase por favor\n")
palabras_unicas = set(frase.split())
lista_palabras = frase.split()

def imprimir_palabras_unicas(set_palabras):    
    print ("Las palabras únicas de la frase son:")
    for palabra in set_palabras:
        print(palabra)

contador_palabras = 0
def diccionario_palabras_cantidad (set_palabras, lista_palabras):
    veces_por_palabras = {}
    for palabra in set_palabras:
        contador_palabras = 0
        for i in range ((len(lista_palabras))):
            if lista_palabras[i] == palabra:
                contador_palabras +=1
        veces_por_palabras [palabra] = contador_palabras

    return veces_por_palabras

#imprimir_palabras_unicas(set_palabras)
#print (f"El diccionario creado es el siguiente:\n{diccionario_palabras_cantidad(set_palabras, lista_palabras)}")

# Ejercicio 6: Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio
# de cada alumno.

