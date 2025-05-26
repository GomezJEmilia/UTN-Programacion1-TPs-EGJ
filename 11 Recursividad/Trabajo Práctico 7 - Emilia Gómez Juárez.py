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

# Prueba ejercicio 1
#factorial_enteros(5)

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

# Pedir al usuario la posición máxima
#n = int(input("¿Hasta qué posición de la serie de Fibonacci querés ver?: "))

#print("Serie de Fibonacci:")
#imprimir_fibonacci(n)

# Ejercicio 3: Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la
# fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * calcular_potencia(base, exponente - 1) 

# print (calcular_potencia(2, 8))

# Ejercicio 4: Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su 
# representación en binario como una cadena de texto.

def conversion_binario_decimal(decimal):
    # Caso base: si el número es 0 o 1, su binario es él mismo
    if decimal < 2:
        return str(decimal)
    # Paso recursivo: dividimos entre 2 y vamos construyendo la cadena
    return conversion_binario_decimal(decimal // 2) + str(decimal % 2)

# Ejemplo de uso
#print(conversion_binario_decimal(57))

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

print (es_palindromo('aaaa'))