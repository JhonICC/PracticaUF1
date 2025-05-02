# Nuestros intentos
intentos = 0
max_intentos = 3

# Menu de opciones
print("****Calculadora****")
print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicacion")
print("4.- Division")
print("5.- Salir")


# Bucle para permitir hasta 3 intentos, si no se cierra el programa
while intentos < max_intentos:
    try:
        option = int(input("Elige qué deseas hacer: "))

        if option == 5:
            print("Hasta luego :))")
            break # Salimos del buble

        elif option >= 1 and option <= 4:
            num1 = int(input("Elige el primer número: "))
            num2 = int(input("Elige el segundo número: "))

            if option == 1:
                print("Resultado:", num1 + num2)
            elif option == 2:
                print("Resultado:", num1 - num2)
            elif option == 3:
                print("Resultado:", num1 * num2)
            elif option == 4:
                # Forma para que salga error al dividir entre 0
                if num2 == 0:
                    print("No se puede dividir entre cero")
                else:
                    print("Resultado:", num1 / num2)
            break # Salimos del buble

        else:
            print("Opción no válida. Intenta otra vez")
    
    # Error si no introducimos un numero
    except ValueError:
        print("Debes introducir un numero")

    # Aumentamos el contador de errores
    intentos += 1

# Si el usuario falla 3 veces, se cierra el programa con aviso
if intentos == max_intentos:
    print("Has superado el número de intentos. Cerrando programa.")


