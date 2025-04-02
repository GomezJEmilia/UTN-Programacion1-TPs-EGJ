# # Trabajo práctico N°3 - Programación I
# Estudiante: Emilia Gómez Juárez

# Ejercicio 1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
def ejercicio1 ():
    # Se solicita al usuario que ingrese su edad
    edad = int(input("Ingrese su edad: "))
    
    # Se verifica si es mayor de edad o no
    if edad > 18:
        print ("Es mayor de edad")
        
# Prueba ejercicio 1
# ejercicio1()

#Ejercicio 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
def ejercicio2 ():
    # Se solicita al usuario que ingrese la nota
    nota = float(input("Ingrese su nota: "))
    
    # Se verifica si esta aprobado o no
    if nota >= 6:
        print ("Aprobado")
    else:
        print("Desaprobado") 

# Prueba ejercicio 2
# ejercicio2()

# Ejercicio 3: Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
def ejercicio3 ():
    # Se solicita al usuario que ingrese un número
    numero = int(input("Ingrese un número par: "))
    
    # Se verifica si el número es par o impar
    if numero % 2 == 0:
        print ("Ha ingresado un número par")
    else:
        print ("Por favor, ingrese un número par")

# Prueba ejercicio 3
#ejercicio3()

# Ejercicio 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: niño/a, adolescente, adulto/a joven, adulto/a
def ejercicio4 ():
    # Se solicita al usuario que ingrese su edad
    edad = int(input("Por favor, ingrese su edad: "))
    
    # Se verifica la categoría a la que pertenece y se imprime el mensaje correspondiente
    if edad < 0:
        pass
    elif edad == 0:
        print ("Eres un/a bebé")
    elif edad < 12:
        print ("Eres un/a niño/a")
    elif edad >= 12 and edad < 18:
        print ("Eres un/a adolescente")
    elif edad >= 18 and edad <= 30:
        print ("Eres un/a adulto/a joven")
    else: print ("Eres un/a adulto/a")

# Prueba ejercicio 4
#ejercicio4 ()

# Ejercicio 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"
def ejercicio5():
    # Se solicita al usuario la contraseña
    contrasenia = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
    
    # Se verifica si la contraseña tiene el largo adecuado
    if len(contrasenia) >= 8 and len(contrasenia) <= 14:
        print ("Ha ingresado una contraseña correcta")
    else: print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Prueba ejercicio 5
#ejercicio5()

# Ejercicio 6: escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Se importan las funciones mode, mean y median del paquete statistic
from statistics import mode, median, mean
import random

def ejercicio6 ():
    # Se crea una lista con 50 números aleatorios entre 1 y 500
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    
    # Se predice el sesgo
    if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
        print ("El sesgo es positivo o a la derecha")
    elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
        print ("El sesgo es negativo o a la izquierda")
    else: print ("No hay sesgo")

# Prueba ejercicio 6
#ejercicio6()

# Ejercicio 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla
def ejercicio7 ():
    # Se solicita al usuario que ingrese una frase o palabra
    frase = input("Por favor, ingrese una palabra o frase: ")
    
    # Se verifica si el string termina con vocal o no
    if frase [len(frase) - 1] == "a" or frase [len(frase) - 1] == "A" or frase [len(frase) - 1] == "e" or frase [len(frase) - 1] == "E" or frase [len(frase) - 1] == "i" or frase [len(frase) - 1] == "I" or frase [len(frase) - 1] == "o" or frase [len(frase) - 1] == "O" or frase [len(frase) - 1] == "u" or frase [len(frase) - 1] == "U":
        print (f"{frase}!")
    else: print (frase)

# Prueba ejercicio 7
#ejercicio7()

# Ejercicio 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: mayúsculas, minúsculas, solo la primera letra en mayúsculas
def ejercicio8 ():
    # Se solicita el nombre al usuario
    nombre = input ("Por favor, ingrese su nombre: ")
    
    # Se solicita que elija una opción al usuario
    opcion = int(input("Elija una opción introduciendo el número que corresponda\n 1: Nombre en mayúsculas\n 2: Nombre en minúsculas\n 3: Solo primera letra en mayúscula\n Opción: "))
    
    # Se modifica el string según la opción elegida por el usuario
    if opcion == 1:
        print (nombre.upper())
    elif opcion == 2:
        print (nombre.lower())
    elif opcion == 3:
        print (nombre.title())
    else: print ("Ingrese una de las opciones (1,2 o 3)")

# Prueba ejercicio 8
#ejercicio8()