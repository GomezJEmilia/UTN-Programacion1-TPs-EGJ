# Trabajo práctico N°4 - Programación I 
# ESTRUCTURAS REPETITIVAS
# Estudiante: Emilia Gómez Juárez

# Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

def ejercicio1 ():
    # Se crea un bucle cuyo valor de salida es el 101
    for i in range (101):
        # Se imprime en cada iteración la variable contador
        print (i)

# Prueba ejercicio 1
# ejercicio1 ()

# Ejercicio 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad 
# de dígitos que contiene.
def ejercicio2 ():
    # Se solicita el número al usuario
    numero = input ("Ingrese un número: ")
    
    # Se determina la cantidad de dígitos utilizando la función len() 
    print (f"El número tiene {len(numero)} dígitos")

# Prueba ejercicio 2
#ejercicio2 ()

# Ejercicio 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

def ejercicio3 ():
    # Se solicita al usuario que ingrese los valores del rango
    numero1 = int(input ("Ingrese el primer valor del rango: "))
    numero2 = int (input("Ingrese el segundo valor del rango: "))
    
    # Se define una variable acumulador
    suma = 0
    
    # Se verifica cuál es el número menor y el mayor
    if numero1 < numero2:
        # Se utiliza un bucle while para sumar los valores dentro del rango
        while numero1 < (numero2 - 1):
            # Se incrementa en 1 el valor de numero1 (valor mínimo del rango) para que no se cree un bucle infinito
            numero1 += 1;
            
            # Se suma el valor de numero1 al resultado total
            suma += numero1
    else:
        # Se utiliza un bucle while para sumar los valores dentro del rango
        while numero2 < (numero1 - 1):
            # Se incrementa en 1 el valor de numero1 (valor mínimo del rango) para que no se cree un bucle infinito
            numero2 += 1;
            
            # Se suma el valor de numero1 al resultado total
            suma += numero2
    
    # Se imprime el resultado de la suma
    print (f"El resultado de sumar los números dentro del rango indicado es igual a {suma}")

# Prueba ejercicio 3
#ejercicio3()

# Ejercicio 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
def ejercicio4 ():
    # Se explica al usuario la función del programa
    print("Hola! Te solicitaremos que ingreses números enteros y los sumaremos. La suma se dentendra cuando ingreses el número 0 (cero)")
    
    # Se define una variable acumulador y una variable de tipo int
    numero = int(input("Ingrese el primer número entero: \n"))
    suma = 0
    # Se inicia un bucle while donde se repite la acción de que el usuario ingrese números enteros que se suman.
    while numero != 0:
        # Se suma el valor del numero ingresado a la suma total
        suma +=numero
        
        # Se solicita al usuario que siga ingresando numeros
        numero = int(input ("Ingrese otro número. Si desea frenar ingrese 0: \n"))
    
    # Se imprime el total de la suma
    print (f"El total de la suma de los números ingresados es: {suma}")

# Prueba ejercicio 4
#ejercicio4()

# Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# Se importa la librería random para generar el número a adivinar
import random

def ejercicio5 ():
    # Se define el número a adivinar utilizando la función randint()
    num_random = random.randint(0,9)
    
    # Se explica al usuario el juego
    print("En este juego debes adivinar un número aleatorio entre 0 y 9")
    
    # Se define la variable para la adivinanza del usuario y una variable contador de intentos
    adivinanza = int(input("Adivina el número! Ingresa un número del 0 al 9 \n"))
    intentos = 1;
    
    # Se inicia un bucle while para repetir hasta que el usuario adivine el número
    while (adivinanza != num_random):
        adivinanza = int(input("Ese número no era, vuelve a intentar! \n"))
        intentos += 1
    
    print (f"Adivinaste! El número es el {num_random}. Lo lograste en {intentos} intentos")

# Prueba ejercicio 5
# ejercicio5()

# Ejercicio 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente

def ejercicio6 ():
    # Se inicia un bucle for con el valor de inicio en 100, el valor final en -1 y el valor de actualización como -2.
    for i in range (100, -1,-2):
        print (i);

# Prueba ejercicio 6
#ejercicio6()

# Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
def ejercicio7 ():
    # Se solicita al usuario que ingrese un número entero positivo
    numero_limite = int (input ("Ingrese un numero entero positivo por favor: "))
    
    # Se crea una variable acumulador:
    suma = 0
    
    # Se crea un bucle for para sumar los números desde 0 hasta el número ingresado por el usuario
    for i in range (numero_limite + 1):
        suma += i
    
    print (f"El total de la suma de los números entre 0 y {numero_limite} es igual a {suma}")

# Prueba ejercicio 7
#ejercicio7()

# Ejercicio 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos.
def ejercicio8 ():
    # Se crean variables contadores para números pares, impares, negativos y positivos
    positivos = 0
    negativos = 0
    pares = 0
    impares = 0
    
    # Se explica al usuario la funcionalidad del programa
    print ("Te pediremos que ingreses 100 números enteros para clasificarlos en pares, impares, positivos y negativos")
    
    # Se crea un bucle for donde se solicita al usuario que ingrese un número y se actualizan los contadores
    for i in range (100):
        numero = int(input (f"Ingresa el número {i + 1}: "))
        
        # Verificación par o impar
        if (numero % 2 == 0):
            pares +=1
        else: impares +=1
        
        # Verificación positivo o negativo
        if (numero < 0):
            negativos +=1
        else: positivos +=1
    
    # Se imprime la cantidad de números según clasificación
    print(f"Se ingresaron: \n{positivos} números positivos \n{negativos} números negativos \n{pares} números pares \n{impares} números impares")

# Prueba ejercicio 8
#ejercicio8()

# Ejercicio 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
def ejercicio9 ():
    # Se crea una variable acumulador
    acumulador = 0
    
    # Se imprime la función del programa
    print ("Ingrese 100 números enteros y el programa calculará el promedio")
    
    # Se inicia un bucle for para sumar los números ingresados por el usuario
    for i in range (100):
        numero = int(input (f"Ingresa el número {i + 1}: "))
        acumulador += numero
    
    # Se calcula e imprime la medio de los valores ingresados
    print (f"La media de los valores ingresados es {acumulador/(i + 1)}")

# Prueba ejercicio 9
#ejercicio9()

# Ejercicio 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
def ejercicio10 ():
    # Se solicita al usuario que ingrese un número
    numero = input("Ingrese un número, invertiremos el orden de los dígitos: \n")
    
    #num_invertido = numero[:: -1] --> Opción encontrada investigando, sin utilizar estructura repetitiva
    #print (num_invertido)
    
    # Se define una variable donde guardar el número con dígitos invertidos
    num_invertido = ""
    
    # Se utiliza un bucle for para recorrer el string de atrás hacia adelante.
    for i in range ((len(numero) - 1), -1, -1):
        num_invertido = num_invertido + numero [i]
    
    print (f"El número {numero} con sus dígitos invertidos es: {num_invertido}")

# Prueba ejercicio 10
#ejercicio10 ()
