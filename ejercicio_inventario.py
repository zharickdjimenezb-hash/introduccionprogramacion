nombres_productos = []
cantidades_stock = []

try:
    n_productos =int(input("cuantos productos va a registrar?"))
    for i in range(n_productos):
            nombre = input(f"Ingrese el nombre del producto {i + 1}:")
            while True:
                try:
                  cantidad = int(input(f"Ingrese stock de {nombre}"))
                  break
                except:
                 print("Error: ingrese un numero entero valido")

            nombres_productos.append(nombre)    
            cantidades_stock.append(cantidad) 
    print("REPORTE INVENTARIO\n")
    suma_total = 0
    for i in range(len(nombres_productos)):
        nombre = nombres_productos[i]
        stock = cantidades_stock[i]
        suma_total += stock

        if stock == 0:
            print(f"CRITICO: {nombre} agotado.")
        else:
            if stock < 5:
                print(f"ALERTA: {nombre} stock bajo {stock} unidades")
            else:
                if stock > 20:
                        print(f"{nombre}: stock excedente, aplicar descuento")
                else:
                        print(f"{nombre}: Stock saludable")
                promedio = suma_total / n_productos
                print(f"total de productos: {n_productos}\n")
                print(f"promedio de stock en bodega: {promedio}")

except ValueError:
   print("Error: el numero de productos debe ser entero")