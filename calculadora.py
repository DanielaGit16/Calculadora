# calculadora.py
# Script básico para operaciones matemáticas
numero_1 = float(input("Primer número: "))
numero_2 = float(input("Segundo número: "))
numero_3 = float(input("Tercer número: "))
operacion = input("Operación (+, -, *, /): ")

if operacion == '+':
    print("Resultado:", numero_1 + numero_2 + numero_3)
elif operacion == '-':
    print("Resultado:", numero_1 - numero_2 - numero_3)
elif operacion == '*':
    print("Resultado:", numero_1 * numero_2 * numero_3)
elif operacion == '/':
    if numero_3 != 0:
        print("Resultado:", numero_1 / numero_2 / numero_3)
    else:
        print("Error: no se puede dividir por cero.")
        
else:
    print("Operación no válida.")