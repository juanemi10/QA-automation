num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
operacion = input("Introduce la operacion (+, -, *, /): ")

if operacion == '+' :
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    resultado = num1 / num2
else:
    resultado = "Operacion invalida"
print(f"El resultado es: {resultado}")