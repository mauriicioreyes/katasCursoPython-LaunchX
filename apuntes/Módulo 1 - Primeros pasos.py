# Programa Python 
# program.py
sum = 1 + 2
print(sum)

# Ejecutar un programa
python3 program.py

# Función print()
print('Hola desde la consola')
# Las funciones se invocan mediante paréntesis.

# Variables
sum = 1 + 2 # 3
product = sum * 2
print(product)

# Tipos de datos
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" # String

type(distancia_a_alfa_centauri)

# Declaramos la variable
distancia_a_alfa_centauri = 4.367
# Descubrimos su tipo de dato
type(distancia_a_alfa_centauri) # float

# OPERADORES
# <left side> <operator> <right side>
left_side = 10
right_side = 5
left_side / right_side # 2
# Python utiliza dos tipos de operadores: aritmética y asignación

# FECHAS
# Importar el módulo: date

# Importamos la biblioteca
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today()) 


# CONVERSIÓN DE TIPOS DE DATOS
print("Today's date is: " + str(date.today()))

# RECOPILAR INFORMACIÓN
# Entrada del usuario
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre: ")
print("Saludos: " + name)


# TRABAJAR CON NÚMEROS
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))