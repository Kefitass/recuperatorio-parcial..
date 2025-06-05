
numero_depositos = 4
numero_insumos = 5
nombre_depositos = ["Rosario", "Cordoba", "Salta", "Bahia Blanca"] 
nombres_insumos = ["Arduino UNO", "Sensor de temperatura", "Cable USB", "Display LCD", "Protoboard"]


def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any = 0) -> list:
    matriz = []
    for fila_actual in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz = matriz + [fila]
    return matriz

def cargar_stock_insumos(matriz_stock: list, nombres_depositos: list, nombres_insumos: list):
    print("Cargar Stock de Insumos")
    for indice_deposito in range(len(matriz_stock)):
        print("Cargando stock para el deposito: " + nombres_depositos[indice_deposito])
        for indice_insumo_actual in range(len(matriz_stock[0])):
            cantidad = int(input("Ingrese la cantidad de " + nombres_insumos[indice_insumo_actual] + " en " + nombres_depositos[indice_deposito] + ": "))
            matriz_stock[indice_deposito][indice_insumo_actual] = cantidad
    print("Carga de stock completada.")

def mostrar_matriz(matriz_a_mostrar: list, titulo_matriz: str):
    print(titulo_matriz)
    for fila_actual in matriz_a_mostrar:
        fila_formateada_str = ""
        for elemento_en_fila in fila_actual:
            fila_formateada_str = fila_formateada_str + str(elemento_en_fila)
        print(fila_formateada_str)


def calcular_stock_total_por_deposito(matriz_stock_general: list) -> list:
    totales_por_deposito = [0] * len(matriz_stock_general)

    for indice_deposito in range(len(matriz_stock_general)):
        suma_unidades_fila = 0
        for indice_insumo_actual in range(len(matriz_stock_general[0])):
            suma_unidades_fila = suma_unidades_fila + matriz_stock_general[indice_deposito][indice_insumo_actual]
        totales_por_deposito[indice_deposito] = suma_unidades_fila

    return totales_por_deposito

def mostrar_depositos_stock_superior_a(matriz_stock_general: list, nombres_depositos: list, umbral_minimo: int):
    print("Depositos con stock total superior a " + str(umbral_minimo) + " Unidades")
    totales_calculados = calcular_stock_total_por_deposito(matriz_stock_general)

    se_encontro_deposito = False
    for indice_deposito in range(len(totales_calculados)):
        if totales_calculados[indice_deposito] > umbral_minimo:
            print("El deposito " + nombres_depositos[indice_deposito] + " tiene un stock total de " + str(totales_calculados[indice_deposito]) + " unidades.")
            se_encontro_deposito = True
    
    if not se_encontro_deposito:
        print("Ningun deposito supera las" + str(umbral_minimo) +"unidades de stock total.")


def calcular_stock_total_por_insumo(matriz_stock_general: list) -> list:
    totales_por_insumo = [0] * len(matriz_stock_general[0])

    for indice_insumo_actual in range(len(matriz_stock_general[0])):
        suma_unidades_columna = 0
        for indice_deposito in range(len(matriz_stock_general)):
            suma_unidades_columna = suma_unidades_columna + matriz_stock_general[indice_deposito][indice_insumo_actual]
        totales_por_insumo[indice_insumo_actual] = suma_unidades_columna

    return totales_por_insumo

