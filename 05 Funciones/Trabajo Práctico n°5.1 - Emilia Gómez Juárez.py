# Trabajo práctico N°5 - Programación I 
# LISTAS EN PYTHON
# Estudiante: Emilia Gómez Juárez

# Ejercicio 1: Crear una lista con los números del 1 al 100 que sean múltiplos de 4. 
# Utilizar la función range.

def ejercicio1 ():
    lista = list(range(0, 101, 4))
    return lista

# Prueba ejercicio 1
print(ejercicio1())

# Ejercicio 2: Crear una lista con cinco elementos (colocar los elementos que
# más te gusten) y mostrar el penúltimo.

def ejercicio2 ():
    lista_cinco_elementos = [1, "lista", "con", 5, "elementos"]
    print (f"El penúltimo elemento de la lista es el siguiente: {lista_cinco_elementos[3]}")

# Pruena ejercicio 2
ejercicio2 ()

# Ejercicio 3: Crear una lista vacía, agregar tres palabras con append e 
# imprimir la lista resultante por pantalla

def ejercicio3 ():
    lista_vacia = []
    lista_vacia.append("primero")
    lista_vacia.append("segundo")
    lista_vacia.append("tercero")
    
    print (f"La lista se llenó con tres elementos y se ve así: {lista_vacia}")

# Prueba ejercicio 3
ejercicio3()

# Ejercicio 4: Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” 
# y “oso”, respectivamente. Imprimir la lista resultante por pantalla

def ejercicio4 ():
    animales = ["perro", "gato", "conejo", "pez"]
    
    animales[1] = "loro"
    animales[-2] = "oso"
    
    print (f"La lista con los nuevos elementos es: {animales}")

# Prueba ejercicio 4
ejercicio4()

# Ejercicio 5: Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

# RESPUESTA EJERCICIO 5: El programa utiliza la función max() para comprobar cuál es el número 
# más grande de la lista, y con la función remove() lo elimina de la lista.


# Ejercicio 6: Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
def ejercicio6 ():
    lista_diez_al_treinta = list(range(10, 31, 5))
    print(f"Los primeros dos numeros de la lista son el {lista_diez_al_treinta[0]} y el {lista_diez_al_treinta[1]}")

# Prueba ejercicio 6
ejercicio6()

# Ejercicio 7: Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos 
# nuevos valores cualesquiera 

def ejercicio7 ():
    autos = ["sedan", "polo", "suran", "gol"]
    autos [1] = "logan"
    autos[2] = "up!"
    
    print (f"La lista modificada es: {autos}")

# Prueba ejercicio 7
ejercicio7 ()

# Ejercicio 8: Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15
# usando append directamente. Imprimir la lista resultante por pantalla.

def ejercicio8 ():
    lista_dobles = []
    lista_dobles.append(2*5)
    lista_dobles.append(2*10)
    lista_dobles.append(2*15)
    
    print(lista_dobles)

# Prueba ejercicio 8
ejercicio8()

# Ejercicio 9: Dada la lista “compras”, cuyos elementos representan los productos comprados 
# por diferentes clientes: 
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

def ejercicio9 ():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras[0].remove("pan")
    
    print(compras)

# Prueba ejercicio 9
ejercicio9()

# Ejercicio 10: Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

def ejercicio10 ():
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    print (f"La lista anidada se ve así: {lista_anidada}")

# Prueba ejercicio 10:
ejercicio10()

