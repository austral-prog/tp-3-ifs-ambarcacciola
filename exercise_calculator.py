def calculator():
    num1 = float(input())
    num2 = float(input())
    operacion = input()

    if operacion not in ['+', '-', '*', '/']:
        print("Operacion invalida")
    elif operacion == '/':
        if num2 == 0:
            print("Error: division por cero")
        else:
            print(f"Resultado: {num1 / num2}")
    elif operacion == '+':
        print(f"Resultado: {num1 + num2}")
    elif operacion == '-':
        print(f"Resultado: {num1 - num2}")
    elif operacion == '*':
        print(f"Resultado: {num1 * num2}")
