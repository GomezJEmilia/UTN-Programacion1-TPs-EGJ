# Trabajo práctico N°4 - Programación I 
# FUNCIONES EN PYTHON
# Estudiante: Emilia Gómez Juárez

# Ejercicio 1: Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

import math

def imprimir_hola_mundo ():
    print ("Hola Mundo!")

# Ejercicio 2: Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y
#  devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario (nombre):
    return (f"Hola {nombre}!")

# Ejercicio 3: Crear una función llamada informacion_personal(nombre, apellido, edad, residencia)
# que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y 
# vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal (nombre, apellido, edad, residencia):
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y 
# devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro 
# y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para 
# mostrar los resultados

def calcular_area_circulo (radio):
    return (math.pi * (radio ** 2))

def calcular_perimetro_circulo (radio):
    return (2 * math.pi * radio)

# Ejercicio 5: Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos
# como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y
# mostrar el resultado usando esta función.

def segundos_a_horas (segundos):
    if segundos > 0:
        return segundos / 3600
    else: print ("El número ingresado debe ser mayor a 0")

# Ejercicio 6: Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro
# y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a 
# la función.

def tabla_multiplicar (numero):
    for i in range (1, 11):
        print (f"{numero} * {i} = {(numero * i)}")

# Ejercicio 7: Crear una función llamada operaciones_basicas(a, b) que reciba dos números como 
# parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
# Mostrar los resultados de forma clara.

def operaciones_basicas (a,b):
    if a > b:
        resultados = ((a+b), (a-b), (a*b), (a/b))
    else: resultados = ((b+a), (b-a), (b*a), (b/a))
    return resultados

# Ejercicio 8: Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y
# la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y 
# llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc (peso, altura):
    return peso / (altura ** 2)

# Ejercicio 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en
# grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y
# mostrar el resultado usando la función.

def celcius_a_fahrenheit (celcius):
    return int( (9/5) * tempCelsius + 32)

# Ejercicio 10: Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como
# parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado
# usando esta función.

def calcular_promedio (a, b, c):
    return  (a + b + c)/3

# PROGRAMA PRINCIPAL

# Ejercicio 1
imprimir_hola_mundo()
print ("")

# Ejercicio 2
nombre = input("Cuál es tu nombre? \n")
print (saludar_usuario(nombre))

# Ejercicio 3
apellido = input ("Cuál es tu apellido?\n")
edad = input ("Cuántos años tenés? \n")
residencia = input ("En dónde vivís?\n")

informacion_personal (nombre, apellido, edad, residencia)

# Ejercicio 4
radio = float (input ("Ingrese el radio en cm para calcular área y perímetro del círculo: \n"))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print (f"El área del círculo es: {area}cm. \nEl perímetro del círculo es: {perimetro}cm.")

# Ejercicio 5
segs = float(input("Ingrese cantidad de segundos para convertirlos a hora: \n"))
print (f"{segs} segundos son {segundos_a_horas(segs)} horas")

# Ejercicio 6
factor = int(input("Indique el número a multiplicar: \n"))
tabla_multiplicar(factor)

# Ejercicio 7
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

print (f"Los resultados de las operaciones básicas son: \nSuma = {operaciones_basicas(num1, num2)[0]} \nResta= {operaciones_basicas(num1, num2)[1]} \nMultiplicacion = {operaciones_basicas(num1, num2)[2]} \nDivision = {operaciones_basicas(num1, num2)[3]}")

# Ejercicio 8
print ("Calculemos tu índice de masa corporal (IMC)")
peso = float (input ("Cuál es tu peso actual? \n"))
altura = float (input ("Cuál es tu altura? \n"))

print (f"Tu IMC es: {calcular_imc (peso, altura)}")

# Ejercicio 9
tempCelsius = int(input("Ingrese la temperatura en grados Celsius: "))
print (f"{tempCelsius}°C son {celcius_a_fahrenheit(tempCelsius)}°F")

# Ejercicio 10
print ("Se solicitaran 3 números para calcular el promedio")
nota1 = int(input("Ingresa el primer número: "))
nota2 = int(input("Ingresa el segundo número: "))
nota3 = int(input("Ingresa el tercer número: "))

print (f"El promedio es: {calcular_promedio(nota1, nota2, nota3)}")
