from heapq import heappush, heappop
from random import randrange
from time import time
import os

dash_div = ("-" * 67)


def selection_sort(unsorted_array, debbug):
    array_copy = unsorted_array.copy()
    print("             " + str(array_copy))

    n = len(array_copy)
    iterations = 0
    swaps = 0
    comparisons = 0

    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            is_smaller = array_copy[j] < array_copy[smallest]
            comparisons += 1
            if is_smaller:
                smallest = j
        if not smallest == i:
            array_copy[i], array_copy[smallest] = array_copy[smallest], array_copy[i]
            swaps += 1
        iterations += 1
        print("Iteración " + str(iterations) + ": " + str(array_copy))

    print("Comparisons: " + str(comparisons))
    print("Swaps: " + str(swaps))
    if debbug:
        analize_selection_sort(n, comparisons, swaps)
    return array_copy


def analize_selection_sort(n, comparisons, shifts):
    comparisonsO = "n^2 = " + str(n ** 2)
    shiftsO = "n^2 = "
    comparisonsC = "((n-1)n)/2 = " + str((n - 1) * n / 2)
    shiftsC = "((n-1)n)/2 = [0," + str((n - 1) * n / 2) + "]"
    comparisonsR = str(comparisons)
    shiftsR = str(shifts)
    analizeAlgorithm(comparisonsO, shiftsO, comparisonsC, shiftsC, comparisonsR, shiftsR)


def bubbleSort(unsort_list):
    arrayCopy = unsort_list.copy()
    print("             " + str(arrayCopy))
    iteration = 0
    shifts = 0
    comparations = 0
    print(str(range(len(arrayCopy) - 1)))
    for i in range(len(arrayCopy) - 1):
        for j in range(len(arrayCopy) - 1 - i):
            comparations += 1
            if arrayCopy[j] > arrayCopy[j + 1]:
                arrayCopy[j], arrayCopy[j + 1] = arrayCopy[j + 1], arrayCopy[j]
                shifts += 1
            iteration += 1
            print("Iteración " + str(iteration) + ": " + str(arrayCopy))

    analizeBubbleSort(arrayCopy, comparations, shifts)
    return shifts, comparations


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def mergeSort(array):
    iteration = 1
    # Punto medio del arreglo
    mitad = len(array) // 2

    # lft es igual al arreglo en la primera parte (IZQ)
    # rgt es igual al arreglo en la segunda parte (DER)
    lft, rgt = array[:mitad], array[mitad:]

    # si el arreglo en la parte izquierda es mayor a 1
    # llama a marge sort de nuevo
    # metodo recursivo
    if len(lft) > 1:
        lft = mergeSort(lft)
    # Si el arreglo en la parte derecha es mayor a 1
    # llama a merge sort de nuevo
    # metodo recursivo
    if len(rgt) > 1:
        rgt = mergeSort(rgt)
    # arreglo de apollo
    res = []

    while lft and rgt:
        # Si el ultimo elemento del arreglo izquierdo es mayor o igual al derecho
        # asignar al areglo de apoyo el valor izquierdo
        # en otro caso asignar el derecho
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())

        print("Iteración " + str(iteration) + ": " + str(array))
        iteration += 1
    # Estado del arreglo de apoyo = [MAX,...,MIN]
    # Ordenar el arreglo en reversa
    res.reverse()

    # Asignar los ultimos elementos de lft y rgt al areglo teporal
    return (lft or rgt) + res


def quickSort(array, start, end):
    print("             " + str(array))

    if start < end:
        pivot = partition(array, start, end)

        quickSort(array, start, pivot - 1)  ## array IZQ llamadas recursivas
        quickSort(array, pivot + 1, end)  ##array DERCH llamasas recurivas
    return array


