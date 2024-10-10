'''
Edicson Rico
Unimonserrate
Programa para validar los tiempos y definir cual metodo de ordenamiento es más rapido
'''
import random
import time
 
def bubble_sort_o(lista):
    lista_copia = lista.copy()
    m = len(lista_copia)
    for i in range(m):
        for j in range(0, m-i-1):
            if lista_copia[j] > lista_copia[j+1]:
                lista_copia[j], lista_copia[j+1] = lista_copia[j+1], lista_copia[j]
    return lista_copia
 
def bubble_sort_m(lista):
    lista_copia = lista.copy()
    p = len(lista_copia)
    for i in range(p):
        swapped = False
        for j in range(0, p-i-1):
            if lista_copia[j] > lista_copia[j+1]:
                lista_copia[j], lista_copia[j+1] = lista_copia[j+1], lista_copia[j]
                swapped = True
        if not swapped:
            break
    return lista_copia
 
def selection_sort(lista):
    lista_copia = lista.copy()
    w = len(lista_copia)
    for i in range(w):
        min_idx = i
        for j in range(i+1, w):
            if lista_copia[j] < lista_copia[min_idx]:
                min_idx = j
        lista_copia[i], lista_copia[min_idx] = lista_copia[min_idx], lista_copia[i]
    return lista_copia
 
def insertion_sort(lista):
    lista_copia = lista.copy()
    for i in range(1, len(lista_copia)):
        key = lista_copia[i]
        j = i-1
        while j >= 0 and key < lista_copia[j]:
            lista_copia[j+1] = lista_copia[j]
            j -= 1
        lista_copia[j+1] = key
    return lista_copia
 
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
   
    mid = len(lista) // 2
    L = merge_sort(lista[:mid])
    R = merge_sort(lista[mid:])
 
    return merge(L, R)
 
def merge(left, right):
    resultado = []
    i = j = 0
   
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
   
    resultado.extend(left[i:])
    resultado.extend(right[j:])
   
    return resultado
 
def medir_tiempo(funcion_ordenamiento, lista):
    inicio = time.time()
    funcion_ordenamiento(lista)
    fin = time.time()
    return fin - inicio
 
def imprimir_tabla(datos, encabezados):
    anchos = [max(len(str(dato)) for dato in col) for col in zip(*datos)]
    anchos = [max(len(encabezado), ancho) for encabezado, ancho in zip(encabezados, anchos)]
   
    for encabezado, ancho in zip(encabezados, anchos):
        print(f"{encabezado:<{ancho}}", end=" | ")
    print()
   
    for ancho in anchos:
        print("-" * ancho, end="-+-")
    print()
   
    for fila in datos:
        for dato, ancho in zip(fila, anchos):
            print(f"{dato:<{ancho}}", end=" | ")
        print()
 
print("Ingrese las cantidades de números a ordenar (separadas por espacios):")
cantidades = list(map(int, input().split()))
 
resultados = []
 
for cantidad in cantidades:
    lista_aleatoria = [random.randint(1, 1000) for _ in range(cantidad)]
   
    tiempo_bubble_o = medir_tiempo(bubble_sort_o, lista_aleatoria)
    tiempo_bubble_m = medir_tiempo(bubble_sort_m, lista_aleatoria)
    tiempo_selection = medir_tiempo(selection_sort, lista_aleatoria)
    tiempo_insertion = medir_tiempo(insertion_sort, lista_aleatoria)
    tiempo_merge = medir_tiempo(merge_sort, lista_aleatoria)
   
    resultados.append([
        cantidad,
        f"{tiempo_bubble_o:.6f}",
        f"{tiempo_bubble_m:.6f}",
        f"{tiempo_selection:.6f}",
        f"{tiempo_insertion:.6f}",
        f"{tiempo_merge:.6f}"
    ])
 
headers = ["Cantidad", "Bubble Original (s)", "Bubble Modificado (s)", "Selection (s)", "Insertion (s)", "Merge (s)"]
print("Resultados de los diferentes tamaños de lista:")
imprimir_tabla(resultados, headers)
