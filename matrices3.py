import os  # Módulo para interactuar con el sistema operativo (por ejemplo, limpiar la pantalla)

def mostrar_matriz(matriz):
    """Imprime una matriz de forma legible por filas."""
    for fila in matriz:
        print(fila)
    print()  # Salto de línea adicional para separar matrices


def leer_matriz_manual():
    """Permite al usuario ingresar una matriz manualmente."""
    try:
        # Solicita dimensiones de la matriz
        filas = int(input("Número de filas: "))
        columnas = int(input("Número de columnas: "))
        matriz = []

        print(f"Ingrese los elementos de la matriz {filas}x{columnas}:")
        for i in range(filas):
            while True:
                valores = input(f"Fila {i+1} (separada por espacios): ").strip().split()
                if len(valores) == columnas:
                    try:
                        fila = list(map(float, valores))  # Convierte a números
                        matriz.append(fila)
                        break
                    except ValueError:
                        print("Error: Solo se permiten números.")
                else:
                    print(f"Debe ingresar exactamente {columnas} valores.")
        return matriz
    except Exception as e:
        print("Error al ingresar la matriz:", e)
        return None


def cargar_matriz_desde_archivo(ruta):
    """Carga una matriz desde un archivo CSV o TXT."""
    try:
        with open(ruta, 'r') as f:
            lineas = f.readlines()
            matriz = []
            num_columnas = None
            for linea in lineas:
                valores = linea.strip().split(',')
                if not valores:
                    continue
                try:
                    fila = list(map(float, valores))
                except ValueError:
                    print("Archivo contiene valores no numéricos.")
                    return None
                if num_columnas is None:
                    num_columnas = len(fila)
                elif len(fila) != num_columnas:
                    print("Archivo tiene filas de diferentes longitudes.")
                    return None
                matriz.append(fila)
            return matriz
    except Exception as e:
        print("Error al leer el archivo:", e)
        return None


def seleccionar_matriz(matrices):
    """Permite al usuario seleccionar una de las matrices cargadas."""
    if not matrices:
        print("No hay matrices disponibles.")
        return None
    print("Matrices disponibles:")
    for idx, mat in enumerate(matrices):
        print(f"{idx + 1}:")
        mostrar_matriz(mat)
    while True:
        try:
            seleccion = int(input("Seleccione una matriz (número): ")) - 1
            if 0 <= seleccion < len(matrices):
                return matrices[seleccion]
            else:
                print("Selección inválida.")
        except ValueError:
            print("Ingrese un número válido.")


# Funciones básicas entre matrices
def sumar_matrices(a, b):
    """Suma dos matrices elemento a elemento."""
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def restar_matrices(a, b):
    """Resta dos matrices elemento a elemento."""
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def multiplicar_matrices(a, b):
    """Multiplica dos matrices usando el algoritmo estándar."""
    filas_a, columnas_a = len(a), len(a[0])
    filas_b, columnas_b = len(b), len(b[0])
    resultado = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]
    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(filas_b):
                resultado[i][j] += a[i][k] * b[k][j]
    return resultado

def transponer_matriz(matriz):
    """Devuelve la transpuesta de una matriz."""
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def multiplicar_por_escalar(matriz, escalar):
    """Multiplica una matriz por un valor escalar."""
    return [[elemento * escalar for elemento in fila] for fila in matriz]


# Cálculo del determinante recursivo
def calcular_determinante(matriz):
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    det = 0
    for col in range(n):
        submatriz = [fila[:col] + fila[col+1:] for fila in matriz[1:]]
        cofactor = matriz[0][col] * calcular_determinante(submatriz)
        det += (-1) ** col * cofactor
    return det


# Nuevas funciones avanzadas
def es_simetrica(matriz):
    """Verifica si una matriz es simétrica (A[i][j] == A[j][i])"""
    return all(matriz[i][j] == matriz[j][i] for i in range(len(matriz)) for j in range(i+1, len(matriz[0])))

def es_antisimetrica(matriz):
    """Verifica si una matriz es antisimétrica (A[i][j] == -A[j][i])"""
    return all(matriz[i][j] == -matriz[j][i] for i in range(len(matriz)) for j in range(i+1, len(matriz[0])))

