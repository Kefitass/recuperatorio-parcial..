from funciones import *
def main():
    numero_depositos = 4
    numero_insumos = 5
    nombre_depositos = ["Rosario", "Cordoba", "Salta", "Bahia Blanca"]
    nombres_insumos = ["Arduino UNO", "Sensor de temperatura", "Cable USB", "Display LCD", "Protoboard"]

    matriz_stock = inicializar_matriz(numero_depositos, numero_insumos)

    
    cargar_stock_insumos(matriz_stock, nombre_depositos, nombres_insumos)

    mostrar_depositos_stock_superior_a(matriz_stock, nombre_depositos, 5000)

    print("Insumos con stock total superior a 3000 unidades")
    stock_total_por_insumo = calcular_stock_total_por_insumo(matriz_stock)
    se_encontro_insumo = False
    for i in range(len(stock_total_por_insumo)):
        if stock_total_por_insumo[i] > 3000:
            print(f"{nombres_insumos[i]} tiene un stock total de {stock_total_por_insumo[i]} unidades.")
            se_encontro_insumo = True
    if not se_encontro_insumo:
        print("Ningun insumo supera las 3000 unidades de stock total.")

main()
