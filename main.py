# Lee un archivo y lo convierte en una matriz.
def leer_archivo(nombre):
    matriz = []

    archivo = open(nombre, "r")

    for linea in archivo:
        fila = []

        for elemento in linea.split():
            fila.append(int(elemento))

        matriz.append(fila)

    archivo.close()

    return matriz

# Convierte una matriz bidimensional en un vector unidimensional.
def expandir_matriz(X):
    matriz_expandida=[]

    for fila in X:
        for elemento in fila:
            matriz_expandida.append(elemento)
    return matriz_expandida

# Convierte un vector en una matriz de una fila si es necesario.
def vector_a_matriz(X):
    Y=[]
    if not isinstance(X[0], list):
        Y.append(X)
    else:
        Y=X
    return Y

# Sustituye todos los valores 0 del vector por -1.
def ceros_por_menos_unos(X):
    for i in range(len(X)):
        if X[i] == 0:
            X[i]=-1
    return X

# Calcula la matriz transpuesta intercambiando filas por columnas.
def transpuesta(X):
    X=vector_a_matriz(X)

    filas = len(X)
    columnas = len(X[0])

    matriz_transpuesta=[]

    for j in range(columnas):
        fila=[]
        for i in range(filas):
            fila.append(X[i][j])

        matriz_transpuesta.append(fila)

    return matriz_transpuesta

# Multiplica dos matrices siempre que sus dimensiones sean compatibles.
def multiplicar_matrices(X1, X2):
    fila=[]
    matriz_resultante=[]
    X1=vector_a_matriz(X1)
    X2=vector_a_matriz(X2)
    filas_X1 = len(X1)
    columnas_X1 = len(X1[0])
    filas_X2 = len(X2)
    columnas_X2 = len(X2[0])

    if columnas_X1 != filas_X2:
        print("Error, no se pueden multiplicar las matrices")
    else:
        for i in range(filas_X1):
            for j in range(columnas_X2):
                suma = 0
                for k in range(filas_X2):
                    suma = suma + (X1[i][k] * X2[k][j])
                fila.append(suma)
            matriz_resultante.append(fila)
            fila=[]
    return matriz_resultante

# Suma dos matrices elemento por elemento si tienen la misma dimensión.
def sumar_matrices(X1, X2):
    fila=[]
    matriz_resultante=[]
    filas_X1 = len(X1)
    columnas_X1 = len(X1[0])
    filas_X2 = len(X2)
    columnas_X2 = len(X2[0])
    if filas_X1 != filas_X2 or columnas_X1 != columnas_X2:
        print("Error, no se pueden sumar las matrices porque no son de la misma dimension")
        return 0
    else:
        for i in range(filas_X1):
            for j in range(columnas_X1):
                fila.append(X1[i][j]+ X2[i][j])
                #print(fila)
            matriz_resultante.append(fila)
            fila = []
    return matriz_resultante

# Sustituye por 0 todos los elementos de la diagonal principal.
def diagonal_por_ceros(X):
    filas = len(X)
    columnas = len(X[0])
    for i in range(filas):
        for j in range(columnas):
            if i == j:
                X[i][j]=0
    return X

# Calcula la matriz de pesos de la red Hopfield a partir de varios patrones.
def mat_de_pesos(patrones):
    matriz_pesos = None

    for patron in patrones:
        patron_t = transpuesta(patron)
        multiplicacion = multiplicar_matrices(patron_t, patron)

        if matriz_pesos is None:
            matriz_pesos = multiplicacion
        else:
            matriz_pesos = sumar_matrices(matriz_pesos, multiplicacion)

    matriz_pesos = diagonal_por_ceros(matriz_pesos)

    return matriz_pesos

# Ejecuta la red Hopfield hasta que el estado deje de cambiar.
def main(A, patrones):
    A = vector_a_matriz(A)
    T = mat_de_pesos(patrones)

    while True:
        A_x_T = multiplicar_matrices(A, T)
        U = escalonada(A_x_T, A)

        if A != U:
            A = U
        else:
            break

    return A

# Aplica la función de activación conservando el estado anterior cuando el valor es 0.
def escalonada(X, estado_anterior):
    filas = len(X)
    columnas = len(X[0])

    for i in range(filas):
        for j in range(columnas):
            if X[i][j] > 0:
                X[i][j] = 1
            elif X[i][j] < 0:
                X[i][j] = -1
            else:
                X[i][j] = estado_anterior[i][j]
    return X

# Imprime un vector en forma de figura según el número de columnas.
def imprimir_figura(vector, columnas):
    if isinstance(vector[0], list):
        vector = vector[0]

    for i in range(0, len(vector), columnas):
        fila = vector[i:i+columnas]

        for elemento in fila:
            if elemento == 1:
                print("██", end="")
            else:
                print("  ", end="")

        print()

if __name__ == "__main__":

    archivos_patrones = [
        "dataset/uno.txt",
        "dataset/dos.txt",
        "dataset/tres.txt"
    ]

    patrones = []

    for archivo in archivos_patrones:
        patron = leer_archivo(archivo)
        patron = expandir_matriz(patron)
        patron = ceros_por_menos_unos(patron)

        patrones.append(patron)

    x = leer_archivo("dataset/x.txt")
    x = expandir_matriz(x)
    x = ceros_por_menos_unos(x)

    resultado = main(x, patrones)

    # Imprime la figura de entrada.
    print("Figura de entrada:")
    imprimir_figura(x, 5)

    # Imprime el resultado de la red Hopfield.
    print("Resultado de la red Hopfield:")
    imprimir_figura(resultado, 5)