#Ejemplos de estructuras de control en Python

import math #math es para operaciones matemáticas
import random #genera números aleatorios

# 1. Asignación y comparación
print("Diferencias entre asignación y comparación")
numero = 27
texto = "Python"

#Comparaciones
print(f"¿{numero} es mayor que 20? {numero > 20}")
print(f"¿{texto} es igual a 'Python'? {texto == 'Python'}")
print(f"¿{numero} es diferente de 8? {numero != 8}")

# 2. If, if else, else
print(f"")
print("Estructura de la condicional if")
edad = 18
if(edad >= 18):
    print(f"Tienes {edad} años, eres mayor de edad")

print(f"")
print("Estructura de la condicional if-else")
calificacion = 5.5
if(calificacion >= 6.0):
    print(f"Calificación: {calificacion} - Aprobado")
else:
    print(f"Calificación: {calificacion} - Reprobado")

print(f"")
print("Estructura de la condicional if-else-if")
nota = 85
if nota >= 90:
    print(f"Nota: {nota} - Excelente")
elif nota >= 80:
    print(f"Nota: {nota} - Muy bien")
elif nota >= 70:
    print(f"Nota: {nota} - Bien")
elif nota >= 60:
    print(f"Nota: {nota} - Suficiente")
else:
    print(f"Nota: {nota} - Necesitas mejorar")

#while
print(f"")
print(f"Estructura de control: while")
contador = 1
while contador <= 5:
    print(f"Número: {contador}")
    contador += 1 #incremento

#for
print(f"")
print("Estructura de control: for")
for i in range(5):
    print(f"Iteración: {i}")

#Otra forma de salto de línea
print(f"\nFor con range(inicio, fin, incremento):")
for i in range(2,10,2):
    print(f"Numero par: {i}")

print(f"\nNúmeros pares con módulo")
for i in range(14):
    if(i % 2 == 0):
        print(f"{i} es par")

#Uso de math
print(f"\nUso de math")
num = 16
raiz = math.sqrt(num)
print(f"Raíz cuadrada de {num} es: {raiz}")

print(f"\nValor de Pi")
print(f"Valor de pi: {math.pi:.4f}")