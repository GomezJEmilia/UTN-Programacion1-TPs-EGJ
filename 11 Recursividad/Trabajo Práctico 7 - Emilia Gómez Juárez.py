# Trabajo práctico N°4 - Programación I 
# RECURSIVIDAD
# Estudiante: Emilia Gómez Juárez

# Ejercicio 1: Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el
# número que indique el usuario.

def calcular_factorial (num):
    if num == 0:
        return 1
    else:
        return num * calcular_factorial (num - 1)

def factorial_enteros (num):
    if num == 1:
        print ("El factorial del número 1 es 1")
    else:
        print (f"El factorial del número {num} es {calcular_factorial (num)}")
        factorial_enteros (num - 1)

# Ejercicio 2: Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def posicion_fibonacci (posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return posicion_fibonacci(posicion - 1) + posicion_fibonacci(posicion -2)

def imprimir_fibonacci(posicion, actual=0):
    if actual > posicion:
        return
    print(posicion_fibonacci(actual), end=" ")
    imprimir_fibonacci(posicion, actual + 1)

# Ejercicio 3: Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la
# fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * calcular_potencia(base, exponente - 1) 

# Ejercicio 4: Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su 
# representación en binario como una cadena de texto.

def conversion_binario_decimal(decimal):
    # Caso base: si el número es 0 o 1, su binario es él mismo
    if decimal < 2:
        return str(decimal)
    else:
        return conversion_binario_decimal(decimal // 2) + str(decimal % 2)


# Ejercicio 5: Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios
# ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    length = len(palabra)
    if length == 0 or length == 1:
        return True
    elif palabra[0] != palabra[length-1]:
        return False
    else: 
        return es_palindromo(palabra[1:length-1])

# Ejercicio 6: Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y 
# devuelva la suma de todos sus dígitos.

def suma_digitos (n):
    if n < 10:
        return n
    
    ultimo_digito = n % 10
    resto = n // 10
    
    return ultimo_digito + suma_digitos(resto)

# Ejercicio 7:Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y
# devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques (n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n -1)

# Prueba ejercicio 7:
#print (contar_bloques(2))

# Ejercicio 8: Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo
# (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número

def contar_digito (numero, digito):
    ultimo_digito = numero % 10
    resto = numero // 10
    
    if numero == 0:
        return 1 if numero == digito else 0
    else:
        return (1 if ultimo_digito == digito else 0) + contar_digito(resto, digito)

# Prueba ejercicio 8:
#print (contar_digito(1234, 5))

def menu (ejercicio):
    match ejercicio:
        case 1:
            print("Mostraremos los factoriales desde el 1 hasta el número que ingreses")
            numero = int(input("Ingrese un número entero positivo:\n"))
            factorial_enteros(numero)
        case 2:
            n = int(input("¿Hasta qué posición de la serie de Fibonacci querés ver?:\n"))
            print("Serie de Fibonacci:")
            imprimir_fibonacci(n)
        case 3:
            print("Calculemos la potencia de un número")
            base = int(input("Ingresa la base de la potencia:\n"))
            exponente = int (input("Indica el exponente de la potencia:\n"))
            print(f"La potencia de {base} elevado a {exponente} es igual a {calcular_potencia(base, exponente)}")
        case 4: 
            decimal = int(input("Ingresa un número decimal para convertirlo en binario:\n"))
            print(f"El número {decimal} equivale al número {conversion_binario_decimal(decimal)} en binario")
        case 5: 
            palabra = input("Ingresa una palabra, veremos si es un palíndromo o no:\n")
            if es_palindromo(palabra):
                print (f"La función devuelve {es_palindromo(palabra)}, la palabra es un palíndromo")
            else:
                print (f"La función devuelve {es_palindromo(palabra)}, la palabra no es un palíndromo")
        case 6: 
            num = int(input("Ingresa un número entero positivo para sumar sus dígitos:\n"))
            print(f"La suma de los dígitos es {suma_digitos(num)}")
        case 7:
            print("Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos, y así sucesivamente hasta llegar al último nivel con un solo bloque.")
            bloques_nivel_bajo = int(input("Indica el número de bloques del nivel más bajo, para calcular cuántos bloques en total necesitaría para armar la pirámide: \n"))
            print(f"Para armar una pirámide con una base de {bloques_nivel_bajo} bloques, necesitarías un total de {contar_bloques(bloques_nivel_bajo)} bloques")
        case 8: 
            print("Vamos a contar cuántas veces aparece un dígito en un número entero!")
            entero = int(input("Indica cuál es el número entero positivo: \n"))
            digito = int(input("Indica cuál es el dígito que quieres contar:\n"))
            
            print(f"El dígito {digito} aparece {contar_digito(entero, digito)} veces en el número {entero}")
        case _ :
            print("El número elegido no corresponde a ningún ejercicio, prueba de nuevo")
print("Elije un ejercicio del 1 al 8 para probar")
ejercicio = int(input("Qué ejercicio deseas probar?\n"))
menu(ejercicio)