def producto_elemento_a_elemento(A, B):
    """Multiplica dos matrices elemento a elemento."""
    if len(A) != len(B) or any(len(a) != len(b) for a, b in zip(A, B)):
        return None
    return [[A[i][j] * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def traspuesta_x_matriz(A):
    """Multiplica la traspuesta de una matriz por sí misma (A^T × A)."""
    A_T = transponer_matriz(A)
    return multiplicar_matrices(A_T, A)


# Menú principal del programa
def menu_principal():
    matrices = []  # Lista donde se guardan todas las matrices procesadas

    while True:
        # os.system('cls')  # Limpia la consola en Windows
        print("=" * 40)
        print("   MENÚ DE OPERACIONES CON MATRICES")
        print("=" * 40)
        print(f"Matrices almacenadas: {len(matrices)}")

        # Opciones de entrada de datos
        print("\n--- Entrada de datos ---")
        print(" 1. Ingresar matriz manualmente")
        print(" 2. Cargar matriz desde archivo")

        # Operaciones básicas
        print("\n--- Operaciones básicas ---")
        print(" 3. Sumar matrices")
        print(" 4. Restar matrices")
        print(" 5. Multiplicar matrices")

        # Más operaciones
        print("\n--- Más operaciones ---")
        print(" 6. Mostrar matrices guardadas")
        print(" 7. Transpuesta de una matriz")
        print(" 8. Multiplicar una matriz por un escalar")

        # Operaciones avanzadas
        print("\n--- Operaciones Avanzadas ---")
        print(" 9. Determinante de una matriz")
        print("10. Verificar simetría o antisimetría")
        print("11. Producto elemento a elemento")
        print("12. Multiplicar traspuesta × matriz")
        print("\n13. Salir")
        print("=" * 40)

        opcion = input("Seleccione una opción: ")

        # Opción 1: Ingreso manual de matriz
        if opcion == "1":
            nueva_matriz = leer_matriz_manual()
            if nueva_matriz:
                matrices.append(nueva_matriz)
                print("Matriz ingresada correctamente.")

        # Opción 2: Cargar desde archivo
        elif opcion == "2":
            ruta = input("Ingrese la ruta del archivo (CSV o TXT): ")
            if os.path.exists(ruta):
                nueva_matriz = cargar_matriz_desde_archivo(ruta)
                if nueva_matriz:
                    matrices.append(nueva_matriz)
                    print("Matriz cargada correctamente.")
            else:
                print("El archivo no existe.")

        # Opción 3: Sumar matrices
        elif opcion == "3":
            if len(matrices) < 2:
                print("Necesita al menos dos matrices para esta operación.")
                continue
            print("Seleccione la primera matriz:")
            a = seleccionar_matriz(matrices)
            print("Seleccione la segunda matriz:")
            b = seleccionar_matriz(matrices)
            if len(a) == len(b) and len(a[0]) == len(b[0]):
                c = sumar_matrices(a, b)
                print("Resultado de la suma:")
                mostrar_matriz(c)
                matrices.append(c)
            else:
                print("Las dimensiones no coinciden para la suma.")

        # Opción 4: Restar matrices
        elif opcion == "4":
            if len(matrices) < 2:
                print("Necesita al menos dos matrices para esta operación.")
                continue
            print("Seleccione la primera matriz:")
            a = seleccionar_matriz(matrices)
            print("Seleccione la segunda matriz:")
            b = seleccionar_matriz(matrices)
            if len(a) == len(b) and len(a[0]) == len(b[0]):
                c = restar_matrices(a, b)
                print("Resultado de la resta:")
                mostrar_matriz(c)
                matrices.append(c)
            else:
                print("Las dimensiones no coinciden para la resta.")

        # Opción 5: Multiplicar matrices
        elif opcion == "5":
            if len(matrices) < 2:
                print("Necesita al menos dos matrices para esta operación.")
                continue
            print("Seleccione la primera matriz:")
            a = seleccionar_matriz(matrices)
            print("Seleccione la segunda matriz:")
            b = seleccionar_matriz(matrices)
            if len(a[0]) == len(b):
                c = multiplicar_matrices(a, b)
                print("Resultado de la multiplicación:")
                mostrar_matriz(c)
                matrices.append(c)
            else:
                print("Las dimensiones no permiten la multiplicación.")

        # Opción 6: Mostrar matrices guardadas
        elif opcion == "6":
            if not matrices:
                print("No hay matrices almacenadas.")
            else:
                print("Matrices almacenadas:")
                for idx, mat in enumerate(matrices):
                    print(f"Matriz {idx + 1}:")
                    mostrar_matriz(mat)

        # Opción 7: Transpuesta
        elif opcion == "7":
            if not matrices:
                print("No hay matrices almacenadas.")
                continue
            print("Seleccione una matriz para transponer:")
            a = seleccionar_matriz(matrices)
            t = transponer_matriz(a)
            print("Matriz transpuesta:")
            mostrar_matriz(t)
            matrices.append(t)

        # Opción 8: Multiplicar por escalar
        elif opcion == "8":
            if not matrices:
                print("No hay matrices almacenadas.")
                continue
            print("Seleccione una matriz para multiplicar por un escalar:")
            a = seleccionar_matriz(matrices)
            while True:
                try:
                    escalar = float(input("Ingrese el valor escalar: "))
                    break
                except ValueError:
                    print("Error: debe ingresar un número válido.")
            m = multiplicar_por_escalar(a, escalar)
            print(f"Resultado de multiplicar por {escalar}:")
            mostrar_matriz(m)
            matrices.append(m)

        # Opción 9: Calcular determinante
        elif opcion == "9":
            if not matrices:
                print("No hay matrices almacenadas.")
                continue
            print("Seleccione una matriz cuadrada para calcular su determinante:")
            a = seleccionar_matriz(matrices)
            if len(a) != len(a[0]):
                print("Error: solo se puede calcular el determinante de una matriz cuadrada.")
            else:
                try:
                    det = calcular_determinante(a)
                    print(f"El determinante de la matriz seleccionada es: {det}")
                except RecursionError:
                    print("Error: la matriz es demasiado grande para este método recursivo.")

        # Opción 10: Simetría/Antisimetría
        elif opcion == "10":
            if not matrices:
                print("No hay matrices almacenadas.")
                continue
            print("Seleccione una matriz para verificar simetría/antisimetría:")
            a = seleccionar_matriz(matrices)
            if len(a) != len(a[0]):
                print("La matriz debe ser cuadrada.")
            else:
                if es_simetrica(a):
                    print("La matriz es simétrica.")
                elif es_antisimetrica(a):
                    print("La matriz es antisimétrica.")
                else:
                    print("La matriz no es ni simétrica ni antisimétrica.")

        # Opción 11: Producto elemento a elemento
        elif opcion == "11":
            if len(matrices) < 2:
                print("Necesita al menos dos matrices para esta operación.")
                continue
            print("Seleccione la primera matriz:")
            a = seleccionar_matriz(matrices)
            print("Seleccione la segunda matriz:")
            b = seleccionar_matriz(matrices)
            if len(a) == len(b) and all(len(x) == len(y) for x, y in zip(a, b)):
                c = producto_elemento_a_elemento(a, b)
                print("Resultado del producto elemento a elemento:")
                mostrar_matriz(c)
                matrices.append(c)
            else:
                print("Las matrices deben tener las mismas dimensiones.")

        # Opción 12: Traspuesta × Matriz
        elif opcion == "12":
            if not matrices:
                print("No hay matrices almacenadas.")
                continue
            print("Seleccione una matriz para calcular A^T × A:")
            a = seleccionar_matriz(matrices)
            try:
                c = traspuesta_x_matriz(a)
                print("Resultado de A^T × A:")
                mostrar_matriz(c)
                matrices.append(c)
            except Exception as e:
                print("Error al realizar la operación:", e)

        # Opción 13: Salir
        elif opcion == "13":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        # Opción no válida
        else:
            print("Opción no válida. Intente nuevamente.")


# Punto de inicio del programa
if __name__ == "__main__":
    menu_principal()