# Esto es un ejercicio 2


# Script para mostrar los primeros 10 números pares

contador = 0      # Cuenta cuántos números pares se han encontrado
numero = 1        # Número inicial para evaluar

while contador < 10:
    if numero % 2 == 0:  # Validar si el número es par
        print(numero)
        contador += 1    # Aumentar el contador solo si el número es par
    numero += 1          # Ir al siguiente número

        ## contraseña = input("ingrese contraseña: ")
        ## contraseña_establecida = "1234"
        ## while not(contraseña == contraseña_establecida):
            ##print("ingresaste correctamente")

        