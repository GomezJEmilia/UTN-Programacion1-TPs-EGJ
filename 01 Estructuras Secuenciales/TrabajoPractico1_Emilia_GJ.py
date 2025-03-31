# Trabajo práctico N°1 - Programación I
# Estudiante: Emilia Gómez Juárez

import math

def ejercicio1 ():
    print ("Hola mundo!")

# Prueba ejercicio 1
#ejercicio1()

def ejercicio2 ():
    # Se solicita el nombre
    nombreEj2 = input ("Ingresa tu nombre por favor: ")

    # Se imprime el saludo
    print (f"Hola {nombreEj2}")

# Prueba ejercicio 2
#ejercicio2()

def ejercicio3 (): 
    # Se solicita nombre, apellido, edad y lugar de residencia
    nombreEj3 = input ("Cuál es tu nombre? ")
    apellidoEj3 = input("Cuál es tu apellido? ")
    edadEj3 = input("Cuántos años tenés? ")
    paisResidenciaEj3 = input("Cuál es tu país de residencia? ")

    # Se imprime el mensaje
    print (f"Soy {nombreEj3} {apellidoEj3}, tengo {edadEj3} y vivo en {paisResidenciaEj3}")

# Prueba ejercicio 3
#ejercicio3()

def ejercicio4 ():
    # Se solicita radio del círculo
    radio = float(input ("Ingresa el radio del círculo: "))

    # Se imprimen el área y el perímetro
    print ("El área del círculo es: ", (2*radio*math.pi))
    print ("El área del círculo es: ", (radio**2)*math.pi)

# Prueba ejercicio 4
#ejercicio4()

def ejercicio5():
    # Se solicita al usuario la cantidad de segundos
    segs = int(input("Ingrese una cantidad de segundos: "))
    # Se realiza el cálculo para convertir segundos a horas
    horas = segs / 3600
    
    # Se imprime el equivalente en horas
    print(f"{segs} segundos son {horas} horas")
    

# Prueba ejercicio 5
#ejercicio5()

def ejercicio6():
    # Se solicita al usuario que ingrese el numero a multiplicar
    num = int(input("Ingrese un número y devolveremos la tabla de multiplicar: "))
    
    # Se inicializa una variable multiplicador
    x = 1
    
    # Se utiliza un bucle while para iterar multiplicando el número por el multiplicador
    while (x <= 10):
        print (num * x)
        x += 1

# Prueba ejercicio 6
#ejercicio6()

def ejercicio7():
    # Se solicitan ambos números
    num1 = int(input("Ingresa un número entero distinto que 0: "))
    num2 = int(input("Ingresa otro número entero distinto que 0: "))
    
    # Se imprimen los resultados de sumar, dividir, multiplicar y restar ambos números
    print(f"{num1} + {num2} = ", num1 + num2)
    print(f"{num1} - {num2} = ", num1 - num2)
    print(f"{num1} * {num2} = ", num1 * num2)
    print(f"{num1} / {num2} = ", num1 / num2)

# Prueba ejercicio 7
#ejercicio7()

def ejercicio8():
    # Se solicita peso y altura
    altura = float(input("¿Cuál es tu altura en metros? "))
    peso = float(input("¿Cuál es tu peso en kilogramos? "))
    
    # Se calcula el indice de masa corporal
    imc = peso / (altura ** 2)
    
    # Se imprime el resultado
    print(f"Tu indice de masa corporal es {imc}")

# Prueba ejercicio 8
#ejercicio8()

def ejercicio9():
    # Se solicita temperatura en celsius
    tempCelsius = int(input("Ingrese la temperatura en grados Celsius: "))
    
    # Se realiza la conversión a Fahrenheit
    tempFarenheit = int( (9/5) * tempCelsius + 32)
    
    # Se imprime temperatura en Fahrenheit
    print (f"La temperatura en Fahrenheit es de {tempFarenheit}°")

# Prueba ejercicio 9
#ejercicio9()

def ejercicio10():
    # Se solicitan los 3 números al usuario
    print ("Se solicitaran 3 números para calcular el promedio")
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))
    
    # Se calcula e imprime el promedio
    
    print("El promedio de los tres números es: ", (num1 + num2 + num3)/3 )

# Prueba ejercicio 10
#ejercicio10()