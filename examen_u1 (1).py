# -*- coding: utf-8 -*-
"""Examen U1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cgg8kzd0UATdzmTRKKbDszP26N_mWXkG
"""

#Ejercicio 1
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    try:
        num = int(input("Ingresa un número entero: "))
        if es_primo(num):
            print(f"{num} es un número primo.")
        else:
            print(f"{num} no es un número primo.")
    except ValueError:
        print("Error: Ingresa un valor entero válido.")

if __name__ == "__main__":
    main()

#Ejercicio 2
def sig_primo(n):
    can = n +1
    while not primo(can):
        can+= 1
    return can

 #El próximo número primo mayor que n
def nextPrime(n):
    if n <= 1:
        return 2
    numero = n + 1
    while True:
        if sig_primo(numero):
            return numero
        numero += 1

def main():
    try:
        n = int(input("Ingrese un número entero: "))
        if n < 0:
            print("Por favor, ingrese un número entero positivo.")
        else:
            siguiente_primo = nextPrime(n)
            print(f"El primer número primo mayor que {n} es {siguiente_primo}.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

if __name__ == "__main__":
    main()

#Ejercicio 3
def mediana(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros[1]

def main():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        num3 = float(input("Ingresa el tercer número: "))

        medianaa = mediana(num1, num2, num3)

        print(f"La mediana de los números es: {medianaa}")
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()

#Ejercicio 4
import random

def contra():
  contrasena = ""
  for i in range(1,random.randrange(7,10)):
    contrasena += chr(random.randrange(33,126,1))
  return contrasena

#Ejercicio 5
import math

def hipotenusa (lado1, lado2):
    return math.sqrt(lado1**2 + lado2**2)

def main():
    try:
        lado1 = float(input("Ingresa la longitud del primer lado más corto: "))
        lado2 = float(input("Ingresa la longitud del segundo lado más corto: "))

        if lado1 <= 0 or lado2 <= 0:
            print("Error: Ingresa longitudes válidas mayores que cero.")
        else:
            hipo = hipotenusa(lado1, lado2)
            print(f"La longitud de la hipotenusa es: {hipo}")
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()