from heapq import heappush, heappop
from random import randrange
from time import time
import os


def bubbleSort(unsort_list):
    print("             " + str(unsort_list))
    iteracion = 0
    intercambios = 0
    comparaciones = 0

    for i in range(len(unsort_list) - 1):
        for j in range(len(unsort_list) - 1 - i):
            comparaciones += 1
            if unsort_list[j] > unsort_list[j + 1]:
                unsort_list[j], unsort_list[j + 1] = unsort_list[j + 1], unsort_list[j]
                intercambios += 1
            iteracion += 1
            print("Iteración " + str(iteracion) + ": " + str(unsort_list))

    print(comparaciones)
    print(intercambios)
    return intercambios, comparaciones


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
    iteracion = 1
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

        print("Iteración " + str(iteracion) + ": " + str(array))
        iteracion += 1
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

def selectionSort(unorderArray, debbug):
    print("             " + str(unorderArray))
    iteracion = 1
    for i in range(len(unorderArray)):
        minInd = i
        for j in range(i + 1, len(unorderArray)):
            if debbug:
                print("Iteración "+ str(iteracion) + ": " + str(unorderArray))
                iteracion += 1
            if unorderArray[minInd] > unorderArray[j]:

                minInd = j
        unorderArray[i], unorderArray[minInd] = unorderArray[minInd], unorderArray[i]

    return unorderArray

def insertionSort(unorderedArray):
    print("             " + str(unorderedArray))
    iteracion = 1
    comparacion = 0
    intercambios = 1

    #initialTime = time.time()
    for i in range(0, len(unorderedArray)):
        for j in range(i + 1, len(unorderedArray)):
            print("Iteración " + str(iteracion) + ": " + str(unorderedArray))
            iteracion += 1
            if unorderedArray[j] < unorderedArray[i]:
                comparacion += 1
                unorderedArray[j], unorderedArray[i] = unorderedArray[i], unorderedArray[j]
                intercambios += 1

    #finalTime = timetime()
    #totalTime = finalTime - initialTime
    # print(initialTime)
    # print(finalTime)
    # print(totalTime)
    return unorderedArray

def menu():
    print((":" * 7) + " ORDENAMIENTOS " + (":" * 7))
    print("a) Ingresa los datos")
    print("b) Ingresa un rango")
    option = ""
    while not option == "a" and not option == "b":
        option = input("Elige una opción: ")
    return option

def printBubble(numeros):
    nBubble = len(numeros)
    print(("-" * 75))
    print((" " * 12) + "|" + (" " * 5) +"COMPARACIONES" + (" " * 8) + ("|") + (" " * 6) + "INTERCAMBIOS" + (" " * 9))
    print("Notación O  |" + (" " * 8) + "n^2 = " + str(nBubble ** 2) + (" " * 10) + "|" + (" " * 8) + "n^2 = ")
    print("Complejidad |" + "   ((n - 1)n) / 2 = " + str((nBubble - 1) * nBubble / 2) + "  |" + (" " * 3) + "de 0 a ((n - 1)n) / 2 = [0," +
          str((nBubble - 1) * nBubble / 2) + "]")
    print(("-" * 75))
    print("Realizadas  |" + (" " * 26) + "|")
    print(("-" * 75) + '\n')

def userInput():
    numDatos = input("¿Cuántos datos?: ")
    numeros = []

    if int(numDatos) > 0:
        strInput = input("Da los " + numDatos + " datos separados por un espacio: ").split(" ")
        for i in range(int(numDatos)):
            numeros.append(int(strInput[i]))
    print((":" * 7) + " BUBBLESORT " + (":" * 6))
    bubbleSort(numeros)
    printBubble(numeros)
    # print((":" * 7) + " HEAPSORT " + (":" * 7))
    # print("             " + str(numeros))
    # heapSort(numeros)
    # print((":" * 7) + " MERGESORT " + (":" * 7))
    # print("             " + str(numeros))
    # mergeSort(numeros)
    # print((":" * 7) + " QUICKSORT " + (":" * 7))
    # quickSort(numeros, 0, len(numeros) - 1)
    # print((":" * 5) + " SELECTIONSORT " + (":" * 5))
    # selectionSort(numeros, True)
    # print((":" * 7) + " INSERTIONSORT " + (":" * 7))
    # insertionSort(numeros)

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