def partition(array, start, end):
    ## El pivote se declara siempre al inicio del rango que desea acomodarse
    pivot = array[start]

    # Lado menores al pivote
    left = start + 1

    # Lado mayoreas al pivote
    right = end
    # miestras el lado IZQ sea mayor al DERCH el arreglo no esta arreglado
    done = False
    while not done:
        while left <= right and array[left] <= pivot:
            left = left + 1
        while array[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp

    temp = array[start]
    array[start] = array[right]
    array[right] = temp
    return right


def insertionSort(unorderedArray):
    arrayCopy = unorderedArray.copy()
    print("             " + str(arrayCopy))
    iteration = 1
    comparition = 0
    shifts = 0

    for i in range(1, len(arrayCopy)):
        small = arrayCopy[i]
        for j in reversed(range(-1, i)):
            comparition += 1
            if j >= 0 and small < arrayCopy[j]:
                arrayCopy[j + 1], arrayCopy[j] = arrayCopy[j], arrayCopy[j + 1]
                shifts += 1
            else:
                break
            print("Iteración " + str(iteration) + ": " + str(arrayCopy))
            iteration += 1
        arrayCopy[j + 1] = small

    print(comparition)
    print(shifts)
    analizeInsertionSort(arrayCopy,comparition,shifts)
    return arrayCopy


def menu():
    print((":" * 7) + " ORDENAMIENTOS " + (":" * 7))
    print("a) Ingresa los datos")
    print("b) Ingresa un rango")
    option = ""
    while not option == "a" and not option == "b":
        option = input("Elige una opción: ")
    return option


def analizeBubbleSort(numbers, comparations, shifts):
    nBubble = len(numbers)
    comparisonsO = "n^2 = " + str(nBubble ** 2)
    shiftsO = "n^2 = "
    comparisonsC = "((n-1)n)/2 = " + str((nBubble - 1) * nBubble / 2)
    shiftsC = "((n-1)n)/2 = [0," + str((nBubble - 1) * nBubble / 2) + "]"
    comparisonsR = str(comparations)
    shiftsR = str(shifts)
    analizeAlgorithm(comparisonsO, shiftsO, comparisonsC, shiftsC, comparisonsR, shiftsR)


def analizeInsertionSort(numbers, comparations, shifts):
    nInsertion = len(numbers)
    comparisonsO = "n^2 = " + str(nInsertion ** 2)
    shiftsO = "n^2 = "
    comparisonsC = "((n-1)n)/2 = " + str((nInsertion - 1) * nInsertion / 2)
    shiftsC = "((n-1)n)/2 = [0," + str((nInsertion - 1) * nInsertion / 2) + "]"
    comparisonsR = str(comparations)
    shiftsR = str(shifts)
    analizeAlgorithm(comparisonsO, shiftsO, comparisonsC, shiftsC, comparisonsR, shiftsR)


def analizeAlgorithm(comparisonsO, shiftsO, comparisonsC, shiftsC, comparisonsR, shiftsR):
    print(dash_div)
    print("\t\t\t|\tCOMPARACIONES\t\t|\t\tINTERCAMBIOS")
    print("Notación O\t|\t\t" + comparisonsO + "\t\t\t|\t\t\t" + shiftsO)
    print("Complejidad\t|\t" + comparisonsC + "\t|\tde 0 a " + shiftsC)
    print(dash_div)
    print("Realizadas\t|\t\t" + comparisonsR + "\t\t\t\t|\t\t\t" + shiftsR)


def userInput():
    dataLength = input("¿Cuántos datos?: ")
    numbers = []

    if int(dataLength) > 0:
        strInput = input("Da los " + dataLength + " datos separados por un espacio: ").split(" ")
        for i in range(int(dataLength)):
            numbers.append(int(strInput[i]))

    print((":" * 7) + " BUBBLESORT " + (":" * 6))
    bubbleSort(numbers)

    # print((":" * 7) + " HEAPSORT " + (":" * 7))
    # print("             " + str(numbers))
    # heapSort(numbers)

    # print((":" * 7) + " MERGESORT " + (":" * 7))
    # print("             " + str(numbers))
    # mergeSort(numbers)

    # print((":" * 7) + " QUICKSORT " + (":" * 7))
    # quickSort(numbers, 0, len(numbers) - 1)

    print((":" * 5) + " SELECTIONSORT " + (":" * 5))
    selection_sort(numbers, True)

    print((":" * 7) + " INSERTIONSORT " + (":" * 7))
    insertionSort(numbers)


def genInput():
    rango = input("Introduce el rango: ")
    print("|" + (" " * 3) + "Ordenamiento" + (" " * 3) + "|" + (" " * 3) + "Comparaciones" + (" " * 3) + "|" + (" " * 3) + "Intercambios/desplazamientos" + (" " * 3) +
          "|" + (" " * 3) + ("Tiempo") + (" " * 3) + "|")


def main():
    os.system('cls')

    option = menu()

    if option == "a":
        userInput()
    elif option == "b":
        genInput()
    # a = [5,7,2,3,9,1]
    # print(selectionSort(a, False))
main()


