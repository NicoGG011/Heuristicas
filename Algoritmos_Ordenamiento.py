##########################################################################
# Algoritmos de Ordenamiento
##########################################################################

# -----------------------------------------------------
# Ejemplo 1: Busqueda secuencial
# -----------------------------------------------------

def busqueda_secuencial(Lista, elemento):
    indice = 0
    encontrado = False

    while indice < len(Lista) and not encontrado:
        if Lista[indice] == elemento:
            encontrado = True
        else:
            indice = indice + 1

    return encontrado


instanciaPrueba = [5, 2, 7, 4, 1, 9]
print(busqueda_secuencial(instanciaPrueba, 1))
print(busqueda_secuencial(instanciaPrueba, 42))


# -----------------------------------------------------
# Ejemplo 2: Busqueda binaria
# -----------------------------------------------------

def busqueda_binaria(Lista, elemento):
    primero = 0
    ultimo = len(Lista) - 1
    encontrado = False

    while primero <= ultimo and not encontrado:
        puntoMedio = (primero + ultimo) // 2
        if Lista[puntoMedio] == elemento:
            encontrado = True
        else:
            if elemento < Lista[puntoMedio]:
                ultimo = puntoMedio - 1
            else:
                primero = puntoMedio + 1

    return encontrado


instanciaPrueba = [1, 2, 4, 5, 7, 9]
print(busqueda_binaria(instanciaPrueba, 7))  # True
print(busqueda_binaria(instanciaPrueba, 42))  # False


# -----------------------------------------------------
# Ejemplo 3: Bubble Sort - Ordenamiento Burbuja
# -----------------------------------------------------

def bubble_sort(Lista):
    for iteracion in range(len(Lista) - 1, 0, -1):
        for i in range(iteracion):
            if Lista[i] > Lista[i + 1]:
                temp = Lista[i]
                Lista[i] = Lista[i + 1]
                Lista[i + 1] = temp


instanciaPrueba = [5, 2, 7, 4, 1, 9]
bubble_sort(instanciaPrueba)
print(instanciaPrueba)


# -----------------------------------------------------
# Ejemplo 4: Insertion Sort - Ordenamiento por Inserción
# -----------------------------------------------------

def insertion_sort(Lista):
    for indice in range(1, len(Lista)):
        valor_actual = Lista[indice]
        posicion = indice

        while posicion > 0 and Lista[posicion - 1] > valor_actual:
            Lista[posicion] = Lista[posicion - 1]
            posicion = posicion - 1

        Lista[posicion] = valor_actual


instancia_prueba = [5, 2, 7, 4, 1, 9]
insertion_sort(instancia_prueba)
print(instancia_prueba)

# -----------------------------------------------------
# Actividad 1
# -----------------------------------------------------


from random import randint


def producto_mas_vendido(Instancia):
    totalVentasProducto = -1
    producto = -1
    for prod in range(len(Instancia[0])):
        suma = 0
        for local in range(len(Instancia)):
            suma = suma + Instancia[local][prod]

        if suma > totalVentasProducto:
            totalVentasProducto = suma
            producto = prod

    return producto, totalVentasProducto


def punto_de_venta_mas_visitado(Instancia):
    totalVentasPunto = -1
    puntoVenta = -1

    for local in range(len(Instancia)):
        suma = 0
        for prod in range(len(Instancia[0])):
            suma = suma + Instancia[local][prod]

        if suma > totalVentasPunto:
            totalVentasPunto = suma
            puntoVenta = local

    return puntoVenta, totalVentasPunto


def punto_venta_producto(Instancia):
    ventas = -1
    puntoVenta = -1
    producto = -1
    for local in range(len(Instancia)):
        for prod in range(len(Instancia[local])):
            if ventas < Instancia[local][prod]:
                ventas = Instancia[local][prod]
                puntoVenta = local
                producto = prod

    return puntoVenta, producto, ventas


numeroInstancias = 5
numeroLocales = 5
numeroProductos = 10
for i in range(numeroInstancias):
    Instancia = []
    for local in range(numeroLocales):
        ventas = []
        for prod in range(numeroProductos):
            ventas.append(randint(0, 100))

        Instancia.append(ventas)

    print('\n*******************************************')
    print('Resultados para instancia', i)
    print('*******************************************')

    producto, totalVentasProducto = producto_mas_vendido(Instancia)
    print('\ni) El producto más vendido fue el: ', producto, 'con un total de ventas de: ', totalVentasProducto)

    puntoVenta, totalVentasPunto = punto_de_venta_mas_visitado(Instancia)
    print('\nii) El punto de venta más visitado fue el: ', puntoVenta, 'con un total de ventas de: ', totalVentasPunto)

    puntoVenta, producto, ventas = punto_venta_producto(Instancia)
    print('\niii) La mejor combinación punto de venta - producto fue: ', puntoVenta, '-', producto,
          'Con un total de ventas de: ', ventas)
