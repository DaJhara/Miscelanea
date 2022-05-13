import math
opcion = 0
ejercicio = 0
while opcion != 99:
    opcion = int(input ("1. Operadores\n2. Condicionales\n3. Ciclos\n99. Salir\n"))
    if opcion == 1:
        ejercicio = int(input("""\n1. Área de un triángulo.\n2. Suma de dos números.
3. Cuadrado de un número.\n4. Euros a dólares.
5. Área y perímetro de un cuadrado.\n6. Área y el volúmen de un cilindro.
7. Longitud y área del círculo.\n8. Promedio de tres números.\n"""))
        if ejercicio == 1:
            base = input("Ingrese la base del triángulo: ")
            altura = input("Ingrese la altura del triángulo: ")
            area = int (base) * int (altura) / 2
            print(f"El área del triángulo es {area}\n")
        elif ejercicio == 2:
            numUno = input("Ingrese el primer número: ")
            numDos = input("Ingrese el segundo número: ")
            suma = int(numUno) + int(numDos)
            print(f"{numUno} + {numDos} = {suma}\n")
        elif ejercicio == 3:
            numero = input("Ingrese un número: ")
            cuadrado = pow(int(numero), 2)
            print(f"El cuadrado de {numero} es {cuadrado}\n")
        elif ejercicio == 4:
            euros = input("Ingrese la cantidad de Euros: ")
            dolares = float(euros)*1.04
            print(f"{euros} Euros son {dolares} dólares\n")
        elif ejercicio == 5:
            ladoCuadrado = int(input("Ingrese el lado del cuadrado: "))
            perimetro = ladoCuadrado*4
            area = pow(ladoCuadrado, 2)
            print(f"El área del cuadrado es: {area}\nEl perímetro del cuadrado es: {perimetro}\n")
        elif ejercicio == 6:
            altura = float(input('Ingresa la altura del cilindro: '))
            radio = float(input('Ingresa el radio del cilindro: '))
            volumen = math.pi*radio*radio*altura
            area = 2.0*math.pi*radio*(radio+altura)
            print(f"El volumen del cilindro es: {volumen}\nEl área del cilindro es: {area}\n")
        elif ejercicio == 7:
            radio = float(input('Ingresa el radio de la circunferencia: '))
            longitud = 2*math.pi*radio
            area = pow(math.pi*radio, 2)
            print(f"El área del círculo es: {area}\nLa longitud de la circunferencia es: {longitud}\n")
        elif ejercicio == 8:
            numUno = float(input('Ingresa el primer número: '))
            numDos = float(input('Ingresa el segundo número: '))
            numTres = float(input('Ingresa el tercer número: '))
            promedio = (numUno+numDos+numTres)/3
            print(f"El proemdio de los números ingresados es: {promedio}\n")
        else:
            print("Ingrese una opción válida")
    elif opcion == 2:
        ejercicio = int(input("""\n1. Positivo o negativo.\n2. Comparar cúal es el mayor y menor.
3. Mostrar el mayor y menor de tres números.\n4. Suma o resta.
5. Cociente entre dos números.\n6. Suma o multiplicación.\n7. Año bisiesto o no bisiesto.\n"""))
        if ejercicio == 1:
            numero = int(input("Ingrese un número: "))
            if numero > 0:
                print(f"El número {numero} es par")
            else:
                print(f"El número {numero} es impar")
        elif ejercicio == 2:
            numUno = int(input("Ingrese un número: "))
            numDos = int(input("Ingrese otro número: "))
            if numUno > numDos:
                print(f"{numUno} es mayor que {numDos}\n")
            else:
                print(f"{numUno} es mayor que {numDos}\n")
        elif ejercicio == 3:
            numUno = int(input("Ingrese el primer número: "))
            numDos = int(input("Ingrese el segundo número: "))
            numTres = int(input("Ingrese el tercer número: "))
            if numUno > numDos and numUno > numTres:
                if numDos > numTres:
                    print (f"El número mayor es: {numUno}\nEl número menor es: {numTres}\n")
                else:
                    print (f"El número mayor es: {numUno}\nEl número menor es: {numDos}\n")
            if numDos > numUno and numDos > numTres:
                if numUno > numTres:
                    print (f"El número mayor es: {numDos}\nEl número menor es: {numTres}\n")
                else:
                    print (f"El número mayor es: {numDos}\nEl número menor es: {numUno}\n")
            if numTres > numDos and numTres > numUno:
                if numDos > numUno:
                    print (f"El número mayor es: {numDos}\nEl número menor es: {numUno}\n")
                else:
                    print (f"El número mayor es: {numDos}\nEl número menor es: {numTres}\n")
        elif ejercicio == 4:
            numUno = int(input("Ingrese el primer número: "))
            numDos = int(input("Ingrese el segundo número: "))
            if numUno < numDos:
                print (f"{numUno} + {numDos} = " + str(numUno+numDos) + "\n")
            else:
                print (f"{numUno} - {numDos} = " + str(numUno-numDos) + "\n")
        elif ejercicio == 5:
            numUno = int(input("Ingrese el primer número: "))
            numDos = int(input("Ingrese el segundo número: "))
            if numDos != 0:
                print (f"{numUno} / {numDos} = " + str(numUno/numDos))
            else:
                print ("La división por cero no está definida")
        elif ejercicio == 6:
            numUno = int(input("Ingrese el primer número: "))
            numDos = int(input("Ingrese el segundo número: "))
            if numUno < 0 or numDos < 0:
                print (f"{numUno} + ({numDos}) = " + str(numUno+numDos) + "\n")
            else:
                print (f"{numUno} * ({numDos}) = " + str(numUno*numDos) + "\n")
        elif ejercicio == 7:
            year = int(input("Ingrese el año para saber si es bisiesto: "))
            if year % 400 == 0:
                print (f"El año {year} es bisiesto.\n")
            elif year % 4 == 0 and year % 100 != 0:
                print (f"El año {year} es bisiesto.\n")
            else:
                print (f"El año {year} no es bisiesto.\n")
        else:
            print("Ingrese una opción válida.\n")
    elif opcion == 3:
        ejercicio = int(input("""\n1. Múltiplos de 3 entre 1 y 100.\n2. Números impares entre 0 y 100.
3. Númweros pares entre 0 y 100.\n4. Cuadrados de los números del 1 al 30.
5. Suma de los cuadrados de los 100 primeros números naturales.\n6. Números comprendidos entre dos números naturales.
7. Suma de números por teclado.\n"""))
        if ejercicio == 1:
            i = 1
            while i <= 100:
                if i % 3 == 0:
                    print(i)
                i = i+1
            print("\n")
        elif ejercicio == 2:
            i = 1
            while i <= 30:
                if i % 2 != 0:
                    print(i)
                i = i+1
            print("\n")
        elif ejercicio == 3:
            i = 1
            while i <= 100:
                if i % 2 == 0:
                    print(i)
                i = i+1
            print("\n")
        elif ejercicio == 4:
            i = 1
            while i <= 30:
                print(pow(i,2))
                i = i+1
            print("\n")
        elif ejercicio == 5:
            suma = 0
            i = 1
            while i <= 30:
                suma = suma + pow(i,2)
                i = i+1
            print(f"La suma de los cuadrados de los 100 primeros números naturales es: {suma}\n")
        elif ejercicio == 6:
            numUno = int(input("Ingrese un número: "))
            numDos = int(input("Ingrese un número mayor que el anterior: "))
            while numUno <= numDos:
                print(numUno)
                numUno = numUno+1
            print("\n")
        elif ejercicio == 7:
            print("Ingrese los números que desea sumar, el programa se detendrá al recibir un cero")
            i = -1
            suma = 0
            while i != 0:
                i =int(input())
                suma = suma + i
            print(f"La suma de los números recibidos es: {suma}\n")
        else:
            print("Ingrese una opción válida.\n")
    elif opcion == 99:
        print("\nEl programa ha finalizado.")
    else:
        print("Ingrese una opción válida.\n")
