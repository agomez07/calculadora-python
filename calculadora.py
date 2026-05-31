def sumar(num1, num2):
    return num1 + num2
    
def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2  

def promedio(notas):
    return sum(notas) / len(notas)

def calcular_promedio():
    lista_notas = []
    while True:
        try:
            nota = float(input("Ingresa una nota // Ingresa (-1) para finalizar: "))

            if nota == -1:
                break
            lista_notas.append(nota)

        except ValueError:
            print("Entrada inválida, ingresa un valor numérico.")

    if not lista_notas:
        print("No se han ingresado notas.")
            
    else:
        resultado = promedio(lista_notas)
        print(f"Promedio: {resultado:.2f}")

def menu():
    print("--------------------------------------")
    print("         Calculadora AG ")
    print("--------------------------------------")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACIÓN")
    print("4. DIVISIÓN")
    print("5. PROMEDIO")
    print("6. SALIR")

def main():
    while True:
        menu()

        try:
            opcion = int(input("Selecciona la operación que deseas realizar: "))

        except ValueError:
            print("Error: Por favor, ingresa un número válido.")
            continue

        if 1 <= opcion <= 4:

            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

            except ValueError:
                print("Entrada inválida, ingresa un valor numérico.")
                continue

            if opcion == 1:
                print("\n ----SUMA----")
                resultado = sumar(num1, num2)
                print(f"Resultado: {resultado}")
    
            elif opcion == 2:
                print("\n ----RESTA----")
                resultado = restar(num1, num2)
                print(f"Resultado: {resultado}")

            elif opcion == 3:
                print("\n ----MULTIPLICACIÓN----")
                resultado = multiplicar(num1, num2)
                print(f"Resultado: {resultado}")

            elif opcion == 4:
                print("\n ----DIVISIÓN----")
                try:
                    resultado = dividir(num1, num2)
                    print(f"Resultado: {resultado:.2f}")

                except ZeroDivisionError:
                    print("Error: División por cero no permitida.")

               

        elif opcion == 5:
            print("----------\n PROMEDIO\n----------")
            calcular_promedio()

        elif opcion == 6:
            print("Cerrando la calculadora...")
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()