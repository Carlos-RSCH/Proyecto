# Alumno: Carlos Roberto Silva Chacón
# Materia: Tópicos Avanzados de Proramación
# Grado y Grupo: S4C

while True:
    print("\n¿Desea realizar una operación")
    print("1. Sí")
    print("2. No")

    opc = input("Ingrese una opción: ")
    if opc =="1":
            print("*********** Menú Principal ***********")
            print("1. Anagrama")
            print("2. Invertir en Cadena")
            print("3. Fibonacci")
            print("4. Eliminar los Duplicados")
            print("5. Palíndromo")
            print("6. Contar Palabras")
            print("7. Encontrar el Elemento Mayor")
            print("8. Invertir en una Lista")
            print("9. Filtrar Números por Pares")
            print("10. Encontrar el Segundo Alcalde")
            print("11. Contar Vocales")
            print("12. Ordenar una Lista de Tuplas")
            print("13. Contar Caracteres Únicos")
            print("14. Encontrar Palabras Más Largas")
            print("15. Encontrar Números Primos")
            print("16. Salir")
            opc = input("Ingrese una opción: ")
            if opc == "1":
                # 1. Anagrama
                def anagrama(palabra1, palabra2):
                    if len(palabra1) != len(palabra2):
                        return False
                    return sorted(palabra1.lower()) == sorted(palabra2.lower())

                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")

                if opc == "1":
                    palabra1 = input("\nIngrese la palabra 1: ")
                    palabra2 = input("Ingrese la palabra 2: ")
                    print("\n¿La palabra " + palabra1 + " y " + palabra2 + " son anagrama?:")
                    print(anagrama(palabra1, palabra2))
                else:
                    print("\n¿La palabra escuela y cuclees son anagrama?: ")
                    print(anagrama("escuela", "cuclees"))  # False
                    print("\n¿La palabra phyton y java es anagrama?: ")
                    print(anagrama("python", "java"))  # False

            elif opc == "2":
                # 2. Invertir en Cadena
                def invertir_cadena(cadena):
                    return cadena[::-1]


                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")

                if opc == "1":
                    palabraOri = input("\nIngrese la cadena original: ")
                    print("Cadena invertida: ")
                    print(invertir_cadena(palabraOri))
                else:
                    print("\nPalabra Original: ")
                    print("Phyton")
                    print("Palabra Invertida: ")
                    print(invertir_cadena("Python"))  # nohtyP
                    print("\nPalabra Original: ")
                    print("Hola mundo")
                    print("Palabra Invertida: ")
                    print(invertir_cadena("Hola mundo"))  # odnum aloH

            elif opc == "3":
                # 3. Fibonacci
                def fibonacci(n):
                    if n <= 0:
                        return 0
                    elif n == 1:
                        return 1
                    else:
                        return fibonacci(n - 1) + fibonacci(n - 2)

                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")

                if opc == "1":
                    numOri = input("\n Ingrese el número: ")
                    numOri=int(numOri)
                    print(fibonacci(numOri))
                else:
                    print("\n n= 0")
                    print(fibonacci(0))  # 0
                    print("\n n= 1")
                    print(fibonacci(1))  # 1
                    print("\n n= 6")
                    print(fibonacci(6))  # 8

            elif opc == "4":
                # 4. Eliminar los Duplicados
                def eliminar_duplicados(lista):
                    return list(set(lista))

                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")

                if opc == "1":
                    print("\n¿Desea ingresar números o palabras?")
                    print("1. Números")
                    print("2. Palabras")
                    tipo = input("Ingrese una opción: ")

                    if tipo == "1":
                        cadenaOri = input("Ingrese la lista de números separados por comas (ej. 1, 2, 2, 3, 4): ")
                        listaOri = list(map(int, cadenaOri.split(",")))
                    elif tipo == "2":
                        cadenaOri = input(
                            "Ingrese la lista de palabras separadas por comas (ej. manzana, pera, pera): ")
                        listaOri = list(map(str, cadenaOri.split(",")))
                    else:
                        print("Opción no válida")
                        listaOri = []

                    if listaOri:
                        print("Cadena sin duplicados:", eliminar_duplicados(listaOri))
                else:
                    print("\nCadena Original: [1, 2, 3, 2, 4, 1, 5]")
                    print(eliminar_duplicados([1, 2, 3, 2, 4, 1, 5]))  # [1, 2, 3, 4, 5]
                    print("\nCadena Original: apple, banana, cherry, banana")
                    print(eliminar_duplicados(["apple", "banana", "cherry", "banana"]))  # ['apple', 'banana', 'cherry']

            elif opc == "5":
                # 5. Palíndromo
                def palindromo(cadena):
                    cadena = cadena.lower().replace(" ", "")
                    return cadena == cadena[::-1]
                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")
                if opc == "1":
                    cadenaOri=input("Ingrese la cadena: ")
                    print(palindromo(cadenaOri))
                else:
                    print("\n ¿La cadena: Anita lava la tina es palíndromo?")
                    print(palindromo("Anita lava la tina"))  # True
                    print("\n ¿La cadena: Phyton es palíndromo?")
                    print(palindromo("Python"))  # False

            elif opc == "6":
                # 6. Contar Palabras
                def contar_palabras(texto):
                    palabras = texto.lower().split()
                    conteo = {}
                    for palabra in palabras:
                        if palabra in conteo:
                            conteo[palabra] += 1
                        else:
                            conteo[palabra] = 1
                    return conteo
                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")
                if opc == "1":
                    cadenaOri = input("Ingrese la cadena: ")
                    print(contar_palabras(cadenaOri))
                else:

                    print("\n¿Cúantas palabras tiene la frase: El perro persiguió al gato. El gato huyó del perro?")
                    texto = "El perro persiguió al gato. El gato huyó del perro."
                    print(contar_palabras(texto))
                    # {'el': 2, 'perro': 2, 'persiguió': 1, 'al': 1, 'gato': 2, 'huyó': 1, 'del': 1}

            elif opc == "7":
                # 7. Encontrar el Elemento Mayor
                def encontrar_mayor(lista):
                    return max(lista)
                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")

                if opc == "1":
                    cadenaOri = input("Ingrese la lista de números separados por comas (ej. 1, 2, 2, 3, 4): ")
                    listaOri = list(map(int, cadenaOri.split(",")))
                    print(encontrar_mayor(listaOri))
                else:
                    print("\n¿Cual es el número mayor de estos números: [5, 2, 8, 1, 9]? ")
                    print(encontrar_mayor([5, 2, 8, 1, 9]))  # 9
                    print("\n¿Cual es el número mayor de estos números: [-3, 0, 4, -1, 7]? ")
                    print(encontrar_mayor([-3, 0, 4, -1, 7]))  # 7

            elif opc == "8":
                # 8. Invertir en una Lista
                def invertir_lista(lista):
                    return lista[::-1]
                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")

                if opc == "1":
                    print("\n¿Desea ingresar números o palabras?")
                    print("1. Números")
                    print("2. Palabras")
                    tipo = input("Ingrese una opción: ")

                    if tipo == "1":
                        cadenaOri = input("Ingrese la lista de números separados por comas (ej. 1, 2, 2, 3, 4): ")
                        listaOri = list(map(int, cadenaOri.split(",")))
                    elif tipo == "2":
                        cadenaOri = input(
                            "Ingrese la lista de palabras separadas por comas (ej. manzana, pera, pera): ")
                        listaOri = list(map(str, cadenaOri.split(",")))
                    else:
                        print("Opción no válida")
                        listaOri = []

                    if listaOri:
                        print("Cadena inertida:", invertir_lista(listaOri))
                    else:
                        print("\nLista original: [1, 2, 3, 4, 5]")
                        print("Lista invertida: ")
                        print(invertir_lista([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
                        print("\nLista original: apple, banana, cherry")
                        print("Lista invertida: ")
                        print(invertir_lista(["apple", "banana", "cherry"]))  # ['cherry', 'banana', 'apple']
            elif opc == "9":
                # 9. Filtrar Números por Pares
                def filtrar_pares(lista):
                    return [num for num in lista if num % 2 == 0]
                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")

                if opc == "1":
                    cadenaOri = input("Ingrese la lista de números separados por comas (ej. 1, 2, 2, 3, 4): ")
                    listaOri = list(map(int, cadenaOri.split(",")))
                    print(filtrar_pares(listaOri))
                else:
                    print("\nLista de números: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
                    print("Lista filtrado por números pares")
                    print(filtrar_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [2, 4, 6, 8, 10]
                    print("\nLista de números: [-2, 0, 1, 3, 5, 8]")
                    print("Lista filtrado por números pares")
                    print(filtrar_pares([-2, 0, 1, 3, 5, 8]))  # [-2, 0, 8]

            elif opc == "10":
                # 10. Encontrar al Segundo Alcalde
                def encontrar_segundo_mayor(lista):
                    if len(lista) < 2:
                        return None
                    lista.sort(reverse=True)
                    return lista[1]
                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")
                if opc == "1":
                    cadenaOri = input("Ingrese la lista de números separados por comas (ej. 1, 2, 2, 3, 4): ")
                    listaOri = list(map(int, cadenaOri.split(",")))
                    print(encontrar_segundo_mayor(listaOri))
                else:
                    print("\n El segundo número mayor de la lista: [5, 2, 8, 1, 9] es:")
                    print(encontrar_segundo_mayor([5, 2, 8, 1, 9]))  # 8
                    print("\n El segundo número mayor de la lista: [10, 5, 8, 12, 7] es:")
                    print(encontrar_segundo_mayor([10, 5, 8, 12, 7]))  # 10
            elif opc == "11":
                # 11. Contar Vocaless
                def contar_vocales(texto):
                    vocales = "aeiou"
                    cuenta = 0
                    for letra in texto.lower():
                        if letra in vocales:
                            cuenta += 1
                    return cuenta
                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")
                if opc == "1":
                    cadenaOri = input("Ingrese la cadena: ")
                    print(contar_vocales(cadenaOri))
                else:

                    print("\nLas vocales que tiene la frase: Hola, ¿cómo estás? son: ")
                    print(contar_vocales("Hola, ¿cómo estás?"))  # 6
                    print("\nLas vocales que tiene la frase:Python es un lenguaje de programación excelente.")
                    print(contar_vocales("Python es un lenguaje de programación excelente."))  # 16

            elif opc == "12":
                # 12. Ordenar una Lista de Tuplas
                def ordenar_tuplas(lista_tuplas):
                    return sorted(lista_tuplas, key=lambda x: x[1])
                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")
                if opc == "1":
                    lista_tuplas = []
                    n = int(input("¿Cuántas tuplas desea ingresar?: "))
                    for i in range(n):
                        elemento1 = input(f"Ingrese el primer elemento de la tupla {i + 1}: ")
                        elemento2 = int(input(f"Ingrese el segundo elemento de la tupla {i + 1}: "))
                        lista_tuplas.append((elemento1, elemento2))
                    print("\nLista original:", lista_tuplas)
                    print("Por Tuplas:", ordenar_tuplas(lista_tuplas))
                else:
                    print("\n Lista original: [(3, 2), (1, 3), (4, 1), (2, 4)]")
                    print("Por Tuplas: ")
                    print(ordenar_tuplas([(3, 2), (1, 3), (4, 1), (2, 4)]))
                    # [(4, 1), (3, 2), (1, 3), (2, 4)]
                    print("\n Lista original: [(apple, 4), (banana, 2), (cherry, 1)]")
                    print("Por Tuplas: ")
                    print(ordenar_tuplas([("apple", 4), ("banana", 2), ("cherry", 1)]))
                    # [('cherry', 1), ('banana', 2), ('apple', 4)]

            elif opc == "13":
                # 13. Contar con Caracteres Únicos
                def contar_unicos(cadena):
                    return len(set(cadena))
                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")
                if opc == "1":
                    cadenaOri = input("Ingrese la cadena: ")
                    print(contar_unicos(cadenaOri))
                else:
                    print("\n¿Cúantas caracteres únicos tiene la palabra: hello? ")
                    print(contar_unicos("hello"))  # 4
                    print("\n¿Cúantas caracteres únicos tiene la palabra: Python? ")
                    print(contar_unicos("Python"))  # 6
                    print("\n¿Cúantas caracteres únicos tiene la palabra: aabbcc ")
                    print(contar_unicos("aabbcc"))  # 3
            elif opc == "14":
                # 14. Encontrar Palabras Más Largas
                def palabras_mas_largas(texto, n):
                    palabras = texto.split()
                    palabras.sort(key=len, reverse=True)
                    return palabras[:n]
                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")
                if opc == "1":
                    texto = input("Ingrese la frase: ")
                    n = int(input("Ingrese el número de palabras más largas a obtener: "))
                    print("\nLas palabras más largas de la frase ingresada:")
                    print(palabras_mas_largas(texto, n))
                else:
                    print("\n¿Cúales son las palabras más largas de la frase: El perro persiguió al gato? ")
                    print(palabras_mas_largas("El perro persiguió al gato", 2))
                    # ['persiguió', 'gato']
                    print("\n¿Cúales son las palabras más largas de la frase: Python es un lenguaje de programación? ")
                    print(palabras_mas_largas("Python es un lenguaje de programación", 3))
                    # ['programación', 'lenguaje', 'Python']

            elif opc == "15":
                # 15. Encontrar Números Primos
                def primo(n):
                    if n < 2:
                        return False
                    for i in range(2, int(n ** 0.5) + 1):
                        if n % i == 0:
                            return False
                    return True


                def primos_hasta(n):
                    primos = []
                    i = 2
                    while len(primos) < n:
                        if primo(i):
                            primos.append(i)
                        i += 1
                    return primos


                print("\n¿Desea ingresar los valores?")
                print("1. Sí")
                print("2. No. Generame ejemplos")
                opc = input("Ingrese una opción: ")

                if opc == "1":
                    if opc == "1":
                        numOri = int(input("\n Ingrese el número: "))
                        print(primos_hasta(numOri))
                else:
                    print("\n Dame 5 números primos")
                    print(primos_hasta(5))  # [2, 3, 5, 7, 11]
                    print("\nDame 10 números primos")
                    print(primos_hasta(10))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
            elif opc == "16":
                print("Gracias por usar el programa")
                break
            else:
                print("Valor Incorrecto. Vuelva a Seleecionar una Opción")

    elif opc=="2":
        print("Gracias por usar el programa")
        break
    else:
        print("Valor Incorrecto. Vuelva a Seleecionar una Opción")












